import os
import tempfile
import logging

from battlehack.conf.global_settings import *


RESOURCES_DIR = os.path.join(os.path.dirname(__file__), 'resources')

SECRET_KEY = 'testsecret01234567890'

DEBUG = TEMPLATE_DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

if os.environ.get('JENKINS_URL', None) is not None:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'battlehack_test',
            'HOST': '/var/run/postgresql',
            'USER': 'jenkins',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }

TEMPLATE_DIRS += (
    os.path.join(RESOURCES_DIR, 'templates'),
)

MEDIA_ROOT = tempfile.mkdtemp()

# Disable logging for unittests.
logging.disable(logging.CRITICAL)


# Explicitly disable compressor to ensure a DEBUG=True
# overwrite does not hurt test performance
COMPRESS_ENABLED = False



# # Celery
# BROKER_BACKEND = 'memory'
# CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
# CELERY_ALWAYS_EAGER = True
