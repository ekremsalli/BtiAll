
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps
from datetime import date

class Command(BaseCommand):
    help = "List payrolls"

    def add_arguments(self , parser):
        parser.add_argument('db', type=str, 
            help='target database')

    def handle(self, *a, **kw):
        from app.models.base import DB
        db_code = kw.get('db')
        if db_code not in settings.DATABASES.keys():
            raise CommandError(f'Unknown database! ({db_code})')

        db = DB.get_db(db_code)
        if db.is_active is False:
            raise CommandError(f'Database is inactive!')

        from app.models.other import Payrolls
        start = date(2019, 12, 25)
        end = date(2020, 1, 24)
        results = Payrolls.query(db.code, start, end)
        from pprint import pprint as pp
        pp(results)