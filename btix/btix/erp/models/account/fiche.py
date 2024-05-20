"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_EMFICHE(
    BaseLogical,
    BaseCode,
    BaseGenexp,
    BaseCancelled,
    BasePrint,
    BaseInfo,
    BaseSiteRec,
    BaseTextINC,
    BaseWF,
    BaseGUID,
    BaseProject,
    models.Model):
    """
        Muhasebe fişleri
        EMFICHE tablosunda Muhasebe fişlerinin başlık bilgileri tutulmaktadır.
        Muhasebe fiş satırları için ise EMFLINE tablosu okunmalıdır.
    """
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Açılış'),
            (2, 'Tahsil'),
            (3, 'Tediye'),
            (4, 'Mahsup'),
            (5, 'Özel'),
            (6, 'Kur farkı hesabı')
        ],
        help_text='Fiş türü'
    )
    ficheno = models.CharField(
        db_column='FICHENO',
        max_length=33,
        blank=True,
        null=True,
        help_text='Fiş numarası'
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    docode = models.CharField(
        db_column='DOCODE',
        max_length=33,
        blank=True,
        null=True,
        help_text='Belge numarası'
    )
    branch = models.SmallIntegerField(
        db_column='BRANCH',
        blank=True,
        null=True,
        help_text='İş yeri'
    )
    department = models.SmallIntegerField(
        db_column='DEPARTMENT',
        blank=True,
        null=True,
        help_text='Bölüm'
    )
    moduleno = models.SmallIntegerField(
        db_column='MODULENO',
        blank=True,
        null=True,
        help_text='Modül numarası (entegrasyon yapılan modüller)'
    )
    sourcefref = models.IntegerField(
        db_column='SOURCEFREF',
        blank=True,
        null=True,
        help_text='İlgili modüldeki ilgili fişin ref.'
    )
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ekstra dosya ref.'
    )
    journalno = models.IntegerField(
        db_column='JOURNALNO',
        blank=True,
        null=True,
        help_text='Yevmiye no'
    )
    totalactive = models.FloatField(
        db_column='TOTALACTIVE',
        blank=True,
        null=True,
        help_text='Toplam aktif'
    )
    totalpassive = models.FloatField(
        db_column='TOTALPASSIVE',
        blank=True,
        null=True,
        help_text='Toplam pasif'
    )
    modulenr = models.SmallIntegerField(
        db_column='MODULENR',
        blank=True,
        null=True,
        help_text='Modül numarası'
    )
    cancfref = models.IntegerField(
        db_column='CANCFREF',
        blank=True,
        null=True,
        help_text='İptal edilen fiş numarası'
    )
    emutotactive = models.FloatField(
        db_column='EMUTOTACTIVE',
        blank=True,
        null=True,
        help_text='Toplam aktif (EURO)'
    )
    emutotpassive = models.FloatField(
        db_column='EMUTOTPASSIVE',
        blank=True,
        null=True,
        help_text='Toplam pasif (EURO)'
    )
    genexctyp = models.SmallIntegerField(
        db_column='GENEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (genel)'
    )
    lineexctyp = models.SmallIntegerField(
        db_column='LINEEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (satır)'
    )
    orglogicalref = models.IntegerField(
        db_column='ORGLOGICALREF',
        blank=True,
        null=True,
        help_text='Orjinal kayıt ref.'
    )
    reptotactive = models.FloatField(
        db_column='REPTOTACTIVE',
        blank=True,
        null=True,
        help_text='Toplam aktif (raporlama dövizi)'
    )
    reptotpassive = models.FloatField(
        db_column='REPTOTPASSIVE',
        blank=True,
        null=True,
        help_text='Toplam pasif (raporlama dövizi)'
    )
    crossfref = models.IntegerField(
        db_column='CROSSFREF', blank=True, null=True)
    crossflag = models.SmallIntegerField(
        db_column='CROSSFLAG', blank=True, null=True)
    doctype = models.SmallIntegerField(
        db_column='DOCTYPE', blank=True, null=True)
    orglogoid = models.CharField(
        db_column='ORGLOGOID', max_length=25, blank=True, null=True)
    status = models.SmallIntegerField(
        db_column='STATUS', blank=True, null=True)
    bdgtfctype = models.SmallIntegerField(
        db_column='BDGTFCTYPE', blank=True, null=True)
    bdgtfcref = models.IntegerField(
        db_column='BDGTFCREF', blank=True, null=True)
    fromdemtype = models.SmallIntegerField(
        db_column='FROMDEMTYPE', blank=True, null=True)
    emdemfcref = models.IntegerField(
        db_column='EMDEMFCREF', blank=True, null=True)
    wflowcrdref = models.IntegerField(
        db_column='WFLOWCRDREF', blank=True, null=True)
    viaautogl = models.SmallIntegerField(
        db_column='VIAAUTOGL', blank=True, null=True)
    approve = models.SmallIntegerField(
        db_column='APPROVE', blank=True, null=True)
    approvedate = models.DateTimeField(
        db_column='APPROVEDATE', blank=True, null=True)
    docdate = models.DateTimeField(
        db_column='DOCDATE', blank=True, null=True)
    batchtype = models.SmallIntegerField(
        db_column='BATCHTYPE', blank=True, null=True)
    linebaseddocdet = models.SmallIntegerField(
        db_column='LINEBASEDDOCDET', blank=True, null=True)
    isimpdistfc = models.SmallIntegerField(
        db_column='ISIMPDISTFC', blank=True, null=True)
    printdate = models.DateTimeField(
        db_column='PRINTDATE', blank=True, null=True)
    persenddate = models.DateTimeField(
        db_column='PERSENDDATE', blank=True, null=True)
    persbegdate = models.DateTimeField(
        db_column='PERSBEGDATE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_EMFICHE'
        unique_together = (
            ('trcode', 'ficheno'),
            ('date_field', 'trcode', 'ficheno'),
            ('date_field', 'logicalref'),
        )
        target_db = 'erp'
