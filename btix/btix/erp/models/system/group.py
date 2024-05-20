"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_CAPIGROUP(
    BaseLogical,
    models.Model):
    nr = models.SmallIntegerField(db_column='NR', unique=True, blank=True, null=True)
    name = models.CharField(db_column='NAME', unique=True, max_length=21, blank=True, null=True)
    superflg = models.SmallIntegerField(db_column='SUPERFLG', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CAPIGROUP'
        target_db = 'system'

    def __str__(self):
        return f'{self.nr} {self.name}'
