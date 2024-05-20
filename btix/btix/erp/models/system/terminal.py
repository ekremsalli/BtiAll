"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_CAPITERMINAL(
    BaseLogical,
    models.Model):
    nr = models.SmallIntegerField(db_column='NR', unique=True, blank=True, null=True)
    code = models.CharField(db_column='CODE', unique=True, max_length=18, blank=True, null=True)
    tattrib = models.IntegerField(db_column='TATTRIB', blank=True, null=True)
    usernr = models.SmallIntegerField(db_column='USERNR', blank=True, null=True)
    prnnr1 = models.SmallIntegerField(db_column='PRNNR1', blank=True, null=True)
    prnnr2 = models.SmallIntegerField(db_column='PRNNR2', blank=True, null=True)
    prnfiles1 = models.CharField(db_column='PRNFILES1', max_length=13, blank=True, null=True)
    prnfiles2 = models.CharField(db_column='PRNFILES2', max_length=13, blank=True, null=True)
    prnfiles3 = models.CharField(db_column='PRNFILES3', max_length=13, blank=True, null=True)
    prnfiles4 = models.CharField(db_column='PRNFILES4', max_length=13, blank=True, null=True)
    prnfiles5 = models.CharField(db_column='PRNFILES5', max_length=13, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=21, blank=True, null=True)
    userext = models.IntegerField(db_column='USEREXT', blank=True, null=True)
    taskcode = models.SmallIntegerField(db_column='TASKCODE', blank=True, null=True)
    gatewayaddr = models.CharField(db_column='GATEWAYADDR', max_length=81, blank=True, null=True)
    key_field = models.CharField(db_column='KEY_', max_length=32, blank=True, null=True)
    progid = models.SmallIntegerField(db_column='PROGID', blank=True, null=True)
    serial = models.IntegerField(db_column='SERIAL', blank=True, null=True)
    licencestr = models.CharField(db_column='LICENCESTR', max_length=21, blank=True, null=True)
    terminfo = models.CharField(db_column='TERMINFO', max_length=255, blank=True, null=True)
    termtype = models.SmallIntegerField(db_column='TERMTYPE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CAPITERMINAL'
        target_db = 'system'

    def __str__(self):
        return f'{self.code} {self.name}'
