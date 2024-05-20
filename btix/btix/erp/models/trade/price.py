"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_PRCLIST(
    BaseLogical,
    BaseTrading,
    BaseActive,
    BaseGUID,
    BaseSiteRec,
    BaseWF,
    BaseInfo,
    BasePriority,
    BaseProject,
    BaseRef,
    models.Model):
    """
        Alış/Satış fiyatları
    """
    cardref = models.ForeignKey(
        "LG_ITEMS",
        db_column='CARDREF',
        blank=True,
        null=True,
        help_text='Kart ref. -> ITEMS',
        on_delete=models.DO_NOTHING
    )
    clientcode = models.CharField(
        db_column='CLIENTCODE',
        max_length=17,
        blank=True,
        null=True,
        help_text='Stok kodu'
    )
    clspecode = models.CharField(
        db_column='CLSPECODE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Hizmet kart kodu'
    )
    payplanref = models.IntegerField(
        db_column='PAYPLANREF',
        blank=True,
        null=True
    )
    price = models.FloatField(
        db_column='PRICE',
        blank=True,
        null=True
    )
    uomref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UOMREF',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )
    incvat = models.SmallIntegerField(
        db_column='INCVAT',
        blank=True,
        null=True
    )
    currency = models.SmallIntegerField(
        db_column='CURRENCY',
        blank=True,
        null=True
    )
    ptype = models.SmallIntegerField(
        db_column='PTYPE',
        blank=True,
        null=True
    )
    mtrltype = models.SmallIntegerField(
        db_column='MTRLTYPE',
        blank=True,
        null=True,
    )
    leadtime = models.IntegerField(
        db_column='LEADTIME',
        blank=True,
        null=True
    )
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True,
        help_text='Temin süresi'
    )
    enddate = models.DateTimeField(
        db_column='ENDDATE',
        blank=True,
        null=True
    )
    condition = models.CharField(
        db_column='CONDITION', max_length=81, blank=True, null=True)
    shiptyp = models.CharField(
        db_column='SHIPTYP', max_length=11, blank=True, null=True)
    specialized = models.SmallIntegerField(
        db_column='SPECIALIZED', blank=True, null=True)
    unitconvert = models.SmallIntegerField(
        db_column='UNITCONVERT', blank=True, null=True)
    extaccessflags = models.IntegerField(
        db_column='EXTACCESSFLAGS', blank=True, null=True)
    cyphcode = models.CharField(
        db_column='CYPHCODE', max_length=11, blank=True, null=True)
    orglogoid = models.CharField(
        db_column='ORGLOGOID', max_length=25, blank=True, null=True)
    begtime = models.IntegerField(
        db_column='BEGTIME', blank=True, null=True)
    endtime = models.IntegerField(
        db_column='ENDTIME', blank=True, null=True)
    definition_field = models.CharField(
        db_column='DEFINITION_', max_length=51, blank=True, null=True)
    code = models.CharField(
        db_column='CODE', max_length=25, blank=True, null=True)
    grpcode = models.CharField(
        db_column='GRPCODE', max_length=17, blank=True, null=True)
    ordernr = models.SmallIntegerField(
        db_column='ORDERNR', blank=True, null=True)
    geniuspaytype = models.CharField(
        db_column='GENIUSPAYTYPE', max_length=3, blank=True, null=True)
    geniusshpnr = models.IntegerField(
        db_column='GENIUSSHPNR', blank=True, null=True)
    prcaltertyp1 = models.SmallIntegerField(
        db_column='PRCALTERTYP1', blank=True, null=True)
    prcalterlmt1 = models.FloatField(
        db_column='PRCALTERLMT1', blank=True, null=True)
    prcaltertyp2 = models.SmallIntegerField(
        db_column='PRCALTERTYP2', blank=True, null=True)
    prcalterlmt2 = models.FloatField(
        db_column='PRCALTERLMT2', blank=True, null=True)
    prcaltertyp3 = models.SmallIntegerField(
        db_column='PRCALTERTYP3', blank=True, null=True)
    prcalterlmt3 = models.FloatField(
        db_column='PRCALTERLMT3', blank=True, null=True)
    purchcontref = models.IntegerField(
        db_column='PURCHCONTREF', blank=True, null=True)
    branch = models.SmallIntegerField(
        db_column='BRANCH', blank=True, null=True)
    costval = models.FloatField(
        db_column='COSTVAL', blank=True, null=True)
    cltradinggrp = models.CharField(
        db_column='CLTRADINGGRP', max_length=17, blank=True, null=True)
    clcyphcode = models.CharField(
        db_column='CLCYPHCODE', max_length=11, blank=True, null=True)
    clspecode2 = models.CharField(
        db_column='CLSPECODE2', max_length=11, blank=True, null=True)
    clspecode3 = models.CharField(
        db_column='CLSPECODE3', max_length=11, blank=True, null=True)
    clspecode4 = models.CharField(
        db_column='CLSPECODE4', max_length=11, blank=True, null=True)
    clspecode5 = models.CharField(
        db_column='CLSPECODE5', max_length=11, blank=True, null=True)
    globalid = models.CharField(
        db_column='GLOBALID', max_length=51, blank=True, null=True)
    variantcode = models.CharField(
        db_column='VARIANTCODE', max_length=51, blank=True, null=True)
    wflowcrdref = models.IntegerField(
        db_column='WFLOWCRDREF', blank=True, null=True)
    markref = models.IntegerField(
        db_column='MARKREF', blank=True, null=True)
    trspecode = models.CharField(
        db_column='TRSPECODE', max_length=17, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_PRCLIST'
        unique_together = (('ptype', 'active', 'code'),)
        target_db = 'erp'
