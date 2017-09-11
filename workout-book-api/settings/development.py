from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#lz5h4kp+e65r3i3fa5o!9+9ohrdl*#h_lu3h%&4uq))+v-s$x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# CORS Settings
CORS_ORIGIN_WHITELIST = (
    'localhost:3000'
)

ALLOWED_HOSTS = ['*']

# Redis Settings
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'workoutbookapi',
        'USER': 'postgres',
        'PASSWORD': 'postgres'
    }
}