"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_QCSET(
    BaseLogical,
    BaseTextINC,
    BaseWF,
    BaseGUID,
    BaseSiteRec,
    BaseCode,
    BaseInfo,
    BaseRef,
    models.Model):
    """
        Kalite kontrol setleri
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=25,
        blank=True,
        null=True,
        help_text='Kalite kontrol kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklaması'
    )
    itype = models.SmallIntegerField(
        db_column='ITYPE',
        blank=True,
        null=True,
        help_text='Türü'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_QCSET'
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"