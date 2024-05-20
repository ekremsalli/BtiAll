"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_DYNREP(
    BaseLogical,
    models.Model):
    repid = models.IntegerField(db_column='REPID', unique=True, blank=True, null=True)
    moduleid = models.SmallIntegerField(db_column='MODULEID', blank=True, null=True)
    reportgrpid = models.SmallIntegerField(db_column='REPORTGRPID', blank=True, null=True)
    active = models.SmallIntegerField(db_column='ACTIVE', blank=True, null=True)
    reportowner = models.SmallIntegerField(db_column='REPORTOWNER', blank=True, null=True)
    reporttype = models.SmallIntegerField(db_column='REPORTTYPE', blank=True, null=True)
    gettfromfilter = models.SmallIntegerField(db_column='GETTFROMFILTER', blank=True, null=True)
    prnttallpages = models.SmallIntegerField(db_column='PRNTTALLPAGES', blank=True, null=True)
    getshwdetfilter = models.SmallIntegerField(db_column='GETSHWDETFILTER', blank=True, null=True)
    enginever = models.IntegerField(db_column='ENGINEVER', blank=True, null=True)
    reportver = models.CharField(db_column='REPORTVER', max_length=17, blank=True, null=True)
    dontprntmstrdetnotex = models.SmallIntegerField(db_column='DONTPRNTMSTRDETNOTEX', blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=129, blank=True, null=True)
    name_lnglistid = models.IntegerField(db_column='NAME_LNGLISTID', blank=True, null=True)
    title = models.CharField(db_column='TITLE', max_length=129, blank=True, null=True)
    title_lnglistid = models.IntegerField(db_column='TITLE_LNGLISTID', blank=True, null=True)
    dbtype = models.SmallIntegerField(db_column='DBTYPE', blank=True, null=True)
    usercansortgrp = models.SmallIntegerField(db_column='USERCANSORTGRP', blank=True, null=True)
    flnamefornav = models.CharField(db_column='FLNAMEFORNAV', max_length=101, blank=True, null=True)
    ldata = models.BinaryField(db_column='LDATA', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_DYNREP'
        target_db = 'system'

    def __str__(self):
        return f'{self.repid} {self.name}'

class L_DYNREPUSRR(
    BaseLogical,
    models.Model):
    user = models.ForeignKey(
        "L_CAPIUSER",
        db_column='USERNR',
        blank=True,
        null=True,
        to_field='nr',
        on_delete=models.DO_NOTHING
    )
    report = models.ForeignKey(
        "L_DYNREP",
        db_column='REPID',
        blank=True,
        to_field="repid",
        null=True,
        on_delete=models.DO_NOTHING
    )
    allowcustdsgn = models.SmallIntegerField(db_column='ALLOWCUSTDSGN', blank=True, null=True)
    allowcustdsgnsel = models.SmallIntegerField(db_column='ALLOWCUSTDSGNSEL', blank=True, null=True)
    allowusereport = models.SmallIntegerField(db_column='ALLOWUSEREPORT', blank=True, null=True)
    firm = models.ForeignKey(
        "L_CAPIFIRM",
        db_column='FIRMNR',
        blank=True,
        null=True,
        to_field='nr',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        managed = False
        db_table = 'L_DYNREPUSRR'
        target_db = 'system'

    def __str__(self):
        return f'{self.user} {self.report}'
