"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_BNTOTFIL(
    BaseLogical,
    BaseMontly,
    models.Model):
    """
        Banka aylık toplamları
        BNTOTFIL tablosunda banka kartlarına ait (BNCARD) ait hesapların
        (BANKACC) aylık bakiye bilgileri tutulmaktadır. Her hesap kartı için
        14 adet toplam kayıt bulunmaktadır. Bu kayıtlardan ilki devir ile
        aktarılan toplamlar için, diğer 13 kayıt ise dönem içerisindeki
        aylara ait toplam bilgileri içindir.
        6 eylül 1999 ve 6 eylül 2000 gibi bir mali yıl içerisinde
        2 adet "eylül" ayı olacağı için 13 adet ay kaydı bulunmaktadır.
        İşlem görmeyen aylar için veri tabanında kayıt bulunmamaktadır.
    """
    cardref = models.ForeignKey(
        "LG_BNCARD",
        db_column='CARDREF',
        blank=True,
        null=True,
        help_text='Kart ref. -> BNCARD',
        on_delete=models.DO_NOTHING
    )
    tottyp = models.SmallIntegerField(
        db_column='TOTTYP',
        blank=True,
        null=True,
        help_text='Toplam türü'
    )
    month_field = models.SmallIntegerField(db_column='MONTH_', blank=True,
        null=True, help_text='Ay')
    branch = models.SmallIntegerField(db_column='BRANCH', blank=True,
        null=True, help_text='İşyeri')
    department = models.SmallIntegerField(db_column='DEPARTMENT', blank=True,
        null=True, help_text='Bölüm')
    year_field = models.SmallIntegerField(db_column='YEAR_', blank=True,
        null=True, help_text='Yıl')

    class Meta:
        managed = False
        unique_together = (('cardref', 'tottyp', 'month_field', 'year_field'),)
        db_table = f'LG_{Active.namespace}_{Active.period}_BNTOTFIL'
        target_db = 'erp'