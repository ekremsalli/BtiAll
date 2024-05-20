"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_BNBRANCH(
    BaseLogical,
    BaseSiteRec,
    BaseRef,
    models.Model):
    code = models.CharField(db_column='CODE', max_length=25, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=51, blank=True, null=True)
    cntrnr = models.IntegerField(db_column='CNTRNR', blank=True, null=True)
    bankref = models.IntegerField(db_column='BANKREF', blank=True, null=True)
    edicode = models.CharField(db_column='EDICODE', max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_BNBRANCH'
        unique_together = (('cntrnr', 'bankref', 'code'),)
        target_db = 'system'