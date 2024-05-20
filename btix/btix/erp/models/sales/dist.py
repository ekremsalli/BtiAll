"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_DISTLINE(
    BaseLogical,
    BaseItem,
    models.Model
    ):
    """
        Dağıtım şablonu satırları
    """
    disttempref = models.ForeignKey(
        "LG_DISTTEMP",
        db_column='DISTTEMPREF',
        blank=True,
        null=True,
        help_text='Dağıtım şablonu referansı -> DISTTEMP',
        on_delete=models.DO_NOTHING
    )
    distfact = models.FloatField(
        db_column='DISTFACT',
        blank=True,
        null=True,
        help_text='Dağıtım katsayısı'
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    variantref = models.IntegerField(db_column='VARIANTREF', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_DISTLINE'
        unique_together = (('disttempref', 'lineno_field'),)
        target_db = 'erp'

class LG_DISTTEMP(
    BaseLogical,
    BaseItem,
    BaseSiteRec,
    BaseInfo,
    BaseCode,
    BaseRef,
    models.Model):
    """
        Dağıtım şablonu
    """
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Dağıtım şablonu kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Dağıtım şablon açıklaması'
    )
    uomref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UOMREF',
        blank=True,
        null=True,
        help_text='Birim ref. -> UNITSETL',
        on_delete=models.DO_NOTHING
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
    barcode = models.CharField(
        db_column='BARCODE',
        max_length=25,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_DISTTEMP'
        unique_together = (
            ('itemref', 'code', 'uomref'),
        )
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"