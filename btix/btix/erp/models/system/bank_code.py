"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_BANKCODE(
    BaseLogical,
    models.Model):
    # bu bir relation olmali!
    cntrnr = models.IntegerField(db_column='CNTRNR', blank=True, null=True)
    code = models.CharField(db_column='CODE', max_length=25, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=51, blank=True, null=True)
    siteid = models.SmallIntegerField(db_column='SITEID', blank=True, null=True)
    recstatus = models.SmallIntegerField(db_column='RECSTATUS', blank=True, null=True)
    orglogicref = models.IntegerField(db_column='ORGLOGICREF', blank=True, null=True)
    edicode = models.CharField(db_column='EDICODE', max_length=25, blank=True, null=True)
    bicode = models.CharField(db_column='BICODE', max_length=25, blank=True, null=True)
    corrpacc = models.CharField(db_column='CORRPACC', max_length=51, blank=True, null=True)
    voen = models.CharField(db_column='VOEN', max_length=51, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_BANKCODE'
        unique_together = (('cntrnr', 'code'),)
        target_db = 'system'

    def __str__(self):
        return f"{self.code} - {self.name}"
