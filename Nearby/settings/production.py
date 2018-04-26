from .base import *

DEBUG = True

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

ALLOWED_HOSTS = ['ec2-18-188-184-129.us-east-2.compute.amazonaws.com','localhost','127.0.0.1', 'nearbyapi.gq']

os.environ.setdefault("HOST_URL", "https://nearbyapi.gq")
