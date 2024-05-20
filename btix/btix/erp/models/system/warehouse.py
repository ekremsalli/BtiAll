"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_CAPIWHOUSE(
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
    name = models.CharField(db_column='NAME', max_length=51, blank=True, null=True)
    division = models.ForeignKey("L_CAPIDIV", db_column='DIVISNR', blank=True, null=True,
        to_field='nr', on_delete=models.DO_NOTHING
    )
    factnr = models.ForeignKey("L_CAPIFACTORY", db_column='FACTNR', blank=True, null=True,
        to_field='nr', on_delete=models.DO_NOTHING
    )
    costgrp = models.SmallIntegerField(db_column='COSTGRP', blank=True, null=True)
    siteid = models.SmallIntegerField(db_column='SITEID', blank=True, null=True)
    userext = models.IntegerField(db_column='USEREXT', blank=True, null=True)
    moddate = models.DateTimeField(db_column='MODDATE', blank=True, null=True)
    modtime = models.IntegerField(db_column='MODTIME', blank=True, null=True)
    virtualinven = models.SmallIntegerField(db_column='VIRTUALINVEN', blank=True, null=True)
    longitude = models.CharField(db_column='LONGITUDE', max_length=41, blank=True, null=True)
    latitute = models.CharField(db_column='LATITUTE', max_length=41, blank=True, null=True)
    addr1 = models.CharField(db_column='ADDR1', max_length=201, blank=True, null=True)
    addr2 = models.CharField(db_column='ADDR2', max_length=201, blank=True, null=True)
    towncode = models.CharField(db_column='TOWNCODE', max_length=13, blank=True, null=True)
    town = models.CharField(db_column='TOWN', max_length=51, blank=True, null=True)
    districtcode = models.CharField(db_column='DISTRICTCODE', max_length=13, blank=True, null=True)
    district = models.CharField(db_column='DISTRICT', max_length=51, blank=True, null=True)
    citycode = models.CharField(db_column='CITYCODE', max_length=13, blank=True, null=True)
    city = models.CharField(db_column='CITY', max_length=21, blank=True, null=True)
    countrycode = models.CharField(db_column='COUNTRYCODE', max_length=13, blank=True, null=True)
    country = models.CharField(db_column='COUNTRY', max_length=21, blank=True, null=True)
    telcodes1 = models.CharField(db_column='TELCODES1', max_length=9, blank=True, null=True)
    telcodes2 = models.CharField(db_column='TELCODES2', max_length=9, blank=True, null=True)
    telnrs1 = models.CharField(db_column='TELNRS1', max_length=51, blank=True, null=True)
    telnrs2 = models.CharField(db_column='TELNRS2', max_length=51, blank=True, null=True)
    telextnums1 = models.CharField(db_column='TELEXTNUMS1', max_length=9, blank=True, null=True)
    telextnums2 = models.CharField(db_column='TELEXTNUMS2', max_length=9, blank=True, null=True)
    emailaddr = models.CharField(db_column='EMAILADDR', max_length=251, blank=True, null=True)
    shpagncod = models.CharField(db_column='SHPAGNCOD', max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CAPIWHOUSE'
        unique_together = (('firm', 'nr', 'costgrp', 'virtualinven'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.nr} {self.name}'
