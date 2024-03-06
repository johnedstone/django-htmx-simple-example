import os
import secrets
import logging
from datetime import datetime

from django.urls import re_path
from django.shortcuts import redirect, render as django_render
from dotenv import load_dotenv
load_dotenv()

DEBUG = os.getenv('DEBUG', 'yes') == 'yes'
SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_urlsafe(32))
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'no') == 'yes' 

logging.debug(f'SECRET_KEY: {SECRET_KEY}')
logging.debug(f'ALLOWED_HOSTS: {ALLOWED_HOSTS}')
logging.debug(f'DEBUG: {DEBUG}')

ROOT_URLCONF = __name__

APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django-htmx',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates/'
        ],
    },
]

STATIC_URL = "static/"
STATIC_ROOT = 'static'

# wrapper renders django template
def render(template_name):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            context = func(request, *args, **kwargs)
            return django_render(request, template_name, context)
        return wrapper
    return decorator


@render(template_name='latest_data.html')
def about(request):
    current_datetime = datetime.now()
    return locals()

def home(request):
    return redirect('latest_data')

@render(template_name='partial_attendees.html')
def attendees(request):
    attendees={'children': 10, 'adults': 4}
    return locals()


urlpatterns = [
    re_path(r'^$', home, name='homepage'),
    re_path(r'^latest-data/$', about, name='latest_data'),
    re_path(r'^latest-data/attendees/$', attendees, name='attendees'),
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# vim: ai et ts=4 sw=4 sts=4 nu
