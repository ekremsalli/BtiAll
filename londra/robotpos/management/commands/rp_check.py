from datetime import datetime, timedelta
import logging

from django.conf import settings

from third_party.robotpos.api import API
from bti.command import BCommand

from robotpos.models import Robotpos

logger = logging.getLogger('app')


class Command(BCommand):
    NAME = 'rp_check'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            '--delta',
            type=int,
            default=40,
            help='Delta'
        )

        parser.add_argument(
            '-d',
            '--display', 
            action='store_true',
            help='Just display'
        )

    def pull(self, cmd, **kwargs):
        try:
            getattr(self.api, cmd)(**kwargs)
        except Exception as exp:
            self.api.error = str(exp)

    def process(self, *args, **kwargs):
        self.api = API(
            url=settings.ROBOTPOS_URL,
            timeout=settings.ROBOTPOS_TIMEOUT
        )

        delta = kwargs.get('delta')
        display = kwargs.get('display')

        yesterday = (datetime.today() - timedelta(days=1)).date()
        start = (datetime.today() - timedelta(days=delta)).date()

        if display:
            print(start, yesterday)
            return

        items = Robotpos.waiting.filter(
            day__gte=start,
            day__lte=yesterday
        )

        for item in items:
            spanned = self.api.span(item.day)
            self.pull(
                item.genre,
                start=spanned[0],
                end=spanned[1],
                branch=item.branch
            )
            if self.api.ok:
                item.data = self.api.data
                item.is_empty = len(self.api.data) == 0
                item.is_error = False
                item.last_synced = datetime.now()
                item.save()
            else:
                item.is_error = True
                item.last_error = self.api.error
                item.last_synced = datetime.now()
                item.save()
