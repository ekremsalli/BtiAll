import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import timedelta, datetime
from app_v1.models import (
    InvoiceBucket,
    InvoiceQue, 
    OpQue, 
    SlipQue,
    TaskActivity
)

import logging
logger = logging.getLogger('app')

class Command(BaseCommand):
    help = "Operate waiting data"

    def add_arguments(self , parser):
        parser.add_argument('--delta', type=int,
            nargs='?', help='Delta (day)', default=1)

        parser.add_argument(
            '-f', 
            '--force',
            action='store_true',
            help='Force'
        )    
        

    def handle(self, *a, **kw):
        try:
            start = datetime.now()
            delta = kw.get('delta')
            forced = kw.get('force')

            target = (datetime.now()-timedelta(days=delta)).date()

            if forced:
                items = OpQue.objects.filter(day=target)
            else:
                items = OpQue.waiting.filter(day=target)

            ops = set([item.op_code for item in items])
            cumulative = {
                op: {
                    'amount': [],
                    'total_amount': [],
                    'commission_amount': []
                }
                for op in ops
            }

            invoices = [
                item for item in items if item.is_invoice
            ]
            for invoice in invoices:
                try:
                    InvoiceBucket.create_request(
                        invoice.identifier,
                        invoice.get_data()
                    )
                except Exception as e:
                    logger.exception(e)
                else:
                    invoice.is_processed = True
                    invoice.processed = datetime.now()
                    invoice.save()
            subs = ['amount', 'total_amount', 'commission_amount']
            for item in items:
                data = json.loads(item.data)
                op = item.op_code
                for sub in subs:
                    cumulative[op][sub].append(data.get(sub))
                
            for code, op_data in cumulative.items():
                data = {}
                for sub in subs:
                    data.update({sub: sum(op_data[sub])})

                if forced:
                    SlipQue.objects.filter(day=target, op_code=code).delete()
                SlipQue.create_request(
                    target,
                    code,
                    data
                )
            
            items.update(is_processed=True, processed=datetime.now())
        except Exception as e:            
            TaskActivity.objects.create(
                name='process_que',
                params=json.dumps(kw),
                is_success=False,
                exception=str(e)
            )
            logger.exception(e)
        else:  
            TaskActivity.objects.create(
                name='process_que',
                params=json.dumps(kw),
                is_success=True,
                took=(datetime.now()-start).total_seconds()
            ) 


