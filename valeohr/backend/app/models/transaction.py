from django.db import models
from django.conf import settings

from .base import BaseTransaction, ActiveManager, DeletedManager

import logging
logger = logging.getLogger("app")

class Transactions(BaseTransaction):
    geco_id = models.BigIntegerField(
        db_index=True,
        help_text='Gecotime kayıt numarası'
    )
    geco_time = models.DateTimeField(null=True, blank=True)

    active_objects = ActiveManager()
    deleted_objects = DeletedManager()
    objects = models.Manager()

    class Meta:
        ordering = ["geco_time"]

    @classmethod
    def sync(cls, db, year=None, month=None, start=None, end=None):
        from datetime import date, datetime
        import calendar
        from geco.models import Ttagles
        from app.models import Employees
        logger.info("Model/Transaction/Sync Fonksiyonu Başladı ")
        MAPP = settings.GECO_MAPPING[db.code].get('M_TRANSACTION')
        bulk_size = 500
        bulk_op = lambda n: [n[i:i + bulk_size] for i in range(0, len(n), bulk_size)]

        if year is None:
            year = date.today().year
        if month is None:
            month = date.today().month

        _, dend = calendar.monthrange(year, month)
        tr_range = []
        if start is not None:
            tr_range.append(start)
        if end is not None:
            tr_range.append(end)

        if len(tr_range) == 0:
            tr_range = [date(year, month, 1), date(year, month, dend)]

        exists = set(cls.objects.filter(
            source_db=db,
            tr_date__range=tr_range
        ).values_list('geco_id', flat=True))
        employees = {
            emp.nr: emp
            for emp in Employees.objects.filter(source_db=db)
        }
        newbies, updates, found = [], [], set([])
        for tr in Ttagles.objects.using(db.code).filter(
                tle_datum__range=tr_range):

            employee = employees[getattr(tr, MAPP['employee'])] if (getattr(tr, MAPP['employee']) and
                                                                    getattr(tr,
                                                                            MAPP['employee']) in employees) else None
            record = {
                'source_db': db,
                'status': 0,
                'employee': employee,
                'tr_date': getattr(tr, MAPP['tr_date']),
                'start': getattr(tr, MAPP['start']),
                'end': getattr(tr, MAPP['end']),
                'work_time': getattr(tr, MAPP['work_time']) if getattr(tr, MAPP['work_time']) else 0,
                'time_type': getattr(tr, MAPP['time_type']),
                'excuse_type': getattr(tr, MAPP['excuse_type']),
                'excuse_day': getattr(tr, MAPP['excuse_day']),
                'day_model': getattr(tr, MAPP['day_model']),
                'account': getattr(tr, MAPP['account']),
                'pay_type': getattr(tr, MAPP['pay_type']),
                'geco_user': getattr(tr, MAPP['geco_user']),
                'geco_id': getattr(tr, MAPP['geco_id']),
                'geco_time': getattr(tr, MAPP['geco_time']) if getattr(tr, MAPP['geco_time']) else None
            }
            if getattr(tr, MAPP['geco_id']) in exists:
                record.update({'modified_on': datetime.now()})
                updates.append(record)
            else:
                newbies.append(cls(**record))
            found.add(record['geco_id'])

        diffs = list(exists.difference(found))

        for group in bulk_op(diffs):
            cls.objects.filter(
                source_db=db,
                tr_date__range=tr_range,
                geco_id__in=group
            ).update(status=-1)

        geco_ids = {rec['geco_id']: rec for rec in updates}
        gkeys = list(geco_ids.keys())

        records = []
        for group in bulk_op(gkeys):
            records.extend(cls.objects.filter(
                source_db=db,
                tr_date__range=tr_range,
                geco_id__in=group
            ))

        for item in records:
            for kx, vx in geco_ids[item.geco_id].items():
                setattr(item, kx, vx)

        cls.objects.bulk_create(newbies)

        fields = [
            'employee', 'tr_date', 'start',
            'end', 'work_time', 'time_type',
            'excuse_type', 'excuse_day',
            'day_model', 'account', 'pay_type',
            'geco_user', 'geco_id', 'geco_time',
            'modified_on'
        ]
        for field in fields:
            tmp = [rec for rec in records if getattr(rec, field) is not None]
            cls.objects.bulk_update(tmp, [field])
        logger.info("Model/Transaction/Sync Fonksiyonu Bitti ")