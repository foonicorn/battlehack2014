import os

from battlehack.conf.global_settings import *


ALLOWED_HOSTS = [
    'chacha.cloudcontrolapp.com',
]

SECRET_KEY = 'asdkohwefsfaacadhfcfhopwiqc238y4wecqrweiourcnew'

ADMINS = (
    ('admin', 'root@localhost'),
)
MANAGERS = ADMINS

f = os.environ['CRED_FILE']
db_data = json.load(open(f))['MYSQLS']

db_config = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': db_data['MYSQLS_DATABASE'],
    'USER': db_data['MYSQLS_USERNAME'],
    'PASSWORD': db_data['MYSQLS_PASSWORD'],
    'HOST': db_data['MYSQLS_HOSTNAME'],
    'PORT': db_data['MYSQLS_PORT'],
}

DATABASES = {
    'default': db_config,
}

STATIC_ROOT = os.path.normpath(os.path.join(ROOT_DIR, 'static'))
MEDIA_ROOT = os.path.normpath(os.path.join(ROOT_DIR, 'media'))

INSTALLED_APPS += (
    'gunicorn',
)

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': 'unix:/var/run/memcached/memcached.sock',
#         'KEY_PREFIX': 'battlehack_live',
#     }
# }

#LOGGING['handlers'].update({
    #'file': {
        #'level': 'DEBUG',
        #'class': 'logging.FileHandler',
        #'filename': os.path.normpath(os.path.join(VHOST_DIR, 'log', 'django.log')),
        #'formatter': 'verbose',
    #},
    #'file-celery': {
        #'level': 'DEBUG',
        #'class': 'logging.FileHandler',
        #'filename': os.path.normpath(os.path.join(VHOST_DIR, 'log', 'celery.log')),
        #'formatter': 'simple',
    #}
#})

#LOGGING['loggers'] = {
    #'root': {
        #'level': 'WARNING',
        #'handlers': ['file', 'sentry'],
    #},
    #'celery': {
        #'level': 'INFO',
        #'handlers': ['file-celery', 'sentry'],
    #},
    #'battlehack': {
        #'level': 'WARNING',
        #'handlers': ['file', 'sentry'],
        #'propagate': True,
    #},
    #'django': {
        #'level': 'WARNING',
        #'handlers': ['file', 'sentry'],
        #'propagate': True,
    #},
#}
