from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import datetime


class Command(BaseCommand):
    help = "Sync transactions"

    def add_arguments(self , parser):
        parser.add_argument('db', type=str, 
            help='target database')
        parser.add_argument('year' , type=int, 
            help='filtered year', 
            default=datetime.now().year,
            nargs='?'
        )
        parser.add_argument('month' , type=int, 
            help='filtered month', 
            default=[datetime.now().month],
            nargs='?'
        )


    def handle(self, *a, **kw):
        from app.models.base import DB
        from app.models import Transactions
        
        db_code = kw.get('db')
        if db_code not in settings.DATABASES.keys():
            raise CommandError(f'Unknown database! ({db_code})')
        db = DB.get_db(db_code)

        if db.is_active is False:
            raise CommandError(f'Database is inactive!')

        print(f'Syncing transactions')
        year = kw.get('year')
        months = kw.get('month')

        for month in months:
            Transactions.sync(db, year=year, month=month)
                
