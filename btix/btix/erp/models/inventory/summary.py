"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_STINVENS(
    BaseLogical,
    models.Model):
    """
        Ambar toplamları
        Stok hareketleri işlendiği veri tabanına kaydedildiği zaman stok
        hareketinin ilgili ambarındaki toplamı ve tüm ambarların genel toplamını
        gösteren bir kayıt güncellenir. Her ambar için 15 adet toplam kayıt
        bulunabilir. Bu kayıtlardan ilki (-1) tüm ambarların o ayki toplamını
        gösteren kaydı gösterir. Devir yapılmış ise bir kayıt devir için
        oluşturulmakta. Cari hesap toplam kayıtlarında toplamlar tüm ayı
        kapsayan kayıtlardır. Bir ayın belli bir bölümüne ait toplamları
        elde etmek için stok hareketleri taranmalıdır.
    """
    stockref = models.ForeignKey(
        "LG_ITEMS",
        db_column='STOCKREF',
        blank=True,
        null=True,
        help_text='Malzeme kartı ref. -> ITEMS',
        on_delete=models.DO_NOTHING
    )
    invenno = models.SmallIntegerField(
        db_column='INVENNO',
        blank=True,
        null=True,
        help_text='Ambar numarası (-1 = tüm ambarlar)'
    )
    month_field = models.SmallIntegerField(
        db_column='MONTH_',
        blank=True,
        null=True,
        help_text='Ay'
    )
    sales_amount = models.FloatField(
        db_column='SALES_AMOUNT',
        blank=True,
        null=True,
        help_text='Aylık toplam satış tutarları (tüm aylar için)',
    )
    sales_cashamnt = models.FloatField(
        db_column='SALES_CASHAMNT',
        blank=True,
        null=True,
        help_text='Aylık toplam satış tutarları (tüm aylar için)'
    )
    sales_curramnt = models.FloatField(
        db_column='SALES_CURRAMNT',
        blank=True,
        null=True,
        help_text='Aylık toplam satış tutarları (tüm aylar için)'
    )
    sales_vatamnt = models.FloatField(
        db_column='SALES_VATAMNT',
        blank=True,
        null=True
    )
    sales_discamnt = models.FloatField(
        db_column='SALES_DISCAMNT',
        blank=True,
        null=True
    )
    sales_retamnt = models.FloatField(
        db_column='SALES_RETAMNT',
        blank=True,
        null=True
    )
    purchases_amount = models.FloatField(
        db_column='PURCHASES_AMOUNT',
        blank=True,
        null=True,
        help_text='Aylık toplam alım tutarları (tüm aylar için)',

    )
    purchases_cashamnt = models.FloatField(
        db_column='PURCHASES_CASHAMNT',
        blank=True,
        null=True,
        help_text='Aylık toplam alım tutarları (tüm aylar için)'
    )
    purchases_curramnt = models.FloatField(
        db_column='PURCHASES_CURRAMNT',
        blank=True,
        null=True,
        help_text='Aylık toplam alım tutarları (tüm aylar için)'
    )
    purchases_vatamnt = models.FloatField(
        db_column='PURCHASES_VATAMNT',
        blank=True,
        null=True
    )
    purchases_discamnt = models.FloatField(
        db_column='PURCHASES_DISCAMNT',
        blank=True,
        null=True
    )
    purchases_retamnt = models.FloatField(
        db_column='PURCHASES_RETAMNT',
        blank=True,
        null=True
    )
    year_field = models.SmallIntegerField(
        db_column='YEAR_',
        blank=True,
        null=True
    )
    variantref = models.IntegerField(
        db_column='VARIANTREF',
        blank=True,
        null=True
    )
    mtrlinc = models.SmallIntegerField(
        db_column='MTRLINC',
        blank=True,
        null=True
    )
    virtualinven = models.SmallIntegerField(
        db_column='VIRTUALINVEN',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_STINVENS'
        unique_together = (
            ('stockref', 'invenno', 'month_field', 'purchases_amount'),
        )
        target_db = 'erp'
