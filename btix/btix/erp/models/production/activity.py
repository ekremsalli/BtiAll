"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_ACTIVITYAMNT(
    BaseLogical,
    BaseAmount,
    models.Model):
    prodordref = models.IntegerField(
        db_column='PRODORDREF',
        blank=True,
        null=True,
        help_text='Üretim emri ref.'
    )
    displineref = models.IntegerField(
        db_column='DISPLINEREF',
        blank=True,
        null=True,
        help_text='İş emri ref.'
    )
    ovhdtrref = models.IntegerField(
        db_column='OVHDTRREF',
        blank=True,
        null=True,
        help_text='Standart genel gider ref.'
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ACTIVITYAMNT'
        target_db = 'erp'

    #rels -> L_PRODORD, L_DISPLINE, L_OVHDTRANS
