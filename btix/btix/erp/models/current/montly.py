"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_CLTOTFIL(
    BaseLogical,
    BaseMontly,
    models.Model):
    """
        Cari hesap aylık toplamları
        CLTOTFIL tablosunda cari hesap kartlarına ait toplamlar
        aylık kayıtlar halinde tutulmaktadır. Her hesap kartı
        için 14 adet toplam kayıt bulunmaktadır.
        Cari hesap toplam kayıtlarında, toplamlar tüm ayı
        kapsayan kayıtlardır. Bir ayın belli bir bölümüne
        ait toplamları elde etmek için cari hesap hareketleri
        taranmalıdır.
    """
    cardref = models.ForeignKey(
        "LG_CLCARD",
        db_column='CARDREF',
        blank=True,
        null=True,
        help_text='Kart ref. -> CLCARD',
        on_delete=models.DO_NOTHING
    )
    tottyp = models.SmallIntegerField(
        db_column='TOTTYP',
        blank=True,
        null=True,
        help_text='Cari hesap toplam türü (AR/AP)'
    )
    month_field = models.SmallIntegerField(db_column='MONTH_', blank=True,
        null=True, help_text='Ay')
    year_field = models.SmallIntegerField(db_column='YEAR_', blank=True,
        null=True, help_text='Yıl')
    branch = models.SmallIntegerField(db_column='BRANCH', blank=True,
        null=True, help_text='İşyeri')
    department = models.SmallIntegerField(db_column='DEPARTMENT', blank=True,
        null=True, help_text='Bölüm')

    class Meta:
        managed = False
        unique_together = (
            (
                'cardref', 'tottyp', 'month_field', 'year_field',
                'branch', 'department'
            ),
        )
        db_table = f'LG_{Active.namespace}_{Active.period}_CLTOTFIL'
        target_db = 'erp'

    # rels -> L_CLCARD