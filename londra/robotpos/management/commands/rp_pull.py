from datetime import datetime
import logging
import json

from django.conf import settings
from dateutil.rrule import rrule, DAILY


from third_party.robotpos.api import API
from bti.command import BCommand
from erp.helpers import BtiJSONEncoder

from robotpos.models import Robotpos

logger = logging.getLogger('app')


class Command(BCommand):
    NAME = 'rp_pull'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            '-start',
            '--start',
            type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
            help='Start of range (Example: 2023-03-20)',
            default=None
        )

        parser.add_argument(
            '-end',
            '--end',
            type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
            help='End of range (Example 2023-03-20)',
            default=None
        )

        parser.add_argument(
            '-sales',
            '--sales',
            action='store_true',
            help='Collect sales'
        )

        parser.add_argument(
            '-revenue', 
            action='store_true',
            help='Collect revenue'
        )

        parser.add_argument(
            '-branch',
            '--branch',
            type=int,
            help='Branches, (Example -branch 506 or -branch 506 507 508)',
            default=[],
            nargs='+'
        )

        parser.add_argument(
            '-d',
            '--display', 
            action='store_true',
            help='Just display'
        )

        parser.add_argument(
            '-f',
            '--forced', 
            action='store_true',
            help='Force'
        )

    def pull(self, cmd, **kwargs):
        try:
            print('pull', cmd, kwargs)
            getattr(self.api, cmd)(**kwargs)
        except Exception as exp:
            self.api.error = str(exp)

    def save(self, forced, day, genre, branch):
        check = Robotpos.is_exists(
            day=day,
            genre=genre,
            branch=branch
        )

        print(forced, day, genre, branch)

        if forced:
            if check:
                record = Robotpos.objects.get(
                    day=day,
                    genre=genre,
                    branch=branch
                )
            if self.api.ok:
                if check:
                    data = json.dumps(self.api.data, cls=BtiJSONEncoder)
                    record.data = data
                    record.is_error = False
                    record.is_empty = len(self.api.data) == 0
                    record.last_synced = datetime.now()
                    record.save()
                    return record
            else:
                if check:
                    record.error = self.api.error
                    record.is_error = True
                    record.last_synced = datetime.now()
                    record.save()
                    return record
        else:
            if check is False:
                record = Robotpos(
                    day=day,
                    genre=genre,
                    branch=branch,
                )
                if self.api.ok:
                    data = json.dumps(self.api.data, cls=BtiJSONEncoder)
                    record.data = data
                    record.is_empty = len(self.api.data) == 0
                else:
                    record.last_error = self.api.error
                return record.save()
        return None

    def process(self, *args, **kwargs):
        self.api = API(
            url=settings.ROBOTPOS_URL,
            timeout=settings.ROBOTPOS_TIMEOUT
        )
        first = kwargs.get('start', None)
        last = kwargs.get('end', None)
        sales = kwargs.get('sales')
        revenue = kwargs.get('revenue')
        branches = kwargs.get('branch', None)
        display = kwargs.get('display')
        forced = kwargs.get('forced')

        if first:
            if last is None:
                last = first
        if last:
            if first is None:
                first = last

        if first and last and first > last:
            first, last = last, first

        if revenue == sales:
            revenue = True
            sales = True

        recent = (first == last) and last is None

        if branches:
            branches = [br for br in set(branches) if br in settings.ROBOTPOS_BRANCHES]
            if len(branches) == 0:
                branches = set(settings.ROBOTPOS_BRANCHES)
        else:
            branches = set(settings.ROBOTPOS_BRANCHES)

        if recent:
            for branch in branches:
                print(branch, sales, revenue)
                if sales:
                    self.pull('recent_sales', branch=branch)
                    if display:
                        if self.api.ok:
                            print(self.api.data)
                        else:
                            print(self.api.error)
                    else:
                        day, _ = self.api.day_span()
                        saved = self.save(forced, day, 'sales', branch)

                if revenue:
                    self.pull('recent_branch_revenue', branch=branch)
                    if display:
                        if self.api.ok:
                            print(self.api.data)
                        else:
                            print(self.api.error)
                    else:
                        day, _ = self.api.day_span()
                        saved = self.save(forced, day, 'branch_revenue', branch)
        else:
            for dt in rrule(DAILY, dtstart=first, until=last):
                print(dt.date())
                for branch in branches:
                    if sales:
                        spanned = self.api.span(dt.date())
                        self.pull(
                            'sales',
                            start=spanned[0],
                            end=spanned[1],
                            branch=branch
                        )
                        if display:
                            if self.api.ok:
                                print(self.api.data)
                            else:
                                print(self.api.error)
                        else:
                            saved = self.save(forced, dt.date(), 'sales', branch)

                    if revenue:
                        spanned = self.api.span(dt.date())
                        self.pull(
                            'branch_revenue',
                            start=spanned[0],
                            end=spanned[1],
                            branch=branch
                        )
                        if display:
                            if self.api.ok:
                                print(self.api.data)
                            else:
                                print(self.api.error)
                        else:
                            saved = self.save(forced, dt.date(), 'branch_revenue', branch)
