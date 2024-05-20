import logging
from datetime import datetime, date
import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

from erp.active import Active
from app.models import ArvatoTrack
from third_party.bazaars.trendyol.models import (
    TrendyolLog
)

from app.arvato import Arvato

import logging
logger = logging.getLogger('app')


class Command(BaseCommand):
    help = "Logoya aktarılmış trendyol siparişlerini arvatoya aktarır"

    def handle(self, *a, **kw):
        transferred = ArvatoTrack.objects.filter(
            firm=Active.name).values_list('identifier', flat=True)

        items = TrendyolLog.objects.exclude(
            internal_ref__isnull=True).exclude(
                order_number__in=transferred
            )

        arvato = Arvato(*Active.settings['ARVATO']['API'].values())
        arvato.generate_token()


        for item in items:
            order = json.loads(item.raw)
            try:
                ArvatoTrack.create_sales_order(order, arvato_token=arvato.token)
            except Exception as e:
                logger.error(e)
