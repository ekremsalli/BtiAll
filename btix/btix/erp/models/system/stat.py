"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class LG_USAGESTAT(
    BaseLogical,
    models.Model):
    objhashid = models.IntegerField(db_column='OBJHASHID', unique=True, blank=True, null=True)
    usagecount = models.IntegerField(db_column='USAGECOUNT', blank=True, null=True)
    objtype = models.SmallIntegerField(db_column='OBJTYPE', blank=True, null=True)
    objname = models.CharField(db_column='OBJNAME', max_length=51, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LG_USAGESTAT'
        target_db = 'system'

    def __str__(self):
        return f'{self.objname}: {self.usagecount}'


"""
# NOT PRODIVING PK'S
class Drive(models.Model):
    drive = models.CharField(db_column='Drive', max_length=1, blank=True, null=True)
    dsize = models.IntegerField(db_column='Dsize', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'YTL_DRIVETBL'
        target_db = 'system'

    def __str__(self):
        return f'{self.drive} {self.dsize}'

class Table(models.Model):
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)
    rows = models.CharField(db_column='Rows', max_length=11, blank=True, null=True)
    reserved = models.CharField(max_length=18, blank=True, null=True)
    data = models.CharField(db_column='Data', max_length=18, blank=True, null=True)
    index_size = models.CharField(max_length=18, blank=True, null=True)
    unused = models.CharField(db_column='Unused', max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'YTL_SPACETBL'
        target_db = 'system'

    def __str__(self):
        return f'{self.name}'
"""