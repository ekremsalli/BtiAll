"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_EBOOKDETAILDOC(
    BaseLogical,
    models.Model):
    emficheref = models.ForeignKey(
        "LG_EMFICHE",
        db_column='EMFICHEREF',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_emficheref"
    )
    documenttype = models.SmallIntegerField(
        db_column='DOCUMENTTYPE', blank=True, null=True)
    explain = models.CharField(
        db_column='EXPLAIN', max_length=51, blank=True, null=True)
    documentnr = models.CharField(
        db_column='DOCUMENTNR', max_length=33, blank=True, null=True)
    documentdate = models.DateTimeField(
        db_column='DOCUMENTDATE', blank=True, null=True)
    paytype = models.CharField(
        db_column='PAYTYPE', max_length=51, blank=True, null=True)
    undocumented = models.SmallIntegerField(
        db_column='UNDOCUMENTED', blank=True, null=True)
    nopayment = models.SmallIntegerField(
        db_column='NOPAYMENT', blank=True, null=True)
    emflineref = models.ForeignKey(
        "LG_EMFLINE",
        db_column='EMFLINEREF',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_emflineref"
    )
    modulenr = models.SmallIntegerField(
        db_column='MODULENR', blank=True, null=True)
    sourcefref = models.IntegerField(
        db_column='SOURCEFREF', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_EBOOKDETAILDOC'
        unique_together = (('emficheref', 'emflineref', 'modulenr', 'sourcefref'),)
        target_db = 'erp'
