"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_SPECODES(
    BaseLogical,
    BaseSiteRec,
    BaseRef,
    models.Model):
    """
        Özel kodlar
    """
    codetype = models.SmallIntegerField(
        db_column='CODETYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Özel kod'),
            (2, 'Yetki kodu'),
            (3, 'Satış hedefi stok kodu'),
            (4, 'Satıcı pozisyon kodu')
        ],
        help_text='Kod tipi'
    )
    specodetype = models.SmallIntegerField(
        db_column='SPECODETYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Stok kartı'),
            (2, 'Stok fişi'),
            (3, 'Stok fişi satırı'),
            (4, 'Alınan hizmet kartları'),
            (5, 'Verilen hizmet kartları'),
            (6, 'Alış indirim kartları'),
            (7, 'Alış masraf kartları'),
            (8, 'Satış indirim kartları'),
            (9, 'Satış masraf kartları'),
            (10, 'Alış promosyon kartları'),
            (11, 'Satış promosyon kartları'),
            (14, 'Alınan siparişler'),
            (15, 'Verilen siparişler'),
            (16, 'Alınan sipariş fiş satırları'),
            (17, 'Verilen sipariş fiş satırları'),
            (18, 'Alım irsaliyeleri'),
            (19, 'Satış irsaliyeleri'),
            (20, 'Alım irsaliye satırları'),
            (21, 'Satış irsaliye satırları'),
            (22, 'Alım faturaları'),
            (23, 'Satış faturaları'),
            (24, 'Alım faturaları satırları'),
            (25, 'Satış fatura satırları'),
            (26, 'Cari hesap kartları'),
            (27, 'Cari hesap fiş satırları'),
            (28, 'Ödeme tahsilat satırları'),
            (29, 'Çek/senet kartları'),
            (30, 'Çek/senet bordroları'),
            (31, 'Banka kartları'),
            (32, 'Banka hesapları'),
            (33, 'Banka fiş satırları'),
            (34, 'Kasa kartı'),
            (35, 'Muhasebe hesapları'),
            (36, 'Masraf merkezi'),
            (37, 'Muhasebe fişleri'),
            (38, 'Muhasebe fişi satırları'),
            (40, 'Kasa işlemleri'),
            (43, 'Banka fişleri'),
            (44, 'Cari hesap fişleri'),
            (50, 'Satış elemanı'),
            (51, 'Satış rotası')
        ],
        help_text='Özel kod tipi'
    )
    specode = models.CharField(
        db_column='SPECODE',
        max_length=41,
        blank=True,
        null=True,
        help_text='Özel kod'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=41,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    color = models.SmallIntegerField(
        db_column='COLOR',
        blank=True,
        null=True,
        help_text='Renk'
    )
    wincolor = models.IntegerField(
        db_column='WINCOLOR',
        blank=True,
        null=True,
        help_text='Pencere rengi'
    )
    spetyp1 = models.SmallIntegerField(
        db_column='SPETYP1',
        blank=True,
        null=True
    )
    spetyp2 = models.SmallIntegerField(
        db_column='SPETYP2',
        blank=True,
        null=True
    )
    spetyp3 = models.SmallIntegerField(
        db_column='SPETYP3',
        blank=True,
        null=True
    )
    spetyp4 = models.SmallIntegerField(
        db_column='SPETYP4',
        blank=True,
        null=True
    )
    spetyp5 = models.SmallIntegerField(
        db_column='SPETYP5',
        blank=True,
        null=True
    )
    globalid = models.CharField(
        db_column='GLOBALID',
        max_length=51,
        blank=True,
        null=True
    )
    definition2 = models.CharField(
        db_column='DEFINITION2',
        max_length=41,
        blank=True,
        null=True
    )
    definition3 = models.CharField(
        db_column='DEFINITION3',
        max_length=41,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_SPECODES'
        target_db = 'erp'
