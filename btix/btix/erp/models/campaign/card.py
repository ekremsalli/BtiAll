"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_CAMPAIGN(
    BaseLogical,
    BaseActive,
    BaseTrading,
    BaseCode,
    BaseInfo,
    BaseSiteRec,
    BasePriority,
    BaseVariable5,
    BaseWF,
    BaseVariable25,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Kampanya kartı
    """
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Satınalma'),
            (2, 'Satış')
        ],
        help_text='Kart türü; 1-> Satınalma, 2-> Satış'
    )
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Kod'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True,
        help_text='Kampanya başlangıç tarihi'
    )
    enddate = models.DateTimeField(
        db_column='ENDDATE',
        blank=True,
        null=True,
        help_text='Kampanya bitiş tarihi'
    )
    prioritygrp = models.CharField(
        db_column='PRIORITYGRP',
        max_length=11,
        blank=True,
        null=True,
        help_text='Öncelik grubu'
    )
    dontfixlines = models.SmallIntegerField(
        db_column='DONTFIXLINES',
        blank=True,
        null=True,
        help_text='Kampanya koşullarını sağlayan malzeme satırları dağıtılabilir'
    )
    clientcode = models.CharField(
        db_column='CLIENTCODE',
        max_length=17,
        blank=True,
        null=True,
        help_text='Cari hesap kodu'
    )
    clspecode = models.CharField(
        db_column='CLSPECODE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Cari özel kodu'
    )
    payplancode = models.CharField(
        db_column='PAYPLANCODE',
        max_length=17,
        blank=True,
        null=True,
        help_text='Ödeme planı kodu'
    )
    ppgroupcode = models.CharField(
        db_column='PPGROUPCODE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Ödeme planı grup kodu'
    )
    towncode = models.CharField(
        db_column='TOWNCODE',
        max_length=13,
        blank=True,
        null=True,
        help_text='İlçe kodu'
    )
    districtcode = models.CharField(
        db_column='DISTRICTCODE',
        max_length=13,
        blank=True,
        null=True,
        help_text='Semt kodu'
    )
    citycode = models.CharField(
        db_column='CITYCODE',
        max_length=13,
        blank=True,
        null=True,
        help_text='Şehir kodu'
    )
    countrycode = models.CharField(
        db_column='COUNTRYCODE',
        max_length=13,
        blank=True,
        null=True,
        help_text='Ülke kodu'
    )
    orglogoid = models.CharField(
        db_column='ORGLOGOID',
        max_length=25,
        blank=True,
        null=True
    )
    docdocode = models.CharField(
        db_column='DOCDOCODE',
        max_length=33,
        blank=True,
        null=True
    )
    docspecode = models.CharField(
        db_column='DOCSPECODE',
        max_length=11,
        blank=True,
        null=True
    )
    doccyphcode = models.CharField(
        db_column='DOCCYPHCODE',
        max_length=11,
        blank=True,
        null=True
    )
    clspecode2 = models.CharField(
        db_column='CLSPECODE2',
        max_length=11,
        blank=True,
        null=True
    )
    clspecode3 = models.CharField(
        db_column='CLSPECODE3',
        max_length=11,
        blank=True,
        null=True
    )
    clspecode4 = models.CharField(
        db_column='CLSPECODE4',
        max_length=11,
        blank=True,
        null=True
    )
    clspecode5 = models.CharField(
        db_column='CLSPECODE5',
        max_length=11,
        blank=True,
        null=True
    )
    clcyphcode = models.CharField(
        db_column='CLCYPHCODE',
        max_length=11,
        blank=True,
        null=True
    )
    clapplycount = models.SmallIntegerField(
        db_column='CLAPPLYCOUNT',
        blank=True,
        null=True
    )
    class Meta:
        managed = False
        unique_together = (
            ('cardtype', 'code'), ('cardtype', 'active', 'code'),
        )
        db_table = f'LG_{Active.namespace}_CAMPAIGN'
        target_db = 'erp'
