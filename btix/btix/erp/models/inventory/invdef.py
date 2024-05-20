"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_INVDEF(
    BaseLogical,
    BaseItem,
    models.Model):
    """
        Malzeme ambar bilgileri
    """
    invenno = models.SmallIntegerField(
        db_column='INVENNO',
        blank=True,
        null=True,
        help_text='Ambar no'
    )
    minlevel = models.FloatField(
        db_column='MINLEVEL',
        blank=True,
        null=True,
        help_text='Minimum stok seviyesi'
    )
    maxlevel = models.FloatField(
        db_column='MAXLEVEL',
        blank=True,
        null=True,
        help_text='Maksimum stok seviyesi'
    )
    safelevel = models.FloatField(
        db_column='SAFELEVEL',
        blank=True,
        null=True,
        help_text='Güvenli stok seviyesi'
    )
    locationref = models.ForeignKey(
        "LG_LOCATION",
        db_column='LOCATIONREF',
        blank=True,
        null=True,
        help_text='Stok yeri öndeğeri ref. -> LOCATION',
        on_delete=models.DO_NOTHING
    )
    perclosedate = models.DateTimeField(
        db_column='PERCLOSEDATE',
        blank=True,
        null=True,
        help_text='Dönem kapama tarihi'
    )
    abccode = models.SmallIntegerField(
        db_column='ABCCODE',
        blank=True,
        null=True,
        help_text='ABC kodu'
    )
    minlevelctrl = models.SmallIntegerField(
        db_column='MINLEVELCTRL',
        blank=True,
        null=True,
        choices=[
            (0, 'Yapılmayacak'),
            (1, 'Kullanıcı uyarılayacak'),
            (2, 'İşlem durdurulacak')
        ],
        help_text='Minimum stok seviyesi kontrolu'
    )
    maxlevelctrl = models.SmallIntegerField(
        db_column='MAXLEVELCTRL',
        blank=True,
        null=True,
        choices=[
            (0, 'Yapılmayacak'),
            (1, 'Kullanıcı uyarılayacak'),
            (2, 'İşlem durdurulacak')
        ],
        help_text='Maksimum stok seviyesi kontrolu'
    )
    safelevelctrl = models.SmallIntegerField(
        db_column='SAFELEVELCTRL',
        blank=True,
        null=True,
        choices=[
            (0, 'Yapılmayacak'),
            (1, 'Kullanıcı uyarılayacak'),
            (2, 'İşlem durdurulacak')
        ],
        help_text='Güvenli stok seviyesi'
    )
    neglevelctrl = models.SmallIntegerField(
        db_column='NEGLEVELCTRL',
        blank=True,
        null=True,
        choices=[
            (0, 'Yapılmayacak'),
            (1, 'Kullanıcı uyarılayacak'),
            (2, 'İşlem durdurulacak')
        ],
        help_text='Negatif stok seviyesi kontrolu'
    )
    ioctrl = models.SmallIntegerField(
        db_column='IOCTRL', blank=True, null=True)
    variantref = models.IntegerField(
        db_column='VARIANTREF', blank=True, null=True)
    outctrl = models.SmallIntegerField(
        db_column='OUTCTRL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_INVDEF'
        unique_together = (('itemref', 'variantref', 'invenno'),)
        target_db = 'erp'
