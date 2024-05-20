from datetime import datetime
from bti.converter import BaseConverter
from erp.helpers import calculate_logo_time
from erp.models.friendly import Project

class InvoiceConverter(BaseConverter):
    def after(self):
        data = self._input
        dt = datetime.fromisoformat(data.get('DateTime'))
        self.update('DATE', dt.strftime('%Y-%m-%d'))
        self.update('TIME', calculate_logo_time(dt))
        self.update('DOC_DATE', dt.strftime('%Y-%m-%d'))

        project = Project.objects.filter(
            code__startswith=data.get('AuxilCode')).first()

        if project:
            self.update('PROJECT_CODE', project.code)


class InvoiceLineConverter(BaseConverter):
    pass


class EConverter(BaseConverter):
    def after(self):
        data = self._input
        if 'PaymentDate' in data and data.get('PaymentDate'):
            try:
                dt = datetime.fromisoformat(data.get('PaymentDate'))
            except:
                pass
            else:
                self.update('EARCHIVEDETR_INTPAYMENTDATE', dt.strftime('%d.%m.%Y'))
