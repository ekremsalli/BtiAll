import logging

from erp.active import Active
from bti.command import BCommand

from robotpos.models import (
    Robotpos,
    RevenueQue,
    SalesQue,
)

logger = logging.getLogger('app')


class Command(BCommand):
    NAME = 'rp_push'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            '-i',
            '--id',
            type=int,
            help='IDs',
            default=[],
            nargs='+'
        )

    def process(self, *args, **kwargs):
        ids = kwargs.get('id')

        items = Robotpos.ready.filter()
        if ids:
            items = items.filter(pk__in=ids)

        for item in items:
            if item.genre == Robotpos.GENRES.branch_revenue:
                check = RevenueQue.control({
                    'firm': Active.name,
                    'identifier': item.get_identifier()
                })

                if check:
                    continue

                RevenueQue.create_request(
                    item,
                    item.get_identifier(),
                    item.get_data(),
                )

                item.is_accounted = True
                item.save()


            if item.genre == Robotpos.GENRES.sales:
                check = SalesQue.control({
                    'firm': Active.name,
                    'identifier': item.get_identifier()
                })

                if check:
                    continue

                SalesQue.create_request(
                    item,
                    item.get_identifier(),
                    item.get_data()
                )

                item.is_accounted = True
                item.save()
