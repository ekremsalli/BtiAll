"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from datetime import datetime, date, timedelta
import os
import hashlib
import time
import zeep
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session



class GittiGidiyor:
    WSDL = {
        'SALE': 'data/IndividualSaleService.wsdl'
    }

    def __init__(self, *a, **kw):
        self.username = kw.get('username', '')
        self.password = kw.get('password', '')
        self.key = kw.get('key', '')
        self.secret = kw.get('secret', '')
        self.lang = kw.get('lang', 'tr')


        self._settings = zeep.Settings(
            strict=False,
            xml_huge_tree=True,
            xsd_ignore_sequence_order=True
        )

        session = Session()
        session.auth = HTTPBasicAuth(self.username, self.password)

        self._transport = Transport(session=session)

        self._last_request = None
        

    @property
    def settings(self):
        return self._settings

    @property
    def transport(self):
        return self._transport

    @property
    def last_request(self):
        return self._last_request

    @property
    def timestamp(self):
        return round(time.time()) * 1000

    @property
    def signature(self):
        htext = f'{self.key}{self.secret}{self.timestamp}'
        return hashlib.md5(htext.encode('utf-8')).hexdigest()

    @property
    def common_params(self):
        return {
            'apiKey': self.key,
            'sign': self.signature,
            'time': self.timestamp,
            'lang': self.lang
        }

    def get_all(self, method, length, item_list_field, item_field, 
        pager='nextPageAvailable', **kw):
        items = []
        page = 1
        while True:
            data = getattr(self, method)(page=page, size=length, **kw)
            page += 1
            if (data and item_list_field in data and \
                data[item_list_field] and \
                item_field in data[item_list_field] and \
                data[item_list_field][item_field]):
                if data[item_list_field][item_field]:
                    items.extend(data[item_list_field][item_field])
            if data is None:
                break
            if pager in data:
                if data[pager] is False:
                    break
        return items



    def get_paged_sales(self, page=1, size=100, with_data=True, 
        by_user='', order_by='A', by_status='S', order_type='D'):
        """
        Satıcı konumundaki kullanıcı bu servis aracılığı ile
        GittiGidiyor Bana Özel sayfasında yer alan "Sattıklarım"
        bölümünde sunulan bilgilerin tamamını elde edebilir,
        bilgileri filtreleyebilir ve sıralayabilir.

        pageNumber: int
            Kaçıncı sayfadan başlayacak?
        pageSize: int
            Kaç kayıt listelenecek?
        withData: boolean
            true: Listelenen ürünler tüm bilgileri ile birlikte
                listelenir.
            false: Sadece ürün numaraları listelenir.
        byUser: String
            Kullanıcı filtresi.
        orderBy: String
            Sıralama filtresi

            P: Ürün numarasına göre sıralama
            C: Satış fiyatına göre sıralama
            A: Son harekete göre sıralama
        byStatus: String
            Durum parametresi(filtresi)

            P: Ödeme Beklediklerim
            S: Kargo Yapılacaklar
            C: Onay Bekleyenler
            T: Para Transferleri
            R: İade Konumunda Olanlar
            O: Tamamlananlar
        orderType: String
            İstekte bulunduktan sonra dönen cevapların
            ID'lerinin artan ya da azalan sırada dönmesini sağlar.

            orderType=A ise artarak,
            orderType=D ise azalarak dönüş yapılır.

        """
        dir = os.path.dirname(__file__)
        wsdl = os.path.join(dir, self.WSDL['SALE'])


        client = zeep.Client(
            wsdl=wsdl,
            settings=self.settings,
            transport=self.transport
        )
        service = client.create_service(
            '{http://sale.individual.ws.listingapi.gg.com}IndividualSaleServiceBinding',
            'http://dev.gittigidiyor.com:8080/listingapi/ws/IndividualSaleService'
        )

        params = self.common_params.copy()
        params.update({
            'pageNumber': page,
            'pageSize': size,
            'withData': with_data,
            'byUser': by_user,
            'orderBy': order_by,
            'byStatus': by_status,
            'orderType': order_type
        })

        self._last_request = service.getPagedSales(
            **params
        )
        return self._last_request      