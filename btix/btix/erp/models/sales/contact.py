"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_CONTACTS(
    BaseLogical,
    BaseAddress,
    BaseGUID,
    BaseCode,
    BaseInfo,
    BaseTextINC,
    BaseSiteRec,
    BaseRef,
    models.Model):
    """
        İlgili kişiler
    """
    name = models.CharField(db_column='NAME', max_length=21, blank=True,
        null=True, help_text='Adı')
    midinit = models.CharField(db_column='MIDINIT', max_length=11, blank=True,
        null=True, help_text='İkinci adı')
    famname = models.CharField(db_column='FAMNAME', max_length=21, blank=True,
        null=True, help_text='Soyadı')
    title = models.CharField(db_column='TITLE', max_length=21, blank=True,
        null=True, help_text='Ünvan')
    cstvndref = models.IntegerField(db_column='CSTVNDREF', blank=True,
        null=True, help_text='Müşteri / Tedarikçi ref.')
    jobtitle = models.CharField(db_column='JOBTITLE', max_length=51,
        blank=True, null=True, help_text='İş tanımı (Ünvanı)')
    workphone = models.CharField(db_column='WORKPHONE', max_length=16,
        blank=True, null=True, help_text='İş telefonu')
    homephone = models.CharField(db_column='HOMEPHONE', max_length=16,
        blank=True, null=True, help_text='Ev tel.')
    mobphone = models.CharField(db_column='MOBPHONE', max_length=16,
        blank=True, null=True, help_text='Mobil tel.')
    asstphone = models.CharField(db_column='ASSTPHONE', max_length=16,
        blank=True, null=True, help_text='')
    officefax = models.CharField(db_column='OFFICEFAX', max_length=16,
        blank=True, null=True, help_text='Ofis fask numarası')
    emailaddr = models.CharField(db_column='EMAILADDR', max_length=251,
        blank=True, null=True, help_text='E-posta adresi')
    contcat = models.IntegerField(db_column='CONTCAT', blank=True,
        null=True, help_text='Kategori')
    countrycode = models.CharField(db_column='COUNTRYCODE', max_length=13,
        blank=True, null=True, help_text='Ülke kodu')
    citycode = models.CharField(db_column='CITYCODE', max_length=13,
        blank=True, null=True, help_text='Şehir kodu')
    towncode = models.CharField(db_column='TOWNCODE', max_length=13,
        blank=True, null=True, help_text='İlçe kodu')
    districtcode = models.CharField(db_column='DISTRICTCODE', max_length=13,
        blank=True, null=True, help_text='Semt kodu')
    workphcod = models.CharField(db_column='WORKPHCOD', max_length=9,
        blank=True, null=True)
    homephcod = models.CharField(db_column='HOMEPHCOD', max_length=9,
        blank=True, null=True)
    mobphcod = models.CharField(db_column='MOBPHCOD', max_length=9,
        blank=True, null=True)
    asstphcod = models.CharField(db_column='ASSTPHCOD', max_length=9,
        blank=True, null=True)
    offfaxcod = models.CharField(db_column='OFFFAXCOD', max_length=9,
        blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LG_CONTACTS'
        target_db = 'erp'

    # rels -> L_CSTVND
