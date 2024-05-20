"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class L_DAILYEXCHANGES(models.Model):
    """
        Günlük döviz kurları
    """
    lref = models.AutoField(
        db_column='LREF',
        primary_key=True,
        help_text='Fiziksel adres'
    )
    date_field = models.IntegerField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    crtype = models.SmallIntegerField(
        db_column='CRTYPE',
        blank=True,
        null=True,
        help_text='Döviz türü'
    )
    rates1 = models.FloatField(
        db_column='RATES1',
        blank=True,
        null=True,
        help_text='Oran 1'
    )
    rates2 = models.FloatField(
        db_column='RATES2',
        blank=True,
        null=True,
        help_text='Oran 2'
    )
    rates3 = models.FloatField(
        db_column='RATES3',
        blank=True,
        null=True,
        help_text='Oran 3'
    )
    rates4 = models.FloatField(
        db_column='RATES4',
        blank=True,
        null=True,
        help_text='Oran 4'
    )
    edate = models.DateTimeField(
        db_column='EDATE',
        blank=True,
        null=True
    )
    globalid = models.CharField(
        db_column='GLOBALID',
        max_length=51,
        blank=True,
        null=True
    )
    approve = models.SmallIntegerField(
        db_column='APPROVE',
        blank=True,
        null=True
    )
    approvedate = models.IntegerField(
        db_column='APPROVEDATE',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'L_DAILYEXCHANGES'
        unique_together = (
            ('crtype', 'date_field'),
            ('date_field', 'crtype'),
            ('crtype', 'edate', 'lref'),
            ('edate', 'crtype', 'lref'),
        )
        target_db = 'system'
