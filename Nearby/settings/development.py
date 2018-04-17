from .base import *

DEBUG = True

# SECRET_KEY = 'rzzoe)b=@=+=$)j-vjxmrtky2po=5w*(qhomn7%hd9r#el&i53'

DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nearby_db',
        'USER': 'sunshine',
        'PASSWORD': 'woofwoof',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }

}