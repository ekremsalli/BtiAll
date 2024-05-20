import logging
from datetime import datetime, date
import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

from erp.models.friendly import Clcard

from erp.active import Active
from erp.helpers import calculate_logo_time
from third_party.bazaars.trendyol import Trendyol
from app.models import TrendyolCancelTrack
import logging
logger = logging.getLogger('app')


class Command(BaseCommand):
    help = "Trendyol iptal edilen siparisleri cekme"

    def handle(self, *a, **kw):
        sett = Active.settings['TRENDYOL']
        trendyol = Trendyol(
            username=sett['username'],
            password=sett['password'],
            supplier=sett['supplier']
        )
        orders = trendyol.collect_all_orders(status='Cancelled,UnSupplied')

        for order in orders:
            if TrendyolCancelTrack.control({
                'firm': Active.name,
                'identifier': order.get('orderNumber')}) is None:
                try:
                    TrendyolCancelTrack.cancel_order(order)
                    break
                except Exception as e:
                    logger.error(e)
                    raise e
