from pprint import pprint as pp
from django.core.management.base import BaseCommand, CommandError


from erp.active import Active
from third_party.idea.api import Idea


class Command(BaseCommand):
    help = "Idea kargo firmalarını listeleme"

    def handle(self, *a, **kw):
        try:
            idea = Idea(Active.settings['IDEA']['URL'])
            idea.read_token_from_ini(Active.settings['IDEA']['TOKEN_PATH'])
        except Exception as e:
            raise Exception('Token dosyası okunamadı!')
        else:
            pp(idea.shipping_companies(limit=100))