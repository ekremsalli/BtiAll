"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_UNITBARCODE(
    BaseLogical,
    BaseItem,
    BaseInfo,
    BaseSiteRec,
    BaseRef,
    models.Model
    ):
    itmunitaref = models.IntegerField(
        db_column='ITMUNITAREF', blank=True, null=True)
    variantref = models.IntegerField(
        db_column='VARIANTREF', blank=True, null=True)
    unitlineref = models.IntegerField(
        db_column='UNITLINEREF', blank=True, null=True)
    linenr = models.SmallIntegerField(
        db_column='LINENR', blank=True, null=True)
    barcode = models.CharField(
        db_column='BARCODE', unique=True, max_length=101, blank=True, null=True)
    typ = models.SmallIntegerField(
        db_column='TYP', blank=True, null=True)
    wbarcodeshift = models.SmallIntegerField(
        db_column='WBARCODESHIFT', blank=True, null=True)
    globalid = models.CharField(
        db_column='GLOBALID', max_length=51, blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (
            ('itmunitaref', 'typ', 'linenr'),
            ('itemref', 'variantref', 'unitlineref', 'typ', 'linenr'),
        )
        db_table = f'LG_{Active.namespace}_UNITBARCODE'
        target_db = 'erp'
