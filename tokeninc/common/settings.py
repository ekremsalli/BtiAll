import os
import datetime
import django.db.models.options as options

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('target_db',)

SECRET_KEY = 'm-a%6$h-7icfbh@i*(17b^yg)&sel@boi*d)b-d6h-kt3df3$x'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'bti',
    'erp',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'common.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, os.path.join(BASE_DIR, 'app', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'common.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASE_CONNECTION_POOLING = False
DATABASE_ROUTERS = [
    'erp.db_router.PrimaryRouter'
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = False
STATIC_URL = '/static/'




XML_CLIENT_TIMEOUT = 15000
REST_TOKEN_TTL = 120 * 60


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'app_file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/app.log',
        },
        'erp_file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/erp.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'app': {
            'handlers': ['app_file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'erp': {
            'handlers': ['erp_file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },

    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

REST_FRAMEWORK = {
    'DATE_FORMAT': '%d.%m.%Y',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
                ],
        "DEFAULT_PARSER_CLASSES": [
                    "rest_framework.parsers.JSONParser",
                ],
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 100,
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.BasicAuthentication',
            'app.dummy.DummyAuthentication'
        ]

}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=3),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1)
}

DUMMY_PWD = "c25856b1fccfc9eb76ed31192c1d5b32"
APPEND_SLASH = True

try:
    from common.local_conf import *
except ImportError:
    pass
except Exception as e:
    print(e)
