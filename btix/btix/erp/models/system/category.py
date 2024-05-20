"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class LG_CATEGLISTS(
    BaseLogical,
    models.Model):
    categid = models.IntegerField(db_column='CATEGID', blank=True, null=True)
    lineno_field = models.SmallIntegerField(db_column='LINENO_', blank=True, null=True)
    tag = models.IntegerField(db_column='TAG', blank=True, null=True)
    catdesc = models.CharField(db_column='CATDESC', max_length=51, blank=True, null=True)
    custom = models.SmallIntegerField(db_column='CUSTOM', blank=True, null=True)
    recordid = models.IntegerField(db_column='RECORDID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LG_CATEGLISTS'
        target_db = 'system'

    def __str__(self):
        return f'{self.catdesc}'
