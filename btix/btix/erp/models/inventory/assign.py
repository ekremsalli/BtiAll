"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_SELCHVAL(
    BaseLogical,
    models.Model):
    """
        Malzeme özellik ataması
    """
    charasgnref = models.ForeignKey(
        "LG_CHARCODE",
        db_column='CHARASGNREF',
        blank=True,
        null=True,
        help_text='Malzeme özellik ref. -> CHARCODE',
        on_delete=models.DO_NOTHING
    )
    charvalref = models.ForeignKey(
        "LG_CHARVAL",
        db_column='CHARVALREF',
        blank=True,
        null=True,
        help_text='Özellik değeri ref. -> CHARVAL',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_SELCHVAL'
        unique_together = (('charasgnref', 'charvalref'),)
        target_db = 'erp'