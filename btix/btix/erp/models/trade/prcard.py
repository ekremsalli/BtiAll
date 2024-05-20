"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_PRCARDS(
    BaseLogical,
    BaseWF,
    BaseActive,
    BaseSiteRec,
    BaseInfo,
    BaseCode,
    BaseRef,
    models.Model):
    """
        Promosyon kartları
    """
    code = models.CharField(
        db_column='CODE',
        max_length=17,
        blank=True,
        null=True,
        help_text='Promosyon kart kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Alış promosyon'),
            (2, 'Satış promosyon')
        ],
        help_text='Kart tipi'
    )
    stockref = models.ForeignKey(
        "LG_ITEMS",
        db_column='STOCKREF',
        blank=True,
        null=True,
        help_text='Malzeme kartı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_stockref"
    )
    mtrltype = models.SmallIntegerField(
        db_column='MTRLTYPE',
        blank=True,
        null=True,
        help_text='Malzeme tipi'
    )
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True,
        help_text='Başlangıç tarihi'
    )
    enddate = models.DateTimeField(
        db_column='ENDDATE',
        blank=True,
        null=True,
        help_text='Bitiş tarihi'
    )
    counter = models.IntegerField(
        db_column='COUNTER',
        blank=True,
        null=True,
        help_text='Sayaç'
    )
    price = models.FloatField(
        db_column='PRICE',
        blank=True,
        null=True,
        help_text='Fiyat'
    )
    promlines1_stockref = models.ForeignKey(
        "LG_ITEMS",
        db_column='PROMLINES1_STOCKREF',
        blank=True,
        null=True,
        help_text='Malzeme kartı ref -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_promlines1_stockref"
    )
    promlines1_formula = models.CharField(
        db_column='PROMLINES1_FORMULA',
        max_length=81,
        blank=True,
        null=True,
        help_text='Formül'
    )
    promlines1_price = models.FloatField(
        db_column='PROMLINES1_PRICE',
        blank=True,
        null=True,
        help_text='Fiyat'
    )
    promlines1_rndval = models.FloatField(
        db_column='PROMLINES1_RNDVAL',
        blank=True,
        null=True,
        help_text='Yuvarlama'
    )
    promlines1_uomref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='PROMLINES1_UOMREF',
        blank=True,
        null=True,
        help_text='Birim ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_promlines1_uomref"
    )
    promlines1_siteid = models.SmallIntegerField(
        db_column='PROMLINES1_SITEID',
        blank=True,
        null=True,
        help_text='Bölge no'
    )
    promlines1_recstatus = models.SmallIntegerField(
        db_column='PROMLINES1_RECSTATUS',
        blank=True,
        null=True
    )
    promlines1_orglogicref = models.IntegerField(
        db_column='PROMLINES1_ORGLOGICREF',
        blank=True,
        null=True,
        help_text='Orjinal kayıt ref.'
    )
    promlines1_wfstatus = models.IntegerField(
        db_column='PROMLINES1_WFSTATUS',
        blank=True,
        null=True
    )
    promlines1_variantref = models.IntegerField(
        db_column='PROMLINES1_VARIANTREF',
        blank=True,
        null=True
    )
    promlines17_stockref = models.ForeignKey(
        "LG_ITEMS",
        db_column='PROMLINES17_STOCKREF',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_promlines17_stockref"
    )
    promlines17_formula = models.CharField(
        db_column='PROMLINES17_FORMULA',
        max_length=81,
        blank=True,
        null=True
    )
    promlines17_price = models.FloatField(
        db_column='PROMLINES17_PRICE',
        blank=True,
        null=True
    )
    promlines17_rndval = models.FloatField(
        db_column='PROMLINES17_RNDVAL',
        blank=True,
        null=True
    )
    promlines17_uomref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='PROMLINES17_UOMREF',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_promlines17_uomref"
    )
    promlines17_siteid = models.SmallIntegerField(
        db_column='PROMLINES17_SITEID',
        blank=True,
        null=True
    )
    promlines17_recstatus = models.SmallIntegerField(
        db_column='PROMLINES17_RECSTATUS',
        blank=True,
        null=True
    )
    promlines17_orglogicref = models.IntegerField(
        db_column='PROMLINES17_ORGLOGICREF',
        blank=True,
        null=True
    )
    promlines17_wfstatus = models.IntegerField(
        db_column='PROMLINES17_WFSTATUS',
        blank=True,
        null=True
    )
    promlines217variantref = models.IntegerField(
        db_column='PROMLINES17_VARIANTREF',
        blank=True,
        null=True
    )


    fichemodul = models.SmallIntegerField(
        db_column='FICHEMODUL',
        blank=True,
        null=True,
        help_text='Fiş modül numarası'
    )
    fichetypes1 = models.SmallIntegerField(
        db_column='FICHETYPES1',
        blank=True,
        null=True,
        help_text='Malzeme fişleri'
    )
    fichetypes2 = models.SmallIntegerField(
        db_column='FICHETYPES2',
        blank=True,
        null=True,
        help_text='Satınalma fişleri'
    )
    fichetypes3 = models.SmallIntegerField(
        db_column='FICHETYPES3',
        blank=True,
        null=True,
        help_text='Satış ve dağıtım fişleri'
    )
    ordfcmodul = models.SmallIntegerField(
        db_column='ORDFCMODUL',
        blank=True,
        null=True
    )
    variantref = models.IntegerField(
        db_column='VARIANTREF',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_PRCARDS'
        unique_together = (
            ('cardtype', 'code'),
            ('cardtype', 'promlines17_uomref', 'code'),
        )
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.definition_field}"
