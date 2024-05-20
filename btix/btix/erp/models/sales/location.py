"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_LOCATION(
    BaseLogical,
    BaseSiteRec,
    BaseWF,
    BasePriority,
    BaseRef,
    models.Model):
    """
        Stok yerleri
    """
    invennr = models.SmallIntegerField(
        db_column='INVENNR',
        blank=True,
        null=True,
        help_text='Ambar no'
    )
    code = models.CharField(
        db_column='CODE',
        max_length=101,
        blank=True,
        null=True,
        help_text='Stok yeri kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=101,
        blank=True,
        null=True,
        help_text='Stok yeri açıklaması'
    )
    width = models.FloatField(
        db_column='WIDTH',
        blank=True,
        null=True
    )
    length = models.FloatField(db_column='LENGTH', blank=True, null=True)
    height = models.FloatField(db_column='HEIGHT', blank=True, null=True)
    widthref = models.IntegerField(
        db_column='WIDTHREF', blank=True, null=True)
    lengthref = models.IntegerField(
        db_column='LENGTHREF', blank=True, null=True)
    heightref = models.IntegerField(
        db_column='HEIGHTREF', blank=True, null=True)
    minlevel = models.FloatField(db_column='MINLEVEL', blank=True, null=True)
    maxlevel = models.FloatField(db_column='MAXLEVEL', blank=True, null=True)
    shelftype = models.SmallIntegerField(
        db_column='SHELFTYPE', blank=True, null=True)
    contenttype = models.SmallIntegerField(
        db_column='CONTENTTYPE', blank=True, null=True)
    usetref = models.IntegerField(db_column='USETREF', blank=True, null=True)
    uomref = models.IntegerField(
        db_column='UOMREF',
        blank=True,
        null=True
    )
    iseuropalette = models.SmallIntegerField(
        db_column='ISEUROPALETTE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_LOCATION'
        unique_together = (('invennr', 'code'),)
        target_db = 'erp'
