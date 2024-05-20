"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_SRVCARD(
    BaseLogical,
    BasePayment,
    BaseAddTax,
    BaseVAT,
    BaseActive,
    BaseCode,
    BaseInfo,
    BaseSiteRec,
    BaseWF,
    BaseProject,
    LowLevelCodes10,
    BaseRef,
    models.Model):
    """
        Hizmet kartları
    """
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Alınan hizmet kartları'),
            (2, 'Verilen hizmet kartları')
        ],
        help_text='Kart tipi'
    )
    code = models.CharField(
        db_column='CODE',
        max_length=17,
        blank=True,
        null=True,
        help_text='Hizmet kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=51,
        blank=True,
        null=True,
        help_text='Hizmet açıklaması'
    )
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ekstra dosya ref.'
    )
    unitsetref = models.ForeignKey(
        "LG_UNITSETF",
        db_column='UNITSETREF',
        blank=True,
        null=True,
        help_text='Birim seti kaydı ref. -> UNITSETF',
        on_delete=models.DO_NOTHING
    )
    returnvat = models.FloatField(
        db_column='RETURNVAT',
        blank=True,
        null=True
    )
    importexpns = models.SmallIntegerField(
        db_column='IMPORTEXPNS',
        blank=True,
        null=True
    )
    affectcost = models.SmallIntegerField(
        db_column='AFFECTCOST',
        blank=True,
        null=True
    )
    disttype = models.SmallIntegerField(
        db_column='DISTTYPE',
        blank=True,
        null=True
    )
    extaccessflags = models.IntegerField(
        db_column='EXTACCESSFLAGS',
        blank=True,
        null=True
    )
    usedinperiods = models.SmallIntegerField(
        db_column='USEDINPERIODS',
        blank=True,
        null=True
    )
    candeduct = models.SmallIntegerField(
        db_column='CANDEDUCT',
        blank=True,
        null=True
    )
    deductionpart1 = models.SmallIntegerField(
        db_column='DEDUCTIONPART1',
        blank=True,
        null=True
    )
    deductionpart2 = models.SmallIntegerField(
        db_column='DEDUCTIONPART2',
        blank=True,
        null=True
    )
    exemptfromtaxdecl = models.SmallIntegerField(
        db_column='EXEMPTFROMTAXDECL',
        blank=True,
        null=True
    )
    currdiff = models.SmallIntegerField(
        db_column='CURRDIFF',
        blank=True,
        null=True
    )
    deductcode = models.CharField(
        db_column='DEDUCTCODE',
        max_length=11,
        blank=True,
        null=True
    )
    definition2 = models.CharField(
        db_column='DEFINITION2',
        max_length=201,
        blank=True,
        null=True
    )
    parentsrvref = models.IntegerField(
        db_column='PARENTSRVREF',
        blank=True,
        null=True
    )
    specode2 = models.CharField(
        db_column='SPECODE2',
        max_length=11,
        blank=True,
        null=True
    )
    specode3 = models.CharField(
        db_column='SPECODE3',
        max_length=11,
        blank=True,
        null=True
    )
    specode4 = models.CharField(
        db_column='SPECODE4',
        max_length=11,
        blank=True,
        null=True
    )
    specode5 = models.CharField(
        db_column='SPECODE5',
        max_length=11,
        blank=True,
        null=True
    )
    multiaddtax = models.SmallIntegerField(
        db_column='MULTIADDTAX',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_SRVCARD'
        unique_together = (
            ('cardtype', 'code'),
            ('cardtype', 'active', 'code'),
            (
                'lowlevelcodes1',
                'lowlevelcodes2',
                'lowlevelcodes3',
                'lowlevelcodes4',
                'lowlevelcodes5',
                'lowlevelcodes6',
                'lowlevelcodes7',
                'logicalref'
            ),
        )
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.definition_field}"