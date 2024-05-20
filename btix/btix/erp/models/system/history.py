"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class LG_HISTORY(
    BaseLogical,
    models.Model):
    tableid = models.IntegerField(db_column='TABLEID', blank=True, null=True)
    dataref = models.IntegerField(db_column='DATAREF', blank=True, null=True)
    modifiedby = models.SmallIntegerField(db_column='MODIFIEDBY', blank=True, null=True)
    modifieddate = models.DateTimeField(db_column='MODIFIEDDATE', blank=True, null=True)
    modifiedhour = models.SmallIntegerField(db_column='MODIFIEDHOUR', blank=True, null=True)
    modifiedmin = models.SmallIntegerField(db_column='MODIFIEDMIN', blank=True, null=True)
    modifiedsec = models.SmallIntegerField(db_column='MODIFIEDSEC', blank=True, null=True)
    username = models.CharField(db_column='USERNAME', max_length=21, blank=True, null=True)
    modiftxt = models.CharField(db_column='MODIFTXT', max_length=201, blank=True, null=True)
    dataguid = models.CharField(db_column='DATAGUID', max_length=37, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LG_HISTORY'
        unique_together = (('tableid', 'dataref', 'logicalref'),)
        target_db = 'system'

    def __str__(self):
        return f'{self.tableid} {self.username}'
