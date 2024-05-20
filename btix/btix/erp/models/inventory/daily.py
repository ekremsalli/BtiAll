"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_STINVTOT(
    BaseLogical,
    models.Model):
    """
        Günlük malzeme ambar toplamları
    """
    stockref = models.ForeignKey(
        "LG_ITEMS",
        db_column='STOCKREF',
        blank=True,
        null=True,
        help_text='Malzeme kartı ref. -> ITEMS',
        on_delete=models.DO_NOTHING
    )
    invenno = models.SmallIntegerField(
        db_column='INVENNO',
        blank=True,
        null=True,
        help_text='Ambar no (-1: tüm ambarlar)'
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih (19.05.1919: kümalatif toplam)'
    )
    plnprodin = models.FloatField(
        db_column='PLNPRODIN',
        blank=True,
        null=True,
        help_text='Planlanan üretimden giriş'
    )
    plnprodout = models.FloatField(
        db_column='PLNPRODOUT',
        blank=True,
        null=True,
        help_text='Planlanan, sarf, fireler'
    )
    plnotherin = models.FloatField(
        db_column='PLNOTHERIN',
        blank=True,
        null=True,
        help_text='Planlanan diğer girişler'
    )
    plnotherout = models.FloatField(
        db_column='PLNOTHEROUT',
        blank=True,
        null=True,
        help_text='Planlanan diğer çıkışlar'
    )
    plnwhousein = models.FloatField(
        db_column='PLNWHOUSEIN',
        blank=True,
        null=True,
        help_text='Planlanan ambar girişleri'
    )
    plnwhouseout = models.FloatField(
        db_column='PLNWHOUSEOUT',
        blank=True,
        null=True,
        help_text='Planlanan ambar çıkışları'
    )
    tempin = models.FloatField(
        db_column='TEMPIN',
        blank=True,
        null=True,
        help_text='Konsinye girişler'
    )
    tempout = models.FloatField(
        db_column='TEMPOUT', blank=True, null=True)
    reserved = models.FloatField(
        db_column='RESERVED',
        blank=True,
        null=True,
        help_text='Rezervasyon miktarı'
    )
    actporder = models.FloatField(
        db_column='ACTPORDER',
        blank=True,
        null=True,
        help_text='Alınan siparişler'
    )
    received = models.FloatField(
        db_column='RECEIVED',
        blank=True,
        null=True,
        help_text='Teslim alınan alım siparişler'
    )
    actprodin = models.FloatField(
        db_column='ACTPRODIN',
        blank=True,
        null=True,
        help_text='Gerçekleşen üretimden girişler'
    )
    actotherin = models.FloatField(
        db_column='ACTOTHERIN',
        blank=True,
        null=True,
        help_text='Gerçekleşen diğer girişler'
    )
    actsorder = models.FloatField(
        db_column='ACTSORDER',
        blank=True,
        null=True,
        help_text='Satış siparişleri'
    )
    shipped = models.FloatField(
        db_column='SHIPPED',
        blank=True,
        null=True,
        help_text='Sevkedilen satış siparişleri'
    )
    actwaste = models.FloatField(
        db_column='ACTWASTE',
        blank=True,
        null=True,
        help_text='Gerçekleşen sarf fireler'
    )
    actotherout = models.FloatField(
        db_column='ACTOTHEROUT',
        blank=True,
        null=True,
        help_text='Gerçekleşen diğer çıkışlar'
    )
    transferred = models.FloatField(
        db_column='TRANSFERRED',
        blank=True,
        null=True,
        help_text='Önceki dönem devri'
    )
    avgvalue = models.FloatField(
        db_column='AVGVALUE',
        blank=True,
        null=True,
        help_text='Ortalama değer'
    )
    avgcurrval = models.FloatField(
        db_column='AVGCURRVAL',
        blank=True,
        null=True,
        help_text='Ortalama değer - raporlama dövizi'
    )
    puramnt = models.FloatField(
        db_column='PURAMNT',
        blank=True,
        null=True,
        help_text='Satınalma miktarı'
    )
    purcash = models.FloatField(
        db_column='PURCASH',
        blank=True,
        null=True,
        help_text='Satınalma tutarı'
    )
    purcurr = models.FloatField(
        db_column='PURCURR',
        blank=True,
        null=True,
        help_text='Satınalma tutarı - raporlama dövizi'
    )
    salamnt = models.FloatField(
        db_column='SALAMNT',
        blank=True,
        null=True,
        help_text='Satış miktarı'
    )
    salcash = models.FloatField(
        db_column='SALCASH',
        blank=True,
        null=True,
        help_text='Satış tutarı'
    )
    salcurr = models.FloatField(
        db_column='SALCURR',
        blank=True,
        null=True,
        help_text='Satış tutarı - raporlama dövizi'
    )
    lasttrdate = models.DateTimeField(
        db_column='LASTTRDATE',
        blank=True,
        null=True,
        help_text='Son hareket tarihi'
    )
    onhand = models.FloatField(
        db_column='ONHAND',
        blank=True,
        null=True,
        help_text='Eldekiler'
    )
    actwhousein = models.FloatField(
        db_column='ACTWHOUSEIN',
        blank=True,
        null=True,
        help_text='Gerçekleşen ambar girişleri'
    )
    actwhouseout = models.FloatField(
        db_column='ACTWHOUSEOUT',
        blank=True,
        null=True,
        help_text='Gerçekleşen ambar çıkışları'
    )
    countadd = models.FloatField(
        db_column='COUNTADD',
        blank=True,
        null=True,
        help_text='Sayım fazlası'
    )
    countdec = models.FloatField(
        db_column='COUNTDEC',
        blank=True,
        null=True,
        help_text='Sayım eksiği'
    )
    distreserved = models.FloatField(
        db_column='DISTRESERVED', blank=True, null=True)
    onvehicle = models.FloatField(
        db_column='ONVEHICLE', blank=True, null=True)
    variantref = models.IntegerField(
        db_column='VARIANTREF', blank=True, null=True)
    invencostgrp = models.SmallIntegerField(
        db_column='INVENCOSTGRP', blank=True, null=True)
    meetplanin = models.FloatField(
        db_column='MEETPLANIN', blank=True, null=True)
    plnrsrvprodin = models.FloatField(
        db_column='PLNRSRVPRODIN', blank=True, null=True)
    plnrsrvprodout = models.FloatField(
        db_column='PLNRSRVPRODOUT', blank=True, null=True)
    plnrsrvwhousein = models.FloatField(
        db_column='PLNRSRVWHOUSEIN', blank=True, null=True)
    plnrsrvwhouseout = models.FloatField(
        db_column='PLNRSRVWHOUSEOUT', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_STINVTOT'
        target_db = 'erp'

