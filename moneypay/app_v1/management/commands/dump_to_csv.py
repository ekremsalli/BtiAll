import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from app_v1.models import (
    OpQue,
)

import logging
logger = logging.getLogger('app')

class Command(BaseCommand):
    help = "Dump opque data"

    def add_arguments(self , parser):
        parser.add_argument('--op_code', type=str, help='Op Code')
        parser.add_argument('day')

    def handle(self, *a, **kw):
        day = datetime.strptime(kw.get('day'), '%Y-%m-%d').date()
        op_code = kw.get('op_code', None)

        items = OpQue.objects.filter(day=day)
        if op_code:
            items = items.filter(op_code=op_code)

        rows = [item.get_data() for item in items]
        if rows:
            with open(f'/tmp/{day}-{op_code if op_code else "all"}.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
        else:
            print('No data!')
