import os
import datetime
import django.db.models.options as options

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('target_db',)

SECRET_KEY = '4a-a@z9!u(w2re4t@ou4wl7*x@#0elmccu5@uuud-*cblxm!uh'
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
    'django_filters',
    'drf_yasg',
    'corsheaders',
    'geco',
    'app.apps.AppConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
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
    }
}

DATABASE_CONNECTION_POOLING = False
DATABASE_ROUTERS = [
    'common.db_router.PrimaryRouter'
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

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = False
STATIC_URL = '/static/'

TODAY = str(datetime.date.today()).replace("-", "_")

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
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
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
        }
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
        'rest_framework_simplejwt.authentication.JWTTokenUserAuthentication'
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=3),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True

}

GECO_MAPPING = {
    'DEF_MAP': {
        'TIME_TYPES': 21,
        'EXCUSE_TYPES': 22,
        'DAY_MODELS': 23,
        'PAY_TYPES': 24,
        'PAY_MODELS': 25,
        'SHIFT_MODELS': 26,
        'FLEX_SHIFT_MODELS': 27
    },
    'GROUP_MAP': {
        'COMPANIES': 1,
        'DEPARTMENTS': 2,
        'TITLES': 3,
        'ACCOUNTS': 11
    },
    'geco1': {
        'GECO_GROUPS_DEFAULT_GTYPE': 11,
        'DEFINITIONS': {
            'TIME_TYPES': {
                'def_type': 21,
                'geco_id': 0,
                'short_code': '',
                'link_code': ''
            },
            'EXCUSE_TYPES': {
                'def_type': 22,
                'geco_id': 0,
            },
            'DAY_MODELS': {
                'def_type': 23,
                'geco_id': 0,
                'link_code': ''
            },
            'PAY_MODELS': {
                'def_type': 24,
                'short_code': '',
                'link_code': ''
            },
            'PAY_TYPES': {
                'def_type': 25,
                'geco_id': 0,
                'short_code': '',
                'link_code': ''
            },
            'SHIFT_MODELS': {
                'def_type': 26,
                'short_code': '',
                'link_code': ''
            },
            'FLEX_SHIFT_MODELS': {
                'def_type': 27,
                'short_code': '',
                'link_code': ''
            }
        },
        'EMPLOYEE': {
            'WORKER_TYPES': {'B': 1, 'M': 2}
        },
        'M_ANOMALIES': {
            'employee': 'nrm_persnr',
            'tr_date': 'nrm_datum',
            'ano_type': 'nrm_normabwkennung',
            'ano_text': 'nrm_normabwtext',
            'geco_id': 'idnr',
            'geco_time': 'nrm_timestamp'
        },
        'M_EMPLOYEE': {
            'per_nr': 'pin_persnr',
            'start': 'per_zeitaktivvondatum',
            'end': 'per_zeitaktivbisdatum',
            'nr': 'per_persnr',
            'name': 'per_vorname',
            'surname': 'per_name',
            'firm': 'per_grp0',
            'department': 'per_grp1',
            'title': 'per_grp2',
            'worker_type': 'per_grp3',
            'psoft_id': 'per_grp7',
            'account': 'per_stammperkstnr',
            'cost_center': 'per_perkstnr',
            'work_id': 'pin_persnrref',
        },
        'M_GECOGROUPS': {
            'description': 'grp_grpbez',
            'geco_id': 'idnr',
            'people_code': 'grp_kstnr',
            'group_code': 'grp_grp',
            'gtype': 'grp_grpnr',
            'is_person': 'grp_kstperson'
        },
        'M_GECODEFS': {
            'TIME_TYPES': {
                'code': 'zei_zeitart',
                'name': 'zei_zeitartbez'
            },
            'EXCUSE_TYPES': {
                'code': 'abw_abwart',
                'name': 'abw_abwartbez',
                'short_code': 'abw_abwartkurzbez',
                'link_code': 'abw_zeitart'
            },
            'DAY_MODELS': {
                'code': 'tag_tagmod',
                'name': 'tag_tagmodbez',
                'short_code': 'tag_tagmodkurzbez'
            },
            'PAY_MODELS': {
                'geco_id': 'idnr',
                'code': 'lom_lohnmod',
                'name': 'lom_lohnmodbez'
            },
            'PAY_TYPES': {
                'code': 'loa_lohnart',
                'name': 'loa_lohnartbez'
            },
            'SHIFT_MODELS': {
                'geco_id': 'idnr',
                'code': 'smo_schmod',
                'name': 'smo_schmodbez'
            },
            'FLEX_SHIFT_MODELS': {
                'geco_id': 'idnr',
                'code': 'spr_sprmod',
                'name': 'spr_sprmodbez'
            }
        },
        'M_TRANSACTION': {
            'employee': 'tle_persnr',
            'tr_date': 'tle_datum',
            'start': 'tle_vonzeit',
            'end': 'tle_biszeit',
            'work_time': 'tle_istzeit',
            'time_type': 'tle_zeitart',
            'excuse_type': 'tle_abwart',
            'excuse_day': 'tle_abwtag',
            'day_model': 'tle_tagmod',
            'account': 'tle_perkstnr',
            'pay_type': 'tle_lohnart',
            'geco_user': 'tle_benutzer',
            'geco_id': 'idnr',
            'geco_time': 'tle_timestamp'
        },
        'DATASSIST': {
            'valeoMazeretIzni': ['DESIZ', 'UCSIZ'],
            'babalikIzniNormalMesaisi': ['DOGUM'],
            'fazlaMesai100': [],
            'fazlaMesai120': [],
            'fazlaMesai200': ['OFMTOP'],
            'geceMesaisi': ['GECEZ'],
            'genelTatilMesaisi': ['RESTA'],
            'genelTatilMesasiSaat': ['RESTA'],
            'haftaSonuSaatlik': ['HTAT'],
            'malzemeYokIzniSaatlik': ['MUCSZ'],
            'normalMesai': ['NCAL'],
            'normalMesaiSaatlik': ['NCAL'],
            'yillikIzin': ['YILIZ'],
            'yillikIzinSaatlik': ['YILIZ'],
            'eksikGunSayisi': [
                'UCSIZ','UCSPZ','DESIZ','DOUCS','DOGPZ','KISAP'
                'KISAC','KISAP','RAPOR','RAPOR_TATIL'
            ],
            'ucretsizIzin': ['UCSIZ'],
            'dogumIzniMesai': ['DOGUM'],
            'evlilikIzniMesai': ['EVLEN'],
            'olumIzniMesaisiValeo': ['OLUM'],
            'sendikalIzinMesaisiValeo': ['SENDK'],
            'kisaCalismaSaatiValeo': ['KISAC'],
            'yarimCalismaMesaiGunlukGenel': [],
            'yarimCalismaMesaiSaatlikGenel': []
        },
    }
}
"""
geco sorgu sütunları ve karşılıkları

Bordroda eksikgünde olması gerekenler;
UCSIZ 
UCSPZ 
DESIZ
DOUCS
DOGPZ 
KISAC
KISAP 
HASTA -> RAPOR           olarak others sorgusunda değiştirilmiş
HASPZ -> RAPOR_TATIL     olarak others sorgusunda değiştirilmiş   

"""
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

FTP = {
    'VALEO': {
        'Host': 'sftp.datassist.com.tr',
        'Username': 'valeo',
        'Password': 'tohpei6K',
        'Port': 22,
        'Path': '/valeo/test/in'
    }
}

RESET_MAIL_WAIT_FOR_RESEND_AGAIN_MIN = 5
RESET_MAIL_ACTIVE_FOR_MIN = 15
DEFAULT_EMAIL_SENDER = 'noreply@valeo.com'
EMAIL_HOST = 'bur1-smptserver.vnet.valeo.com'
EMAIL_PORT = 25

try:
    from common.local_conf import *
except ImportError:
    pass
except Exception as e:
    print(e)

