"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_PRDCOST(
    BaseLogical,
    BaseItem,
    models.Model):
    """
        Maliyet dönem kapama kayıtları
    """
    prdenddate = models.DateTimeField(
        db_column='PRDENDDATE',
        blank=True,
        null=True
    )
    prdendtime = models.IntegerField(
        db_column='PRDENDTIME',
        blank=True,
        null=True
    )
    prdcosttype = models.SmallIntegerField(
        db_column='PRDCOSTTYPE',
        blank=True,
        null=True
    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True
    )
    invencosttype = models.SmallIntegerField(
        db_column='INVENCOSTTYPE',
        blank=True,
        null=True
    )
    invencostgrpnr = models.SmallIntegerField(
        db_column='INVENCOSTGRPNR', blank=True, null=True)
    invencostwsref = models.IntegerField(
        db_column='INVENCOSTWSREF', blank=True, null=True)
    sttransref = models.IntegerField(
        db_column='STTRANSREF', blank=True, null=True)
    totamnt = models.FloatField(
        db_column='TOTAMNT', blank=True, null=True)
    totval = models.FloatField(
        db_column='TOTVAL', blank=True, null=True)
    totcurr = models.FloatField(
        db_column='TOTCURR', blank=True, null=True)
    totdiffval = models.FloatField(
        db_column='TOTDIFFVAL', blank=True, null=True)
    totdiffcurr = models.FloatField(
        db_column='TOTDIFFCURR', blank=True, null=True)
    mainunitref = models.IntegerField(
        db_column='MAINUNITREF', blank=True, null=True)
    totataxval = models.FloatField(
        db_column='TOTATAXVAL', blank=True, null=True)
    totataxcurr = models.FloatField(
        db_column='TOTATAXCURR', blank=True, null=True)
    totinf = models.FloatField(
        db_column='TOTINF', blank=True, null=True)
    totdiffinf = models.FloatField(
        db_column='TOTDIFFINF', blank=True, null=True)
    variantref = models.IntegerField(
        db_column='VARIANTREF', blank=True, null=True)
    totdiffprice = models.FloatField(
        db_column='TOTDIFFPRICE', blank=True, null=True)
    totdiffrepprice = models.FloatField(
        db_column='TOTDIFFREPPRICE', blank=True, null=True)
    totvalufrs = models.FloatField(
        db_column='TOTVALUFRS', blank=True, null=True)
    totcurrufrs = models.FloatField(
        db_column='TOTCURRUFRS', blank=True, null=True)
    totinfufrs = models.FloatField(
        db_column='TOTINFUFRS', blank=True, null=True)
    totdiffvalufrs = models.FloatField(
        db_column='TOTDIFFVALUFRS', blank=True, null=True)
    totdiffcurrufrs = models.FloatField(
        db_column='TOTDIFFCURRUFRS', blank=True, null=True)
    totdiffinfufrs = models.FloatField(
        db_column='TOTDIFFINFUFRS', blank=True, null=True)
    totadjvalufrs = models.FloatField(
        db_column='TOTADJVALUFRS', blank=True, null=True)
    totadjcurrufrs = models.FloatField(
        db_column='TOTADJCURRUFRS', blank=True, null=True)
    totadjinfufrs = models.FloatField(
        db_column='TOTADJINFUFRS', blank=True, null=True)
    totdiffpriceufrs = models.FloatField(
        db_column='TOTDIFFPRICEUFRS', blank=True, null=True)
    totdiffreppriceufrs = models.FloatField(
        db_column='TOTDIFFREPPRICEUFRS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_PRDCOST'
        target_db = 'erp'
