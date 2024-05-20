"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class Emukellef(models.Model):
    identifier = models.CharField(db_column='Identifier', max_length=250, primary_key=True)
    title = models.TextField(db_column='Title', blank=True, null=True)
    type = models.CharField(db_column='Type', max_length=250, blank=True, null=True)
    accounttype = models.CharField(db_column='AccountType', max_length=250, blank=True, null=True)
    aliasinvoicepk = models.CharField(db_column='AliasInvoicePK', max_length=250, blank=True, null=True)
    aliasinvoicegb = models.CharField(db_column='AliasInvoiceGB', max_length=250, blank=True, null=True)
    aliasdespatchadvicepk = models.CharField(db_column='AliasDespatchAdvicePK', max_length=250, blank=True, null=True)
    aliasdespatchadvicegb = models.CharField(db_column='AliasDespatchAdviceGB', max_length=250, blank=True, null=True)
    firstcreationtimeinvoicepk = models.DateField(db_column='FirstCreationTimeInvoicePK', blank=True, null=True)
    firstcreationtimeinvoicegb = models.DateField(db_column='FirstCreationTimeInvoiceGB', blank=True, null=True)
    aliascreationtimeinvoicepk = models.DateField(db_column='AliasCreationTimeInvoicePK', blank=True, null=True)
    aliasdeletiontimeinvoicepk = models.DateField(db_column='AliasDeletionTimeInvoicePK', blank=True, null=True)
    aliascreationtimeinvoicegb = models.DateField(db_column='AliasCreationTimeInvoiceGB', blank=True, null=True)
    aliasdeletiontimeinvoicegb = models.DateField(db_column='AliasDeletionTimeInvoiceGB', blank=True, null=True)
    aliascreationtimedespatchadvicepk = models.DateField(db_column='AliasCreationTimeDespatchAdvicePK', blank=True, null=True)
    aliascreationtimedespatchadvicegb = models.DateField(db_column='AliasCreationTimeDespatchAdviceGB', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BTI_EMUKELLEF'
        target_db = 'system'

    def __str__(self):
        return f"{self.identifier} - {self.title}"        
