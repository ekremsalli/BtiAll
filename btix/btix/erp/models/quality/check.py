"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_QCLVAL(
    BaseLogical,
    BaseTextINC,
    models.Model):
    """
        Kalite kontrol değerleri
    """
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklaması'
    )
    setref = models.ForeignKey(
        "LG_QCSET",
        db_column='SETREF',
        blank=True,
        null=True,
        help_text='Kalite kontrol seti -> QCSET',
        on_delete=models.DO_NOTHING
    )
    lineref = models.ForeignKey(
        "LG_QCSLINE",
        db_column='LINEREF',
        blank=True,
        null=True,
        help_text='Kalite kontrol satırı -> QCSLINE',
        on_delete=models.DO_NOTHING
    )
    targetflag = models.SmallIntegerField(
        db_column='TARGETFLAG',
        blank=True,
        null=True,
        help_text='Hedef işareti (bayrağı)'
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır no'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_QCLVAL'
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"