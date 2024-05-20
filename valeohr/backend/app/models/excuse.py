import json

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from .base import BaseModel
from geco.models import Ttagles, Ttastab, Ttagmos


class ApproveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(verify_status=0)


class SendManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(verify_status=1)


class Excuse(BaseModel):
    """Yeni mazeret oluşturma"""
    EXCUSE_DAY_TYPES = [
        (0, 'Tam gün'),
        (1, 'Öğleden önce'),
        (2, 'Öğleden sonra')
    ]
    DAY_TYPES = [
        (0, "Bugün"),
        (1, "SonrakiGün"),
        (-1, "Dün")
    ]
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
    day_types = models.SmallIntegerField(choices=DAY_TYPES, help_text="dün,bugün, sonrakigün", null=True, blank=True)
    employee_id = models.BigIntegerField(db_index=True,
                                         help_text='Sicil numarası', null=True, blank=True)
    tr_date = models.DateField(help_text='Hareket tarihi', null=True)
    start = models.DateTimeField(help_text='Giriş saati', null=True, blank=True)
    end = models.DateTimeField(help_text='Çıkış saati', null=True, blank=True)
    work_time = models.IntegerField(
        default=0,
        help_text='Çalışma süresi Saat * 100 + Dakika', null=True, blank=True
    )
    time_type = models.CharField(
        max_length=6, help_text='Zaman tipi',
        null=True, blank=True
    )
    excuse_type = models.CharField(
        max_length=5, help_text='Mazeret tipi',
        null=True, blank=True
    )
    excuse_day = models.SmallIntegerField(
        choices=EXCUSE_DAY_TYPES,
        null=True, blank=True
    )
    day_model = models.CharField(
        max_length=5, help_text='Gün modeli kayıt numarası',
        null=True, blank=True
    )
    account = models.CharField(
        max_length=20, help_text='Hesaplama grubu',
        null=True, blank=True
    )
    pay_type = models.CharField(
        max_length=6, help_text='Puantaj tipi',
        null=True, blank=True
    )
    geco_user = models.CharField(
        max_length=20,
        help_text='Geco kaydını düzenleyen kullanıcı',
        null=True, blank=True
    )
    description = models.TextField(blank=True, null=True)

    waiting_for_approve = ApproveManager()
    waiting_for_send = SendManager()

    objects = models.Manager()

    class Meta:
        db_table = 'excuse'

    def approve(self, verify_status):
        self.verify_status = verify_status
        self.save()

    def send_approve(self, data, db):
        from datetime import datetime, time
        import pytz
        # tz.localize(datetime.now())
        tz = pytz.timezone(settings.TIME_ZONE)

        date1 = data['tle_vonzeit']
        date2 = data['tle_biszeit']
        difference = date2 - date1
        hours = difference.seconds // 3600
        minutes = (difference.seconds // 60) % 60
        time_diff = float(f"{hours}.{minutes}")

        obj = Ttagles(tle_persnr=data['tle_persnr'],
                      tle_datum=data['tle_datum'],
                      tle_vonzeit=tz.localize(data['tle_vonzeit']),
                      tle_biszeit=tz.localize(data['tle_biszeit']),
                      tle_istzeit=time_diff,
                      tle_zeitart=data['tle_zeitart'],
                      tle_abwart=data['tle_abwart'],
                      tle_abwtag=data['tle_abwtag'],
                      tle_perkstnr=data['tle_perkstnr'],
                      tle_tagmod=data['tle_tagmod'],
                      tle_benutzer=data['tle_benutzer'],
                      tle_beginnkz=data['tle_beginnkz'],
                      tle_infkz="",
                      tle_info=data['tle_info'],
                      tle_timestamp=data['tle_timestamp'])
        obj.save(using=db)

        from django.db import connections
        conn = connections[db]
        with conn.cursor() as cursor:
            cursor.execute("UPDATE TTagMoS  SET TMS_TagMod = %s WHERE TMS_PersNr = %s AND TMS_Datum = %s",
                           [data['tle_tagmod'], data['tle_persnr'], data['tle_datum']])
        # TtagmoS.objects.filter(tms_persnr=data['tle_persnr'], tms_datum=data['tle_datum']).update(tms_tagmod=data['tle_tagmod'])

        tas = Ttastab(
            tas_erfdatum=data['tle_datum'],
            tas_erfzeit=tz.localize(datetime.now()),
            tas_taskart=0,
            tas_persnr=data['tle_persnr'],
            tas_vondatum=data['tle_datum'],
            tas_bisdatum=data['tle_datum'],
            tas_bearbprio=1
        )
        tas.save(using=db)
        return ""
