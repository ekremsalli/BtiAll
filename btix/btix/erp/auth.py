"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import logging
from requests import request, auth

logger = logging.getLogger("logo")

import requests
from django.conf import settings
from django.core.cache import cache

from erp.active import Active


class Auth(auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        if self.token:
            r.headers["Authorization"] = "Bearer " + self.token['access_token']
        return r

class Token:
    @classmethod
    def check_settings(cls, firm=None):
        if hasattr(settings, 'FIRMS') is False:
            raise Exception('Ayarlar yapılandırılmamış!')

        if firm not in settings.FIRMS:
            raise Exception('Öntanımlı firma ayarlanmamış (settings.FIRMS)')
        if 'DEFAULT_REST_USER' not in settings.FIRMS[firm]:
            raise Exception('Öntanımlı rest kullanıcısı ayarlanmamış.')

        if settings.FIRMS[firm]['REST_IS_ACTIVE'] is False:
            raise Exception('Bu firma için REST aktif değil!')

    @classmethod
    def get_token_from_cache(cls, user):
        tokens = cache.get('LRT')
        if tokens and Active.name in tokens and user in tokens[Active.name]:
            if tokens[Active.name][user] and 'access_token' in tokens[Active.name][user]:
                return tokens[Active.name][user]
        return None

    @classmethod
    def generate_token(self, user, firm=None):
        print('generate_token: firm->', firm)
        if firm is not None:
            Active.load_firm(firm)

        if user not in Active.rest_users:
            raise Exception(f'Geçersiz kullanıcı! ({user})')
        user, pwd = user, Active.rest_users[user]
        chunks = [
            f'username={user}',
            f'password={pwd}',
            f'grant_type=password',
            f'firmNo={Active.number}',
            f'termNo={Active.period}'
        ]
        payload = "&".join(chunks)
        headers = {
            'Authorization': 'Basic {}'.format(Active.rest_head_key),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        endpoint = f'{Active.rest_url}/{Active.rest_version}/token'
        resp = request("POST", endpoint, headers=headers, data=payload)
        return resp

    @classmethod
    def get_user(cls, user, firm=None):
        cls.check_settings(firm=firm if firm is not None else "default")
        if firm is None:
            firm = 'default'
            Active.load_defaults()
        else:
            Active.load_firm(firm)

        if user is None:
            user = Active.default_rest_user
        return user

    @classmethod
    def get_or_create_token(cls, user=None, firm=None):
        if firm is None and cache.get('active'):
            firm = cache.get('active')
        cls.check_settings(firm=firm if firm is not None else "default")
        if firm is None:
            firm = 'default'
            Active.load_defaults()
        else:
            Active.load_firm(firm)

        if user is None or len(user) == 0:
            user = Active.default_rest_user
        token = cls.get_token_from_cache(user)
        if token is None:
            resp = cls.generate_token(user, firm=firm)
            token = resp.json()
            if 'access_token' not in token:
                raise Exception('Token alınamadı!')
        return token
