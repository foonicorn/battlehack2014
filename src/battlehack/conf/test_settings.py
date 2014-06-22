import os

from battlehack.conf.global_settings import *

ALLOWED_HOSTS = [
    'eniac.local',
]

SECRET_KEY = 'asdfkljsdffwwcqfhoiunhcqrwiuohwqeiucnriuwhencroh'

ADMINS = (
    ('admin', 'root@localhost'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'battlehack_test',
    }
}

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

STATIC_ROOT = os.path.normpath(os.path.join(ROOT_DIR, 'web', 'static'))
MEDIA_ROOT = os.path.normpath(os.path.join(ROOT_DIR, 'web', 'media'))

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': 'unix:/var/run/memcached/memcached.sock',
#         'KEY_PREFIX': 'battlehack_test',
#     }
# }
