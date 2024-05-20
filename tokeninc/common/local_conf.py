import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


FIRMS = {
    'default': {
        'NR': 11,
        'NS': '011',
        'PER': '01',
        'PREV_NR': 1,
        'PREV_NS': '01',
        'PREV_PER': '01',
        'REST_IS_ACTIVE': True,
        # 'REST_URL': 'http://10.40.12.35:32001/api/',
        'REST_URL': 'http://localhost:32001/api/',
        'REST_VERSION': 'v1',
        'REST_HEAD_KEY': 'QlRJOm5UVzFmT1dTK21KbVkxUm1DcEh3dHlKMU9tSDRQdS9xak8yUzdSUkkwMlk9',
        # 'DEFAULT_REST_USER': 'BTI',
        'DEFAULT_REST_USER': 'LOGO',
        # 'REST_USERS': {
        #     'BTI': '3333',
        # },
        'REST_USERS': {
            'LOGO': 'LOGO',
        },
        'XML_SERVER': 'tcp://*:5555',
        'XML_SECRET': '',
        'XML_IS_ACTIVE': False,
        'SETTINGS': {
            'ELOGO_USER': '8470436038',
            'ELOGO_PWD': 'veKrnbcu',
            'KODLAMA': {
                'MUHASEBE_KART_NUMARALAMA': '120.002',  # kontrol edilecek 120.01
                'MUHASEBE_KART_SABLON': '0000',
                'CARI_KART_NUMARALAMA': 'M',
                'CARI_KART_SABLON': '000000000',
                'GELIR01_GL_KOD': '600.01.001',
                'BSMV_GL_KOD': '360.01.004',
                'CARI_KART': {
                    'ACCOUNT_TYPE': 3,
                    'CORRESP_LANG': 1,
                    'CL_ORD_FREQ': 1,
                    'ORD_DAY': 1,
                    'PURCHBRWS': 1,
                    'SALESBRWS': 1,
                    'IMPBRWS': 1,
                    'EXPBRWS': 1,
                    'FINBRWS': 1,
                    'COLLATRLRISK_TYPE': 1,
                    'RISK_TYPE1': 1,
                    'RISK_TYPE2': 1,
                    'RISK_TYPE3': 1,
                    'COUNTRY_CODE': 'TR',
                    # 'GL_CODE': '120.01.00100',
                    'GL_CODE': '120.002.001',

                },
                'SATIS_FATURASI': {
                    'DataObjectParameter': {
                        'FillAccCodesOnPreSave': True
                    },
                    'TYPE': 9,
                    'NUMBER': '~',
                    'GL_CODE': '120.01.002',
                    'VAT_INCLUDED_GRS': 1,
                    'CURRSEL_TOTALS': 2,
                    'CURRSEL_DETAILS': 2
                },
                'SATIS_FATURASI_SATIRI': {
                }
            }
        }
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'erp': {
        'ENGINE': 'mssql',
        'NAME': 'GENEKS',
        'USER': 'sa',
        'PASSWORD': '1905',
        'HOST': 'DESKTOP-K6AB32H',
        'PORT': 1433,
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    },
    'system': {
        'ENGINE': 'mssql',
        'NAME': 'GENEKS',
        'USER': 'sa',
        'PASSWORD': '1905',
        'HOST': 'DESKTOP-K6AB32H',
        'PORT': 1433,
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    },

}