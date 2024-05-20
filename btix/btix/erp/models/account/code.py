"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_ACCCODES(
    BaseLogical,
    BaseModule,
    BaseAccount,
    BaseCenter,
    BaseInfo,
    BaseBranchNr,
    BaseSiteRec,
    BaseProject,
    BaseRef,
    BasePriority,
    models.Model):
    """
        Entegrasyon bağlantı kodları
    """
    grpfilter = models.BinaryField(
        db_column='GRPFILTER',
        blank=True,
        null=True,
        help_text='Grup filtre kaydı'
    )
    vatrate = models.FloatField(
        db_column='VATRATE',
        blank=True,
        null=True,
        help_text='KDV oranı'
    )
    lineexp = models.CharField(
        db_column='LINEEXP',
        max_length=31,
        blank=True,
        null=True,
        help_text='Satır açıklaması'
    )
    calcformula = models.CharField(
        db_column='CALCFORMULA',
        max_length=251,
        blank=True,
        null=True,
        help_text='Hesap formülü'
    )
    indexcode = models.CharField(
        db_column='INDEXCODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='İndeks kodu'
    )
    prevalue = models.SmallIntegerField(
        db_column='PREVALUE',
        blank=True,
        null=True,
        help_text='Öntanımlı değer'
    )
    prdiff = models.SmallIntegerField(
        db_column='PRDIFF',
        blank=True,
        null=True,
        help_text='Fiyatlar'
    )
    effectivecost = models.SmallIntegerField(
        db_column='EFFECTIVECOST',
        blank=True,
        null=True
    )
    specode = models.CharField(
        db_column='SPECODE',
        max_length=25,
        blank=True,
        null=True
    )
    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ACCCODES'
        target_db = 'erp'

class LG_CRDACREF(
    BaseLogical,
    BaseAccount,
    BaseCenter,
    BaseProject,
    BaseSiteRec,
    BaseRef,
    models.Model):
    """
        Kart-muhasebe kodları
    """
    cardref = models.IntegerField(
        db_column='CARDREF',
        blank=True,
        null=True,
        help_text='Kart referansı',
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Stok kartı'),
            (3, 'Hizmet kartı'),
            (4, 'Hizmet satış'),
            (5, 'Cari hesap'),
            (8, 'Kasa işlemi'),
            (9, 'Alış promosyon'),
            (10, 'Satış promosyon'),
            (11, 'Alış indirim'),
            (12, 'Alış masraf'),
            (13, 'Satış indirim'),
            (14, 'Satış masraf')
        ],
        help_text="""
            İşlem türü;
            1 -> Stok kartı
            3 -> Hizmet kartı
            4 -> Hizmet satış
            5 -> Cari hesap
            8 -> Kasa işlemi
            9 -> Alış promosyon
            10 -> Satış promosyon
            11 -> Alış indirim
            12 -> Alış masraf
            13 -> Satış indirim
            14 -> Satış masraf
        """
    )
    typ = models.SmallIntegerField(db_column='TYP', blank=True,
        null=True,
        help_text="""
            İşlem tipi;
            1 -> (trCode=1 için) Alım
            2 -> (trCode=1 için) Diğer giriş
            3 -> (trCode=1 için) Satış
            4 -> (trCode=1 için) Diğer çıkış
            5 -> (trCode=1 için) Sarf
            6 -> (trCode=1 için) Fire
            7 -> (trCode=1 için) Diğer giriş
            8 -> (trCode=1 için) Kullanıcı tanımlı giriş
            9 -> (trCode=1 için) Kullanıcı tanımlı çıkış
            10 -> (trCode=1 için) Alım iade
            11 -> (trCode=1 için) Satış iade
            12 -> (trCode=1 için) Alım indirim
            13 -> (trCode=1 için) Satış indirim
            14 -> (trCode=1 için) Alım masraf
            15 -> (trCode=1 için) Satış masraf
            16 -> (trCode=1 için) Alınan promosyon
            17 -> (trCode=1 için) Verilen promosyon
            18 -> (trCode=1 için) Prom KDV
            19 -> (trCode=1 için) Satışta kar/zarar
            20 -> (trCode=1 için) Amortisman tükenme payları
            21 -> (trCode=1 için) Yeniden değerlendirmeler
            22 -> (trCode=1 için) Sonraki yıl indirilecek
            23 -> (trCode=1 için) Birikmiş amortismanlar
            24 -> (trCode=1 için) Sabit kıymet giderleri

            1 -> (trCode=3 için) Hizmetler
            2 -> (trCode=3 için) Hizmet indirimleri
            3 -> (trCode=3 için) Hizmet masrafları
            4 -> (trCode=3 için) Hizmet promosyonlar
            5 -> (trCode=3 için) Hizmet iadeleri
        """
    )

    class Meta:
        managed = False
        unique_together = (('trcode', 'cardref', 'typ'),)
        db_table = f'LG_{Active.namespace}_CRDACREF'
        target_db = 'erp'
