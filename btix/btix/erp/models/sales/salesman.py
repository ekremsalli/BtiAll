"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_SLSMAN(
    BaseLogical,
    BaseSiteRec,
    BaseActive,
    BaseCode,
    BaseInfo,
    BaseRef,
    models.Model):
    """
        Satış elemanları
    """
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Satış elemanı kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True,
        help_text='Kart tipi'
    )
    position_field = models.CharField(
        db_column='POSITION_',
        max_length=11,
        blank=True,
        null=True,
        help_text='Satıcı pozisyon kodu'
    )
    userid = models.SmallIntegerField(
        db_column='USERID',
        blank=True,
        null=True
    )
    deptid = models.SmallIntegerField(
        db_column='DEPTID',
        blank=True,
        null=True
    )
    divisid = models.SmallIntegerField(
        db_column='DIVISID',
        blank=True,
        null=True
    )
    firmnr = models.SmallIntegerField(
        db_column='FIRMNR',
        blank=True,
        null=True
    )
    typ = models.SmallIntegerField(
        db_column='TYP',
        blank=True,
        null=True
    )
    telnumber = models.CharField(
        db_column='TELNUMBER',
        max_length=31,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'LG_SLSMAN'
        unique_together = (('firmnr', 'code'), ('firmnr', 'active', 'code'),)
        target_db = 'system'

    def __str__(self):
        return f"{self.code} {self.definition_field}"

class LG_SLSCLREL(
    BaseLogical,
    BaseSiteRec,
    BaseClient,
    BaseSalesMan,
    BaseRef,
    models.Model):
    """
        Satış elemanı - cari hesap ilişkisi
    """
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satıcı satır numarası'
    )
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True
    )
    visitday = models.SmallIntegerField(
        db_column='VISITDAY',
        blank=True,
        null=True
    )
    visitperiod = models.CharField(
        db_column='VISITPERIOD',
        max_length=51,
        blank=True,
        null=True
    )
    shipref = models.IntegerField(
        db_column='SHIPREF',
        blank=True,
        null=True
    )
    cllineno_field = models.SmallIntegerField(
        db_column='CLLINENO_',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_SLSCLREL'
        unique_together = (('salesmanref', 'lineno_field'),)
        target_db = 'erp'
