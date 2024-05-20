import json
from django.core.management.base import BaseCommand
from datetime import datetime
from django.core.management import call_command

from app_v1.models import TaskActivity


import logging
logger = logging.getLogger('app')

class Command(BaseCommand):
    help = "Process all"

  
    def handle(self, *a, **kw):
        try:
            start = datetime.now()  
            commands = [
                'process_que',
                'process_bucket',
                'slip_que',
                'invoice_que',
            ]
            for cmd in commands:
                result = call_command(cmd)
                if result:
                    print(result)        

        except Exception as e:            
            TaskActivity.objects.create(
                name='process_all',
                params=json.dumps(kw),
                is_success=False,
                exception=str(e)
            )
            logger.exception(e)
        else:  
            TaskActivity.objects.create(
                name='process_all',
                params=json.dumps(kw),
                is_success=True,
                took=(datetime.now()-start).total_seconds()
            ) 


