"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from datetime import datetime, date, timedelta
import os
import hashlib
import time
import requests


class Ciceksepeti:

    def __init__(self, *a, **kw):
        self.service_url = "https://apis.ciceksepeti.com/api/v1"
        self.test_url = "https://sandbox-apis.ciceksepeti.com/api/v1"
        self.supplier =  kw.get('supplier', '')
        self.api_key = kw.get('api_key', '')
        self.test = kw.get('test', False)


    @property
    def base_url(self):
        if self.test:
            return self.test_url
        else:
            return self.service_url

    @property
    def default_headers(self):
        return {
            'x-api-key': self.api_key,
            'Content-Type': 'application/json'
        }

    @staticmethod
    def to_min_time(day):
        return datetime.combine(day, datetime.min.time())

    @staticmethod
    def to_max_time(day):
        return datetime.combine(day, datetime.max.time())

    def get_last_request(self):
        return self.last_request
            
    def _request(self, type, url, params=None, headers={}, data=None, json=None):
        dheaders = self.default_headers
        dheaders.update(headers)
        self._last_request = requests.api.request(
            type,
            url,
            params=params,
            headers=dheaders,
            data=data,
            json=json
        )
        return self._last_request

    def collect_all_orders(self, **kw):
        if 'page' in kw:
            kw.pop('page')
        page = 0
        items = list()
        while True:
            req = self.get_orders(page=page, **kw)
            if req is None:
                break
            if req and 'supplierOrderListWithBranch' in req and req['supplierOrderListWithBranch']:
                items.extend(req['supplierOrderListWithBranch'])
            else:
                break
            page += 1

        return items


    def get_orders(self, start=None, end=None, page=0, size=100, status=1, **kw):
        """
        status:
            1: Yeni
            2: Hazırlanıyor
            5: Kargoya verildi
            11: Kargoya verilecek
            7: Teslim edildi
        """
        if start is None:
            start = self.to_min_time(date.today())

        if end is None:
            end = self.to_max_time(date.today())

        payload = {
            'statusId': status,
            'page': page,
            'pageSize': size            
        }
        if start:
            payload.update({'startDate': start.isoformat() })
        
        if end:
            payload.update({'endDate': end.isoformat() })

        pops = []
        for k,v in payload.items():
            if v is None:
                pops.append(k)
        for pop in pops:
            payload.pop(pop)
        
        url = f"{self.base_url}/Order/GetOrders"
        return self._request('POST', url, json=payload).json()