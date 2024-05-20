"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_SHIPINFO(
    BaseLogical,
    BaseClient,
    BaseContact,
    BaseTax,
    BaseCode,
    BaseAddress,
    BaseInfo,
    BaseSiteRec,
    BaseActive,
    BaseTrading,
    BaseTextINC,
    BaseRef,
    models.Model):
    """
        Sevkiyat adresi
    """
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True
    )
    postcode = models.CharField(
        db_column='POSTCODE',
        max_length=11,
        blank=True,
        null=True
    )
    towncode = models.CharField(
        db_column='TOWNCODE',
        max_length=13,
        blank=True,
        null=True
    )
    districtcode = models.CharField(
        db_column='DISTRICTCODE',
        max_length=13,
        blank=True,
        null=True
    )
    citycode = models.CharField(
        db_column='CITYCODE',
        max_length=13,
        blank=True,
        null=True
    )
    countrycode = models.CharField(
        db_column='COUNTRYCODE',
        max_length=13,
        blank=True,
        null=True
    )
    inchange = models.CharField(
        db_column='INCHANGE',
        max_length=21,
        blank=True,
        null=True
    )
    telcodes1 = models.CharField(db_column='TELCODES1', max_length=9,
        blank=True, null=True)
    telcodes2 = models.CharField(db_column='TELCODES2', max_length=9,
        blank=True, null=True)
    faxcode = models.CharField(db_column='FAXCODE', max_length=9,
        blank=True, null=True)
    longitude = models.CharField(db_column='LONGITUDE', max_length=41,
        blank=True, null=True)
    latitute = models.CharField(db_column='LATITUTE', max_length=41,
        blank=True, null=True)
    cityid = models.CharField(db_column='CITYID', max_length=9,
        blank=True, null=True)
    townid = models.CharField(db_column='TOWNID', max_length=18,
        blank=True, null=True)
    shipbegtime1 = models.IntegerField(db_column='SHIPBEGTIME1',
        blank=True, null=True)
    shipbegtime2 = models.IntegerField(db_column='SHIPBEGTIME2',
        blank=True, null=True)
    shipbegtime3 = models.IntegerField(db_column='SHIPBEGTIME3',
        blank=True, null=True)
    shipendtime1 = models.IntegerField(db_column='SHIPENDTIME1',
        blank=True, null=True)
    shipendtime2 = models.IntegerField(db_column='SHIPENDTIME2',
        blank=True, null=True)
    shipendtime3 = models.IntegerField(db_column='SHIPENDTIME3',
        blank=True, null=True)
    postlabelcode = models.CharField(db_column='POSTLABELCODE',
        max_length=101, blank=True, null=True)
    senderlabelcode = models.CharField(db_column='SENDERLABELCODE',
        max_length=101, blank=True, null=True)
    title = models.CharField(db_column='TITLE', max_length=201,
        blank=True, null=True)
    defaultflg = models.SmallIntegerField(db_column='DEFAULTFLG',
        blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (
            ('clientref', 'code'),
            ('clientref', 'active', 'code'),
        )
        db_table = f'LG_{Active.namespace}_SHIPINFO'
        target_db = 'erp'

