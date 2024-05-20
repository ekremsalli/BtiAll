"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_SERILOTN(
    BaseLogical,
    BaseItem,
    BaseSiteRec,
    BaseWF,
    BaseInfo,
    BaseRef,
    models.Model):
    """
        Malzeme seri/lot no bilgileri
    """
    sltype = models.SmallIntegerField(
        db_column='SLTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Seri'),
            (2, 'Lot')
        ],
        help_text='Seri lot/türü'
    )
    code = models.CharField(
        db_column='CODE',
        max_length=101,
        blank=True,
        null=True,
        help_text='Seri/lot kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=101,
        blank=True,
        null=True,
        help_text='Seri/lot açıklaması'
    )
    state = models.SmallIntegerField(
        db_column='STATE',
        blank=True,
        null=True,
        help_text='Durumu'
    )
    orglogoid = models.CharField(
        db_column='ORGLOGOID',
        max_length=25,
        blank=True,
        null=True,
        help_text=''
    )
    variantref = models.IntegerField(
        db_column='VARIANTREF',
        blank=True,
        null=True,
        help_text=''
    )
    grouplotno = models.CharField(
        db_column='GROUPLOTNO',
        max_length=101,
        blank=True,
        null=True,
        help_text=''
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_SERILOTN'
        unique_together = (('itemref', 'variantref', 'sltype', 'code'),)
        target_db = 'erp'

