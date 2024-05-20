import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from app_v1.operations import ARPOperation

class Command(BaseCommand):
    help = "Bulk clcard operation"

    def add_arguments(self , parser):
        parser.add_argument('file', type=str, 
            help='JSON file')

    def handle(self, *a, **kw):
        try:
            with open(kw.get('file'), 'r') as fp:
                cards = json.load(fp)
                for card in cards:
                    ARPOperation.create_or_update(card)

        except Exception as e:
            raise CommandError(e)
