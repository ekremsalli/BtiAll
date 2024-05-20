"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_PROJECT(
    BaseLogical,
    BaseCode,
    BaseInfo,
    BaseActive,
    BaseSiteRec,
    BaseRef,
    BaseWF,
    BaseGUID,
    models.Model):
    code = models.CharField(db_column='CODE', unique=True, max_length=101, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=101, blank=True, null=True)
    prjrespon = models.CharField(db_column='PRJRESPON', max_length=81, blank=True, null=True)
    enddate = models.DateTimeField(db_column='ENDDATE', blank=True, null=True)
    begdate = models.DateTimeField(db_column='BEGDATE', blank=True, null=True)
    ioctrl = models.SmallIntegerField(db_column='IOCTRL', blank=True, null=True)
    specode4 = models.CharField(db_column='SPECODE4', max_length=11, blank=True, null=True)
    specode5 = models.CharField(db_column='SPECODE5', max_length=11, blank=True, null=True)
    specode2 = models.CharField(db_column='SPECODE2', max_length=11, blank=True, null=True)
    specode3 = models.CharField(db_column='SPECODE3', max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (('active', 'code'),)
        db_table = f'LG_{Active.namespace}_PROJECT'
        target_db = 'erp'