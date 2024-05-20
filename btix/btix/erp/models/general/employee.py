"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_EMGRPASS(
    BaseLogical,
    BasePriority,
    models.Model):
    """
        Çalışan - grup ataması
    """
    empgrpref = models.ForeignKey(
        "LG_EMPGROUP",
        db_column='EMPGRPREF',
        blank=True,
        null=True,
        help_text='Çalışan-Grup ref. -> EMPGROUP',
        on_delete=models.DO_NOTHING
    )
    empref = models.ForeignKey(
        "LG_EMPLOYEE",
        db_column='EMPREF',
        blank=True,
        null=True,
        help_text='Çalışanlar ref. -> EMPLOYEE',
        on_delete=models.DO_NOTHING
    )
    dominshftgrp = models.SmallIntegerField(
        db_column='DOMINSHFTGRP',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_EMGRPASS'
        unique_together = (
            ('empgrpref', 'priority', 'empref'),
            ('empref', 'empgrpref'),
        )
        target_db = 'erp'

class LG_EMPGROUP(
    BaseLogical,
    BaseCenter,
    BaseAccount,
    BaseApproved,
    BaseInfo,
    BaseSiteRec,
    BaseActive,
    BaseCode,
    BaseWF,
    BaseTextINC,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Çalışan grubu
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=25,
        blank=True,
        null=True,
        help_text='Çalışan grup kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Çalılan grup açıklaması'
    )
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika no'
    )
    operationtime = models.FloatField(
        db_column='OPERATIONTIME',
        blank=True,
        null=True,
        help_text='Operasyon zamanı'
    )
    hourlystdcost = models.FloatField(
        db_column='HOURLYSTDCOST',
        blank=True,
        null=True,
        help_text='Saatlik çalışma maliyeti'
    )
    hourlystdrpcost = models.FloatField(
        db_column='HOURLYSTDRPCOST',
        blank=True,
        null=True,
        help_text='Günlük çalışma maliyeti'
    )
    imageinc = models.SmallIntegerField(
        db_column='IMAGEINC',
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_EMPGROUP'
        unique_together = (('active', 'code'),)
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"

class LG_EMPLOYEE(
    BaseLogical,
    BaseAccount,
    BaseCenter,
    BaseApproved,
    BaseInfo,
    BaseSiteRec,
    BaseActive,
    BaseTextINC,
    BaseWF,
    BaseCode,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Çalışanlar
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=25,
        blank=True,
        null=True,
        help_text='Çalışan kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Çalışan açıklaması'
    )
    factorydivnr = models.SmallIntegerField(
        db_column='FACTORYDIVNR',
        blank=True,
        null=True,
        help_text='Fabrika bölümü'
    )
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika no'
    )
    calendarref = models.IntegerField(
        db_column='CALENDARREF',
        blank=True,
        null=True,
        help_text='Takvim ref.'
    )
    perscardref = models.IntegerField(
        db_column='PERSCARDREF',
        blank=True,
        null=True,
        help_text='Personel kartı ref.'
    )
    operationtime = models.FloatField(
        db_column='OPERATIONTIME',
        blank=True,
        null=True,
        help_text='Operasyon zamanı'
    )
    hourlystdcost = models.FloatField(
        db_column='HOURLYSTDCOST',
        blank=True,
        null=True,
        help_text='Saatlik çalışma maliyeti'
    )
    hourlystdrpcost = models.FloatField(
        db_column='HOURLYSTDRPCOST',
        blank=True,
        null=True,
        help_text='Günlük çalışma maliyeti'
    )
    imageinc = models.SmallIntegerField(
        db_column='IMAGEINC', blank=True, null=True)
    shftgrpref = models.IntegerField(
        db_column='SHFTGRPREF', blank=True, null=True)
    empname = models.CharField(
        db_column='EMPNAME', max_length=51, blank=True, null=True)
    empsurname = models.CharField(
        db_column='EMPSURNAME', max_length=51, blank=True, null=True)
    tckno = models.CharField(
        db_column='TCKNO', max_length=16, blank=True, null=True)
    birthdate = models.DateTimeField(
        db_column='BIRTHDATE', blank=True, null=True)
    bloodgrp = models.CharField(
        db_column='BLOODGRP', max_length=9, blank=True, null=True)
    registercode = models.CharField(
        db_column='REGISTERCODE', max_length=17, blank=True, null=True)
    socialsecno = models.CharField(
        db_column='SOCIALSECNO', max_length=21, blank=True, null=True)
    districtcode = models.CharField(
        db_column='DISTRICTCODE', max_length=13, blank=True, null=True)
    towncode = models.CharField(db_column='TOWNCODE',
        max_length=13, blank=True, null=True)
    citycode = models.CharField(db_column='CITYCODE',
        max_length=13, blank=True, null=True)
    countrycode = models.CharField(db_column='COUNTRYCODE',
        max_length=13, blank=True, null=True)

    telnrs1 = models.CharField(db_column='TELNRS1', max_length=16,
        blank=True, null=True, help_text='Telefon numarası (1)')
    telnrs2 = models.CharField(db_column='TELNRS2', max_length=16, blank=True,
        null=True, help_text='Telefon numarası (2)')
    emailaddr = models.CharField(db_column='EMAILADDR', max_length=51,
        blank=True, null=True, help_text='E-posta adresi')

    addr1 = models.CharField(db_column='ADDR1', max_length=201,
        blank=True, null=True, help_text='Adres satırı (1)')
    addr2 = models.CharField(db_column='ADDR2', max_length=201,
        blank=True, null=True, help_text='Adres satırı (2)')
    city = models.CharField(db_column='CITY', max_length=21,
        blank=True, null=True, help_text='Şehir')
    country = models.CharField(db_column='COUNTRY', max_length=21,
        blank=True, null=True, help_text='Ülke')
    town = models.CharField(db_column='TOWN', max_length=51,
        blank=True, null=True, help_text='İlçe')
    district = models.CharField(db_column='DISTRICT', max_length=51,
        blank=True, null=True, help_text='Semt')


    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_EMPLOYEE'
        unique_together = (('active', 'code'),)
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"
