# import os
#
# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'f9%v*^8rr2y0yu(5-wqoansld+2bs-a&(a)-1@)6pyp+k=rh7c'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = []
#
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'application',
#     'adminboard',
#     'social_django',
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'adminboard.middleware.RemoveuserMiddleware',
#
# ]
#
# ROOT_URLCONF = 'testingapp.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'social_django.context_processors.backends',
#                 'social_django.context_processors.login_redirect',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'testingapp.wsgi.application'
#
#
# # Database
# # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
#
#
# # Password validation
# # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/2.2/topics/i18n/
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/2.2/howto/static-files/
#
# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.google.GoogleOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )
#
# SITE_ID =1
#
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '461917644557-6i015r8m4uvtpigk75i1kt021dg7r17m.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'F9dpcSj_KZQlTg8wft_dHznm'
#
# SOCIAL_AUTH__KEY = 'ID'
# SOCIAL_AUTH__SECRET = 'SECRET'
# LOGIN_REDIRECT_URL = '/adminboard/adminhome/'
#
#
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
#
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
#
# CELERY_BROKER_URL = 'amqp://172.73.10.166//'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
#
#
#
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'analytics@dataflowgroup.com'
# EMAIL_HOST_PASSWORD = 'Dashboards@123'



#apache2 config
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f9%v*^8rr2y0yu(5-wqoansld+2bs-a&(a)-1@)6pyp+k=rh7c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_PATH = '/;HttpOnly'
#SESSION_COOKIE_SECURE = True

#SECURE_SSL_REDIRECT = True



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'application',
    'adminboard',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'adminboard.middleware.RemoveuserMiddleware',

]

ROOT_URLCONF = 'testingapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'testingapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'devanalytics',
        'USER': 'raghav',
        'PASSWORD': 'programming',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SITE_ID =1

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '461917644557-6i015r8m4uvtpigk75i1kt021dg7r17m.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'F9dpcSj_KZQlTg8wft_dHznm'

SOCIAL_AUTH__KEY = 'ID'
SOCIAL_AUTH__SECRET = 'SECRET'
LOGIN_REDIRECT_URL = '/adminboard/adminhome/'


STATIC_URL = '/static/'
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static')
#]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CELERY_BROKER_URL = 'amqp://localhost//'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'analytics@dataflowgroup.com'
EMAIL_HOST_PASSWORD = 'Dashboards@123'

# second try

#DEFAULT_FROM_EMAIL = 'analytics@dataflowgroup.com'
#EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
#EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'AKIA6MOGWBGBCBL3LFR3'
#EMAIL_HOST_PASSWORD = 'BBighTezVs/o++KjQFieuL7sJO+Xe9CmAk96KhcC2eyv'
#EMAIL_USE_TLS = True




