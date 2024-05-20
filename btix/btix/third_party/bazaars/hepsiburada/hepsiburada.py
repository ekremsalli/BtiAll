"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import hashlib
import time
import urllib
from datetime import date, datetime, timedelta


import requests
import requests.api

class Hepsiburada:
    def __init__(self, *a, **kw):
        self.base_url = "https://oms-external.hepsiburada.com"
        self.username = kw.get('username', '')
        self.password = kw.get('password', '')
        self.merchant_id = kw.get('merchant_id', '')
        self._last_request = None

    @property
    def auth(self):
        from base64 import b64encode
        val = f'{self.username}:{self.password}'
        return b64encode(val.encode('utf-8')).decode('utf-8')

    @property
    def agent(self):
        return f'{self.merchant_id}-BTI'


    def collect_all(self, limit=10, **kwargs):
        page = 0
        orders = []
        while True:
            temp = self.get_orders(limit=10, offset=limit*page)
            if temp:
                orders.extend(temp)
            pc = self._last_request.headers.get('Pagecount')
            if int(pc) <= (page+1):
                break
            page += 1
        return orders

    def get_orders(self, limit=10, offset=0, **kwargs):
        params = {
            'limit': limit,
            'offset': offset
        }
        params.update(kwargs)

        url = f"{self.base_url}/packages/merchantid/{self.merchant_id}"

        self._last_request = requests.api.request(
            'GET',
            url,
            params=params,
            headers={
                'Authorization': f'Basic {self.auth}',
                'User-Agent': self.agent
            }
        )
        if self._last_request.status_code == 200:
            return self._last_request.json()
        return []