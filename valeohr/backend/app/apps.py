from django.apps import AppConfig


class AppConfig(AppConfig):

    name = 'app'

    def ready(self):
        from .jobs import updater
        updater.start()

