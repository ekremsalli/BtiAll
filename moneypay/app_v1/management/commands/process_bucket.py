import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import timedelta, datetime
from django.contrib.contenttypes.models import ContentType


from erp.models.friendly import Invoice
from app_v1.models import (
    InvoiceBucket,
    InvoiceQue,
    InvoiceQueLog,
    TaskActivity
)

import logging
logger = logging.getLogger('app')

class Command(BaseCommand):
    help = "Operate invoice bucket que"

    def add_arguments(self , parser):
        parser.add_argument(
            '-i',
            '--id', 
            type=int, 
            help='IDs', 
            default=[],
            nargs='+'
        )
        parser.add_argument(
            '-r',
            '--ref', 
            type=str, 
            help='Refs', 
            default=[],
            nargs='+'
        ) 
        parser.add_argument(
            '-f', 
            '--force',
            action='store_true',
            help='Force'
        )    
        

    def handle(self, *a, **kw):
        try:
            start = datetime.now()            
            ids = kw.get('id')
            refs = kw.get('ref')
            forced = kw.get('force')
            if forced and len(ids) == 0 and len(refs) == 0:
                raise CommandError(
                    'Force flag without id or ref is dangerous, please speficify id or ref.')
            

            # generate companies
            for item in InvoiceBucket.waiting.filter(is_company=True):
                InvoiceQue.create_request(
                    True,
                    item.identifier,
                    '',
                    [item]
                )
                item.is_processed = True
                item.proccesed = datetime.now()    
                item.save()

            # group via day and uid
            days = set(
                InvoiceBucket.waiting.filter(
                    is_company=False).values_list('day', flat=True)
            )
            for day in days:
                uids = set(InvoiceBucket.waiting.filter(
                    is_company=False,
                    day=day
                ).values_list('uid', flat=True))

                for uid in uids:
                    qs = InvoiceBucket.waiting.filter(
                        is_company=False,
                        day=day,
                        uid=uid
                    )
                    identifier = f'{day}-{uid}'
                    InvoiceQue.create_request(
                        False,
                        identifier,
                        '',
                        qs
                    )
                    for item in qs:
                        item.is_processed = True
                        item.proccesed = datetime.now()    
                        item.save()

        except Exception as e:            
            TaskActivity.objects.create(
                name='process_bucket',
                params=json.dumps(kw),
                is_success=False,
                exception=str(e)
            )
            logger.exception(e)
        else:  
            TaskActivity.objects.create(
                name='process_bucket',
                params=json.dumps(kw),
                is_success=True,
                took=(datetime.now()-start).total_seconds()
            ) 


