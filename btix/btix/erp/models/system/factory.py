"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_CAPIFACTORY(
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
    nr = models.SmallIntegerField(unique=True, db_column='NR', blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=51, blank=True, null=True)
    divisnr = models.SmallIntegerField(db_column='DIVISNR', blank=True, null=True)
    siteid = models.SmallIntegerField(db_column='SITEID', blank=True, null=True)
    userext = models.IntegerField(db_column='USEREXT', blank=True, null=True)
    moddate = models.DateTimeField(db_column='MODDATE', blank=True, null=True)
    modtime = models.IntegerField(db_column='MODTIME', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CAPIFACTORY'
        unique_together = (('firm', 'nr'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.nr} {self.name}'

class L_CAPIFACTDIV(
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
    recnr = models.SmallIntegerField(db_column='RECNR', blank=True, null=True)
    nr = models.SmallIntegerField(unique=True, db_column='NR', blank=True, null=True)
    factnr = models.ForeignKey(
        "L_CAPIFACTORY",
        db_column='FACTNR',
        blank=True,
        null=True,
        to_field='nr',
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(db_column='NAME', max_length=51, blank=True, null=True)
    userext = models.IntegerField(db_column='USEREXT', blank=True, null=True)
    workdays = models.IntegerField(db_column='WORKDAYS', blank=True, null=True)
    moddate = models.DateTimeField(db_column='MODDATE', blank=True, null=True)
    modtime = models.IntegerField(db_column='MODTIME', blank=True, null=True)
    recordnr = models.IntegerField(db_column='RECORDNR', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CAPIFACTDIV'
        unique_together = (('firm', 'recordnr'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.nr} {self.name}'
