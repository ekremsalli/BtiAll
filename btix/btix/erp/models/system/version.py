"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_CAPIVERS(
    BaseLogical,
    models.Model):
    nr = models.SmallIntegerField(db_column='NR', blank=True, null=True)
    # not linked?
    firmnr = models.SmallIntegerField(db_column='FIRMNR', blank=True, null=True)
    majdbvers = models.SmallIntegerField(db_column='MAJDBVERS', blank=True, null=True)
    mindbvers = models.SmallIntegerField(db_column='MINDBVERS', blank=True, null=True)
    reldbvers = models.SmallIntegerField(db_column='RELDBVERS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CAPIVERS'
        unique_together = (('firmnr', 'nr'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.nr} Major DB: {self.majdbvers}, Minor DB: {self.mindbvers}, Related DB: {self.reldbvers}'

