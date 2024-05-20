"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

class PrimaryRouter:
    def db_for_read(self, model, **hints):
        if hasattr(model._meta, "target_db"):
            return model._meta.target_db

        return 'default'

    def db_for_write(self, model, **hints):
        if hasattr(model._meta, "target_db"):
            return model._meta.target_db
        return 'default'
        

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True
