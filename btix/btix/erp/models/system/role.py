"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_CAPIROLE(
    BaseLogical,
    models.Model):
    nr = models.SmallIntegerField(db_column='NR', unique=True, blank=True, null=True)
    name = models.CharField(db_column='NAME', unique=True, max_length=51, blank=True, null=True)
    custtable = models.CharField(db_column='CUSTTABLE', max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CAPIROLE'
        target_db = 'system'

    def __str__(self):
        return f'{self.nr} {self.name}'