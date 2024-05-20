from django.conf import settings
from datetime import date, datetime, timedelta

from app.models.base import DB
from app.models import Anomalies, Employees, GecoGroups, Transactions, GecoDefs


class Syncing:
    year = date.today().year
    month = date.today().month
    start = datetime.today() - timedelta(days=3)
    end = datetime.today() + timedelta(days=1)
    db = DB.get_db('geco1')

    @staticmethod
    def sync_anomalies():
        if Syncing.db.is_active is False:
            raise CommandError(f'Database is inactive!')

        Anomalies.sync(Syncing.db, year=Syncing.year, month=Syncing.month, start=Syncing.start, end=Syncing.end)
        # print(f'Syncing anomalies')

    @staticmethod
    def sync_employees():
        if Syncing.db.is_active is False:
            raise CommandError(f'Database is inactive!')

        Employees.sync(Syncing.db)
        # print(f'Syncing employees')

    @staticmethod
    def sync_gecogroups():
        if Syncing.db.is_active is False:
            raise CommandError(f'Database is inactive!')

        GecoGroups.sync(Syncing.db)
        # print(f'Syncing gecogroups')

    @staticmethod
    def sync_gecodefs():
        if Syncing.db.is_active is False:
            raise CommandError(f'Database is inactive!')

        GecoDefs.sync(Syncing.db)
        # print(f'Syncing gecodefs')

    @staticmethod
    def sync_transaction():
        if Syncing.db.is_active is False:
            raise CommandError(f'Database is inactive!')

        Transactions.sync(Syncing.db, year=Syncing.year, month=Syncing.month, start=Syncing.start, end=Syncing.end)
        # print(f'Syncing transactions')
