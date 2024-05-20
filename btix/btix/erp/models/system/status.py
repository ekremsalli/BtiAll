"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_STATUSINFO(
    BaseLogical,
    models.Model):
    infotyp = models.SmallIntegerField(db_column='INFOTYP', blank=True, null=True)
    nr = models.SmallIntegerField(db_column='NR', blank=True, null=True)
    description = models.CharField(db_column='DESCRIPTION', max_length=201, blank=True, null=True)
    fromwhere = models.SmallIntegerField(db_column='FROMWHERE', blank=True, null=True)
    ldata = models.BinaryField(db_column='LDATA', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_STATUSINFO'
        unique_together = (('infotyp', 'nr'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.nr} {self.description}'