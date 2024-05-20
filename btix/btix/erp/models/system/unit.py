"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_CAPIUNIT(
    BaseLogical,
    models.Model):
    firm = models.ForeignKey(
        "L_CAPIFIRM",
        db_column='FIRMNR',
        blank=True,
        null=True,
        to_field='nr',
        on_delete=models.DO_NOTHING
    )
    nr = models.SmallIntegerField(db_column='NR', blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=61, blank=True, null=True)
    userext = models.IntegerField(db_column='USEREXT', blank=True, null=True)
    moddate = models.DateTimeField(db_column='MODDATE', blank=True, null=True)
    modtime = models.IntegerField(db_column='MODTIME', blank=True, null=True)
    passive = models.SmallIntegerField(db_column='PASSIVE', blank=True, null=True)
    netflag = models.CharField(db_column='NETFLAG', max_length=37, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CAPIUNIT'
        unique_together = (('firm', 'nr'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.nr} {self.name}'
