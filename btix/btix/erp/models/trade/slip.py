"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_PAYTRANS(
    BaseLogical,
    BaseCard,
    BaseSign,
    BaseCancelled,
    BaseSiteRec,
    BaseWF,
    models.Model):
    """
        Ödeme hareketi
        Fatura, cari hesap, çek/senet, banka işlemlerinde sonra ödeme
        hareketleri oluşmaktadır. Fatura geneli ua da satırlarının
        ödeme planı kartlarına bağlanması durumunda ödeme hareketleri
        ödeme planı kartında belirtilen formüle göre oluşturulur.
        Borç kapama işleminden sonra tüm ödeme hareketi kapanmamış
        ise kalan miktar için yeni bir ödeme hareketi oluşturulmaktadır.
    """
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    modulenr = models.SmallIntegerField(
        db_column='MODULENR',
        blank=True,
        null=True,
        choices=[
            (4, 'Fatura'),
            (5, 'Cari hesap'),
            (6, 'Çek/senet'),
            (7, 'Banka'),
            (10, 'Banka hareketi'),
            (61, 'Çek/senet'),
            (62, 'Cari hesap')
        ],
        help_text='Kart modül numarası'
    )

    ficheref = models.ForeignKey(
        "LG_STFICHE",
        db_column='FICHEREF',
        blank=True,
        null=True,
        help_text='Fiş ref. -> STFICHE',
        on_delete=models.DO_NOTHING
    )
    fichelineref = models.ForeignKey(
        "LG_STLINE",
        db_column='FICHELINEREF',
        blank=True,
        null=True,
        help_text='Fiş satır ref. -> STLINE',
        on_delete=models.DO_NOTHING
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        help_text='İlgili fiş türü'
    )
    total = models.FloatField(
        db_column='TOTAL',
        blank=True,
        null=True,
        help_text='Tutar'
    )
    paid = models.FloatField(
        db_column='PAID',
        blank=True,
        null=True,
        help_text='Ödenen tutar'
    )
    earlyintrate = models.FloatField(
        db_column='EARLYINTRATE',
        blank=True,
        null=True,
        help_text='Erken ödeme faiz oranı'
    )
    latelyintrate = models.FloatField(
        db_column='LATELYINTRATE',
        blank=True,
        null=True,
        help_text='Geç ödeme faiz oranı'
    )
    crossref = models.IntegerField(
        db_column='CROSSREF',
        blank=True,
        null=True,
        help_text='Karşı işlem ref. -> PAYTRANS'
    )
    paidincash = models.SmallIntegerField(
        db_column='PAIDINCASH',
        blank=True,
        null=True,
        help_text='Peşi̇n ödenmi̇ş (E/H)'
    )
    procdate = models.DateTimeField(
        db_column='PROCDATE',
        blank=True,
        null=True,
        help_text='İşlem tarihi'
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
    reportrate = models.FloatField(
        db_column='REPORTRATE',
        blank=True,
        null=True,
        help_text='Raporlama döviz kuru'
    )
    modified = models.SmallIntegerField(
        db_column='MODIFIED', blank=True, null=True)
    remindlev = models.SmallIntegerField(
        db_column='REMINDLEV', blank=True, null=True)
    remindsent = models.SmallIntegerField(
        db_column='REMINDSENT', blank=True, null=True)
    crosscurr = models.SmallIntegerField(
        db_column='CROSSCURR', blank=True, null=True)
    crosstotal = models.FloatField(
        db_column='CROSSTOTAL', blank=True, null=True)
    discflag = models.SmallIntegerField(
        db_column='DISCFLAG', blank=True, null=True)
    orglogicref = models.IntegerField(
        db_column='ORGLOGICREF',
        blank=True,
        null=True,
        help_text='Orjinal kayıt ref.'
    )
    closingrate = models.FloatField(
        db_column='CLOSINGRATE', blank=True, null=True)
    discduedate = models.DateTimeField(
        db_column='DISCDUEDATE', blank=True, null=True)
    opstat = models.SmallIntegerField(
        db_column='OPSTAT', blank=True, null=True)
    infidx = models.FloatField(
        db_column='INFIDX', blank=True, null=True)
    payno = models.SmallIntegerField(
        db_column='PAYNO', blank=True, null=True)
    delaytotal = models.FloatField(
        db_column='DELAYTOTAL', blank=True, null=True)
    lastsendremlev = models.IntegerField(
        db_column='LASTSENDREMLEV', blank=True, null=True)
    pointtrans = models.SmallIntegerField(
        db_column='POINTTRANS', blank=True, null=True)
    bankpaydate = models.DateTimeField(
        db_column='BANKPAYDATE', blank=True, null=True)
    poscomsn = models.FloatField(
        db_column='POSCOMSN', blank=True, null=True)
    pointcomsn = models.FloatField(
        db_column='POINTCOMSN', blank=True, null=True)
    bankaccref = models.IntegerField(
        db_column='BANKACCREF', blank=True, null=True)
    paymenttype = models.SmallIntegerField(
        db_column='PAYMENTTYPE', blank=True, null=True)
    cashaccref = models.IntegerField(
        db_column='CASHACCREF', blank=True, null=True)
    trnet = models.FloatField(
        db_column='TRNET', blank=True, null=True)
    repayplanref = models.IntegerField(
        db_column='REPAYPLANREF', blank=True, null=True)
    duediffcomsn = models.FloatField(
        db_column='DUEDIFFCOMSN', blank=True, null=True)
    calctype = models.SmallIntegerField(
        db_column='CALCTYPE', blank=True, null=True)
    nettotal = models.FloatField(
        db_column='NETTOTAL', blank=True, null=True)
    repyplnapplied = models.SmallIntegerField(
        db_column='REPYPLNAPPLIED', blank=True, null=True)
    paytrcurr = models.SmallIntegerField(
        db_column='PAYTRCURR', blank=True, null=True)
    paytrrate = models.FloatField(
        db_column='PAYTRRATE', blank=True, null=True)
    paytrnet = models.FloatField(
        db_column='PAYTRNET', blank=True, null=True)
    bntrcreated = models.SmallIntegerField(
        db_column='BNTRCREATED', blank=True, null=True)
    bnfchref = models.IntegerField(
        db_column='BNFCHREF', blank=True, null=True)
    bnflnref = models.IntegerField(
        db_column='BNFLNREF', blank=True, null=True)
    instaltype = models.SmallIntegerField(
        db_column='INSTALTYPE', blank=True, null=True)
    instalref = models.IntegerField(
        db_column='INSTALREF', blank=True, null=True)
    maininstalref = models.IntegerField(
        db_column='MAININSTALREF', blank=True, null=True)
    orglogoid = models.CharField(
        db_column='ORGLOGOID', max_length=25, blank=True, null=True)
    stlineref = models.IntegerField(
        db_column='STLINEREF', blank=True, null=True)
    specode = models.CharField(
        db_column='SPECODE', max_length=11, blank=True, null=True)
    creditcardnum = models.CharField(
        db_column='CREDITCARDNUM', max_length=17, blank=True, null=True)
    valbegdate = models.DateTimeField(
        db_column='VALBEGDATE', blank=True, null=True)
    retrefno = models.CharField(
        db_column='RETREFNO', max_length=13, blank=True, null=True)
    docode = models.CharField(
        db_column='DOCODE', max_length=33, blank=True, null=True)
    batchnum = models.CharField(
        db_column='BATCHNUM', max_length=17, blank=True, null=True)
    approvenum = models.CharField(
        db_column='APPROVENUM', max_length=17, blank=True, null=True)
    posterminalnum = models.CharField(
        db_column='POSTERMINALNUM', max_length=17, blank=True, null=True)
    cldiffinv = models.SmallIntegerField(
        db_column='CLDIFFINV', blank=True, null=True)
    lineexp = models.CharField(
        db_column='LINEEXP', max_length=51, blank=True, null=True)
    devirprocdate = models.DateTimeField(
        db_column='DEVIRPROCDATE', blank=True, null=True)
    devir = models.SmallIntegerField(
        db_column='DEVIR', blank=True, null=True)
    devircardref = models.IntegerField(
        db_column='DEVIRCARDREF', blank=True, null=True)
    globalcode = models.CharField(
        db_column='GLOBALCODE', max_length=11, blank=True, null=True)
    clbnaccountno = models.CharField(
        db_column='CLBNACCOUNTNO', max_length=17, blank=True, null=True)
    matchdate = models.DateTimeField(
        db_column='MATCHDATE', blank=True, null=True)
    devirbranch = models.SmallIntegerField(
        db_column='DEVIRBRANCH', blank=True, null=True)
    devirdepartment = models.SmallIntegerField(
        db_column='DEVIRDEPARTMENT', blank=True, null=True)
    devirficheref = models.IntegerField(
        db_column='DEVIRFICHEREF', blank=True, null=True)
    devirlineref = models.IntegerField(
        db_column='DEVIRLINEREF', blank=True, null=True)
    currdiffclsref = models.IntegerField(
        db_column='CURRDIFFCLSREF', blank=True, null=True)
    currdiffclosed = models.SmallIntegerField(
        db_column='CURRDIFFCLOSED', blank=True, null=True)
    currdiffrate = models.FloatField(
        db_column='CURRDIFFRATE', blank=True, null=True)
    vatflag = models.SmallIntegerField(
        db_column='VATFLAG', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_PAYTRANS'
        target_db = 'erp'

