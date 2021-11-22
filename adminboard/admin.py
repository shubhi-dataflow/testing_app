from django.contrib import admin
from . models import AuthorizedHr, CreateCandidate, History

class CandidateList(admin.ModelAdmin):
    list_display = ('username', 'email', 'invitestatus')
    list_display_links = ('username', 'email')
    search_fields = ('username', 'email')

admin.site.register([AuthorizedHr, History])
admin.site.register(CreateCandidate, CandidateList)
