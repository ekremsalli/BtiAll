import logging
import json

from django.core.management.base import BaseCommand


from app.models import ArvatoLog 
import logging
logger = logging.getLogger('app')



class Command(BaseCommand):
    help = "Check arvato log"

    def add_arguments(self , parser):        
        parser.add_argument(
            '-r',
            '--ref', 
            type=str, 
            help='Refs', 
            nargs='?'
        )   

    def handle(self, *a, **kw):
        for item in ArvatoLog.objects.filter():
            req = json.loads(item.request)
            for xitem in req['ItemList']:
                print("check:", xitem['orderNumber'])
                if str(xitem['orderNumber']) == kw.get('ref'):
                    print('match:', item.id)

