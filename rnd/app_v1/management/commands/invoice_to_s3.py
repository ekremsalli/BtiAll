import logging
from datetime import datetime, date

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps


from erp.active import Active
from erp.models.friendly import Invoice

class Command(BaseCommand):
    help = "e-Logoda oluşturulan faturaların - S3'e aktarımı"

    def handle(self, *a, **kw):
        print(Invoice.objects.filter(grpcode=2))
        pass
        #Invoice.objects.filter()
