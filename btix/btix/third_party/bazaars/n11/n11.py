"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from datetime import datetime, date, timedelta
import os
import zeep

class N11:
    def __init__(self, *a, **kw):
        self.key = kw.get('key', '')
        self.secret = kw.get('secret', '')

        self._settings = zeep.Settings(
            strict=False,
            xml_huge_tree=True,
            xsd_ignore_sequence_order=True
        )

        self._last_request = None

    @property
    def settings(self):
        return self._settings

    @property
    def last_request(self):
        return self._last_request

    @property
    def auth(self):
        return {
            'appKey': self.key,
            'appSecret': self.secret
        }

    @property
    def order_structure(self):
        return {
            'status': '',
            'buyerName': '',
            'orderNumber': '',
            'recipient': '',
            'productSellerCode': '',
            'period': {
                'startDate': '',
                'endDate': ''
            },
            'sortForUpdateDate': False
        }

    def get_all_orders(self, start=None, end=None, params={}):
        current = 0
        hit = self.get_orders(start=start, end=end, **params)
        orders = []
        if ("orderList" in hit and hit["orderList"] and \
            "result" in hit and "status" in hit['result'] and \
                hit['result']['status'] == 'success'):
            pages = hit['pagingData']['pageCount'] - 1
            
            orders.extend(hit['orderList']['order'])
            while current < pages:
                current += 1
                data = self.get_orders(page=current, start=start, end=end)
                if "result" in data and "status" in data["result"] and data['result']['status'] == 'success':
                    orders.extend(data['orderList']['order'])
        return orders

    def get_orders(self, page=0, length=20, start=None, end=None, **kwargs):                
        dir = os.path.dirname(__file__)
        wsdl = os.path.join(dir, 'data/OrderService.wsdl')
        client = zeep.Client(wsdl=wsdl, settings=self.settings)
        data = self.order_structure.copy()
        if start is None:
            data['period']['startDate'] = (datetime.now()-timedelta(days=30)).strftime('%d/%m/%Y')
        if end is None:
            data['period']['endDate'] = datetime.now().strftime('%d/%m/%Y')

        data.update(**kwargs)

        self._last_request = client.service.OrderList(
            auth=self.auth,
            searchData=data,
            pagingData={'currentPage': page, 'pageSize': length}
        )
        return self._last_request

    def get_order_detail(self, id):
        dir = os.path.dirname(__file__)
        wsdl = os.path.join(dir, 'data/OrderService.wsdl')

        client = zeep.Client(wsdl=wsdl, settings=self.settings)
        self._last_request = client.service.OrderDetail(
            auth=self.auth,
            orderRequest={'id': id}
        )
        return self._last_request

    def get_detail(self, id):
        from zeep.helpers import serialize_object

        detail = self.get_order_detail(id)
        if (detail and 'result' in detail and 
            detail['result'] and
            'status' in detail['result'] and 
            detail['result']['status'] == 'success' and 
            'orderDetail' in detail and detail['orderDetail']):
            order = serialize_object(detail['orderDetail'], target_cls=dict)
            new_lines = []
            for per in order['itemList']['item']:
                per.pop('_raw_elements')
                new_lines.append(per)
            order['items'] = new_lines
            order.pop('itemList')  
            return order
        return None      


if __name__ == "__main__":
    api = N11(
        key='47328a76-2795-46b7-9a96-08042912ee0b',
        secret='etG3vOT6W9SBFUfg'
    )
    print(api.get_orders(status='Requested'))
    print(api.get_order_detail(284050975))