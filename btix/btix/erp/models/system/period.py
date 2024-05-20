"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_CAPIPERIOD(
    BaseLogical,
    models.Model):
    nr = models.SmallIntegerField(db_column='NR', blank=True, null=True)
    firm = models.ForeignKey(
        "L_CAPIFIRM",
        db_column='FIRMNR',
        blank=True,
        null=True,
        to_field='nr',
        on_delete=models.DO_NOTHING
    )
    begdate = models.DateTimeField(db_column='BEGDATE', blank=True, null=True)
    enddate = models.DateTimeField(db_column='ENDDATE', blank=True, null=True)
    active = models.SmallIntegerField(db_column='ACTIVE', blank=True, null=True)
    key1 = models.SmallIntegerField(db_column='KEY1', blank=True, null=True)
    key2 = models.SmallIntegerField(db_column='KEY2', blank=True, null=True)
    key3 = models.SmallIntegerField(db_column='KEY3', blank=True, null=True)
    key4 = models.SmallIntegerField(db_column='KEY4', blank=True, null=True)
    # @check
    perlocalctype = models.SmallIntegerField(db_column='PERLOCALCTYPE', blank=True, null=True)
    perrepcurr = models.SmallIntegerField(db_column='PERREPCURR', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CAPIPERIOD'
        unique_together = (('firm', 'nr'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.nr} {self.firm}'


