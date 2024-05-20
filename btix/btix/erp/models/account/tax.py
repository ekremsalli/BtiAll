"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_ADDTAX(
    BaseLogical,
    BaseInfo,
    BaseSiteRec,
    BaseRef,
    models.Model):
    """
        Ek vergi
    """
    taxgroupid = models.CharField(
        db_column='TAXGROUPID',
        max_length=31,
        blank=True,
        null=True,
        help_text='Ek vergi grubu ID'
    )
    taxcode = models.CharField(
        db_column='TAXCODE',
        unique=True,
        max_length=31,
        blank=True,
        null=True,
        help_text='Ek vergi kodu'
    )
    taxdef = models.CharField(
        db_column='TAXDEF',
        max_length=61,
        blank=True,
        null=True,
        help_text='Ek vergi açıklaması'
    )
    addtocost = models.SmallIntegerField(
        db_column='ADDTOCOST',
        blank=True,
        null=True,
        help_text='Ek vergi maliyeti'
    )
    effectkdv = models.SmallIntegerField(
        db_column='EFFECTKDV',
        blank=True,
        null=True
    )
    inlinenet = models.SmallIntegerField(
        db_column='INLINENET',
        blank=True,
        null=True
    )
    globalcode = models.CharField(
        db_column='GLOBALCODE',
        max_length=11,
        blank=True, null=True
    )
    canteffectcost = models.SmallIntegerField(
        db_column='CANTEFFECTCOST',
        blank=True,
        null=True
    )
    multipleaddtax = models.SmallIntegerField(
        db_column='MULTIPLEADDTAX',
        blank=True,
        null=True
    )
    multipleorderno = models.SmallIntegerField(
        db_column='MULTIPLEORDERNO',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ADDTAX'
        target_db = 'erp'

class LG_ADDTAXLINE(
    BaseAddTax,
    BaseLogical,
    BaseAmount,
    BaseSiteRec,
    BaseRef,
    models.Model):
    """
        Ek vergi detayları
    """
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True,
        help_text='Başlangıç tarihi'
    )
    taxtype = models.SmallIntegerField(
        db_column='TAXTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Oran'),
            (1, 'Tutar')
        ],
        help_text='Vergi türü; 0->Oran, 1->Tutar'
    )
    rate = models.FloatField(
        db_column='RATE',
        blank=True,
        null=True,
        help_text='Oran'
    )
    unittype = models.SmallIntegerField(
        db_column='UNITTYPE',
        blank=True,
        null=True,
        help_text='Birim türü'
    )
    unitsetref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UNITSETREF',
        blank=True,
        null=True,
        help_text='Birim seti ref.',
        on_delete=models.DO_NOTHING
    )
    unitref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UNITREF',
        blank=True,
        null=True,
        help_text='Birim ref.',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_unitref"
    )
    discamount = models.FloatField(
        db_column='DISCAMOUNT',
        blank=True,
        null=True,
        help_text='İndirim tutarı'
    )
    exceptrate = models.FloatField(
        db_column='EXCEPTRATE',
        blank=True,
        null=True
    )
    exceptamount = models.FloatField(
        db_column='EXCEPTAMOUNT',
        blank=True,
        null=True
    )
    collectrate = models.FloatField(
        db_column='COLLECTRATE',
        blank=True,
        null=True
    )
    collectamount = models.FloatField(
        db_column='COLLECTAMOUNT',
        blank=True,
        null=True
    )
    fcspecode = models.CharField(
        db_column='FCSPECODE',
        max_length=11,
        blank=True,
        null=True
    )
    trspecode = models.CharField(
        db_column='TRSPECODE',
        max_length=17,
        blank=True,
        null=True
    )
    trspecode2 = models.CharField(
        db_column='TRSPECODE2',
        max_length=41,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ADDTAXLINE'
        target_db = 'erp'