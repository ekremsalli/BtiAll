"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_ITMBOMAS(
    BaseLogical,
    BaseItem,
    BasePriority,
    BaseSiteRec,
    BaseRef,
    models.Model):
    """
        Malzeme- Ürün Recetesi ataması
    """
    bomref = models.ForeignKey(
        "LG_BOMASTER",
        db_column='BOMREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi -> BOMASTER',
        on_delete=models.DO_NOTHING
    )
    reltype = models.SmallIntegerField(
        db_column='RELTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Genel'),
            (1, 'Mühendislik'),
            (2, 'Üretim'),
            (3, 'Maliyetlendirme')
        ],
        help_text='Malzeme-ürün reçetesi ilişkisi'
    )
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika no'
    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    maxquantity = models.FloatField(
        db_column='MAXQUANTITY',
        blank=True,
        null=True,
        help_text='Maksimum miktar'
    )
    minquantity = models.FloatField(
        db_column='MINQUANTITY',
        blank=True,
        null=True,
        help_text='Minimum miktar'
    )
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True,
        help_text='Başlangıç tarihi'
    )
    stdcostflag = models.SmallIntegerField(
        db_column='STDCOSTFLAG', blank=True, null=True)
    formrp = models.SmallIntegerField(
        db_column='FORMRP', blank=True, null=True)
    enddate = models.DateTimeField(
        db_column='ENDDATE',
        blank=True,
        null=True
    )
    revref = models.IntegerField(
        db_column='REVREF',
        blank=True,
        null=True
    )
    bomtype = models.SmallIntegerField(
        db_column='BOMTYPE',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ITMBOMAS'
        target_db = 'erp'
