from datetime import datetime

from erp.models.friendly import (
    Stfiche,
    Itmunita,
)

from bti.converter import BaseConverter


class RevenueConverter(BaseConverter):
    def after(self):
        data = self._input
        line = data[0]
        dt = datetime.fromisoformat(line.get('Tarih'))
        self.update('DIVISION', line.get('SubeKod'))
        self.update('NOTES4', line.get('Sube'))
        self.update('DATE', dt.strftime('%d.%m.%Y'))


class RevenueLineConverter(BaseConverter):
    def after(self):
        data = self._input
        self.update('OHP_CODE1', data.get('SubeKod'))
        self.update('BANK_OHP_CODE', data.get('SubeKod'))
        credit = data.get('Tutar')
        if data.get('Kur') and data.get('Kur') > 0:
            credit *= data.get('Kur')

            self.update('TC_XRATE', 1)
            self.update('TC_AMOUNT', credit)
            self.update('RC_XRATE', data.get('Kur'))
            self.update('RC_AMOUNT', data.get('Tutar'))
            # KAC OLMALI?
            # self.update('BNLN_TC_CURR', 20)
            self.update('BNLN_TC_XRATE', data.get('Kur'))

        self.update('CREDIT', credit)
        self.update('PAYMENT_LIST', [])


class SalesConverter(BaseConverter):
    def after(self):
        data = self._input
        line = data[0]

        branch = line.get('SubeKod')
        day = line.get('Tarih').split('-')
        dt = datetime.strptime(line.get('Tarih'), '%Y-%m-%d')

        self.update('SOURCE_WH', branch)
        self.update('SOURCE_DIVISION_NR', branch)
        self.update('DATE', dt.strftime('%d.%m.%Y'))

        pattern = [f'D.K{str(branch).zfill(3)}']
        pattern.append(day[2])
        pattern.append(day[1])
        pattern.append(day[0][-2:])

        ficheno = Stfiche.next_code(
            'ficheno',
            '0'*4,
            ''.join(pattern),
            merge='',
            exclude={'ficheno__contains': 'M'}
        )
        self.update('NUMBER', ficheno)


class SalesLineConverter(BaseConverter):
    def after(self):
        data = self._input
        self.update('ITEM_CODE', data.get('UrunKod'))

        unit = Itmunita.objects.filter(
            itemref__code=data.get('UrunKod'), linenr=1).first()

        if unit and unit.unitlineref and unit.unitlineref.code:
            self.update('UNIT_CODE', unit.unitlineref.code)

        self.update('QUANTITY', data.get('Miktar'))
        self.update('AUXIL_CODE', data.get('UrunKod'))
        self.update('COST_RATE', data.get('KdvOrani'))
        self.update('SOURCEINDEX', data.get('SubeKod'))

        price = data.get('VergiHaricTutar') / data.get('Miktar')
        self.update('PRICE', price)


class ProductionConverter(BaseConverter):
    def after(self):
        data = self._input
        branch = data.sourceindex
        day = str(data.date_field).split()[0].split('-')

        pattern = [f'D.U{str(branch).zfill(3)}']
        pattern.append(day[2])
        pattern.append(day[1])
        pattern.append(day[0][-2:])

        ficheno = Stfiche.next_code(
            'ficheno',
            '0'*4,
            ''.join(pattern),
            merge='',
            exclude={'ficheno__contains': 'M'}
        )
        self.update('NUMBER', ficheno)

        self.update('DATE', data.date_field.strftime('%d.%m.%Y'))

        self.update('SOURCE_WH', branch)
        self.update('SOURCE_DIVISION_NR', branch)


class ConsumptionConverter(BaseConverter):
    def after(self):
        data = self._input
        branch = data.sourceindex
        day = str(data.date_field).split()[0].split('-')

        pattern = [f'D.S{str(branch).zfill(3)}']
        pattern.append(day[2])
        pattern.append(day[1])
        pattern.append(day[0][-2:])

        ficheno = Stfiche.next_code(
            'ficheno',
            '0'*4,
            ''.join(pattern),
            merge='',
            exclude={'ficheno__contains': 'M'}
        )
        self.update('NUMBER', ficheno)

        self.update('DATE', data.date_field.strftime('%d.%m.%Y'))

        self.update('SOURCE_WH', branch)
        self.update('SOURCE_DIVISION_NR', branch)


class WasteConverter(BaseConverter):
    def after(self):
        data = self._input
        branch = data.sourceindex
        day = str(data.date_field).split()[0].split('-')

        pattern = [f'D.F{str(branch).zfill(3)}']
        pattern.append(day[2])
        pattern.append(day[1])
        pattern.append(day[0][-2:])

        ficheno = Stfiche.next_code(
            'ficheno',
            '0'*4,
            ''.join(pattern),
            merge='',
            exclude={'ficheno__contains': 'M'}
        )
        self.update('NUMBER', ficheno)

        self.update('DATE', data.date_field.strftime('%d.%m.%Y'))

        self.update('SOURCE_WH', branch)
        self.update('SOURCE_DIVISION_NR', branch)
