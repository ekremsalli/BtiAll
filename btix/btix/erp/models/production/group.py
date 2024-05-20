"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_WSGRPF(
    BaseLogical,
    BaseCode,
    BaseApproved,
    BaseAccount,
    BaseCenter,
    BaseActive,
    BaseInfo,
    BaseTextINC,
    BaseSiteRec,
    BaseWF,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        İş istasyonu grupları
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=25,
        blank=True,
        null=True,
        help_text='Kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
    )
    operationtime = models.FloatField(
        db_column='OPERATIONTIME',
        blank=True,
        null=True,
        help_text='Günlük çalışma saati'
    )
    hourlystdcost = models.FloatField(
        db_column='HOURLYSTDCOST',
        blank=True,
        null=True,
        help_text='Saatlik maliyet'
    )
    hourlystdrpcost = models.FloatField(
        db_column='HOURLYSTDRPCOST',
        blank=True,
        null=True,
        help_text='Saatlik maliyet'
    )
    imageinc = models.SmallIntegerField(
        db_column='IMAGEINC',
        blank=True,
        null=True
    )
    hourdiffaccref = models.IntegerField(
        db_column='HOURDIFFACCREF',
        blank=True,
        null=True
    )
    hourdiffcenter = models.IntegerField(
        db_column='HOURDIFFCENTER',
        blank=True,
        null=True
    )
    paydiffaccref = models.IntegerField(
        db_column='PAYDIFFACCREF',
        blank=True,
        null=True
    )
    paydiffcenter = models.IntegerField(
        db_column='PAYDIFFCENTER',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_WSGRPF'
        unique_together = (('active', 'code'),)
        target_db = 'erp'

class LG_WSGRPASS(
    BaseLogical,
    BasePriority,
    models.Model):
    """
        İş istasyonu - Grup ataması
    """
    wsgrpref = models.ForeignKey(
        "LG_WSGRPF",
        db_column='WSGRPREF',
        blank=True,
        null=True,
        help_text='İş istasyonu grup ref -> ',
        on_delete=models.DO_NOTHING
    )
    wsref = models.ForeignKey(
        "LG_WORKSTAT",
        db_column='WSREF',
        blank=True,
        null=True,
        help_text='İş istasyonu ref -> WORKSTAT',
        on_delete=models.DO_NOTHING
    )
    dominshftgrp = models.SmallIntegerField(
        db_column='DOMINSHFTGRP',
        blank=True,
        null=True,
        help_text=''
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_WSGRPASS'
        target_db = 'erp'



