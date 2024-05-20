import logging
from datetime import datetime, date
import json
from pprint import pprint as pp

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

from erp.models.friendly import Clcard

from erp.active import Active
from erp.helpers import calculate_logo_time
from third_party.bazaars.trendyol import Trendyol
from app.models import TrendyolTrack


class Command(BaseCommand):
    help = "Trendyol siparislerini cekme"

    def add_arguments(self, parser):
        parser.add_argument('status', type=str, nargs='?', default='Created')
        parser.add_argument('size', type=int, nargs='?', default=10)

    def handle(self, *a, **kw):
        sett = Active.settings['TRENDYOL']
        status = kw.get('status', None)
        size = kw.get('size', None)

        trendyol = Trendyol(**sett)
        orders = trendyol.collect_all_orders(status=status, size=size)
        for order in orders:
            pp(order)
