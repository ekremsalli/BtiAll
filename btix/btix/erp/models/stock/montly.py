"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_SRVTOT(
    BaseLogical,
    models.Model):
    """
        Hizmet kartı toplamları portu
        SRVTOT tablosunda hizmet kartlarının aylık borç ve alacak hesap
        toplamları tutulmaktadır. Her hizmet kartı için 14 adet toplam kaydı
        bulunmaktadır.
    """
    cardref = models.ForeignKey(
        "LG_SRVCARD",
        db_column='CARDREF',
        blank=True,
        null=True,
        help_text='Hizmet kartı ref. -> SRVCARD',
        on_delete=models.DO_NOTHING
    )
    invenno = models.SmallIntegerField(
        db_column='INVENNO',
        blank=True,
        null=True,
        help_text='Ambar numarası'
    )
    month_field = models.SmallIntegerField(
        db_column='MONTH_',
        blank=True,
        null=True,
        help_text='Ay'
    )
    totals_amount = models.FloatField(
        db_column='TOTALS_AMOUNT',
        blank=True,
        null=True,
        help_text='Aylık toplam satış tutarları (tüm aylar için)'
    )
    totals_cashamnt = models.FloatField(
        db_column='TOTALS_CASHAMNT',
        blank=True,
        null=True,
        help_text='Aylık toplam satış tutarları (tüm aylar için)'
    )
    totals_curramnt = models.FloatField(
        db_column='TOTALS_CURRAMNT',
        blank=True,
        null=True,
        help_text='Ayılk toplam satış tutarları (tüm aylar için)'
    )
    totals_vatamnt = models.FloatField(
        db_column='TOTALS_VATAMNT', blank=True, null=True)
    totals_discamnt = models.FloatField(
        db_column='TOTALS_DISCAMNT', blank=True, null=True)
    totals_retamnt = models.FloatField(
        db_column='TOTALS_RETAMNT', blank=True, null=True)
    year_field = models.SmallIntegerField(
        db_column='YEAR_', blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (
            ('cardref', 'invenno', 'month_field', 'totals_vatamnt'),
        )
        db_table = f'LG_{Active.namespace}_{Active.period}_SRVTOT'
        target_db = 'erp'
