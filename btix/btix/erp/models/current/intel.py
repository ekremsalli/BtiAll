"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_CLINTEL(
    BaseLogical,
    BaseClient,
    models.Model):
    """
        Cari hesap istihbarat bilgileri
    """
    linenum = models.SmallIntegerField(
        db_column='LINENUM',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    intelline = models.CharField(
        db_column='INTELLINE',
        max_length=51,
        blank=True,
        null=True,
        help_text='İstihbarat bilgileri satırı'
    )

    class Meta:
        managed = False
        unique_together = (('clientref', 'linenum'),)
        db_table = f'LG_{Active.namespace}_CLINTEL'
        target_db = 'erp'