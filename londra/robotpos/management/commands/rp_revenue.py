from datetime import datetime
import logging

from django.core.management.base import CommandError
from django.contrib.contenttypes.models import ContentType

from bti.command import BCommand

from robotpos.models import (
    RevenueQue,
    RevenueQueLog,
)

logger = logging.getLogger('app')


class Command(BCommand):
    NAME = 'rp_revenue'

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
        parser.add_argument(
            '-r',
            '--ref',
            type=str,
            help='Refs',
            default=[],
            nargs='+'
        )
        parser.add_argument(
            '-f',
            '--force',
            action='store_true',
            help='Force'
        )
        parser.add_argument(
            '--max',
            type=int,
            default=20
        )

    def process(self, *args, **kwargs):
        ids = kwargs.get('id')
        refs = kwargs.get('ref')
        forced = kwargs.get('force')
        max_try = kwargs.get('max')

        if forced and len(ids) == 0 and len(refs) == 0:
            raise CommandError(
                'Force flag without id or ref is dangerous, please speficify id or ref.')

        if forced:
            revenues = RevenueQue.objects.prefetch_related('robotpos').all()
        else:
            revenues = RevenueQue.waiting.prefetch_related('robotpos').all()

        if ids:
            revenues = revenues.filter(pk__in=ids)

        if refs:
            revenues = revenues.filter(identifier__in=refs)

        for item in revenues:

            if forced is False and RevenueQueLog.objects.filter(
                content_type=ContentType.objects.get_for_model(item),
                object_id=item.id
            ).count() > max_try:
                item.is_cancelled = True
                item.cancellation_reason = f'Reached max try {max_try}'
                item.save()
                continue

            try:
                issues, lines = RevenueQue.check_payments(
                    item.get_data(),
                    item.robotpos
                )
                print(item, len(issues), len(lines))
                if issues:
                    item.is_cancelled = True
                    item.cancellation_reason = f'Unknown payment type'
                    item.save()
                    continue

                if len(lines) == 0:
                    item.is_cancelled = True
                    item.cancellation_reason = f'No transaction!'
                    item.save()
                    continue

                result = RevenueQue.generate_fiche(
                    lines,
                    item.robotpos
                )
            except Exception as e:
                logger.exception(e)
                RevenueQueLog.objects.create(
                    content_type=ContentType.objects.get_for_model(item),
                    object_id=item.id,
                    exception=str(e)
                )
            else:
                if result:
                    check = all([
                        result.flow,
                        result.flow.success,
                        result.flow.internal_ref
                    ])
                    RevenueQueLog.objects.create(
                        content_type=ContentType.objects.get_for_model(item),
                        object_id=item.id,
                        flow=result.flow,
                        is_success=check
                    )

                    if check:
                        item.is_processed = True
                        item.proccesed = datetime.now()
                        item.invoice_ref = result.flow.internal_ref
                        item.flow = result.flow
                        item.save()
