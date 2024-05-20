from os import makedirs, environ
import datetime
import django.db.models.options as options
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('target_db',)

SECRET_KEY = environ.get('SECRET_KEY') or '(^2o%(f(4%cv-$e__-%_3rq%8#s95kw6u9g=#mf7r^uvzt!@$v'
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

makedirs('logs', exist_ok=True)

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
            'filename': f'logs/app_{TODAY}.log',
            'formatter': 'verbose'
        },
        'erp_file': {
            'class': 'logging.FileHandler',
            'filename': f'logs/erp_{TODAY}.log',
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
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTTokenUserAuthentication'
    ],
    'EXCEPTION_HANDLER': 'bti.exp_handler.bti_exception_handler'
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=3),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True
}

MAPPING = {
    'INVOICE': {
        'InvoiceNo': 'NUMBER',
        'type': 'TYPE',
        'DocumentNo': 'DOC_NUMBER',
        'ARP_CODE': 'ARP_CODE',
        'Payments': 'PAYMENT_CODE',
        'AuxilCode': 'AUXIL_CODE',
        'Warehouse': 'SOURCE_WH',
        'vatexcept_reason': 'VATEXCEPT_REASON',
        'vatexcept_code': 'VATEXCEPT_CODE',
    },
    'INVOICE_LINE': {
        'LineType': 'TYPE',
        'Code': 'MASTER_CODE',
        'LineDescription': 'DESCRIPTION',
        'Quantity': 'QUANTITY',
        'UnitPrice': 'PRICE',
        'VAT': 'VAT_RATE',
        'Total': 'TOTAL',
        'VatAmount': 'VAT_AMNT',
        'UnitCode': 'UNIT_CODE',
        'UnitConv1': 'UNIT_CONV1',
        'UnitConv2': 'UNIT_CONV2',
        'vatexcept_reason': 'VATEXCEPT_REASON',
        'vatexcept_code': 'VATEXCEPT_CODE',
        'ret_cost_type': 'RET_COST_TYPE',
        'source_reference': 'SOURCE_REFERENCE'
    },
    'ECONVERTER': {
        'eInvoice':'EINVOICE',
        'SendingType': 'EARCHIVEDETR_SENDMOD',
        'EArchiveType': 'EINVOICE_TYPE',
        'PaymentMethod': 'EARCHIVEDETR_INTPAYMENTTYPE',
        'PayingAgent': 'EARCHIVEDETR_INTPAYMENTAGENT',
        'InstallationNumber': 'EARCHIVEDETR_INSTALLMENTNUMBER',
        'WebAddress': 'EARCHIVEDETR_INTSALESADDR',
        'InsteadOfDispatch': 'EARCHIVEDETR_INSTEADOFDESP',
    }
}

try:
    from common.local_conf import *
except ImportError:
    pass
except Exception as e:
    print(e)
