"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_BNCARD(
    BaseLogical,
    BaseWF,
    BaseTextINC,
    BaseAddress,
    BaseActive,
    BaseInfo,
    BaseCode,
    BaseSiteRec,
    BaseContact,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Bankalar
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=7,
        blank=True,
        null=True,
        help_text='Banka kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=51,
        blank=True,
        null=True,
        help_text='Banka adı'
    )
    branch = models.CharField(
        db_column='BRANCH',
        max_length=21,
        blank=True,
        null=True,
        help_text='Banka şubesi'
    )
    branchno = models.CharField(
        db_column='BRANCHNO',
        max_length=17,
        blank=True,
        null=True,
        help_text='Şube numarası'
    )
    incharge = models.CharField(
        db_column='INCHARGE',
        max_length=21,
        blank=True,
        null=True,
        help_text='Yetkili'
    )
    webaddr = models.CharField(
        db_column='WEBADDR',
        max_length=101,
        blank=True,
        null=True,
        help_text='Web adresi'
    )
    cntrycode = models.CharField(
        db_column='CNTRYCODE',
        max_length=13,
        blank=True,
        null=True,
        help_text='Ülke ref.'
    )
    corrpacc = models.CharField(
        db_column='CORRPACC',
        max_length=51,
        blank=True,
        null=True
    )
    voen = models.CharField(
        db_column='VOEN',
        max_length=51,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        unique_together = (('active', 'code'),)
        db_table = f'LG_{Active.namespace}_BNCARD'
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.definition_field}"