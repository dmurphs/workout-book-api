import dj_database_url
import os

from .base import *

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {}
DATABASES['default'] = db_from_env

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

# CORS Settings
CORS_ORIGIN_WHITELIST = ()

ALLOWED_HOSTS = ['workout-book-api.herokuapp.com']

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ADMINS = (
    ('Daniel Murphy', 'd.p.murph19@gmail.com'),
)

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE¶ = True