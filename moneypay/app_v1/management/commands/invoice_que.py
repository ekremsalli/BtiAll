import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import timedelta, datetime
from django.contrib.contenttypes.models import ContentType


from erp.models.friendly import Invoice
from app_v1.models import (
    InvoiceQue,
    InvoiceQueLog,
    TaskActivity
)

import logging
logger = logging.getLogger('app')

class Command(BaseCommand):
    help = "Operate invoice que"

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
            
            if forced:
                invoices = InvoiceQue.objects.all()
            else:
                invoices = InvoiceQue.waiting.all()

            if ids:
                invoices = invoices.filter(id__in=ids)
            if refs:
                invoices = invoices.filter(identifier__in=refs)

            for invoice in invoices:
                if Invoice.objects.filter(
                    doctrackingnr=invoice.identifier).exists():
                    invoice.is_cancelled = True
                    invoice.cancellation_reason=f'Already invoiced!: {invoice.identifier}'
                    continue

                try:
                    result = InvoiceQue.generate_invoice(invoice)          
                except Exception as e:
                    logger.exception(e)
                    InvoiceQueLog.objects.create(
                        content_type=ContentType.objects.get_for_model(invoice),
                        object_id=invoice.id,
                        exception=str(e)                        
                    )
                else:
                    if result:
                        check = all([
                            result.flow, 
                            result.flow.success, 
                            result.flow.internal_ref
                        ])
                        if check:
                            invoice.is_processed = True
                            invoice.proccesed = datetime.now()
                            invoice.invoice_ref = result.flow.internal_ref
                            invoice.flow = result.flow
                            invoice.save()            

        except Exception as e:            
            TaskActivity.objects.create(
                name='invoice_que',
                params=json.dumps(kw),
                is_success=False,
                exception=str(e)
            )
            logger.exception(e)
        else:  
            TaskActivity.objects.create(
                name='invoice_que',
                params=json.dumps(kw),
                is_success=True,
                took=(datetime.now()-start).total_seconds()
            ) 


