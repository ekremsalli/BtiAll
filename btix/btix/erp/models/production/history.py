"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_PRVOPASG(
    BaseLogical,
    models.Model):
    """
        Önceki operasyon ilişkileri
    """
    routingref = models.ForeignKey(
        "LG_ROUTING",
        db_column='ROUTINGREF',
        blank=True,
        null=True,
        help_text='Üretim rotaları -> ROUTING',
        on_delete=models.DO_NOTHING
    )
    routlineref = models.ForeignKey(
        "LG_RTNGLINE",
        db_column='ROUTLINEREF',
        blank=True,
        null=True,
        help_text='Üretim rotaları satırları kartı -> RTNGLINE',
        on_delete=models.DO_NOTHING
    )
    lineopref = models.ForeignKey(
        "LG_OPERTION",
        db_column='LINEOPREF',
        blank=True,
        null=True,
        help_text='Satır operasyon ref. -> OPERTION',
        on_delete=models.DO_NOTHING,
        related_name="lineopref"
    )
    prevopref = models.ForeignKey(
        "LG_OPERTION",
        db_column='PREVOPREF',
        blank=True,
        null=True,
        help_text='Önceki operasyon ref. -> OPERTION',
        on_delete=models.DO_NOTHING,
        related_name="prevopref"
    )
    overlapper = models.FloatField(
        db_column='OVERLAPPER',
        blank=True,
        null=True,
        help_text='Çakışma oranı'
    )
    overlaptype = models.SmallIntegerField(
        db_column='OVERLAPTYPE',
        blank=True,
        null=True
    )
    overlapamnt = models.FloatField(
        db_column='OVERLAPAMNT',
        blank=True,
        null=True
    )
    overlapmethod = models.SmallIntegerField(
        db_column='OVERLAPMETHOD',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_PRVOPASG'
        unique_together = (('prevopref', 'routlineref'),)
        target_db = 'erp'