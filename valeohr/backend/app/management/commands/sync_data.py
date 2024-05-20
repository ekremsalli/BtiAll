
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

class Command(BaseCommand):
    help = "Sync models"

    def add_arguments(self , parser):
        parser.add_argument('db', type=str, 
            help='target database')
        parser.add_argument(
            'model' , 
            nargs='+' , 
            type=str, 
            help='target model'
        )

    def handle(self, *a, **kw):
        from app.models.base import DB
        blacklist = ['db', 'changes']
        db_code = kw.get('db')
        if db_code not in settings.DATABASES.keys():
            raise CommandError(f'Unknown database! ({db_code})')

        db = DB.get_db(db_code)
        if db.is_active is False:
            raise CommandError(f'Database is inactive!')

        targets = kw.get('model')
        models = { 
            mod.__name__.lower() : mod
            for mod in apps.get_app_config('app').get_models() 
            if mod.__name__.lower() not in blacklist
        }
        if len(targets) == 1 and targets[0] == 'all':
            targets = models.keys()

        repr = ", ".join(list(models.keys()))
        for target in targets:
            if target.lower() in models:
                if hasattr(models[target], 'sync'):
                    print(f'Syncing {target.capitalize()}')
                    models[target].sync(db)
            else:
                raise CommandError(f"{target} not found in models! " \
                    f"(avail models: {repr})"
                )
                
