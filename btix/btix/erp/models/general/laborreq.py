"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_LABORREQ(
    BaseLogical,
    models.Model):
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
        help_text='Satır no'
    )
    group_field = models.SmallIntegerField(
        db_column='GROUP_',
        blank=True,
        null=True,
        help_text='Çalışan grubu'
    )
    empref = models.IntegerField(
        db_column='EMPREF',
        blank=True,
        null=True,
        help_text='Çalışan kartı ref. -> EMPLOYEE'
    )
    amount = models.FloatField(
        db_column='AMOUNT',
        blank=True,
        null=True,
        help_text='Çalışan sayısı'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_LABORREQ'
        unique_together = (
            ('opreqref', 'lineno_field', 'group_field', 'empref'),
            ('opreqref', 'lineno_field'),
        )
        target_db = 'erp'
