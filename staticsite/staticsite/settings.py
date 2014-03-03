# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'izpxs7y)yvl0dov6!nnm_5_cy4%!f38zpayn2zv3b1gtmqk0!+'
DEBUG = TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = (
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'pages.context_processors.google_analytics',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
ROOT_URLCONF = 'staticsite.urls'
WSGI_APPLICATION = 'staticsite.wsgi.application'
STATIC_URL = '/static/'

# Analytics
GOOGLE_ANALYTICS_KEY = ''
GOOGLE_ANALYTICS_DOMAIN = ''
