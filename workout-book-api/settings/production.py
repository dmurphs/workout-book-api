import os

from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

# CORS Settings
CORS_ORIGIN_WHITELIST = ()