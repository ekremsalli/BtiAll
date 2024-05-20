from app.models import anomaly
import json

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from .base import BaseModel


class ApproveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(verify_status=0)


class SendManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(verify_status=1)


class Changes(BaseModel):
    VERIFY_STATUS = [
        (0, 'Onay bekliyor'),
        (1, 'Onaylanmış'),
        (2, 'Gönderilmiş'),
        (3, 'Reddedilmiş')
    ]
    status = None
    verify_status = models.SmallIntegerField(
        choices=VERIFY_STATUS,
        help_text='Onay durumu',
        db_index=True,
        default=0
    )
    geco_id = models.BigIntegerField(
        db_index=True,
        help_text='Gecotime kayıt numarası',
        null=True,
        blank=True
    )
    geco_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    snapshot = models.TextField(null=True, blank=True)
    updates = models.TextField(null=True, blank=True)
    is_remove_request = models.BooleanField(default=False)
    is_annual_off = models.BooleanField(default=False)
    start_annual = models.DateField(null=True, blank=True)
    start_annual_type = models.SmallIntegerField(null=True, blank=True)
    end_annual = models.DateField(null=True, blank=True)
    end_annual_type = models.SmallIntegerField(null=True, blank=True)
    annual_excuse_type = models.CharField(max_length=32, null=True, blank=True)

    tr_date = models.DateField(null=True, blank=True)
    employee = models.ForeignKey(
        'Employees',
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.SET_NULL
    )

    geco_anomaly_id = models.BigIntegerField(
        null=True, blank=True,
        db_index=True
    )
    anomaly = models.ForeignKey(
        'Anomalies', null=True, blank=True,
        on_delete=models.SET_NULL
    )
    transaction = models.ForeignKey(
        'Transactions', null=True, blank=True,
        on_delete=models.SET_NULL)

    sent_on = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Gönderim'
    )
    sent_by = models.ForeignKey(
        User,
        null=True,
        help_text='Gönderen',
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_sby'
    )

    waiting_for_approve = ApproveManager()
    waiting_for_send = SendManager()

    objects = models.Manager()

    class Meta:
        ordering = ['created_on']

    def annual_span(self):
        from geco.models import Ttagles
        from app.models.other import get_week_of_month
        from dateutil.rrule import rrule, DAILY
        records = []

        if self.is_annual_off:
            for dt in rrule(DAILY, dtstart=self.start_annual, until=self.end_annual):
                record = {}

                if dt.date() == self.start_annual:
                    excuse_day = self.start_annual_type - 1

                elif dt.date() == self.end_annual:
                    excuse_day = self.end_annual_type - 1

                else:
                    excuse_day = 0
                check = Ttagles.objects.using(self.source_db.code).filter(
                    tle_abwtag__isnull=False,
                    tle_datum__date=dt.date(),
                    tle_persnr=self.employee.nr).exists()

                if check is False:
                    record['excuse_day'] = excuse_day
                    record['day'] = dt.weekday()
                    record['employee'] = str(self.employee)
                    record['excuse'] = self.annual_excuse_type
                    record['tr_date'] = dt.strftime('%Y-%m-%d')
                    record['tr_day'] = dt.day
                    record['week'] = get_week_of_month(dt)
                    record['year'] = dt.year
                    record['month'] = dt.month
                    record['waiting'] = True
                    records.append(record)
        return records

    def send(self):
        from datetime import datetime, time
        import pytz
        from geco.models import Ttagles, Ttastab

        tz = pytz.timezone(settings.TIME_ZONE)
        target_db = self.source_db
        MAPP = settings.GECO_MAPPING[target_db.code]['M_TRANSACTION']

        if self.is_remove_request:
            try:
                instance = Ttagles.objects.using(target_db.code).get(
                    **{MAPP['geco_id']: self.geco_id})
                instance.delete(using=target_db.code)
                tas = Ttastab(
                    tas_erfdatum=self.tr_date,
                    tas_erfzeit=tz.localize(datetime.now()),
                    tas_taskart=0,
                    tas_persnr=self.employee.nr,
                    tas_vondatum=self.tr_date,
                    tas_bisdatum=self.tr_date,
                    tas_bearbprio=1
                )
                tas.save(using=target_db.code)
            except Exception as e:
                print(e)
                return False
            else:
                return True

        if self.is_annual_off:
            # 1 tam gün
            # 2 öö
            # 3 ös
            from dateutil.rrule import rrule, DAILY
            for dt in rrule(DAILY, dtstart=self.start_annual, until=self.end_annual):
                if dt.date() == self.start_annual:
                    work_time = self.start_annual_type - 1
                elif dt.date() == self.end_annual:
                    work_time = self.end_annual_type - 1
                else:
                    work_time = 0
               
                check = Ttagles.objects.using(self.source_db.code).filter(
                    tle_abwtag__isnull=False,
                    tle_abwtag=work_time,
                    tle_datum=dt,
                    tle_persnr=self.employee.nr).exists()
               
                checked = []
                if check is False:
                    record = {
                        'employee': self.employee.nr,
                        'tr_date': tz.localize(dt),
                        'work_time': None,
                        'excuse_type': self.annual_excuse_type,
                        'excuse_day': work_time,
                        'geco_user': f'b-{self.created_by.username}'[0:20],
                        'geco_time': tz.localize(datetime.now().today()),
                        'day_model': '818',
                    }

                    convert = {}
                    for kx, vx in record.items():
                        convert.update({MAPP[kx]: vx})

                    convert.update({
                        'tle_infkz': ''
                    })

                    
                    instance = Ttagles(**convert)
                    instance.save(using=target_db.code)
                    checked.append(instance)
           
            if checked:
                # tagles at
                min_start = datetime.combine(self.start_annual, time.min)
                max_end = datetime.combine(self.end_annual, time.max)

                tas = Ttastab(
                    tas_erfdatum=tz.localize(dt),
                    tas_erfzeit=tz.localize(datetime.now()),
                    tas_taskart=0,
                    tas_persnr=self.employee.nr,
                    tas_vondatum=min_start,
                    tas_bisdatum=max_end,
                    tas_bearbprio=1
                )
                tas.save(using=target_db.code)

                return True
            return False

        snapshot = json.loads(self.snapshot)
        updates = json.loads(self.updates)

        changes = {
            'tle_infkz': 'm',
            'tle_timestamp': tz.localize(datetime.now())
        }
        if self.created_by:
            changes.update({
                'tle_benutzer': f'b-{self.created_by.username}'[0:20]
            })
        if ('start' in snapshot and 'start' in updates and
                snapshot['start'] != updates['start']):
            changes.update({'tle_infkzko': 'm'})

        if ('end' in snapshot and 'end' in updates and
                snapshot['end'] != updates['end']):
            changes.update({'tle_infkzge': 'm'})

        for kx, vx in updates.items():
            if kx == 'tr_date' and vx:
                try:
                    vx = tz.localize(datetime.strptime(vx, '%Y-%m-%d'))
                except:
                    vx = None
            if kx == 'start' or kx == 'end':
                try:
                    vx = tz.localize(datetime.strptime(vx, '%H:%M'))
                except:
                    vx = None
            if vx:
                changes.update({MAPP[kx]: vx})

        if self.transaction:
            if self.geco_id:
                instance = Ttagles.objects.using(target_db.code).get(
                    **{MAPP['geco_id']: self.geco_id})
                for kx, vx in changes.items():
                    setattr(instance, kx, vx)

                instance.save(using=target_db.code)
                tas = Ttastab(
                    tas_erfdatum=self.tr_date,
                    tas_erfzeit=tz.localize(datetime.now()),
                    tas_taskart=0,
                    tas_persnr=self.employee.nr,
                    tas_vondatum=self.tr_date,
                    tas_bisdatum=self.tr_date,
                    tas_bearbprio=1
                )
                tas.save(using=target_db.code)
                return True
        else:
            changes.update({
                MAPP['employee']: self.employee.nr,
            })
            instance = Ttagles(**changes)
            instance.save(using=target_db.code)
            tas = Ttastab(
                tas_erfdatum=self.tr_date,
                tas_erfzeit=tz.localize(datetime.now()),
                tas_taskart=0,
                tas_persnr=self.employee.nr,
                tas_vondatum=self.tr_date,
                tas_bisdatum=self.tr_date,
                tas_bearbprio=1
            )
            tas.save(using=target_db.code)
            return True
        return False
