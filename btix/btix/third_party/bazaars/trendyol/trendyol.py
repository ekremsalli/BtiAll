"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from datetime import datetime, date, timedelta
import hashlib
import time
import urllib
import humps

import requests
import requests.api
from requests.auth import HTTPBasicAuth

class Trendyol:
    def __init__(self, *a, **kw):
        self.service_url = "https://api.trendyol.com/sapigw"
        self.test_url = "https://stageapi.trendyol.com/stagesapigw"
        self.username = kw.get('username', '')
        self.password = kw.get('password', '')
        self.supplier = kw.get('supplier', '')
        self.test = kw.get('test', False)
        self._last_request = None

    @property
    def base_url(self):
        if self.test:
            return self.test_url
        else:
            return self.service_url

    @property
    def default_headers(self):
        return {
            'Authorization': f'Basic {self.auth}',
            'User-Agent': self.agent,
            'Content-Type': 'application/json'
        }

    @property
    def auth(self):
        from base64 import b64encode
        val = f'{self.username}:{self.password}'
        return b64encode(val.encode('utf-8')).decode('utf-8')

    @staticmethod
    def to_min_time(day):
        return datetime.combine(day, datetime.min.time())

    @staticmethod
    def to_max_time(day):
        return datetime.combine(day, datetime.max.time())

    @staticmethod
    def to_timestamp(dt):
        return int(dt.timestamp())

    @property
    def agent(self):
        return f'{self.supplier}-BTI'

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
        if 'supplier.developer.authorization.failed' in self._last_request.text:
            raise Exception('User auth problem!')
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
            if req and 'content' in req and req['content']:
                items.extend(req['content'])
            page += 1
            if 'totalElements' in req and len(items) == req['totalElements']:
                break

        return items


    def get_brands(self, page=1, size=500):
        # trendyol marka bilgileri
        # createProduct v2 servisine yapılacak isteklerde gönderilecek brandId
        url = f"{self.base_url}/brands"
        params = {
            'page': page,
            'size': size
        }
        return self._request('GET', url, params=params).json()

    def collect_all_brands(self):
        brands = {}
        page = 0
        stack = 0
        while True:
            temp = self.get_brands(page=page)
            if temp:
                for item in temp['brands']:
                    brands[item['id']] = item['name']
                if len(brands) == stack:
                    break
                stack = len(brands)
                page += 1
            else:
                break
        return brands

    def brand_by_name(self, name):
        url = f"{self.base_url}/brands/by-name"
        params = {
            'name': name
        }
        return self._request('GET', url, params=params).json()

    def get_category_tree(self):
        url = f"{self.base_url}/product-categories"
        return self._request('GET', url).json()

    def shipment_providers(self):
        url = f"{self.base_url}/shipment-providers"
        return self._request('GET', url).json()

    def get_category_attributes(self, category_id):
        url = f"{self.base_url}/product-categories/{category_id}/attributes"
        return self._request('GET', url).json()

    def create_test_order(self, data):
        url = "https://stageapi.trendyol.com/integration/oms/core"
        return self._request('POST', url, json=data).json()

    def create_product(self, **kw):
        # required: barcode, title, productMainId, brandId,
        # categoryId, quantity, stockCode,
        # dimensionalWeight, description,
        # currencyType, listPrice, salePrice,
        # cargoCompanyId, Images, vatRate, attributes
        # optionals -> deliveryDuration, shipmentAddressId, returningAddressId
        data = humps.camelize(kw)
        url = f"{self.base_url}/suppliers/{self.supplier}/v2/products"
        return self._request('POST', url, json=data).json()
        # needs implementation

    def get_products(self, approved=None, barcode=None, start_date=None, end_date=None, page=0,
        size=10, date_query_type=None):
        # filters => approved, barcode, startDate, endDate,
        # page, dateQueryType, size
        params = {}
        plist = [
            'approved', 'barcode', 'start_date', 'end_date',
            'page', 'size', 'date_query_type'
        ]
        for param in plist:
            if locals()[param] is not None:
                params.update({param: locals()[param]})
        params = humps.camelize(params)

        url = f"{self.base_url}/suppliers/{self.supplier}/products"
        return self._request('GET', url, params=params).json()

    def update_price_and_inventory(self, items):
        # [{'barcode': '', 'quantity': int, 'salePrice': float, 'listPrice': float}]
        url = f"{self.base_url}/suppliers/{self.supplier}/products/price-and-inventory"
        data = {
            'items': items
        }
        return self._request('POST', url, json=data)

    def set_picking(self, id, lines):
        url = f"{self.base_url}/suppliers/{self.supplier}/shipment-packages/{id}"
        data = {
            'lines': lines,
            'params': {},
            'status': 'Picking'
        }
        return self._request('PUT', url, json=data)

    def set_invoiced(self, id, invoice, lines):
        url = f"{self.base_url}/suppliers/{self.supplier}/shipment-packages/{id}"
        data = {
            'lines': lines,
            'params': {
                'invoiceNumber': invoice
            },
            'status': 'Invoiced'
        }
        return self._request('PUT', url, json=data)


    def set_unsupplied(self, id, lines):
        url = f"{self.base_url}/suppliers/{self.supplier}/shipment-packages/{id}"
        data = {
            'lines': lines,
            'params': {},
            'status': 'UnSupplied'
        }
        return self._request('PUT', url, json=data)


    def set_cargo_number(self, id, number):
        url = f"{self.base_url}/suppliers/{self.supplier}/{id}/update-tracking-number"
        data = {
            'trackingNumber': number
        }
        return self._request('PUT', url, json=data)


    def set_cargo_url(self, id, url):
        url = f"{self.base_url}/suppliers/{self.supplier}/shipment-packages/{id}/alternative-delivery"
        data = {
            'isPhoneNumber': False,
            'params': {},
            'trackingInfo': url
        }
        return self._request('PUT', url, json=data)


    def get_orders(self, start=None, end=None, page=0, size=200, status='Picking',
        order_by_field='CreatedDate', order_by_direction='ASC', extra={}):
        if start is not None:
            start = self.to_min_time(date.today())

        if end is not None:
            end = self.to_max_time(date.today())

        payload = {
            'status': status,
            'OrderByField': order_by_field,
            'supplierId': self.supplier,
            'startDate': self.to_timestamp(start) if start else None,
            'endDate': self.to_timestamp(end) if end else None,
            'page': page,
            'size': size
        }
        if status is None:
            payload.pop('status')
        payload.update(extra)
        pops = []
        for k,v in payload.items():
            if v is None:
                pops.append(k)
        for pop in pops:
            payload.pop(pop)


        url = f"{self.base_url}/suppliers/{self.supplier}/orders"
        return self._request('GET', url, params=payload).json()
