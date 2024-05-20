import logging
from datetime import datetime, date
import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

from erp.models.friendly import Items

from erp.active import Active
from third_party.bazaars.trendyol import Trendyol
from third_party.bazaars.trendyol.models import (
    TrendyolProductMatch as TrendyolProductMatchTable
)

import logging
logger = logging.getLogger('app')


class Command(BaseCommand):
    help = "Stokları güncelle"

    def handle(self, *a, **kw):
        items = Items.objects.filter(projectref=1).exclude(name4='')
        prepared = list()
        for item in items:
            try:
                # is there any mapping?
                tpmt = TrendyolProductMatchTable.objects.filter(
                    erp_code=item.code).first()
                if tpmt is None:
                    product = item.code
                else:
                    product = tpmt.barcode

                quantity = int(item.name4)

                prepared.append({
                    'barcode': product,
                    'quantity': quantity if quantity > 0 else 0
                })
            except Exception as e:
                print(e)
                logger.error(
                    f'Geçersiz stok değeri {item.code} -> {item.name4}')
        logger.error('Active Stocks: {}'.format(json.dumps(prepared)))
        if prepared:
            sett = Active.settings['TRENDYOL']
            trendyol = Trendyol(**sett)
            result = trendyol.update_price_and_inventory(prepared)
            print(prepared)
            print(result, result.text)
