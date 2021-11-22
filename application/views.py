from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from application.models import Question
from adminboard.models import CreateCandidate, History
from django.http import HttpResponse
from django.contrib.auth.models import User
from application.models import Instructions
from django.core.cache import cache
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.core.mail import send_mail
from django.conf import settings
from itertools import chain
import numpy as np
from django.db.models import Count
import math


def applogin(request):
    return render(request, 'application/index.html')

def appsignup(request):
    data1 = CreateCandidate.objects.all()
    data2 = User.objects.all()
    data = list(chain(data1, data2))
    return render(request, 'application/signup.html', {'data': data})

@csrf_exempt
def postsignup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullName')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        resume = request.FILES.get('resume')
        location = request.POST.get('location')
        source = request.POST.get('source')
        referral = request.POST.get('referral')
        dob = dob[6:10] + '-' + dob[:2] + '-' + dob[3:5]
        CreateCandidate.objects.create(fullname=fullname, username=username, password=password, email=email,
                                       phone=phone, created_at=datetime.today(),
                                       dob=dob, resume=resume, location=location, source=source, referralid=referral, invitestatus='Invite sent', status='Invite sent')
        History.objects.create(fullname=fullname, username=username, password=password, email=email,
                               phone=phone, created_at=datetime.today(),
                               dob=dob, resume=resume, location=location, source=source,
                               referralid=referral, updated_at=datetime.now(), invitestatus='Invite sent', status='Invite sent')
        User.objects.create_user(first_name=fullname, username=username, password=password, email=email)
        sub = 'no-reply: Test details'
        content = f'Hi {fullname},\nThank you for showing interest in working with DataFlow Group.\nTo complete the application process, you are required to take an online test. The test would include assessment for English Grammar, Logic Check and Reasoning Skills.\n\nBelow are the credentials for the test:\n\nusername- {username}\npassword- {password}\nTest link: https://test.dfgateway.com\nThe test cannot be fragmented, but must be completed in a single attempt. The duration for the test is 45 minutes.\n\nBest Regards\nHR Team- Dataflow Group'
        tomail = [f'{email}']
        # sendmailtask.delay(sub, content, tomail)

        send_mail(sub, content, settings.EMAIL_HOST_USER, tomail)
        return redirect('application:applogin')
    return redirect('application:appsignup')

@csrf_exempt
def logincand(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('application:instructions')
        else:
            messages.error(request, "Incorrect Credentials")
            return redirect('application:applogin')
    return redirect('application:applogin')

@login_required(login_url='logincand/')
def instructions(request):
    username = request.user.username
    obj = CreateCandidate.objects.get(username=username)
    instruct = Instructions.objects.all().order_by('-id')
    return render(request, 'application/instructions.html', {'username': username, 'name': obj.fullname, 'email': obj.email, 'phone': obj.phone, 'instruct': instruct,'declaration_accepted':obj.declaration_accepted})

@login_required(login_url='logincand/')
def logout_user(request):
    logout(request)
    return redirect('application:applogin')

@login_required(login_url='logincand/')
def panel(request):
    username = request.user.username
    CreateCandidate.objects.filter(username__exact=username).update(declaration_accepted='Yes')
    # comp_count = Question.objects.values('question').filter(category__iexact='english').annotate(Count('id')).filter(id__count__gte=2).count()
    comp_count = [i for i in Question.objects.filter(category__iexact='english') if len(i.question) > 2000]
    if len(comp_count) > 0:
        nocomp_quest = [j.id for j in Question.objects.filter(category__iexact='english') if len(j.question) < 1000]
        english = Question.objects.filter(pk__in=nocomp_quest).order_by('?')[:8]
        random_count = np.random.randint(len(comp_count))
        comp_quest = [i.question for i in Question.objects.filter(category__iexact='english') if len(i.question) > 2000]
        comprehensive = Question.objects.filter(question__icontains=comp_quest[random_count][:1000])[:2]
        english_questions = list(chain(english, comprehensive))
    else:
        nocomp_quest = [j.id for j in Question.objects.filter(category__iexact='english') if len(j.question) < 1000]
        english_questions = Question.objects.filter(pk__in=nocomp_quest).order_by('?')[:10]

    quantitative_questions = Question.objects.filter(category__iexact='quantitative').order_by('?')[:10]
    reasoning_questions = Question.objects.filter(category__iexact='reasoning').order_by('?')[:10]
    return render(request, 'application/panel.html', {'english_questions': english_questions, 'quantitative_questions': quantitative_questions,
                                                      'reasoning_questions': reasoning_questions, 'username': username})

@login_required(login_url='logincand/')
@csrf_exempt
def submitted(request):
    if request.method == 'POST':
        percent_reas = request.POST.get('vichar__')
        percent_eng = request.POST.get('angrezi__')
        percent_math = request.POST.get('ganith__')
        username = request.POST.get('username__')
        # try:
        user = CreateCandidate.objects.get(username=username)
        user.score_reasoning = math.ceil(int(percent_reas)/10 * 100)
        user.score_english = math.ceil(int(percent_eng)/10 * 100)
        user.score_math = math.ceil(int(percent_math)/10 * 100)
        percent = math.ceil(((int(percent_reas) + int(percent_eng) + int(percent_math))/30) * 100)
        user.score = percent
        user.teststatus = 'Test Taken'
        user.status = 'Test Taken'
        user.testcomplete_at= datetime.now()
        user.save()
        History.objects.create(username=user.username, password=user.password,
                                          phone=user.phone, fullname=user.fullname, designation=user.designation,
                                          email=user.email, team=user.team, location=user.location, score=user.score,
                                          score_reasoning=percent_reas, score_english=percent_eng, score_math=percent_math,
                                          invitestatus=user.invitestatus, teststatus='Test Taken',
                                          status='Test Taken', dob=user.dob, resume=user.resume, created_at=user.created_at,
                                          activestatus=user.activestatus, selectionstatus=user.selectionstatus, source=user.source, referralid=user.referralid,
                                          candempid=user.candempid, updated_at=datetime.now(), updated_by=user.email)
        # except:
        #     return HttpResponse('<h2>Unique contraint failed for username</h2>')
        logout(request)
        return render(request, 'application/submit.html', {'score': percent})
    return redirect('application:panel')


def forcelogout(request, username):
    User.objects.get(username=username).delete()
    CreateCandidate.objects.filter(username__exact=username).update(status='force-logout')
    logout(request)
    return render(request, 'application/forcelogout.html')
