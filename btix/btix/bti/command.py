import logging
from datetime import datetime
import json

from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder


from bti.models import TaskActivity

import logging
logger = logging.getLogger('app')


class BCommand(BaseCommand):
    NAME = 'command'
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--disable-activity',
            action='store_true',
            help='Disable activity record'
        )

    def process(self, *a, **kw):
        pass

    def handle(self, *a, **kw):
        try:
            start = datetime.now()
            self.process(*a, **kw)
        except Exception as e:
            if 'disable_activity' not in kw or kw.get('disable_activity') is False:
                TaskActivity.objects.create(
                    name=self.NAME,
                    params=json.dumps(kw, cls=DjangoJSONEncoder),
                    is_success=False,
                    exception=str(e)
                )
            logger.exception(e)
        else:
            if 'disable_activity' not in kw or kw.get('disable_activity') is False:
                TaskActivity.objects.create(
                    name=self.NAME,
                    params=json.dumps(kw, cls=DjangoJSONEncoder),
                    is_success=True,
                    took=(datetime.now()-start).total_seconds()
                )