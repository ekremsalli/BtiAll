"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_DECARDS(
    BaseLogical,
    BaseCode,
    BaseInfo,
    BaseSiteRec,
    BaseActive,
    BaseWF,
    BaseVAT,
    BaseRef,
    models.Model):
    """
        İndirim / masraf kartları
    """
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Alış indirim'),
            (2, 'Satış indirim'),
            (3, 'Alış masraf'),
            (4, 'Satış masraf')
        ],
        help_text="""
            Kart türü;
            1 -> Alış indirim
            2 -> Satış indirim
            3 -> Alış masraf
            4 -> Satış masraf
        """
    )
    code = models.CharField(db_column='CODE', max_length=17, blank=True,
        null=True, help_text='Kart kodu')
    definition_field = models.CharField(db_column='DEFINITION_',
        max_length=51, blank=True, null=True,
        help_text='Açıklama'
    )
    formula = models.CharField(
        db_column='FORMULA',
        max_length=251,
        blank=True,
        null=True,
        help_text='Formül'
    )
    rndval = models.FloatField(
        db_column='RNDVAL',
        blank=True,
        null=True,
        help_text='Yuvarlama tabanı'
    )
    counter = models.IntegerField(
        db_column='COUNTER',
        blank=True,
        null=True,
        help_text='Sayaç'
    )
    unitstr = models.CharField(
        db_column='UNITSTR',
        max_length=5,
        blank=True,
        null=True,
        help_text='Birim'
    )
    lprodstat = models.SmallIntegerField(
        db_column='LPRODSTAT',
        blank=True,
        null=True,
        help_text='Üretim durumu'
    )
    extaccessflags = models.IntegerField(
        db_column='EXTACCESSFLAGS',
        blank=True,
        null=True
    )
    stoppagedisc = models.SmallIntegerField(
        db_column='STOPPAGEDISC',
        blank=True,
        null=True
    )
    globalcode = models.CharField(
        db_column='GLOBALCODE',
        max_length=11,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        unique_together = (
            ('cardtype', 'code'),
            ('cardtype', 'active', 'code'),
        )
        db_table = f'LG_{Active.namespace}_DECARDS'
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.definition_field}"