"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import os
import django.db.models.options as options
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('target_db',)

SECRET_KEY = '6@5y(190)0$4wvej#-v0dkc8otq6of*!jjr1p2lo(d3yc)%)s8'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bti',
    'erp',
    'third_party.robotpos',
    'third_party.bazaars.trendyol',
    'third_party.bazaars.n11',
    'third_party.bazaars.hepsiburada',
    'third_party.bazaars.gittigidiyor',
    'third_party.bazaars.ciceksepeti'
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
        'DIRS': [],
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
    },
    'erp': {
        'ENGINE': 'mssql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server'
        },
        'TEST': {
            'NAME': ''
        }
    },
    'system': {
        'ENGINE': 'mssql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server'
        },
        'TEST': {
            'NAME': 'KD_TIGER'
        }
    },
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

FIRMS = {
    'default': {
        'NR': 20,
        'NS': '020',
        'PER': '02',
        'PREV_NR': 19,
        'PREV_NS': '19',
        'PREV_PER': '01',
        'RS_PAYMENT_MATCHING': 'KD_PaymentMathing',
        'REST_IS_ACTIVE': True,
        'REST_URL': 'http://192.168.1.9:32001/api/',
        'REST_VERSION': 'v1',
        'REST_HEAD_KEY': 'QlRJOm5UVzFmT1dTK21KbVkxUm1DcEh3dHlKMU9tSDRQdS9xak8yUzdSUkkwMlk9',
        'DEFAULT_REST_USER': 'BTI',
        'REST_USERS': {
            'BTI': '3333',
        },
        'XML_SERVER': 'tcp://127.0.0.1:5555',
        'XML_SECRET': '***',
        'XML_IS_ACTIVE': True
    }
}

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
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DATE_FORMAT': '%d.%m.%Y',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
                ],
        'DEFAULT_PERMISSION_CLASSES': [
                    'rest_framework.permissions.IsAuthenticated',
                ],
        "DEFAULT_PARSER_CLASSES": [
                    "rest_framework.parsers.JSONParser",
                ],
        "DEFAULT_AUTHENTICATION_CLASSES": [
                    "rest_framework_simplejwt.authentication.JWTTokenUserAuthentication"
                ],
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 100,
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=3),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1)
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


try:
    from common.local_conf import *
except ImportError:
    pass
except Exception as e:
    print(e)
