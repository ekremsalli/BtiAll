"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_ASCOND(
    BaseLogical,
    BaseCard,
    BasePriority,
    BaseSiteRec,
    BaseActive,
    BaseRef,
    models.Model):
    """
        Satın alma / Satış koşulları
    """
    usetype = models.SmallIntegerField(
        db_column='USETYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Satınalma/Satış,'),
            (2, 'Satınalma için (fiş satırı)'),
            (3, 'Satınalma için (fiş genel)'),
            (4, 'Satış için (fiş satırı)'),
            (5, 'Satış için (fiş genel)')
        ],
        help_text='''
            1-> Satınalma/Satış,
            2-> Satınalma için (fiş satırı)
            3-> Satınalma için (fiş genel)
            4-> Satış için (fiş satırı)
            5-> Satış için (fiş genel)
        ''')
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    linetype = models.SmallIntegerField(
        db_column='LINETYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'İndirim'),
            (2, 'Masraf'),
            (3, 'Promosyon')
        ],
        help_text='Satır tipi; 1-> İndirim, 2-> Masraf, 3-> Promosyon'
    )
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True,
        help_text='Başlangıç tarihi'
    )
    enddate = models.DateTimeField(
        db_column='ENDDATE',
        blank=True,
        null=True,
        help_text='Bitiş tarihi'
    )
    stcodes = models.CharField(
        db_column='STCODES',
        max_length=101,
        blank=True,
        null=True,
        help_text='Malzeme kodu'
    )
    cicodes = models.CharField(
        db_column='CICODES',
        max_length=101,
        blank=True,
        null=True,
        help_text='Cari hesap kodu'
    )
    paycodes = models.CharField(
        db_column='PAYCODES',
        max_length=101,
        blank=True,
        null=True,
        help_text='Ödeme kodu'
    )
    itemtype = models.SmallIntegerField(
        db_column='ITEMTYPE',
        blank=True,
        null=True,
        help_text='Malzeme kartı türü'
    )
    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ASCOND'
        target_db = 'erp'