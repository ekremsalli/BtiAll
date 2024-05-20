"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_CSROLL(
    BaseLogical,
    BaseCode,
    BaseGenexp,
    BaseInfo,
    BaseSiteRec,
    BaseCenter,
    BaseBranch,
    BasePrint,
    BaseTrading,
    BaseWF,
    BaseProject,
    BaseSalesMan,
    BaseAccounted,
    BaseCancelled,
    BaseTextINC,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Çek / senet bordları
        Çek ve senetlerle ilgili tüm hareketler çek/senet bordroları aracılığı
        ile kaydedilmekte ve bu kayıtlar CSROLL tablosunda tutulmaktadır.
    """
    cardref = models.IntegerField(
        db_column='CARDREF',
        blank=True,
        null=True,
        help_text='Banka hesap kartı -> CLCARD veya  -> BNCARD'
    )
    rollno = models.CharField(
        db_column='ROLLNO',
        max_length=9,
        blank=True,
        null=True,
        help_text='Bordro numarası'
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Çek girişi'),
            (2, 'Senet girişi'),
            (3, 'Çek çıkış (cari hesaba)'),
            (4, 'Senet çıkış (cari hesaba)'),
            (5, 'Çek çıkış (banka tahsil)'),
            (6, 'Senet çıkış (banka tahsil)'),
            (7, 'Çek çıkış (banka teminat)'),
            (8, 'Senet çıkış (banka teminat)'),
            (9, 'İşlem bordrosu (müşteri çeki)'),
            (10, 'İşlem bordrosu (müşteri senedi)'),
            (11, 'İşlem bordrosu (kendi çekimiz)'),
            (12, 'İşlem bordrosu (borç senedimiz)')
        ],
        help_text='İşlem türü'
    )
    destbranch = models.SmallIntegerField(
        db_column='DESTBRANCH',
        blank=True,
        null=True,
        help_text='Gönderilen işyeri'
    )
    destdepartment = models.SmallIntegerField(
        db_column='DESTDEPARTMENT',
        blank=True,
        null=True,
        help_text='Gönderilen bölüm'
    )
    cardmd = models.SmallIntegerField(
        db_column='CARDMD',
        blank=True,
        null=True,
        help_text="""
            Kart modül numarası;
            1-4 Cari hesap (5)
            5-8 Banka hesabı (7)
        """
    )
    proctype = models.SmallIntegerField(
        db_column='PROCTYPE',
        blank=True,
        null=True,
        help_text="""İşlem bordrosu fiş türü
            (İşlem bordrosu için geçerli. Diğer bordrolar için sıfır (0) olur)
        """
    )
    onepayline = models.SmallIntegerField(
        db_column='ONEPAYLINE',
        blank=True,
        null=True,
        help_text='Tek satırda (ortalama) ödeme'
    )
    fromcash = models.SmallIntegerField(
        db_column='FROMCASH',
        blank=True,
        null=True,
        help_text='Kasadan'
    )
    averageage = models.IntegerField(
        db_column='AVERAGEAGE',
        blank=True,
        null=True,
        help_text='Ortalama yaş'
    )
    doccnt = models.SmallIntegerField(
        db_column='DOCCNT',
        blank=True,
        null=True,
        help_text='Fişlere ait çek/senet sayısı'
    )
    total = models.FloatField(
        db_column='TOTAL',
        blank=True,
        null=True,
        help_text='Tutar'
    )
    trcurr = models.SmallIntegerField(
        db_column='TRCURR',
        blank=True,
        null=True,
        help_text='İşlem döviz türü'
    )
    trrate = models.FloatField(
        db_column='TRRATE',
        blank=True,
        null=True,
        help_text='İşlem döviz kuru'
    )
    trnet = models.FloatField(
        db_column='TRNET',
        blank=True,
        null=True,
        help_text='İşlem döviz tutarı'
    )
    reportrate = models.FloatField(
        db_column='REPORTRATE',
        blank=True,
        null=True,
        help_text='Raporlama döviz kuru'
    )
    reportnet = models.FloatField(
        db_column='REPORTNET',
        blank=True,
        null=True,
        help_text='Raporlama döviz tutarı'
    )
    accficheref = models.ForeignKey(
        "LG_CLFICHE",
        db_column='ACCFICHEREF',
        blank=True,
        null=True,
        help_text='Muhasebe fişi ref. -> CLFICHE',
        on_delete=models.DO_NOTHING
    )
    cashtransref = models.ForeignKey(
        "LG_KSLINES",
        db_column='CASHTRANSREF',
        blank=True,
        null=True,
        help_text='Kasa hareketi ref. -> KSLINES',
        on_delete=models.DO_NOTHING
    )
    accref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='ACCREF',
        blank=True,
        null=True,
        help_text='muhasebe hesabı ref. -> EMUHACC',
        on_delete=models.DO_NOTHING
    )
    cancelledacc = models.SmallIntegerField(
        db_column='CANCELLEDACC',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Muhasebeleştirme iptal')
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
    department = models.SmallIntegerField(
        db_column='DEPARTMENT',
        blank=True,
        null=True
    )

    opstat = models.SmallIntegerField(db_column='OPSTAT', blank=True,
        null=True, help_text='Hareket durumu')
    infidx = models.FloatField(db_column='INFIDX', blank=True,
        null=True, help_text='Enflasyon endeksi')
    affectcollatrl = models.SmallIntegerField(db_column='AFFECTCOLLATRL',
        blank=True, null=True)
    collatrollref = models.IntegerField(db_column='COLLATROLLREF',
        blank=True, null=True)
    grpfirmtrans = models.SmallIntegerField(db_column='GRPFIRMTRANS',
        blank=True, null=True)
    affectrisk = models.SmallIntegerField(db_column='AFFECTRISK',
        blank=True, null=True)
    bncreref = models.IntegerField(db_column='BNCREREF', blank=True, null=True)
    orglogoid = models.CharField(db_column='ORGLOGOID', max_length=25,
        blank=True, null=True)
    frombank = models.SmallIntegerField(db_column='FROMBANK',
        blank=True, null=True)
    degactive = models.SmallIntegerField(db_column='DEGACTIVE',
        blank=True, null=True)
    degcurr = models.SmallIntegerField(db_column='DEGCURR',
        blank=True, null=True)
    degcurrrate = models.FloatField(db_column='DEGCURRRATE',
        blank=True, null=True)
    approve = models.SmallIntegerField(db_column='APPROVE',
        blank=True, null=True)
    approvedate = models.DateTimeField(db_column='APPROVEDATE',
        blank=True, null=True)
    degactive2 = models.SmallIntegerField(db_column='DEGACTIVE2',
        blank=True, null=True)
    degcurr2 = models.SmallIntegerField(db_column='DEGCURR2',
        blank=True, null=True)
    degcurrrate2 = models.FloatField(db_column='DEGCURRRATE2',
        blank=True, null=True)
    docdate = models.DateTimeField(db_column='DOCDATE', blank=True, null=True)
    printdate = models.DateTimeField(db_column='PRINTDATE', blank=True,
        null=True)
    docode = models.CharField(db_column='DOCODE', max_length=33,
        blank=True, null=True)
    status = models.SmallIntegerField(db_column='STATUS', blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (
            ('trcode', 'rollno'), ('date_field', 'trcode', 'rollno'),
        )
        db_table = f'LG_{Active.namespace}_{Active.period}_CSROLL'
        target_db = 'erp'