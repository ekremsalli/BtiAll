Prepare target_db in settings;
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('target_db',)


Setup primary router in settings;
DATABASE_ROUTERS = [
    'erp.db_router.PrimaryRouter'
]