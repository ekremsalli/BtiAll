"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_TOOLREQ(
    BaseLogical,
    BaseAmount,
    BaseUnitSet,
    models.Model):
    """
        Araç ihtiyaçları
    """
    opreqref = models.IntegerField(
        db_column='OPREQREF',
        blank=True,
        null=True,
        help_text='Operasyon kartı ref.'
    )
    lineno_field = models.IntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    toolref = models.IntegerField(
        db_column='TOOLREF',
        blank=True,
        null=True,
        help_text='Araç kartı ref.'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_TOOLREQ'
        unique_together = (
            ('opreqref', 'lineno_field'), ('opreqref', 'toolref'),
        )
        target_db = 'erp'
