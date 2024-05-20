from django.db import models
from django.conf import settings

from .base import BaseModel, ActiveManager, DeletedManager
import logging

logger = logging.getLogger("app")

class Anomalies(BaseModel):
    employee = models.ForeignKey(
        'Employees',
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_employee',
        db_index=True
    )
    tr_date = models.DateField(
        help_text='Anormallik tarihi',
        db_index=True
    )
    ano_type = models.IntegerField(help_text='Sapma kodu')
    ano_text = models.CharField(max_length=255, db_index=True)
    description = models.TextField(null=True, blank=True)
    geco_id = models.BigIntegerField(
        help_text='Gecotime kayıt numarası',
        db_index=True
    )
    geco_time = models.DateTimeField()

    active_objects = ActiveManager()
    deleted_objects = DeletedManager()
    objects = models.Manager()

    class Meta:
        ordering = ['-tr_date']

    @classmethod
    def sync(cls, db, year=None, month=None, start=None, end=None):
        from datetime import date, datetime
        import calendar
        from geco.models import Tnrmabw
        from app.models import Employees
        logger.info("Model/Anamolia/Sync Fonksiyonu Başladı ")
        bulk_size = 500
        bulk_op = lambda n: [n[i:i + bulk_size] for i in range(0, len(n), bulk_size)]

        if year is None:
            year = date.today().year
        if month is None:
            month = date.today().month

        MAPP = settings.GECO_MAPPING.get(db.code).get('M_ANOMALIES')

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

        for anom in Tnrmabw.objects.using(db.code).filter(
                nrm_datum__range=tr_range):
                # nrm_normabwkennung=3,
                # nrm_timestamp__range=tr_range

            employee = employees[getattr(anom, MAPP['employee'])] if (getattr(anom, MAPP['employee']) and
                                                                      getattr(anom,
                                                                              MAPP['employee']) in employees) else None

            record = {
                'source_db': db,
                'status': 0,
                'employee': employee,
                'tr_date': getattr(anom, MAPP['tr_date']),
                'ano_type': getattr(anom, MAPP['ano_type']),
                # 'ano_text': getattr(anom, MAPP['ano_text']),
                'geco_id': getattr(anom, MAPP['geco_id']),
                'geco_time': getattr(anom, MAPP['geco_time'])
            }

            if getattr(anom, MAPP['ano_text']) is None:
                record.update({
                    'ano_text': "",
                })
            else:
                record.update({
                    'ano_text': getattr(anom, MAPP['ano_text']),
                })

            if anom.idnr in exists:
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
            "employee", "tr_date",
            "ano_type", "ano_text",
            "modified_on"
        ]

        for field in fields:
            tmp = [rec for rec in records if getattr(rec, field) is not None]
            cls.objects.bulk_update(tmp, [field])
        logger.info("Model/Anamolia/Sync Fonksiyonu Bitti ")