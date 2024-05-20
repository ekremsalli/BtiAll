"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_FIRMDOC(models.Model):
    """
        Döküman katalog girişi(watermark)
    """
    lref = models.AutoField(
        db_column='LREF',
        primary_key=True,
        help_text='Fiziksel adres'
    )
    infotyp = models.SmallIntegerField(
        db_column='INFOTYP',
        blank=True,
        null=True
    )
    inforef = models.IntegerField(
        db_column='INFOREF',
        blank=True,
        null=True
    )
    doctyp = models.IntegerField(
        db_column='DOCTYP',
        blank=True,
        null=True
    )
    docnr = models.IntegerField(
        db_column='DOCNR',
        blank=True,
        null=True
    )
    ldata = models.BinaryField(
        db_column='LDATA',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_FIRMDOC'
        target_db = 'erp'