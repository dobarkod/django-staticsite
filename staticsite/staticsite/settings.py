# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'izpxs7y)yvl0dov6!nnm_5_cy4%!f38zpayn2zv3b1gtmqk0!+'
DEBUG = TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = (
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
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
