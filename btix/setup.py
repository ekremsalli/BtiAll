"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from setuptools import setup, find_packages

kw = {
    'name': 'btix',
    'version': '0.0.2',
    'author': 'Emrah Atalay',
    'author_email': 'emrah.atalay@btidanismanlik.com',
    'description': 'BTIX',
    'license': 'MIT',
    'install_requires': [
        'Django==3.2.12',
        'pyodbc==4.0.30',
        'pytz==2020.5',
        'sqlparse==0.4.1',
        'requests',
        'djangorestframework==3.13.1',
        'markdown',
        'django-filter',
        'djangorestframework-simplejwt',
        'PyJWT',
        'python-dateutil',
        'arrow',
        'django-cors-headers',
        'pyyaml',
        'django_redis',
        'uritemplate',
        'drf-yasg',
        'dicttoxml',
        'zeep',
        'pyzmq',
        'pyhumps',
        'xmltodict'
    ],
    'package_dir': {"": "btix"},
    'packages': find_packages(where="btix"),
    'include_package_data': True,
    'package_data': {
        'btix': [
        ]
    },
    'zip_safe': False,
}

setup(**kw)

print('!')
