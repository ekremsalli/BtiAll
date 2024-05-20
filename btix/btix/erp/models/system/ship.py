"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_SHPAGENT(
    BaseLogical,
    models.Model):
    code = models.CharField(db_column='CODE', unique=True, max_length=13, blank=True, null=True)
    title = models.CharField(db_column='TITLE', max_length=51, blank=True, null=True)
    email = models.CharField(db_column='EMAIL', max_length=41, blank=True, null=True)
    webaddr = models.CharField(db_column='WEBADDR', max_length=81, blank=True, null=True)
    trackingform = models.CharField(db_column='TRACKINGFORM', max_length=201, blank=True, null=True)
    addr1 = models.CharField(db_column='ADDR1', max_length=51, blank=True, null=True)
    addr2 = models.CharField(db_column='ADDR2', max_length=51, blank=True, null=True)
    city = models.CharField(db_column='CITY', max_length=41, blank=True, null=True)
    citycode = models.CharField(db_column='CITYCODE', max_length=13, blank=True, null=True)
    country = models.CharField(db_column='COUNTRY', max_length=41, blank=True, null=True)
    countrycode = models.CharField(db_column='COUNTRYCODE', max_length=13, blank=True, null=True)
    town = models.CharField(db_column='TOWN', max_length=51, blank=True, null=True)
    towncode = models.CharField(db_column='TOWNCODE', max_length=13, blank=True, null=True)
    district = models.CharField(db_column='DISTRICT', max_length=51, blank=True, null=True)
    districtcode = models.CharField(db_column='DISTRICTCODE', max_length=13, blank=True, null=True)
    postcode = models.CharField(db_column='POSTCODE', max_length=21, blank=True, null=True)
    telnrs1 = models.CharField(db_column='TELNRS1', max_length=16, blank=True, null=True)
    telnrs2 = models.CharField(db_column='TELNRS2', max_length=16, blank=True, null=True)
    faxnr = models.CharField(db_column='FAXNR', max_length=16, blank=True, null=True)
    incharge = models.CharField(db_column='INCHARGE', max_length=21, blank=True, null=True)
    clanguage = models.SmallIntegerField(db_column='CLANGUAGE', blank=True, null=True)
    firmtype = models.SmallIntegerField(db_column='FIRMTYPE', blank=True, null=True)
    taxnr = models.CharField(db_column='TAXNR', max_length=21, blank=True, null=True)
    tcno = models.CharField(db_column='TCNO', max_length=21, blank=True, null=True)
    definition_field = models.CharField(db_column='DEFINITION_', max_length=201, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=31, blank=True, null=True)
    surname = models.CharField(db_column='SURNAME', max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_SHPAGENT'
        target_db = 'system'

    def __str__(self):
        return f'{self.code} {self.title}'

class L_SHPTYPES(
    BaseLogical,
    models.Model):
    scode = models.CharField(db_column='SCODE',
        unique=True, max_length=13,
        blank=True, null=True,
        help_text='Sevkiyat türü kodu'
    )
    sdef = models.CharField(db_column='SDEF',
        max_length=51, blank=True, null=True,
        help_text='Sevkiyat türü açıklaması'
    )
    sdef2 = models.CharField(db_column='SDEF2', max_length=51, blank=True, null=True)
    pricelevel = models.SmallIntegerField(db_column='PRICELEVEL', blank=True, null=True)
    edicode = models.CharField(db_column='EDICODE', max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_SHPTYPES'
        target_db = 'system'

    def __str__(self):
        return f'{self.scode} {self.sdef}'