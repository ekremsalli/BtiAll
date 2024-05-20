"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_ROUTE(
    BaseLogical,
    BaseSiteRec,
    BaseInfo,
    BaseSalesMan,
    BaseCode,
    BaseRef,
    models.Model):
    """
        Satış yönetim raporları? (hatalı olabilir)
    """
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Rota kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=51,
        blank=True,
        null=True,
        help_text='Rota açıklaması'
    )
    status = models.SmallIntegerField(
        db_column='STATUS',
        blank=True,
        null=True,
        help_text='Rota geçerlilik durumu'
    )
    period = models.CharField(
        db_column='PERIOD',
        max_length=16,
        blank=True,
        null=True,
        help_text='Rota periyotu'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ROUTE'
        unique_together = (('salesmanref', 'code'),)
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.definition_field}"


class LG_ROUTETRS(
    BaseLogical,
    BaseClient,
    models.Model):
    """
        Satış rota satırları
    """
    routeref = models.ForeignKey(
        "LG_ROUTE",
        db_column='ROUTEREF',
        blank=True,
        null=True,
        help_text='Rota ref. -> ROUTE',
        on_delete=models.DO_NOTHING
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Rota satır numarası'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ROUTETRS'
        unique_together = (
            ('routeref', 'lineno_field'),
            ('clientref', 'routeref'),
        )
        target_db = 'erp'