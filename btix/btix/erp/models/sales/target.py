"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_TARGETS(
    BaseLogical,
    BaseSiteRec,
    BaseSalesMan,
    BaseInfo,
    BaseRef,
    models.Model):
    """
        Satış elemanı hareketleri
    """
    code = models.CharField(
        db_column='CODE',
        max_length=17,
        blank=True,
        null=True,
        help_text='Hedef kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=51,
        blank=True,
        null=True,
        help_text='Hedef açıklaması'
    )
    typ = models.SmallIntegerField(
        db_column='TYP',
        blank=True,
        null=True,
        help_text='Hedef tipi'
    )
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True,
        help_text='Başlangıç tarihi'
    )
    enddate = models.DateTimeField(
        db_column='ENDDATE',
        blank=True,
        null=True,
        help_text='Bitiş tarihi'
    )
    stcode = models.CharField(
        db_column='STCODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Stok kodu'
    )
    stgroupcode = models.CharField(
        db_column='STGROUPCODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Stok grup kodu'
    )
    targetsaleamount = models.FloatField(
        db_column='TARGETSALEAMOUNT',
        blank=True,
        null=True,
        help_text='Hedef satış miktarı'
    )
    saleamountlimit = models.FloatField(
        db_column='SALEAMOUNTLIMIT',
        blank=True,
        null=True,
        help_text='Miktar sınırı'
    )
    netsaleamount = models.FloatField(
        db_column='NETSALEAMOUNT',
        blank=True,
        null=True,
        help_text='Net satış miktarı'
    )
    salediscountlimit = models.FloatField(
        db_column='SALEDISCOUNTLIMIT',
        blank=True,
        null=True,
        help_text='Satış indirim limiti'
    )
    saleexpenselimit = models.FloatField(
        db_column='SALEEXPENSELIMIT',
        blank=True,
        null=True,
        help_text='Satış masraf limiti'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_TARGETS'
        unique_together = (('salesmanref', 'code'),)
        target_db = 'erp'
