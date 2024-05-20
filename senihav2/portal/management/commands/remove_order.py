import logging
from datetime import datetime, date
import json
from pprint import pprint as pp

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps


from erp.active import Active
from third_party.bazaars.trendyol.models import (
    TrendyolLog,
    TrendyolLineLog,
)
from app.models import TrendyolStatusLog, ArvatoLog
from app.models import TrendyolTrack


class Command(BaseCommand):
    help = "Trendyol siparislerini sil"

    def add_arguments(self, parser):
        parser.add_argument('order', type=str, nargs='+', help='Order numbers', default=[])

    def handle(self, *a, **kw):
        sett = Active.settings['TRENDYOL']
        orders = kw.get('order')
        for order in orders:
            log = TrendyolLog.objects.filter(order_number=order).first()
            if log:
                print(TrendyolStatusLog.objects.filter(trendyol=log).delete())
                print(ArvatoLog.objects.filter(trendyol=log).delete())
                print(TrendyolLineLog.objects.filter(log=log).delete())
                print(TrendyolTrack.objects.filter(identifier=order).delete())
                print(log.delete())
            else:
                print(f'Unknown order -> {order}')

