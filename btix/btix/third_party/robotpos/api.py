"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""
import logging
from datetime import date, time, datetime, timedelta

from requests import request

from bti.helpers import var_conversion

logger = logging.getLogger('robotpos')


class API:
    url = ""
    secure_key = ""

    def __init__(self, **kw):
        self.error = None
        self.ok = False
        self.data = []
        self.action = ""
        self._request = None
        self._response = None
        self.timeout = kw.get('timeout', 5)
        if "url" in kw:
            self.url = kw.pop("url")

        self.gheaders = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def set_url(self, url):
        self.url = url

    def _raw(self, headers, payload):
        try:
            resp = request('POST', self.url + self.action,
                headers=headers, data=payload, timeout=self.timeout)
            data = resp.json()
            self._request = {
                'url': self.url,
                'action': self.action,
                'method': 'POST',
                'headers': headers,
                'data': payload
            }
            logger.info(self._request)
            self._response = resp.text
            logger.info(self._response)
        except Exception as e:
            self.error = e
            logger.exception(e)
        else:
            if data:
                if "Status" in data and data["Status"]:
                    self.data = data['Data']
                else:
                    self.error = data['Message']
            else:
                self.error = "Empty response"
        finally:
            self.ok = False if self.error else True

    def _req(self, all_='false', **kw):
        kw.update({'all_': all_})
        pbuilder = [
            'Type={type_}',
            'StartDate={start}',
            'EndDate={end}',
            'BranchCode={branch}',
            'All={all_}'
        ]
        kw['branch'] = str(kw.pop('branch')).zfill(3)

        payload = '&'.join(pbuilder).format(**kw)
        self.action = "Data"
        self._raw(self.gheaders, payload)

    def span(self, day):
        return (
            datetime.combine(day, time.min),
            datetime.combine(day, time.max).replace(microsecond=0)
        )

    def day_span(self, delta=1):
        return (
            datetime.combine(date.today() - timedelta(days=delta), time.min),
            datetime.combine(
                date.today() - timedelta(days=delta), time.max).replace(
                    microsecond=0)
        )

    def sales(self, start, end, branch):
        # gruplu urun satislari
        return self._req(type_=3, start=start, end=end, branch=branch)

    def recent_sales(self, branch):
        start, end = self.day_span()
        self.sales(start, end, branch)

    def accounting(self, start, end, branch):
        # z raporu
        self._req(type_=7, start=start, end=end, branch=branch)

    def recent_accounting(self, branch):
        start, end = self.day_span()
        self.accounting(start, end, branch)

    def pcw(self, start, end, branch):
        # production-consume-waste
        self._req(type_=3, start=start, end=end, branch=branch)

    def recent_pcw(self, branch):
        start, end = self.day_span()
        self.pcw(start, end, branch)

    def branch_revenue(self, start, end, branch):
        # foy odemeleri
        self._req(type_=1, start=start, end=end, branch=branch)

    def recent_branch_revenue(self, branch):
        start, end = self.day_span()
        self.branch_revenue(start=start, end=end, branch=branch)

    def wantage(self, start, end, branch):
        self._req(type_=8, start=start, end=end, branch=branch)

    def recent_wantage(self, branch):
        start, end = self.day_span()
        self.wantage(start, end, branch)

    def sales_invoice(self, start, end, branch):
        self._req(all_="true", type_=5, start=start, end=end, branch=branch)

    def recent_sales_invoice(self, branch):
        start, end = self.day_span()
        self.sales_invoice(start, end, branch)

    def refunds(self, start, end, branch):
        self._req(type_=6, start=start, end=end, branch=branch)

    def recent_refunds(self, branch):
        start, end = self.day_span()
        self.refunds(start, end, branch)

    def payment_plans(self, branch):
        payload = "Type=4"
        self._raw(self.gheaders, payload)

    def replace_product(self, **kw):
        # create or update product
        params = [
            "code", "external_code", "name", "tax_percent",
            "unit_name", "is_active"
        ]
        if None in [kw.get(par, None) for par in params]:
            raise Exception('Missing parameter!')
        self.action = "ProductIntegration"
        data = {var_conversion(param) : kw.get(param) for param in params}
        try:
            resp = request('POST', self.url + self.action, headers=self.gheaders, data=data)
            result = resp.json()
        except Exception as e:
            self.error = e
        else:
            self.data = result
        finally:
            self.ok = False if self.error else True

    def deactivate_product(self, code):
        self.action = "ProductIntegration"
        data = {
            'Code': code,
            'IsActive': 0
        }
        try:
            resp = request('POST', self.url + self.action, headers=self.gheaders, data=data)
            result = resp.json()
        except Exception as e:
            self.error = e
        else:
            self.data = result
        finally:
            self.ok = False if self.error else True
