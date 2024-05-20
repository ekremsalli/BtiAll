"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_SUPPASGN(
    BaseLogical,
    BaseItem,
    BasePriority,
    BaseClient,
    BaseTrading,
    models.Model):
    """
        Malzeme - Tedarikçi ataması
    """
    supplytype = models.SmallIntegerField(
        db_column='SUPPLYTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Müşteri'),
            (2, 'Tedarikçi')
        ],
        help_text='Türü'
    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    clcardtype = models.SmallIntegerField(
        db_column='CLCARDTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Alıcı'),
            (1, 'Satıcı'),
            (2, 'Alıcı+Satıcı')
        ],
        help_text='Cari hesap türü'
    )
    kkkcheck = models.SmallIntegerField(
        db_column='KKKCHECK',
        blank=True,
        null=True,
        choices=[
            (0, 'İşleme devam edilecek'),
            (1, 'Kullanıcı uyarılacak'),
            (2, 'İşlem durdurulacak')
        ],
        help_text='K.K işlemi yapıldığında'
    )
    leadtime = models.FloatField(
        db_column='LEADTIME',
        blank=True,
        null=True,
        help_text='Teslim/Temin süresi'
    )
    maxquantity = models.FloatField(
        db_column='MAXQUANTITY',
        blank=True,
        null=True,
        help_text='Azami stok seviyesi'
    )
    minquantity = models.FloatField(
        db_column='MINQUANTITY',
        blank=True,
        null=True,
        help_text='Asgari stok seviyesi'
    )
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True,
        help_text='Başlangıç tarihi'
    )
    specialized = models.SmallIntegerField(
        db_column='SPECIALIZED',
        blank=True,
        null=True
    )
    icustsupcode = models.CharField(
        db_column='ICUSTSUPCODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Müşteri/Tedarik kodu'
    )
    icustsupname = models.CharField(
        db_column='ICUSTSUPNAME',
        max_length=51,
        blank=True,
        null=True
    )
    qtydepleadtime = models.FloatField(
        db_column='QTYDEPLEADTIME',
        blank=True,
        null=True
    )
    packetref = models.IntegerField(
        db_column='PACKETREF',
        blank=True,
        null=True
    )
    packagingamnt = models.FloatField(
        db_column='PACKAGINGAMNT',
        blank=True,
        null=True
    )
    packaginguomref = models.IntegerField(
        db_column='PACKAGINGUOMREF',
        blank=True,
        null=True
    )
    packetusetype = models.SmallIntegerField(
        db_column='PACKETUSETYPE',
        blank=True,
        null=True
    )
    ordperc = models.FloatField(
        db_column='ORDPERC',
        blank=True,
        null=True
    )
    ordfreq = models.SmallIntegerField(
        db_column='ORDFREQ',
        blank=True,
        null=True
    )
    variantref = models.IntegerField(
        db_column='VARIANTREF',
        blank=True,
        null=True
    )
    icustsupbarcode = models.CharField(
        db_column='ICUSTSUPBARCODE',
        max_length=25,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_SUPPASGN'
        target_db = 'erp'

