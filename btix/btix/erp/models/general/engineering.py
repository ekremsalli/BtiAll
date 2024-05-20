"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_ENGCLINE(
    BaseLogical,
    BaseClient,
    BaseItem,
    BaseSiteRec,
    BaseInfo,
    BaseApproved,
    BaseActive,
    BaseCode,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Mühendislik değişiklik işlemi
    """
    ficheno = models.CharField(
        db_column='FICHENO',
        unique=True,
        max_length=17,
        blank=True,
        null=True,
        help_text='Fiş no'
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    appstatus = models.SmallIntegerField(
        db_column='APPSTATUS',
        blank=True,
        null=True,
        help_text='Durumu'
    )
    reason = models.CharField(
        db_column='REASON',
        max_length=51,
        blank=True,
        null=True,
        help_text='Nedeni'
    )
    bommasterref = models.ForeignKey(
        "LG_BOMASTER",
        db_column='BOMMASTERREF',
        blank=True,
        null=True,
        help_text='Üretim reçetesi ref. -> BOMASTER',
        on_delete=models.DO_NOTHING
    )
    oldrevref = models.ForeignKey(
        "LG_BOMREVSN",
        db_column='OLDREVREF',
        blank=True,
        null=True,
        help_text='Eski revizyon ref. -> BOMREVSN',
        related_name="%(app_label)s_%(class)s_oldrevref",
        on_delete=models.DO_NOTHING
    )
    newrevref = models.ForeignKey(
        "LG_BOMREVSN",
        db_column='NEWREVREF',
        blank=True,
        null=True,
        help_text='Yeni revizyon ref. -> BOMREVSN',
        related_name="%(app_label)s_%(class)s_newrevref",
        on_delete=models.DO_NOTHING
    )
    method = models.SmallIntegerField(
        db_column='METHOD',
        blank=True,
        null=True,
        help_text="""
            Yöntem;
            Tarih
            Tükenme
            Lot/Parti Seri No
        """
    )
    datefrom = models.DateTimeField(
        db_column='DATEFROM',
        blank=True,
        null=True,
        help_text='Geçerlilik tarihi'
    )
    serilotfrom = models.CharField(
        db_column='SERILOTFROM',
        max_length=101,
        blank=True,
        null=True,
        help_text='Lot parti / seri no'
    )
    bomlineref = models.ForeignKey(
        "LG_BOMLINE",
        db_column='BOMLINEREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi satırı ref. -> BOMLINE',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_bomlineref"
    )
    validdate = models.DateTimeField(
        db_column='VALIDDATE',
        blank=True,
        null=True,
        help_text='Geçerlilik tarihi'
    )
    validstatus = models.SmallIntegerField(
        db_column='VALIDSTATUS',
        blank=True,
        null=True,
        help_text='Geçerlilik durumu'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ENGCLINE'
        unique_together = (
            ('date_field', 'ficheno'),
            ('validdate', 'ficheno', 'date_field'),
        )
        target_db = 'erp'