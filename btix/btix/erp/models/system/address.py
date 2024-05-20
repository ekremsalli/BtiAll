"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *


class L_COUNTRY(
    BaseLogical,
    BaseSiteRec,
    BaseRef,
    models.Model):
    code = models.CharField(db_column='CODE', max_length=13, blank=True, null=True)
    name = models.CharField(db_column='NAME', unique=True, max_length=41, blank=True, null=True)
    countrynr = models.IntegerField(db_column='COUNTRYNR', unique=True, blank=True, null=True)
    statestr = models.CharField(db_column='STATESTR', max_length=13, blank=True, null=True)
    name2 = models.CharField(db_column='NAME2', max_length=41, blank=True, null=True)
    edicode = models.CharField(db_column='EDICODE', max_length=25, blank=True, null=True)
    netflag = models.CharField(db_column='NETFLAG', max_length=37, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_COUNTRY'
        unique_together = (('code', 'statestr'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.countrynr} {self.name}'

class L_CITY(
    BaseLogical,
    BaseSiteRec,
    BaseRef,
    models.Model):
    country = models.ForeignKey(
        L_COUNTRY,
        db_column='COUNTRY',
        blank=True,
        null=True,
        to_field='countrynr',
        on_delete=models.DO_NOTHING,
        help_text='Ülke'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=41,
        blank=True,
        null=True,
        help_text='Şehir adı'
    )
    code = models.CharField(db_column='CODE', max_length=13, blank=True, null=True)
    name2 = models.CharField(db_column='NAME2', max_length=41, blank=True, null=True)
    netflag = models.CharField(db_column='NETFLAG', max_length=37, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CITY'
        unique_together = (('country', 'name'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.code} {self.name}'

class L_TOWN(
    BaseLogical,
    BaseSiteRec,
    BaseRef,
    models.Model):
    city = models.ForeignKey(
        L_CITY,
        db_column='CTYREF',
        blank=True,
        null=True,
        to_field='logicalref',
        on_delete=models.DO_NOTHING
    )
    cntrnr = models.IntegerField(db_column='CNTRNR', blank=True, null=True)
    code = models.CharField(db_column='CODE', max_length=13, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=51, blank=True, null=True)
    name2 = models.CharField(db_column='NAME2', max_length=51, blank=True, null=True)
    netflag = models.CharField(db_column='NETFLAG', max_length=37, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_TOWN'
        unique_together = (('city', 'code'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.code} {self.name}'


class L_DISTRICT(
    BaseLogical,
    BaseSiteRec,
    BaseRef,
    models.Model):
    townnr = models.IntegerField(db_column='TOWNNR', blank=True, null=True)
    code = models.CharField(db_column='CODE', max_length=13, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=51, blank=True, null=True)
    name2 = models.CharField(db_column='NAME2', max_length=51, blank=True, null=True)
    netflag = models.CharField(db_column='NETFLAG', max_length=37, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_DISTRICT'
        unique_together = (('townnr', 'code'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.code} {self.name}'


class L_POSTCODE(
    BaseLogical,
    BaseSiteRec,
    BaseRef,
    models.Model):
    country = models.IntegerField(
        db_column='COUNTRY',
        blank=True,
        null=True,
        help_text='Ülke'
    )
    city = models.IntegerField(
        db_column='CITY',
        blank=True,
        null=True,
        help_text='Şehir'
    )
    postcode = models.CharField(
        db_column='POSTCODE',
        max_length=21,
        blank=True,
        null=True,
        help_text='Posta kodu'
    )

    class Meta:
        managed = False
        db_table = 'L_POSTCODE'
        unique_together = (('country', 'city', 'postcode'),)
        target_db = 'system'
