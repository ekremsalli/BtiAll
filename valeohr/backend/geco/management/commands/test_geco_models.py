from datetime import datetime, date

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

from geco.models import *

class Command(BaseCommand):    
    help = "Test geco models"

    def add_arguments(self , parser):
        parser.add_argument('db' , type=str, help='target database')

    def handle(self, *a, **kw):
        db = kw.get('db')
        if db not in settings.DATABASES:
            raise CommandError(f'Unknown database! ({db})')
        errors = []
        for model in apps.get_app_config('geco').get_models():
            try:
                x1 = model.objects.using(db).filter().count()
                x2 = model.objects.using(db).filter()[0:10]
                if x2:
                    print(x2[0])
            except Exception as e:
                errors.append((model, e, db))
        print("="*10)
        for model, e, db in errors:
            print(model, e, db)
            print("-"*10)


