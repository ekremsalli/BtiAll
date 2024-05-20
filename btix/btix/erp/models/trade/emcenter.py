"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_EMCENTER(
    BaseLogical,
    BaseInfo,
    BaseActive,
    BaseWF,
    BaseSiteRec,
    BaseCode,
    models.Model):
    """
        Masraf merkezi
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=101,
        blank=True,
        null=True,
        help_text='Masraf kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=101,
        blank=True,
        null=True,
        help_text='Masraf adı'
    )
    units = models.CharField(
        db_column='UNITS',
        max_length=5,
        blank=True,
        null=True,
        help_text='Birim'
    )
    addinforef = models.IntegerField(
        db_column='ADDINFOREF',
        blank=True,
        null=True,
        help_text='Ek bilgi dosyası ref.'
    )
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Extra dosya ref.'
    )
    orglogicalref = models.IntegerField(
        db_column='ORGLOGICALREF',
        blank=True,
        null=True
    )
    specode4 = models.CharField(
        db_column='SPECODE4',
        max_length=11,
        blank=True,
        null=True,
        help_text='Özel kod 4'
    )
    specode5 = models.CharField(
        db_column='SPECODE5',
        max_length=11,
        blank=True,
        null=True,
        help_text='Özel kod 5'
    )
    specode2 = models.CharField(
        db_column='SPECODE2',
        max_length=11,
        blank=True,
        null=True,
        help_text='Özel kod 2'
    )
    specode3 = models.CharField(
        db_column='SPECODE3',
        max_length=11,
        blank=True,
        null=True,
        help_text='Özel kod 3'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_EMCENTER'
        unique_together = (('active', 'code'),)
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.definition_field}"
