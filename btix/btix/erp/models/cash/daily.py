"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_CSHTOTS(
    BaseLogical,
    models.Model):
    """
        Kasa günlük toplamları;
        CSHTOTS tablosunda kasa kartlarına ait (KSCARD) ait günlük
        kasa toplamları oluşmaktadır. Veri tabanında hareket
        olmayan günlere ait kasa toplam kaydı bulunmamaktadır.
    """
    cardref = models.ForeignKey(
        "LG_KSCARD",
        db_column='CARDREF',
        blank=True,
        null=True,
        help_text='Kasa ref. -> KSCARD',
        on_delete=models.DO_NOTHING
    )
    tottype = models.SmallIntegerField(
        db_column='TOTTYPE',
        blank=True,
        null=True,
        help_text='Toplam türü (TL ya da döviz)'
    )
    day_field = models.SmallIntegerField(
        db_column='DAY_',
        blank=True,
        null=True,
        help_text='Gün (Yılın kaçıncı gününe ait kasa toplamı olduğunu gösterir)'
    )
    debit = models.FloatField(
        db_column='DEBIT',
        blank=True,
        null=True,
        help_text='Borç'
    )
    credit = models.FloatField(
        db_column='CREDIT',
        blank=True,
        null=True,
        help_text='Alacak'
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    currtyp = models.SmallIntegerField(
        db_column='CURRTYP',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        unique_together = (
            ('cardref', 'tottype', 'day_field', 'date_field', 'currtyp'),
        )
        db_table = f'LG_{Active.namespace}_{Active.period}_CSHTOTS'
        target_db = 'erp'
