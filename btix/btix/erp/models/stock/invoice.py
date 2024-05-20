"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_INVOICE(
    BaseLogical,
    BaseCode,
    BaseClient,
    BaseCenter,
    BaseAccount,
    BaseCancelled,
    BaseAccounted,
    BaseGenexp,
    BasePrint,
    BaseInfo,
    BaseVAT,
    BaseSalesMan,
    BaseTrading,
    BaseTextINC,
    BaseSiteRec,
    BaseWF,
    BaseProject,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        INVOICE tablosunda veri tabanına kaydedilen faturaların başlık bilgileri
        tutulmaktadır. Faturanın satır bilgilerine ulaşmak için STLINE
        tablosu okunmalıdır.
    """
    grpcode = models.SmallIntegerField(
        db_column='GRPCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Alım faturası'),
            (2, 'Satış faturası')
        ],
        help_text='Grup kodu'
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Mal alım faturası'),
            (2, 'Perakende satış iade faturası'),
            (3, 'Toptan satış iade faturası'),
            (4, 'Alınan hizmet faturası'),
            (5, 'Alınan proforma fatura'),
            (6, 'Alım iade faturası'),
            (7, 'Perakende satış faturası'),
            (8, 'Toptan satış faturası'),
            (9, 'Verilen hizmet faturası'),
            (10, 'Verilen proforma fatura'),
            (13, 'Alınan fiyat farkı faturası'),
            (14, 'Verilen fiyat farkı faturası'),
            (26, 'Müstahsil makbuzu')
        ],
    )
    ficheno = models.CharField(
        db_column='FICHENO',
        max_length=17,
        blank=True,
        null=True,
        help_text='Fatura numarası'
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    time_field = models.IntegerField(
        db_column='TIME_',
        blank=True,
        null=True,
        help_text='Zaman'
    )
    docode = models.CharField(
        db_column='DOCODE',
        max_length=33,
        blank=True,
        null=True,
        help_text='Belge no'
    )
    recvref = models.IntegerField(
        db_column='RECVREF',
        blank=True,
        null=True,
        help_text='Alıcı (sevkiyat) cari hesap ref. -> CLCARD'
    )
    sourceindex = models.SmallIntegerField(
        db_column='SOURCEINDEX',
        blank=True,
        null=True,
        help_text='Ambar no'
    )
    sourcecostgrp = models.SmallIntegerField(
        db_column='SOURCECOSTGRP',
        blank=True,
        null=True,
        help_text=''
    )
    paidincash = models.SmallIntegerField(
        db_column='PAIDINCASH',
        blank=True,
        null=True,
        help_text='Peşin ödenmiş (E/H)'
    )
    fromkasa = models.SmallIntegerField(
        db_column='FROMKASA',
        blank=True,
        null=True,
        help_text='Kasadan fatura (E/H)'
    )
    entegset = models.SmallIntegerField(
        db_column='ENTEGSET',
        blank=True,
        null=True,
        help_text="""
            1. bit -> İndirimler dağılmış
            2. bit -> Masraflar dağılmış
            3. bit -> Promosyonlar dağılmış
        """
    )
    adddiscounts = models.FloatField(
        db_column='ADDDISCOUNTS',
        blank=True,
        null=True,
        help_text='Satıra uygulanan ek indirimler'
    )
    totaldiscounts = models.FloatField(
        db_column='TOTALDISCOUNTS',
        blank=True,
        null=True,
        help_text='Toplam indirimler'
    )
    totaldiscounted = models.FloatField(
        db_column='TOTALDISCOUNTED',
        blank=True,
        null=True,
        help_text='Satır indirimleri düşülmüş tutar'
    )
    addexpenses = models.FloatField(
        db_column='ADDEXPENSES',
        blank=True,
        null=True,
        help_text='Satıra uygulanan ek masraflar'
    )
    totalexpenses = models.FloatField(
        db_column='TOTALEXPENSES',
        blank=True,
        null=True,
        help_text='Toplam masraflar'
    )
    distexpense = models.FloatField(
        db_column='DISTEXPENSE',
        blank=True,
        null=True,
        help_text='Stok maliyetine dağıtılacak masraf'
    )
    totaldepozito = models.FloatField(
        db_column='TOTALDEPOZITO',
        blank=True,
        null=True,
        help_text='Toplam depozito'
    )
    totalpromotions = models.FloatField(
        db_column='TOTALPROMOTIONS',
        blank=True,
        null=True,
        help_text='Toplam promosyonlar'
    )
    vatincgross = models.FloatField(
        db_column='VATINCGROSS',
        blank=True,
        null=True,
        help_text='KDV dahil tutar'
    )
    totalvat = models.FloatField(
        db_column='TOTALVAT',
        blank=True,
        null=True,
        help_text='Toplam KDV'
    )
    grosstotal = models.FloatField(
        db_column='GROSSTOTAL',
        blank=True,
        null=True,
        help_text='Toplam'
    )
    nettotal = models.FloatField(
        db_column='NETTOTAL',
        blank=True,
        null=True,
        help_text='Net tutar'
    )
    interestapp = models.FloatField(
        db_column='INTERESTAPP',
        blank=True,
        null=True,
        help_text='Kapanan vade farkı'
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
        help_text='İşlem net tutarı'
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
        help_text='Raporlama net tutarı'
    )
    onlyonepayline = models.SmallIntegerField(
        db_column='ONLYONEPAYLINE',
        blank=True,
        null=True,
        help_text='Tek satırlı ödeme planı'
    )
    kastransref = models.ForeignKey(
        "LG_KSLINES",
        db_column='KASTRANSREF',
        blank=True,
        null=True,
        help_text='Kasa hareketi ref. -> KSLINES',
        on_delete=models.DO_NOTHING
    )
    paydefref = models.ForeignKey(
        "LG_PAYPLANS",
        db_column='PAYDEFREF',
        blank=True,
        null=True,
        help_text='Ödeme planı ref. -> PAYPLANS',
        on_delete=models.DO_NOTHING
    )
    gvatinc = models.SmallIntegerField(
        db_column='GVATINC',
        blank=True,
        null=True,
        choices=[
            (0, 'Dahil'),
            (1, 'Hariç')
        ],
        help_text='KDV'
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
    accficheref = models.ForeignKey(
        "LG_EMFICHE",
        db_column='ACCFICHEREF',
        blank=True,
        null=True,
        help_text='Muhasebe fiş ref. -> EMFICHE',
        on_delete=models.DO_NOTHING
    )
    addexpaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='ADDEXPACCREF',
        blank=True,
        null=True,
        help_text='Ek masraf muhasebe ref. -> EMUHACC',
        on_delete=models.DO_NOTHING
    )
    addexpcentref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='ADDEXPCENTREF',
        blank=True,
        null=True,
        help_text='Ek masraf muhasebe masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING
    )
    decprdiff = models.SmallIntegerField(
        db_column='DECPRDIFF',
        blank=True,
        null=True,
        help_text=''
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
    shptypcod = models.CharField(
        db_column='SHPTYPCOD',
        max_length=13,
        blank=True,
        null=True,
        help_text='Sevkiyat türü'
    )
    shpagncod = models.CharField(
        db_column='SHPAGNCOD',
        max_length=13,
        blank=True,
        null=True,
        help_text='Taşıyıcı kodu'
    )
    tracknr = models.CharField(
        db_column='TRACKNR',
        max_length=65,
        blank=True,
        null=True,
        help_text='Paket / Koli no'
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
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika no'
    )
    shipinforef = models.IntegerField(
        db_column='SHIPINFOREF',
        blank=True,
        null=True
    )
    distorderref = models.IntegerField(
        db_column='DISTORDERREF', blank=True, null=True)
    sendcnt = models.SmallIntegerField(
        db_column='SENDCNT', blank=True, null=True)
    dlvclient = models.SmallIntegerField(
        db_column='DLVCLIENT', blank=True, null=True)
    costofsalefcref = models.IntegerField(
        db_column='COSTOFSALEFCREF', blank=True, null=True)
    opstat = models.SmallIntegerField(
        db_column='OPSTAT', blank=True, null=True)
    doctrackingnr = models.CharField(
        db_column='DOCTRACKINGNR',
        max_length=21,
        blank=True,
        null=True
    )
    totaladdtax = models.FloatField(
        db_column='TOTALADDTAX',
        blank=True,
        null=True
    )
    paymenttype = models.SmallIntegerField(
        db_column='PAYMENTTYPE',
        blank=True,
        null=True
    )
    infidx = models.FloatField(
        db_column='INFIDX',
        blank=True,
        null=True
    )
    accountedcnt = models.SmallIntegerField(
        db_column='ACCOUNTEDCNT',
        blank=True,
        null=True
    )
    orglogoid = models.CharField(
        db_column='ORGLOGOID',
        max_length=25,
        blank=True,
        null=True
    )
    fromexim = models.SmallIntegerField(
        db_column='FROMEXIM', blank=True, null=True)
    frgtypcod = models.CharField(
        db_column='FRGTYPCOD', max_length=13, blank=True, null=True)
    eximfctype = models.SmallIntegerField(
        db_column='EXIMFCTYPE', blank=True, null=True)
    fromordwithpay = models.SmallIntegerField(
        db_column='FROMORDWITHPAY', blank=True, null=True)
    wflowcrdref = models.IntegerField(
        db_column='WFLOWCRDREF', blank=True, null=True)
    status = models.SmallIntegerField(
        db_column='STATUS', blank=True, null=True)
    deductionpart1 = models.SmallIntegerField(
        db_column='DEDUCTIONPART1', blank=True, null=True)
    deductionpart2 = models.SmallIntegerField(
        db_column='DEDUCTIONPART2', blank=True, null=True)
    totalexaddtax = models.FloatField(
        db_column='TOTALEXADDTAX', blank=True, null=True)
    exaccounted = models.SmallIntegerField(
        db_column='EXACCOUNTED', blank=True, null=True)
    frombank = models.SmallIntegerField(
        db_column='FROMBANK', blank=True, null=True)
    bntransref = models.IntegerField(
        db_column='BNTRANSREF', blank=True, null=True)
    affectcollatrl = models.SmallIntegerField(
        db_column='AFFECTCOLLATRL', blank=True, null=True)
    grpfirmtrans = models.SmallIntegerField(
        db_column='GRPFIRMTRANS', blank=True, null=True)
    affectrisk = models.SmallIntegerField(
        db_column='AFFECTRISK', blank=True, null=True)
    controlinfo = models.SmallIntegerField(
        db_column='CONTROLINFO', blank=True, null=True)
    postransferinfo = models.SmallIntegerField(
        db_column='POSTRANSFERINFO', blank=True, null=True)
    taxfreechx = models.SmallIntegerField(
        db_column='TAXFREECHX', blank=True, null=True)
    passportno = models.CharField(
        db_column='PASSPORTNO', max_length=51, blank=True, null=True)
    creditcardno = models.CharField(
        db_column='CREDITCARDNO', max_length=17, blank=True, null=True)
    ineffectivecost = models.SmallIntegerField(
        db_column='INEFFECTIVECOST', blank=True, null=True)
    reflected = models.SmallIntegerField(
        db_column='REFLECTED', blank=True, null=True)
    reflaccficheref = models.IntegerField(
        db_column='REFLACCFICHEREF', blank=True, null=True)
    cancelledreflacc = models.SmallIntegerField(
        db_column='CANCELLEDREFLACC', blank=True, null=True)
    creditcardnum = models.CharField(
        db_column='CREDITCARDNUM', max_length=17, blank=True, null=True)
    approve = models.SmallIntegerField(
        db_column='APPROVE', blank=True, null=True)
    approvedate = models.DateTimeField(
        db_column='APPROVEDATE', blank=True, null=True)
    cantcrededuct = models.SmallIntegerField(
        db_column='CANTCREDEDUCT', blank=True, null=True)
    entrust = models.SmallIntegerField(
        db_column='ENTRUST', blank=True, null=True)
    docdate = models.DateTimeField(
        db_column='DOCDATE', blank=True, null=True)
    einvoice = models.SmallIntegerField(
        db_column='EINVOICE', blank=True, null=True)
    profileid = models.SmallIntegerField(
        db_column='PROFILEID', blank=True, null=True)
    estatus = models.SmallIntegerField(
        db_column='ESTATUS', blank=True, null=True)
    estartdate = models.DateTimeField(
        db_column='ESTARTDATE', blank=True, null=True)
    eenddate = models.DateTimeField(
        db_column='EENDDATE', blank=True, null=True)
    edescription = models.CharField(
        db_column='EDESCRIPTION', max_length=51, blank=True, null=True)
    eduration = models.FloatField(
        db_column='EDURATION', blank=True, null=True)
    edurationtype = models.SmallIntegerField(
        db_column='EDURATIONTYPE', blank=True, null=True)
    devir = models.SmallIntegerField(
        db_column='DEVIR', blank=True, null=True)
    distadjpriceufrs = models.FloatField(
        db_column='DISTADJPRICEUFRS', blank=True, null=True)
    cosfcrefufrs = models.IntegerField(
        db_column='COSFCREFUFRS', blank=True, null=True)
    globalid = models.CharField(
        db_column='GLOBALID', max_length=51, blank=True, null=True)
    totalservices = models.FloatField(
        db_column='TOTALSERVICES', blank=True, null=True)
    fromleasing = models.SmallIntegerField(
        db_column='FROMLEASING', blank=True, null=True)
    cancelexp = models.CharField(
        db_column='CANCELEXP', max_length=251, blank=True, null=True)
    undoexp = models.CharField(
        db_column='UNDOEXP', max_length=251, blank=True, null=True)
    vatexceptreason = models.CharField(
        db_column='VATEXCEPTREASON', max_length=201, blank=True, null=True)
    campaigncode = models.CharField(
        db_column='CAMPAIGNCODE', max_length=25, blank=True, null=True)
    canceldespsinv = models.SmallIntegerField(
        db_column='CANCELDESPSINV', blank=True, null=True)
    fromexchdiff = models.SmallIntegerField(
        db_column='FROMEXCHDIFF', blank=True, null=True)
    eximvat = models.SmallIntegerField(
        db_column='EXIMVAT', blank=True, null=True)
    serialcode = models.CharField(
        db_column='SERIALCODE', max_length=17, blank=True, null=True)
    appcldeductlim = models.SmallIntegerField(
        db_column='APPCLDEDUCTLIM', blank=True, null=True)
    einvoicetyp = models.SmallIntegerField(
        db_column='EINVOICETYP', blank=True, null=True)
    vatexceptcode = models.CharField(
        db_column='VATEXCEPTCODE', max_length=11, blank=True, null=True)
    offerref = models.IntegerField(
        db_column='OFFERREF', blank=True, null=True)
    ataxexceptreason = models.CharField(
        db_column='ATAXEXCEPTREASON', max_length=201, blank=True, null=True)
    ataxexceptcode = models.CharField(
        db_column='ATAXEXCEPTCODE', max_length=11, blank=True, null=True)
    fromstaffotherex = models.SmallIntegerField(
        db_column='FROMSTAFFOTHEREX', blank=True, null=True)
    nocalculate = models.SmallIntegerField(
        db_column='NOCALCULATE', blank=True, null=True)
    insteadofdesp = models.SmallIntegerField(
        db_column='INSTEADOFDESP', blank=True, null=True)
    okcfiche = models.SmallIntegerField(
        db_column='OKCFICHE', blank=True, null=True)
    canceldate = models.DateTimeField(
        db_column='CANCELDATE', blank=True, null=True)
    frgtypdesc = models.CharField(
        db_column='FRGTYPDESC', max_length=251, blank=True, null=True)
    markref = models.IntegerField(
        db_column='MARKREF', blank=True, null=True)
    printdate = models.DateTimeField(
        db_column='PRINTDATE', blank=True, null=True)
    delivercode = models.CharField(
        db_column='DELIVERCODE', max_length=11, blank=True, null=True)
    typecode = models.CharField(
        db_column='TYPECODE', max_length=5, blank=True, null=True)
    futmnthyrexpinc = models.SmallIntegerField(
        db_column='FUTMNTHYREXPINC', blank=True, null=True)
    accepteinvpublic = models.SmallIntegerField(
        db_column='ACCEPTEINVPUBLIC', blank=True, null=True)
    publicbnaccref = models.IntegerField(
        db_column='PUBLICBNACCREF', blank=True, null=True)
    docdetail = models.SmallIntegerField(
        db_column='DOCDETAIL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_INVOICE'
        unique_together = (
            ('grpcode', 'trcode', 'ficheno'),
            ('trcode', 'ficheno'),
        )
        target_db = 'erp'
