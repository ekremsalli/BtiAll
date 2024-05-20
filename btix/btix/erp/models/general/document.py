"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_FOLDER(
    BaseLogical,
    models.Model):
    """
        Döküman katalog bilgileri (watermark varsa)
        Döküman takip sisteminde fiş ya da kayıtların dökümanlarının
        bulunduğu tablodur.
    """
    linetype = models.SmallIntegerField(
        db_column='LINETYPE',
        blank=True,
        null=True,
        help_text='Satır tipi'
    )
    fpath = models.CharField(
        db_column='FPATH',
        max_length=201,
        blank=True,
        null=True,
        help_text='Dosyanın bulunduğu yer'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_FOLDER'
        target_db = 'erp'
