"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_ROUTING(
    BaseLogical,
    BaseApproved,
    BaseActive,
    BaseInfo,
    BaseCode,
    BaseSiteRec,
    BaseTextINC,
    BaseWF,
    BasePrint,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Üretim rotaları
    """
    code = models.CharField(
        db_column='CODE',
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
        help_text='Açıklaması'
    )
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True
    )
    printdate = models.DateTimeField(
        db_column='PRINTDATE',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ROUTING'
        unique_together = (('cardtype', 'code'),)
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"

class LG_RTNGLINE(
    BaseLogical,
    BaseSiteRec,
    BaseWF,
    BaseRef,
    models.Model):
    """
        Üretim rota satırları
    """
    routingref = models.ForeignKey(
        "LG_ROUTING",
        db_column='ROUTINGREF',
        blank=True,
        null=True,
        help_text='Rota ref. -> ROUTING',
        on_delete=models.DO_NOTHING
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    operationref = models.ForeignKey(
        "LG_OPERTION",
        db_column='OPERATIONREF',
        blank=True,
        null=True,
        help_text='Operasyon ref. -> OPERTION',
        on_delete=models.DO_NOTHING
    )
    specode = models.CharField(
        db_column='SPECODE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Özel kod'
    )
    costrelated = models.SmallIntegerField(
        db_column='COSTRELATED',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Maliyet hesaplanacak'
    )
    planrelated = models.SmallIntegerField(
        db_column='PLANRELATED',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Planlama yapılacak'
    )
    outitemref = models.ForeignKey(
        "LG_ITEMS",
        db_column='OUTITEMREF',
        blank=True,
        null=True,
        help_text='Malzeme ref. -> ITEMS',
        on_delete=models.DO_NOTHING
    )
    lineexp = models.CharField(
        db_column='LINEEXP',
        max_length=51,
        blank=True,
        null=True,
        help_text='Satır açıklaması'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_RTNGLINE'
        target_db = 'erp'
