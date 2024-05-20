"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_ITMCLSAS(
    BaseLogical,
    BaseSiteRec,
    BaseRef,
    models.Model):
    """
        Malzeme-malzeme sınıfı ataması
    """
    parentref = models.ForeignKey(
        "LG_ITEMS",
        db_column='PARENTREF',
        blank=True,
        null=True,
        help_text='Üst malzeme sınıfı kartı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_parentref'
    )
    childref = models.ForeignKey(
        "LG_ITEMS",
        db_column='CHILDREF',
        blank=True,
        null=True,
        help_text='Alt malzeme sınıfı kartı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_childref'
    )
    uplevel = models.SmallIntegerField(
        db_column='UPLEVEL',
        blank=True,
        null=True,
        help_text='Atama seviyesi'
    )
    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ITMCLSAS'
        unique_together = (
            ('uplevel', 'parentref', 'childref'),
            ('childref', 'uplevel', 'parentref'),
            ('parentref', 'childref', 'uplevel'),
            ('parentref', 'uplevel', 'childref'),
        )
        target_db = 'erp'
