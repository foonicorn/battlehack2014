from __future__ import absolute_import
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from django.core.urlresolvers import reverse_lazy

_ = lambda x: x

# Basic constants that can be used to structure paths
# relative to the project.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
PROJECT_NAME = os.path.split(BASE_DIR)[-1]

# Secret key. If changed, secure cookies will be invalidated.
SECRET_KEY = 'battlehack'

DEBUG = TEMPLATE_DEBUG = False

ADMINS = ()

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'none@none.none'
SERVER_EMAIL = 'none@none.none'

# Database settings. We depend on PostgreSQL 9.1+ and do not
# support SQLite, MySQL or other Django supported engines.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'battlehack',
    }
}

ALLOWED_HOSTS = []

SITE_ID = 1

# i18n/l10n settings. We do use those features so keep them enabled.
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', _('English')),
)

TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (

    os.path.join(ROOT_DIR, 'templates/locale'),
)

LOGIN_URL = reverse_lazy('login')

# Do not make the session and csrf cookie secure (https:// only)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

MEDIA_ROOT = os.path.join(ROOT_DIR, 'web', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ROOT_DIR, 'web', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(ROOT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'battlehack.utils.context_processors.config',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'battlehack.urls'

WSGI_APPLICATION = 'battlehack.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social.apps.django_app.default',
    'south',
    'rest_framework',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'formatters': {
        'verbose': {
            'format':
                '[%(asctime)s] %(levelname)s:%(name)s %(funcName)s %(message)s',  # noqa
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        # This is the root logger that catches everything, if there's no other
        # match on the logger name. If we want custom logging handing for our
        # code vs. third-party code, define loggers for each module/app
        # that's using standard python logging.
        'root': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'celery': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },

        'battlehack': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

# Disable South in tests as it is sending incorrect create signals
SOUTH_TESTS_MIGRATE = True
