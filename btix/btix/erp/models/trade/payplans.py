"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_PAYPLANS(
    BaseLogical,
    BaseWF,
    BaseSiteRec,
    BaseActive,
    BaseInfo,
    BaseCode,
    BaseRef,
    models.Model):
    """
        Ödeme planları
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=17,
        blank=True,
        null=True,
        help_text='Plan kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=201,
        blank=True,
        null=True,
        help_text='Plan açıklaması'
    )
    earlyinterest = models.FloatField(
        db_column='EARLYINTEREST',
        blank=True,
        null=True,
        help_text='Erken ödeme faiz oranı'
    )
    lateinterest = models.FloatField(
        db_column='LATEINTEREST',
        blank=True,
        null=True,
        help_text='Geç ödeme faiz oranı'
    )
    counter = models.IntegerField(
        db_column='COUNTER',
        blank=True,
        null=True,
        help_text='Kaç kere basıldığı'
    )
    wrkdays = models.SmallIntegerField(
        db_column='WRKDAYS',
        blank=True,
        null=True,
        help_text='Çalışma günleri'
    )
    ppgroupcode = models.CharField(
        db_column='PPGROUPCODE',
        max_length=17,
        blank=True,
        null=True
    )
    ppgroupref = models.IntegerField(
        db_column='PPGROUPREF',
        blank=True,
        null=True
    )
    bankaccref = models.IntegerField(
        db_column='BANKACCREF',
        blank=True,
        null=True
    )
    definition2 = models.CharField(
        db_column='DEFINITION2',
        max_length=201,
        blank=True,
        null=True
    )
    globalcode = models.CharField(
        db_column='GLOBALCODE',
        max_length=11,
        blank=True,
        null=True
    )
    sepdays = models.SmallIntegerField(
        db_column='SEPDAYS',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_PAYPLANS'
        unique_together = (('active', 'code'),)
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.definition_field}"
