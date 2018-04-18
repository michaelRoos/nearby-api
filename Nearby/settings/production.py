from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nearby_db',
        'USER': 'sunshine',
        'PASSWORD': 'woofwoof',
        'HOST': 'nearby-db-instance.czc9wuatwimq.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }

}