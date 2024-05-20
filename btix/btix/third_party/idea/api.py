"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import requests
import configparser

class Idea:
    def __init__(self, base_url):
        self.base_url = base_url
        self.last_request = None

    def read_token_from_ini(self, path, section='Ideasoft', key='token'):
        config = configparser.ConfigParser()
        config.read(path)
        self.token = config[section].get(key)



    @property
    def default_headers(self):
        headers = {
            'Content-Type': 'application/json'
        }
        if self.token:
            headers.update({
                'Authorization': f'Bearer {self.token}'
            })
        return headers

    def set_token(self, token):
        self.token = token

    def _request(self, type, url, params=None, headers={}, data=None, json=None):
        dheaders = self.default_headers
        dheaders.update(headers)
        self.last_request = requests.api.request(
            type,
            url,
            params=params,
            headers=dheaders,
            data=data,
            json=json
        )
        return self.last_request

    def shipping_companies(self, **kw):
        url = f"{self.base_url}/api/shipping_companies"
        result = self._request('GET', url, params=kw)
        return result.json() 

    def orders(self):
        url = f"{self.base_url}/api/orders/"
        result = self._request('GET', url)
        return result.json()

    def update_order(self, id, data):
        url = f"{self.base_url}/api/orders/{id}"
        result = self._request('PUT', url, json=data)
        return result.json()
