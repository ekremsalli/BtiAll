"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_PEGGING(
    BaseLogical,
    BaseItem,
    BaseAmount,
    models.Model):
    """
        İşlem bağlantıları (üretim emri, sipariş)
    """
    pegtype = models.SmallIntegerField(
        db_column='PEGTYPE',
        blank=True,
        null=True,
        help_text='İşlem bağlantısı tipi'
    )
    pegref = models.IntegerField(
        db_column='PEGREF',
        blank=True,
        null=True,
        help_text='İşlem bağlantısı ref.'
    )
    reltype = models.SmallIntegerField(
        db_column='RELTYPE',
        blank=True,
        null=True,
        help_text="""
            pegtype 0 ise ->
                0 -> Üretim emri
                1 -> Verilen sipariş
            pegtype 1 ise ->
                0 -> Üretim emri
                1 -> Alınan sipariş
        """
    )
    prodordref = models.ForeignKey(
        "LG_PRODORD",
        db_column='PRODORDREF',
        blank=True,
        null=True,
        help_text='Üretim emirleri kartı -> PRODORD',
        on_delete=models.DO_NOTHING
    )
    subcontref = models.IntegerField(
        db_column='SUBCONTREF',
        blank=True,
        null=True,
        help_text='Fason ref'
    )
    pordficheref = models.IntegerField(
        db_column='PORDFICHEREF',
        blank=True,
        null=True,
        help_text='Sipariş fişi ref.'
    )
    pordlineref = models.IntegerField(
        db_column='PORDLINEREF',
        blank=True,
        null=True,
        help_text='Sipariş satırı ref'
    )
    uomref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UOMREF',
        blank=True,
        null=True,
        help_text='Birim ref -> UNITSETL',
        on_delete=models.DO_NOTHING
    )
    canchange = models.SmallIntegerField(
        db_column='CANCHANGE',
        blank=True,
        null=True,
        help_text='Değiştirebilir'
    )
    displineref = models.IntegerField(
        db_column='DISPLINEREF', blank=True, null=True)
    prodlineref = models.IntegerField(
        db_column='PRODLINEREF', blank=True, null=True)
    otherpegref = models.IntegerField(
        db_column='OTHERPEGREF', blank=True, null=True)
    periodnr = models.IntegerField(
        db_column='PERIODNR', blank=True, null=True)
    mrppropref = models.IntegerField(
        db_column='MRPPROPREF', blank=True, null=True)
    pdemficheref = models.IntegerField(
        db_column='PDEMFICHEREF', blank=True, null=True)
    pdemlineref = models.IntegerField(
        db_column='PDEMLINEREF', blank=True, null=True)
    variantref = models.IntegerField(
        db_column='VARIANTREF', blank=True, null=True)
    fichetype = models.SmallIntegerField(
        db_column='FICHETYPE', blank=True, null=True)
    prodordtyp = models.SmallIntegerField(
        db_column='PRODORDTYP', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_PEGGING'
        target_db = 'erp'

