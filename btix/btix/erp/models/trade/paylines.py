"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_PAYLINES(
    BaseLogical,
    models.Model):
    """
        Ödeme planı satırları
    """
    payplanref = models.ForeignKey(
        "LG_PAYPLANS",
        db_column='PAYPLANREF',
        blank=True,
        null=True,
        help_text='Ödeme planı -> PAYPLANS',
        on_delete=models.DO_NOTHING
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    afterdays = models.SmallIntegerField(
        db_column='AFTERDAYS',
        blank=True,
        null=True,
        help_text='Tarihe eklenecek değer'
    )
    formula = models.CharField(
        db_column='FORMULA',
        max_length=31,
        blank=True,
        null=True,
        help_text='Formül'
    )
    condition = models.CharField(
        db_column='CONDITION',
        max_length=51,
        blank=True,
        null=True,
        help_text='Koşul'
    )
    day_field = models.CharField(
        db_column='DAY_',
        max_length=8,
        blank=True,
        null=True,
        help_text='Gün'
    )
    mounth = models.CharField(
        db_column='MOUNTH',
        max_length=6,
        blank=True,
        null=True,
        help_text='Ay'
    )
    year_field = models.CharField(
        db_column='YEAR_',
        max_length=6,
        blank=True,
        null=True,
        help_text='Yıl'
    )
    rndvalue = models.FloatField(
        db_column='RNDVALUE',
        blank=True,
        null=True,
        help_text='Yuvarlama tabanı'
    )
    absdate = models.DateTimeField(
        db_column='ABSDATE',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    datetype = models.SmallIntegerField(
        db_column='DATETYPE',
        blank=True,
        null=True,
        help_text='Tarih türü'
    )
    discrate = models.FloatField(
        db_column='DISCRATE',
        blank=True,
        null=True,
        help_text='İndirim oranı'
    )
    paymenttype = models.SmallIntegerField(
        db_column='PAYMENTTYPE', blank=True, null=True)
    bankaccref = models.IntegerField(
        db_column='BANKACCREF', blank=True, null=True)
    repaydefref = models.IntegerField(
        db_column='REPAYDEFREF', blank=True, null=True)
    trcurr = models.SmallIntegerField(
        db_column='TRCURR', blank=True, null=True)
    globalcode = models.CharField(
        db_column='GLOBALCODE', max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_PAYLINES'
        unique_together = (('payplanref', 'lineno_field'),)
        target_db = 'erp'
