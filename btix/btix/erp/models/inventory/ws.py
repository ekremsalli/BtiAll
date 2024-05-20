"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_ITMWSDEF(
    BaseLogical,
    BaseItem,
    models.Model):
    wsref = models.ForeignKey(
        "LG_WORKSTAT",
        db_column='WSREF',
        blank=True,
        null=True,
        help_text='WORKSTAT',
        on_delete=models.DO_NOTHING
    )
    minlevel = models.FloatField(
        db_column='MINLEVEL',
        blank=True,
        null=True,
        help_text='Asgari stok seviyesi'
    )
    maxlevel = models.FloatField(
        db_column='MAXLEVEL',
        blank=True,
        null=True,
        help_text='Azami stok seviyesi'
    )
    safelevel = models.FloatField(
        db_column='SAFELEVEL',
        blank=True,
        null=True,
        help_text='Güvenli stok seviyesi'
    )
    minlevelctrl = models.SmallIntegerField(
        db_column='MINLEVELCTRL',
        blank=True,
        null=True,
        help_text='Asgari stok seviyesi kontrolü'
    )
    maxlevelctrl = models.SmallIntegerField(
        db_column='MAXLEVELCTRL',
        blank=True,
        null=True,
        help_text='Azami satok seviyesi kontrolü'
    )
    safelevelctrl = models.SmallIntegerField(
        db_column='SAFELEVELCTRL',
        blank=True,
        null=True,
        help_text='Güvenli stok seviyesi kontrolü'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ITMWSDEF'
        target_db = 'erp'