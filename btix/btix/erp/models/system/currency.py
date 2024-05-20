"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_CURRENCYLIST(
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
    curtype = models.SmallIntegerField(db_column='CURTYPE', blank=True, null=True)
    curcode = models.CharField(db_column='CURCODE', max_length=6, blank=True, null=True)
    curname = models.CharField(db_column='CURNAME', max_length=31, blank=True, null=True)
    coef = models.SmallIntegerField(db_column='COEF', blank=True, null=True)
    subdigits = models.SmallIntegerField(db_column='SUBDIGITS', blank=True, null=True)
    subname = models.CharField(db_column='SUBNAME', max_length=11, blank=True, null=True)
    divflag = models.SmallIntegerField(db_column='DIVFLAG', blank=True, null=True)
    emucurr = models.SmallIntegerField(db_column='EMUCURR', blank=True, null=True)
    eurorate = models.FloatField(db_column='EURORATE', blank=True, null=True)
    sublimit = models.SmallIntegerField(db_column='SUBLIMIT', blank=True, null=True)
    cursymbol = models.CharField(db_column='CURSYMBOL', max_length=6, blank=True, null=True)
    roundmtd = models.SmallIntegerField(db_column='ROUNDMTD', blank=True, null=True)
    triexch = models.SmallIntegerField(db_column='TRIEXCH', blank=True, null=True)
    curinuse = models.SmallIntegerField(db_column='CURINUSE', blank=True, null=True)
    globalid = models.CharField(db_column='GLOBALID', max_length=51, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CURRENCYLIST'
        unique_together = (('firm', 'curtype'), ('firm', 'curcode'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.curcode} {self.curname}'

class L_CURRENCYPARS(
    BaseLogical,
    models.Model):
    firm = models.OneToOneField(
        "L_CAPIFIRM",
        db_column='FIRMNR',
        unique=True,
        blank=True,
        null=True,
        to_field='nr',
        on_delete=models.DO_NOTHING
    )
    exctypheads1 = models.CharField(db_column='EXCTYPHEADS1', max_length=21, blank=True, null=True)
    exctypheads2 = models.CharField(db_column='EXCTYPHEADS2', max_length=21, blank=True, null=True)
    exctypheads3 = models.CharField(db_column='EXCTYPHEADS3', max_length=21, blank=True, null=True)
    exctypheads4 = models.CharField(db_column='EXCTYPHEADS4', max_length=21, blank=True, null=True)
    useexctype = models.SmallIntegerField(db_column='USEEXCTYPE', blank=True, null=True)
    ptolerperc = models.SmallIntegerField(db_column='PTOLERPERC', blank=True, null=True)
    ntolerperc = models.SmallIntegerField(db_column='NTOLERPERC', blank=True, null=True)
    chktoler = models.SmallIntegerField(db_column='CHKTOLER', blank=True, null=True)
    chktolerexc = models.SmallIntegerField(db_column='CHKTOLEREXC', blank=True, null=True)
    chktolertrn = models.SmallIntegerField(db_column='CHKTOLERTRN', blank=True, null=True)
    monfrac = models.SmallIntegerField(db_column='MONFRAC', blank=True, null=True)
    useexctypeitm = models.SmallIntegerField(db_column='USEEXCTYPEITM', blank=True, null=True)
    useexctypeprch = models.SmallIntegerField(db_column='USEEXCTYPEPRCH', blank=True, null=True)
    useexctypesale = models.SmallIntegerField(db_column='USEEXCTYPESALE', blank=True, null=True)
    useexctypecl = models.SmallIntegerField(db_column='USEEXCTYPECL', blank=True, null=True)
    useexctypecs = models.SmallIntegerField(db_column='USEEXCTYPECS', blank=True, null=True)
    useexctypebn = models.SmallIntegerField(db_column='USEEXCTYPEBN', blank=True, null=True)
    useexctypecash = models.SmallIntegerField(db_column='USEEXCTYPECASH', blank=True, null=True)
    useexctypeimport = models.SmallIntegerField(db_column='USEEXCTYPEIMPORT', blank=True, null=True)
    useexctypeexport = models.SmallIntegerField(db_column='USEEXCTYPEEXPORT', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CURRENCYPARS'
        target_db = 'system'

    def __str__(self):
        return f'{self.exctypheads1} {self.exctypheads2} {self.exctypheads3} {self.exctypheads4}'
