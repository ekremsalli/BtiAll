from datetime import datetime
from bti.converter import BaseConverter
from erp.helpers import calculate_logo_time


class WantageConverter(BaseConverter):
    def after(self):
        data = self._input
        dt = datetime.fromisoformat(data.get('TARIH'))
        self.update('DATE', dt.strftime('%Y-%m-%d'))
        self.update('TIME', calculate_logo_time(dt))
        self.update('SOURCE_DIVISION_NR', data.get('SUBE_KOD').zfill(3))
        if 'ACIKLAMA' in data and data.get('ACIKLAMA', None):
            self.update('FOOTNOTE1', data.get('ACIKLAMA'))


class WantageItemConverter(BaseConverter):
    def after(self):
        pass


class WantageItemConsumedConverter(BaseConverter):
    def after(self):
        pass


class TransferConverter(BaseConverter):
    def after(self):
        data = self._input
        dt = datetime.fromisoformat(data.get('DATE'))
        self.update('DATE', dt.strftime('%Y-%m-%d'))
        self.update('TIME', calculate_logo_time(dt))
        self.update('SOURCE_WH', int(data.get('SOURCE_WH')))
        self.update('DEST_WH', int(data.get('DEST_WH')))
        if 'SHIP_DATE' in data:
            self.update(
                'SHIP_DATE',
                datetime.fromisoformat(data.get('SHIP_DATE')).strftime('%Y-%m-%d')
            )


class TransferLineConverter(BaseConverter):
    def after(self):
        data = self._input
        self.update('QUANTITY', float(data.get('QUANTITY')))
