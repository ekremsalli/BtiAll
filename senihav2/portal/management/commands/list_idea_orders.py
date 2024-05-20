import logging
from datetime import datetime, date
import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

from erp.models.friendly import Clcard

from erp.active import Active
from erp.helpers import calculate_logo_time
from third_party.idea import Idea


class Command(BaseCommand):
    help = "Idea siparislerini cekme"

    def handle(self, *a, **kw):
        pass
        """
        sett = Active.settings['TRENDYOL']
        status = kw.get('status', None)
        size = kw.get('size', None)

        trendyol = Trendyol(**sett)
        orders = trendyol.collect_all_orders(status=status, size=size)
        for order in orders:
            pp(order)
        """
