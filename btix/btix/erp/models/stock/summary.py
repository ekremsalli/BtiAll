"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_SRVNUMS(
    BaseLogical,
    BaseCard,
    models.Model):
    """
        Hizmet kartları ambar rakamları
        Hizmet kartlarının da toplamları kayıtlar halinde tutulmakta SRVNUMS
        tablosunda tutulmaktadır.
    """
    invenno = models.SmallIntegerField(
        db_column='INVENNO',
        blank=True,
        null=True,
        help_text='Ambar no'
    )
    duration = models.SmallIntegerField(
        db_column='DURATION',
        blank=True,
        null=True,
        help_text='Süre'
    )
    ordered = models.FloatField(
        db_column='ORDERED',
        blank=True,
        null=True,
        help_text='Sipariş verilmiş miktar'
    )
    shipped = models.FloatField(
        db_column='SHIPPED',
        blank=True,
        null=True,
        help_text='Sevk edilmiş miktar'
    )
    lasttrdate = models.DateTimeField(
        db_column='LASTTRDATE',
        blank=True,
        null=True,
        help_text='Hareket gördüğü son tarih'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_SRVNUMS'
        unique_together = (('cardref', 'invenno'),)
        target_db = 'erp'
