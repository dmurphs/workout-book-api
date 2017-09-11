import os

from .base import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'ec2-50-17-217-166.compute-1.amazonaws.com:5432',
        'NAME': 'dc40cpp3hslsr5',
        'USER': 'jxkexsbuqphcaf',
        'PASSWORD': '231b00b8ae1bfbf7c893e436cb862c168ecfebe9865e7404dffb926e51c348a7'
    }
}

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

# CORS Settings
CORS_ORIGIN_WHITELIST = ()

ALLOWED_HOSTS = ['workout-book-api.herokuapp.com']