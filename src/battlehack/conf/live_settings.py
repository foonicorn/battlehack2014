import os

from battlehack.conf.global_settings import *


VHOST_DIR = '/srv/battlehack-live'

ALLOWED_HOSTS = [
    'battlehack-live.moccu.com',
]

SECRET_KEY = ''

ADMINS = (
    ('admin', 'root@localhost'),
)
MANAGERS = ADMINS

EMAIL_SUBJECT_PREFIX = '[battlehack-live] '

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'battlehack_live',
    }
}

STATIC_ROOT = os.path.normpath(os.path.join(VHOST_DIR, 'web', 'static'))
MEDIA_ROOT = os.path.normpath(os.path.join(VHOST_DIR, 'web', 'media'))

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': 'unix:/var/run/memcached/memcached.sock',
#         'KEY_PREFIX': 'battlehack_live',
#     }
# }

LOGGING['handlers'].update({
    'file': {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': os.path.normpath(os.path.join(VHOST_DIR, 'log', 'django.log')),
        'formatter': 'verbose',
    },
    'file-celery': {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': os.path.normpath(os.path.join(VHOST_DIR, 'log', 'celery.log')),
        'formatter': 'simple',
    }
})

LOGGING['loggers'] = {
    'root': {
        'level': 'WARNING',
        'handlers': ['file', 'sentry'],
    },
    'celery': {
        'level': 'INFO',
        'handlers': ['file-celery', 'sentry'],
    },
    'battlehack': {
        'level': 'WARNING',
        'handlers': ['file', 'sentry'],
        'propagate': True,
    },
    'django': {
        'level': 'WARNING',
        'handlers': ['file', 'sentry'],
        'propagate': True,
    },
}

# BROKER_URL = 'redis://localhost:6379/23'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/42'
CELERY_ALWAYS_EAGER = False

# RAVEN_CONFIG = {
#     'dsn': 'https://xxx:xxx@sentry.moccu.com/xxx'  # noqa
# }
