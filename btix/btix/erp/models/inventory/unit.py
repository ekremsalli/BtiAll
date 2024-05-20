"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_ITMUNITA(
    BaseLogical,
    BaseItem,
    BaseSiteRec,
    models.Model):
    """
        Malzeme-birim ataması
    """
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    unitlineref = models.ForeignKey(
        'LG_UNITSETL',
        db_column='UNITLINEREF',
        blank=True,
        null=True,
        help_text='Brim ref. UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_unitlineref"        
    )
    barcode = models.CharField(
        db_column='BARCODE',
        max_length=101,
        blank=True,
        null=True,
        help_text='Barkod'
    )
    mtrlclas = models.SmallIntegerField(
        db_column='MTRLCLAS',
        blank=True,
        null=True,
        help_text='Kullanım yeri malzeme yönetimi'
    )
    purchclas = models.SmallIntegerField(
        db_column='PURCHCLAS',
        blank=True,
        null=True,
        help_text='Kullanım yeri satınalma'
    )
    salesclas = models.SmallIntegerField(
        db_column='SALESCLAS',
        blank=True,
        null=True,
        help_text='Kullanım yeri satış'
    )
    mtrlpriority = models.SmallIntegerField(
        db_column='MTRLPRIORITY',
        blank=True,
        null=True,
        help_text='Malzeme yönetimi önceliği'
    )
    purchpriorty = models.SmallIntegerField(
        db_column='PURCHPRIORTY',
        blank=True,
        null=True,
        help_text='Satınalma önceliği'
    )
    salespriority = models.SmallIntegerField(
        db_column='SALESPRIORITY',
        blank=True,
        null=True,
        help_text='Satış önceliği'
    )
    width = models.FloatField(db_column='WIDTH', blank=True, null=True)
    length = models.FloatField(db_column='LENGTH', blank=True, null=True)
    height = models.FloatField(db_column='HEIGHT', blank=True, null=True)
    area = models.FloatField(db_column='AREA', blank=True, null=True)
    volume_field = models.FloatField(db_column='VOLUME_', blank=True, null=True)
    weight = models.FloatField(db_column='WEIGHT', blank=True, null=True)
    widthref = models.IntegerField(db_column='WIDTHREF', blank=True, null=True)
    lengthref = models.IntegerField(
        db_column='LENGTHREF', blank=True, null=True)
    heightref = models.IntegerField(
        db_column='HEIGHTREF', blank=True, null=True)
    arearef = models.IntegerField(
        db_column='AREAREF', blank=True, null=True)
    volumeref = models.IntegerField(
        db_column='VOLUMEREF', blank=True, null=True)
    weightref = models.IntegerField(
        db_column='WEIGHTREF', blank=True, null=True)
    grossvolume = models.FloatField(
        db_column='GROSSVOLUME', blank=True, null=True)
    grossweight = models.FloatField(
        db_column='GROSSWEIGHT', blank=True, null=True)
    grossvolref = models.IntegerField(
        db_column='GROSSVOLREF', blank=True, null=True)
    grosswghtref = models.IntegerField(
        db_column='GROSSWGHTREF', blank=True, null=True)
    convfact1 = models.FloatField(
        db_column='CONVFACT1', blank=True, null=True)
    convfact2 = models.FloatField(
        db_column='CONVFACT2', blank=True, null=True)
    extaccessflags = models.IntegerField(
        db_column='EXTACCESSFLAGS', blank=True, null=True)
    orglogicref = models.IntegerField(
        db_column='ORGLOGICREF',
        blank=True,
        null=True,
        help_text='Orjinal kayıt ref.'
    )
    barcode2 = models.CharField(
        db_column='BARCODE2', max_length=101, blank=True, null=True)
    barcode3 = models.CharField(
        db_column='BARCODE3', max_length=101, blank=True, null=True)
    wbarcode = models.CharField(
        db_column='WBARCODE', max_length=101, blank=True, null=True)
    wbarcodeshift = models.SmallIntegerField(
        db_column='WBARCODESHIFT', blank=True, null=True)
    variantref = models.IntegerField(
        db_column='VARIANTREF', blank=True, null=True)
    globalid = models.CharField(
        db_column='GLOBALID', max_length=51, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ITMUNITA'
        unique_together = (('itemref', 'variantref', 'unitlineref'),)
        target_db = 'erp'
