"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_STCOMPLN(
    BaseLogical,
    BaseClient,
    models.Model):
    """
        Karma koli satırları/mamul alt malzemeleri
    """
    stcref = models.ForeignKey(
        "LG_ITEMS",
        db_column='STCREF',
        blank=True,
        null=True,
        help_text='Stok kartı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_stcref"
    )
    amnt = models.FloatField(
        db_column='AMNT',
        blank=True,
        null=True,
        help_text='Miktar'
    )
    price = models.FloatField(
        db_column='PRICE',
        blank=True,
        null=True,
        help_text='Fiyat'
    )
    perc = models.FloatField(
        db_column='PERC',
        blank=True,
        null=True,
        help_text='Yüzde'
    )
    maincref = models.ForeignKey(
        "LG_ITEMS",
        db_column='MAINCREF',
        blank=True,
        null=True,
        help_text='Karma koli kart ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_maincref"
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    lostfactor = models.FloatField(
        db_column='LOSTFACTOR',
        blank=True,
        null=True
    )
    sourceindex = models.SmallIntegerField(
        db_column='SOURCEINDEX',
        blank=True,
        null=True
    )
    uomref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UOMREF',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True
    )
    department = models.SmallIntegerField(
        db_column='DEPARTMENT',
        blank=True,
        null=True
    )
    qprofcref = models.IntegerField(
        db_column='QPROFCREF',
        blank=True,
        null=True
    )
    vrntref = models.IntegerField(
        db_column='VRNTREF',
        blank=True,
        null=True
    )
    comptype = models.SmallIntegerField(
        db_column='COMPTYPE',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_STCOMPLN'
        target_db = 'erp'
