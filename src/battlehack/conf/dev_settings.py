from battlehack.conf.global_settings import *


SECRET_KEY = 'dev'

DEBUG = TEMPLATE_DEBUG = THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = ('127.0.0.1', 'localhost')

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

# INTERNAL_IPS = ('127.0.0.1',)
#
# INSTALLED_APPS += (
#     'debug_toolbar',
# )
# MIDDLEWARE_CLASSES += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# )
# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
# }
