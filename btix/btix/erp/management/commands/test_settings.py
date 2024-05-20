"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import logging
from datetime import datetime, date

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

from erp.integration import base

logger = logging.getLogger("erp")

class Command(BaseCommand):
    help = "Test settings"

    def handle(self, *a, **kw):
        if hasattr(settings, "DATABASE_ROUTERS"):
            if len(settings.DATABASE_ROUTERS) == 0:
                raise CommandError('PrimaryRouter not found in DATABASE_ROUTERS')
        else:
            raise CommandError('DATABASE_ROUTERS is not defined')

        if hasattr(settings, "FIRMS"):
            if 'default' not in settings.FIRMS:
                raise CommandError('default not found in FIRMS')
            firm = settings.FIRMS['default']
            # check props
            if 'NR' not in firm or isinstance(firm['NR'], int) is False:
                raise CommandError('NR is not defined in FIRMS.default or its not int')
            if 'NS' not in firm or isinstance(firm['NS'], str) is False:
                raise CommandError('NS is not defined in FIRMS.default or its not str')
            if 'PER' not in firm or isinstance(firm['PER'], str) is False:
                raise CommandError('PER is not defined in FIRMS.default or its not str')

            if 'PREV_NR' not in firm or isinstance(firm['PREV_NR'], int) is False:
                raise CommandError('PREV_NR is not defined in FIRMS.default or its not int')
            if 'PREV_NS' not in firm or isinstance(firm['PREV_NS'], str) is False:
                raise CommandError('PREV_NS is not defined in FIRMS.default or its not str')
            if 'PREV_PER' not in firm or isinstance(firm['PREV_PER'], str) is False:
                raise CommandError('PREV_PER is not defined in FIRMS.default or its not str')

            if 'REST_IS_ACTIVE' not in firm or isinstance(firm['REST_IS_ACTIVE'], bool) is False:
                raise CommandError('REST_IS_ACTIVE is not defined in FIRMS.default or its not boolean')
            if firm['REST_IS_ACTIVE']:
                if 'REST_URL' not in firm or isinstance(firm['REST_URL'], str) is False:
                    raise CommandError('REST_URL is not defined in FIRMS.default or its not str')
                if 'REST_VERSION' not in firm or isinstance(firm['REST_VERSION'], str) is False:
                    raise CommandError('REST_VERSION is not defined in FIRMS.default or its not str')
                if 'REST_HEAD_KEY' not in firm or isinstance(firm['REST_HEAD_KEY'], str) is False:
                    raise CommandError('REST_HEAD_KEY is not defined in FIRMS.default or its not str')
                if 'DEFAULT_REST_USER' not in firm or isinstance(firm['DEFAULT_REST_USER'], str) is False:
                    raise CommandError('DEFAULT_REST_USER is not defined in FIRMS.default or its not str')
                if 'REST_USERS' not in firm or isinstance(firm['REST_USERS'], dict) is False:
                    raise CommandError('REST_USERS is not defined in FIRMS.default or its not dict')
                if firm['DEFAULT_REST_USER'] not in firm['REST_USERS']:
                    raise CommandError('DEFAULT_REST_USER not found ni REST_USERS')
                if hasattr(settings, 'REST_TOKEN_TTL') is False or isinstance(settings.REST_TOKEN_TTL, int) is False:
                    raise CommandError('REST_TOKEN_TTL is not defined or its not int')

            if 'XML_IS_ACTIVE' not in firm or isinstance(firm['XML_IS_ACTIVE'], bool) is False:
                raise CommandError('XML_IS_ACTIVE is not defined in FIRMS.default or its not boolean')
            if firm['XML_IS_ACTIVE']:
                if 'XML_SERVER' not in firm or isinstance(firm['XML_SERVER'], str) is False:
                    raise CommandError('XML_SERVER is not defined in FIRMS.default or its not str')

                if 'XML_SECRET' not in firm or isinstance(firm['XML_SECRET'], str) is False:
                    raise CommandError('XML_SECRET is not defined in FIRMS.default or its not str')

                if hasattr(settings, 'XML_CLIENT_TIMEOUT') is False or isinstance(settings.XML_CLIENT_TIMEOUT, int) is False:
                    raise CommandError('XML_CLIENT_TIMEOUT is not defined or its not int')

            import django.db.models.options as options
            if 'target_db' not in options.DEFAULT_NAMES:
                raise CommandError('target_db not found in options.DEFAULT_NAMES (options.DEFAULT_NAMES = options.DEFAULT_NAMES + (\'target_db\',))')


        else:
            raise CommandError('FIRMS is not defined')
