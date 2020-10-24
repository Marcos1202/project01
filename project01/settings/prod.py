from .base import *
import os

""" Util para podernos conectar desde el servidor """
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'marcos',
        'PASSWORD': 'root123',
        'HOST':'localhost',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

#cargango archivos estaticos
STATICFILES_DIRS = [BASE_DIR.child('static')]
#necesario para los estaticos de produccion
STATIC_ROOT = BASE_DIR.child('staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.child('media')