import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import datetime
from django.contrib.contenttypes.models import ContentType


from app_v1.models import (
    SlipQue,
    SlipQueLog,
    TaskActivity,
    EmptyOperationError
)

import logging
logger = logging.getLogger('app')

class Command(BaseCommand):
    help = "Operate slip que"

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
                slips = SlipQue.objects.all()
            else:
                slips = SlipQue.waiting.all()

            if ids:
                slips = slips.filter(id__in=ids)
            if refs:
                slips = slips.filter(identifier__in=refs)

            for slip in slips:
                try:

                    result = SlipQue.generate_slip(
                        slip
                    )
                except EmptyOperationError as e:
                    SlipQueLog.objects.create(
                        content_type=ContentType.objects.get_for_model(slip),
                        object_id=slip.id,
                        exception=str(e)
                    )
                    slip.is_processed = True
                    slip.proccesed = datetime.now()
                    slip.save()
                except Exception as e:
                    logger.exception(e)
                    SlipQueLog.objects.create(
                        content_type=ContentType.objects.get_for_model(slip),
                        object_id=slip.id,
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
                            slip.is_processed = True
                            slip.proccesed = datetime.now()
                            slip.invoice_ref = result.flow.internal_ref
                            slip.flow = result.flow
                            slip.save()

                        if result.flow and 'Alacak toplam' in result.flow.response:
                            slip.is_cancelled = True
                            slip.cancellation_reason = 'Borç / alacak toplamı eşit değil!'
                            slip.save()
        except Exception as e:            
            TaskActivity.objects.create(
                name='slip_que',
                params=json.dumps(kw),
                is_success=False,
                exception=str(e)
            )
            logger.exception(e)
        else:  
            TaskActivity.objects.create(
                name='slip_que',
                params=json.dumps(kw),
                is_success=True,
                took=(datetime.now()-start).total_seconds()
            )