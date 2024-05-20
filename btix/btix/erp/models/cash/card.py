"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_KSCARD(
    BaseLogical,
    BaseCode,
    BaseInfo,
    BaseActive,
    BaseSiteRec,
    BaseWF,
    BaseGUID,
    BaseBranch,
    BaseRef,
    models.Model):
    """
        Kasalar
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=17,
        blank=True,
        null=True,
        help_text='Hesap kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Hesap ismi'
    )
    explain = models.CharField(
        db_column='EXPLAIN',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    addr1 = models.CharField(
        db_column='ADDR1',
        max_length=51,
        blank=True,
        null=True,
        help_text='Adres satırı'
    )
    addr2 = models.CharField(
        db_column='ADDR2',
        max_length=51,
        blank=True,
        null=True,
        help_text='Adres satırı'
    )
    ccurrency = models.SmallIntegerField(
        db_column='CCURRENCY',
        blank=True,
        null=True
    )
    curratetype = models.SmallIntegerField(
        db_column='CURRATETYPE', blank=True, null=True)
    fixedcurrtype = models.SmallIntegerField(
        db_column='FIXEDCURRTYPE', blank=True, null=True)
    usedinperiods = models.SmallIntegerField(
        db_column='USEDINPERIODS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_KSCARD'
        unique_together = (('active', 'code'),)
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"