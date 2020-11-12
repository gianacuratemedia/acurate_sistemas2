import os
from .base import *

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = ['localhost','165.227.62.217' ]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")