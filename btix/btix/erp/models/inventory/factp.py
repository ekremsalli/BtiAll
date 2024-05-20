"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_ITMFACTP(
    BaseLogical,
    BaseItem,
    models.Model):
    """
        Malzeme-fabrika bilgileri
    """
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika no'
    )
    specialized = models.SmallIntegerField(
        db_column='SPECIALIZED',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ]
    )
    procureclass = models.SmallIntegerField(
        db_column='PROCURECLASS',
        blank=True,
        null=True,
        choices=[
            (0, 'Satınalma'),
            (1, 'Üretim')
        ],
        help_text='Temin şekli'
    )
    lowlevelcode = models.IntegerField(
        db_column='LOWLEVELCODE',
        blank=True,
        null=True,
        help_text='Düşük seviye kodu'
    )
    divlotsize = models.SmallIntegerField(
        db_column='DIVLOTSIZE',
        blank=True,
        null=True,
        help_text='Üretimden girişlerde lot büyüklüğü (Üretim miktarı)'
    )
    mrpcntrl = models.SmallIntegerField(
        db_column='MRPCNTRL',
        blank=True,
        null=True,
        help_text='Kullanımda değil'
    )
    planpolicy = models.SmallIntegerField(
        db_column='PLANPOLICY',
        blank=True,
        null=True,
        help_text='Planlama yöntemi'
    )
    lotsizingmtd = models.SmallIntegerField(
        db_column='LOTSIZINGMTD',
        blank=True,
        null=True,
        help_text='Lot belirleme yöntemi'
    )
    fixedlotsize = models.FloatField(
        db_column='FIXEDLOTSIZE',
        blank=True,
        null=True,
        help_text='Sabit lot büyüklüğü'
    )
    yield_field = models.FloatField(
        db_column='YIELD',
        blank=True,
        null=True,
        help_text='Verim'
    )
    minorderqty = models.FloatField(
        db_column='MINORDERQTY',
        blank=True,
        null=True,
        help_text='Minimum sipariş miktarı'
    )
    maxorderqty = models.FloatField(
        db_column='MAXORDERQTY',
        blank=True,
        null=True,
        help_text='Maksimum sipariş miktarı'
    )
    multorderqty = models.FloatField(
        db_column='MULTORDERQTY',
        blank=True,
        null=True,
        help_text='Sipariş miktarı çarpanı'
    )
    minorderday = models.FloatField(
        db_column='MINORDERDAY',
        blank=True,
        null=True,
        help_text='Minimum sipariş günü'
    )
    maxorderday = models.FloatField(
        db_column='MAXORDERDAY',
        blank=True,
        null=True,
        help_text='Maksimum sipariş günü'
    )
    reorderpoint = models.FloatField(
        db_column='REORDERPOINT',
        blank=True,
        null=True,
        help_text='Yeniden sipariş noktası'
    )
    automtrissue = models.SmallIntegerField(
        db_column='AUTOMTRISSUE',
        blank=True,
        null=True,
        help_text='Otomatik malzeme çekişi'
    )
    plannerref = models.CharField(
        db_column='PLANNERREF',
        max_length=25,
        blank=True,
        null=True,
        help_text='Planlayacı ref.'
    )
    buyerref = models.CharField(
        db_column='BUYERREF',
        max_length=25,
        blank=True,
        null=True,
        help_text='Alıcı (müşteri) ref.'
    )
    seladminref = models.CharField(
        db_column='SELADMINREF',
        max_length=25,
        blank=True,
        null=True,
        help_text='Satış yöneticisi ref.'
    )
    cstanalystref = models.CharField(
        db_column='CSTANALYSTREF',
        max_length=25,
        blank=True,
        null=True,
        help_text='Maliyetten sorumlu personel ref.'
    )
    defserilotno = models.CharField(
        db_column='DEFSERILOTNO',
        max_length=101,
        blank=True,
        null=True,
        help_text='Lot seri no ilk değeri'
    )
    autolotoutmtd = models.SmallIntegerField(
        db_column='AUTOLOTOUTMTD',
        blank=True,
        null=True,
        choices=[
            (0, 'FIFO'),
            (1, 'LIFO')
        ],
        help_text='Sar ve firelerle lot/seri belirleme yöntemi'
    )
    lotparty = models.SmallIntegerField(
        db_column='LOTPARTY',
        blank=True,
        null=True,
        help_text='Üretimden girişlerde parti büyüklüğü'
    )
    outlotsize = models.FloatField(
        db_column='OUTLOTSIZE',
        blank=True,
        null=True,
        help_text='Çıkış lot büyüklüğü'
    )
    countformps = models.SmallIntegerField(
        db_column='COUNTFORMPS', blank=True, null=True)
    lotsizingmtd2 = models.SmallIntegerField(
        db_column='LOTSIZINGMTD2', blank=True, null=True)
    fixedlotsize2 = models.FloatField(
        db_column='FIXEDLOTSIZE2', blank=True, null=True)
    yield2 = models.FloatField(
        db_column='YIELD2', blank=True, null=True)
    minorderqty2 = models.FloatField(
        db_column='MINORDERQTY2', blank=True, null=True)
    maxorderqty2 = models.FloatField(
        db_column='MAXORDERQTY2', blank=True, null=True)
    multorderqty2 = models.FloatField(
        db_column='MULTORDERQTY2', blank=True, null=True)
    checkallinvens = models.SmallIntegerField(
        db_column='CHECKALLINVENS', blank=True, null=True)
    productionfact = models.SmallIntegerField(
        db_column='PRODUCTIONFACT', blank=True, null=True)
    procureinven = models.SmallIntegerField(
        db_column='PROCUREINVEN', blank=True, null=True)
    variantref = models.IntegerField(
        db_column='VARIANTREF', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ITMFACTP'
        unique_together = (('itemref', 'variantref', 'factorynr'),)
        target_db = 'erp'
