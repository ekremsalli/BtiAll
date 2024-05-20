"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import logging
from datetime import datetime, date

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps
from django.core.cache import cache
from erp.active import Active
from erp.auth import Token

logger = logging.getLogger("erp")

class Command(BaseCommand):
    help = "Setup logo rest tokens"

    def handle(self, *a, **kw):
        tokens = {app: {} for app in settings.FIRMS.keys()}
        for firm in settings.FIRMS.keys():
            Active.load_firm(firm)
            if Active.rest_is_active:
                for usr in Active.rest_users.keys():
                    try:
                        resp = Token.generate_token(usr)
                        token = resp.json()
                    except:
                        logger.exception('message')
                    else:
                        print(token)
                        if 'access_token' in token and token['access_token']:
                            tokens[firm][usr] = token
                        else:
                            logger.warning('Token error: {} {} {}'.format(
                            firm, usr, resp.text
                        ))
        cache.set('LRT', tokens, settings.REST_TOKEN_TTL)
