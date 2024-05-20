"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_CLFICHE(
    BaseLogical,
    BaseAccounted,
    BaseGenexp,
    BaseInfo,
    BaseSiteRec,
    BaseBranch,
    BasePrint,
    BaseCancelled,
    BaseWF,
    BaseTrading,
    BaseSalesMan,
    BaseTextINC,
    BaseProject,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Cari hesap fişleri
        CLFICHE tablosunda cari hesap fişlerinin başlık bilgileri
        bulunmaktadır. Cari hesap hareketleri bilgilerine ulaşmak
        için CLFLINE tablosu okunmalıdır.
    """
    ficheno = models.CharField(
        db_column='FICHENO',
        max_length=17,
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
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Nakit tahsilat'),
            (2, 'Borç ödeme'),
            (3, 'Borç dekontu'),
            (4, 'Alacak dekontu'),
            (5, 'Virman fişi'),
            (6, 'Kur farkı fişi'),
            (12, 'Özel fiş'),
            (14, 'Açılış fişi'),
            (41, 'Verilen vade farkı faturası'),
            (42, 'Alınan vade farkı faturası')
        ],
        help_text='Hareket türü'
    )
    debit = models.FloatField(
        db_column='DEBIT',
        blank=True,
        null=True,
        help_text='Borç'
    )
    credit = models.FloatField(
        db_column='CREDIT',
        blank=True,
        null=True,
        help_text='Alacak'
    )
    repdebit = models.FloatField(
        db_column='REPDEBIT',
        blank=True,
        null=True,
        help_text='Borç (Raporlama Dövizi)'
    )
    repcredit = models.FloatField(
        db_column='REPCREDIT',
        blank=True,
        null=True,
        help_text='Alacak (Raporlama Dövizi)'
    )
    invoref = models.IntegerField(
        db_column='INVOREF',
        blank=True,
        null=True,
        help_text='Cari hesap istihbarat bilgileri ref.'
    )
    cashaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='CASHACCREF',
        blank=True,
        null=True,
        help_text='Kasa muhasebe hesabı ref. -> EMUHACC',
        on_delete=models.DO_NOTHING
    )
    cashcenref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='CASHCENREF',
        blank=True,
        null=True,
        help_text='Kasa masraf merkezi ref. -> EMCENTER',
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
        help_text='Muhasebeleştirme iptal'
    )
    accficheref = models.ForeignKey(
        "LG_EMFLINE",
        db_column='ACCFICHEREF',
        blank=True,
        null=True,
        help_text='Muhasebe fiş ref. -> EMFLINE',
        on_delete=models.DO_NOTHING
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
    time = models.IntegerField(
        db_column='TIME',
        blank=True,
        null=True,
        help_text='Zaman'
    )
    clcardref = models.IntegerField(
        db_column='CLCARDREF',
        blank=True,
        null=True,
        help_text='Müşteri kartı ref.'
    )
    bankaccref = models.IntegerField(
        db_column='BANKACCREF',
        blank=True,
        null=True,
        help_text='Banka hesabı ref.'
    )
    bnaccref = models.IntegerField(
        db_column='BNACCREF',
        blank=True,
        null=True,
        help_text='Muhasebe hesabı ref.'
    )
    bncenterref = models.IntegerField(
        db_column='BNCENTERREF',
        blank=True,
        null=True,
        help_text='Masraf merkezi ref.'
    )
    poscommaccref = models.IntegerField(
        db_column='POSCOMMACCREF',
        blank=True,
        null=True,
        help_text='Genel muhasebe hesapları ref.'
    )
    poscommcenref = models.IntegerField(
        db_column='POSCOMMCENREF',
        blank=True,
        null=True,
        help_text='Masraf merkezi ref.'
    )
    pointcommaccref = models.IntegerField(
        db_column='POINTCOMMACCREF',
        blank=True,
        null=True,
        help_text='Genel muhasebe hesapları ref.'
    )
    pointcommcenref = models.IntegerField(
        db_column='POINTCOMMCENREF',
        blank=True,
        null=True,
        help_text="Masraf merkezi ref."
    )
    status = models.SmallIntegerField(
        db_column='STATUS',
        blank=True,
        null=True
    )
    wflowcrdref = models.IntegerField(
        db_column='WFLOWCRDREF',
        blank=True,
        null=True
    )
    orglogoid = models.CharField(
        db_column='ORGLOGOID',
        max_length=25,
        blank=True,
        null=True
    )
    affectcollatrl = models.SmallIntegerField(
        db_column='AFFECTCOLLATRL',
        blank=True,
        null=True
    )
    grpfirmtrans = models.SmallIntegerField(
        db_column='GRPFIRMTRANS',
        blank=True,
        null=True
    )
    affectrisk = models.SmallIntegerField(
        db_column='AFFECTRISK',
        blank=True,
        null=True
    )
    posterminalnr = models.IntegerField(
        db_column='POSTERMINALNR',
        blank=True,
        null=True
    )
    posterminalnum = models.CharField(
        db_column='POSTERMINALNUM',
        max_length=17,
        blank=True,
        null=True
    )
    approve = models.SmallIntegerField(
        db_column='APPROVE',
        blank=True,
        null=True
    )
    approvedate = models.DateTimeField(
        db_column='APPROVEDATE',
        blank=True,
        null=True
    )
    cstransref = models.IntegerField(
        db_column='CSTRANSREF',
        blank=True,
        null=True
    )
    docdate = models.DateTimeField(
        db_column='DOCDATE',
        blank=True,
        null=True
    )
    devir = models.SmallIntegerField(
        db_column='DEVIR',
        blank=True,
        null=True
    )
    printdate = models.DateTimeField(
        db_column='PRINTDATE',
        blank=True,
        null=True
    )
    forexim = models.SmallIntegerField(
        db_column='FOREXIM',
        blank=True,
        null=True
    )
    typecode = models.CharField(
        db_column='TYPECODE',
        max_length=5,
        blank=True,
        null=True
    )
    einvoice = models.SmallIntegerField(
        db_column='EINVOICE',
        blank=True,
        null=True
    )
    deductcode = models.CharField(
        db_column='DEDUCTCODE',
        max_length=11,
        blank=True,
        null=True
    )
    department = models.SmallIntegerField(
        db_column='DEPARTMENT',
        blank=True,
        null=True
    )
    speccode = models.CharField(
        db_column='SPECCODE',
        max_length=11,
        blank=True,
        null=True
    )
    cyphcode = models.CharField(
        db_column='CYPHCODE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Yetki kodu'
    )
    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_CLFICHE'
        target_db = 'erp'