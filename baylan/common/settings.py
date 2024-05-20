from os import makedirs, environ
from pathlib import Path
import datetime

import django.db.models.options as options

BASE_DIR = Path(__file__).resolve().parent.parent

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('target_db',)

SECRET_KEY = environ.get('SECRET_KEY') or '3bpvox*&3@))(gqyf1%xft%nl!7--x$!-7n68sk^hx*ctrb=yx'

DEBUG = int(environ.get('DEBUG', default=0))

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'corsheaders',
    'bti',
    'erp',
    'app_v1'
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
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
        'NAME': BASE_DIR / 'db.sqlite3',
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
STATIC_ROOT = BASE_DIR / 'static'

XML_CLIENT_TIMEOUT = 15000
REST_TOKEN_TTL = 120 * 60
CORS_ALLOW_ALL_ORIGINS = True

TODAY = str(datetime.date.today()).replace("-", "_")

LOG_PATH = environ.get('LOG_PATH', 'logs')

makedirs(LOG_PATH, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module}: {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },    
    'handlers': {
        'app_file': {
            'class': 'logging.FileHandler',
            'filename': f'{LOG_PATH}/app_{TODAY}.log',
            'formatter': 'verbose'
        },
        'erp_file': {
            'class': 'logging.FileHandler',
            'filename': f'{LOG_PATH}/erp_{TODAY}.log',
            'formatter': 'verbose'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True
        },
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


REST_FRAMEWORK = {
    'DATE_FORMAT': '%d.%m.%Y',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.BasicAuthentication',
        'common.dummy.DummyAuthentication'
    ],
    'EXCEPTION_HANDLER': 'bti.exp_handler.bti_exception_handler',
}

MAPPING = {
    'WANTAGE': {
        'YETKI_KODU': 'AUXIL_CODE',
        'SUBE_KODU': 'SOURCE_WH',
        'ACIKLAMA': 'FOOTNOTE1',
        'ORDER_KEY': 'FOOTNOTE4',
    },
    'WANTAGE_ITEM': {
        'UrunKod': 'ITEM_CODE',
        'Miktar': 'QUANTITY',
    },
    'WANTAGE_ITEM_CONSUMED': {
        'ITEMCODE': 'ITEM_CODE',
        'UNITCODE': 'UNIT_CODE',
        'AUXILCODE': 'AUXIL_CODE',
    },
    'TRANSFER': {
        'UNIQUENUMBER': 'DOC_NUMBER',
        'EXP1': 'FOOTNOTE1',
        'EXP2': 'FOOTNOTE2',
    },
    'TRANSFER_LINE': {
        'CODE': 'ITEM_CODE',
        'UNIT': 'UNIT_CODE',
    },
}


FIRMS = {
    'default': {
        'NR': int(environ.get('FIRMS_DEF_NR', 0)),
        'NS': environ.get('FIRMS_DEF_NS'),
        'PER': environ.get('FIRMS_DEF_PER'),
        'PREV_NR': int(environ.get('FIRMS_PER_NR', 0)),
        'PREV_NS': environ.get('FIRMS_DEF_PREV_NS'),
        'PREV_PER': environ.get('FIRMS_DEF_PREV_PER'),
        'REST_IS_ACTIVE': bool(environ.get('FIRMS_DEF_REST_IS_ACTIVE', 0)),
        'REST_URL': environ.get('FIRMS_DEF_REST_URL'),
        'REST_VERSION': environ.get('FIRMS_DEF_REST_VERSION', 'v1'),
        'REST_HEAD_KEY': environ.get('FIRMS_DEF_REST_HEAD_KEY'),
        'DEFAULT_REST_USER': environ.get('FIRMS_DEF_DEFAULT_REST_USER', 'BTI'),
        'REST_USERS': {
            environ.get('FIRMS_DEF_REST_USERS0_USER'): environ.get('FIRMS_DEF_REST_USERS0_PWD'),
        },
        'XML_SERVER': environ.get('FIRMS_DEF_XML_SERVER', ''),
        'XML_SECRET': environ.get('FIRMS_DEF_XML_SECRET'),
        'XML_IS_ACTIVE': bool(environ.get('FIRMS_DEF_XML_IS_ACTIVE', 0)),
        'SETTINGS': {
            'DEFAULT_SALES_ORDER': {
                'NUMBER': '~'
            },
            'DEFAULT_PURCHASE_ORDER': {

            },
            'DEFAULT_PURCHASE_DISPATCH': {

            },
            'CANCEL_PURCHASE_ORDER': {
                'ORDER_STATUS': 2
            },
            'DEFAULT_EXPANSE': {

            },
            'DEFAULT_REFUND': {

            },
            'DEFAULT_WANTAGE': {
                'NUMBER': '~',
                'GROUP': 3,
                'TYPE': 21
            },
            'DEFAULT_WANTAGE_ITEM': {
                'LINE_TYPE': 0,
            },
            'DEFAULT_TRANSFER': {
                'TYPE': 25,
                'NUMBER': '~',
            },
            'DEFAULT_TRANSFER_LINE': {
                'UNIT_CONV1': 1,
                'UNIT_CONV2': 1,
            },
        }
    }
}

DUMMY_PWD = "c25856b1fccfc9eb76ed31192c1d5b32"

try:
    from common.local_conf import *
except ImportError:
    pass
except Exception as e:
    print(e)
