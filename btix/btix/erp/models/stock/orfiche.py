"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_ORFICHE(
    BaseLogical,
    BaseCode,
    BaseClient,
    BaseAccount,
    BaseCenter,
    BaseGenexp,
    BasePrint,
    BaseInfo,
    BaseSalesMan,
    BaseTrading,
    BaseTextINC,
    BaseSiteRec,
    BaseWF,
    BaseCancelled,
    BaseProject,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Sipariş fişleri
        ORFICHE tablosunda sipariş fişlerinin başlık bilgileri tutulmaktadır.
        Sipariş fişlerinin satırlarına ait bilgilere ORFLINE tablosundan
        erişebilir
    """
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Alınan sipariş'),
            (2, 'Verilen sipariş')
        ],
        help_text='Fiş türü'
    )
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
    time_field = models.IntegerField(
        db_column='TIME_',
        blank=True,
        null=True,
        help_text='Saat'
    )
    docode = models.CharField(
        db_column='DOCODE',
        max_length=33,
        blank=True,
        null=True,
        help_text='Belge no'
    )
    recvref = models.ForeignKey(
        "LG_CLCARD",
        db_column='RECVREF',
        blank=True,
        null=True,
        help_text='Teslimat cari hesap ref. -> CLCARD',
        on_delete=models.DO_NOTHING
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
    updcurr = models.SmallIntegerField(
        db_column='UPDCURR',
        blank=True,
        null=True,
        help_text="""İrsaliye ve faturaya aktarıldığında fiyatlandırma
            dövizi güncellenecek (E/H)"""
    )
    adddiscounts = models.FloatField(
        db_column='ADDDISCOUNTS',
        blank=True,
        null=True,
        help_text='Ek indirimler'
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
        help_text='Ek masraflar'
    )
    totalexpenses = models.FloatField(
        db_column='TOTALEXPENSES',
        blank=True,
        null=True,
        help_text='Toplam masraflar'
    )
    totalpromotions = models.FloatField(
        db_column='TOTALPROMOTIONS',
        blank=True,
        null=True,
        help_text='Toplam promosyonlar'
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
        help_text='Net toplam'
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
    extenref = models.ForeignKey(
        "LG_SRVCARD",
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ek dosya ref.',
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
    status = models.SmallIntegerField(
        db_column='STATUS',
        blank=True,
        null=True,
        choices=[
            (1, 'Öneri'),
            (2, 'Sevkedilemez'),
            (3, 'Sevkedilebilir')
        ],
        help_text='Onay bilgisi'
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
    genexctyp = models.SmallIntegerField(
        db_column='GENEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (Genel)'
    )
    lineexctyp = models.SmallIntegerField(
        db_column='LINEEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (Satır)'
    )
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika no'
    )
    shipinforef = models.ForeignKey(
        "LG_SHIPINFO",
        db_column='SHIPINFOREF',
        blank=True,
        null=True,
        help_text='Taşıyıcı ref',
        on_delete=models.DO_NOTHING
    )
    custordno = models.CharField(
        db_column='CUSTORDNO', max_length=51, blank=True, null=True)
    sendcnt = models.SmallIntegerField(
        db_column='SENDCNT', blank=True, null=True)
    dlvclient = models.SmallIntegerField(
        db_column='DLVCLIENT', blank=True, null=True)
    doctrackingnr = models.CharField(
        db_column='DOCTRACKINGNR', max_length=21, blank=True, null=True)
    orglogoid = models.CharField(
        db_column='ORGLOGOID',
        max_length=25,
        blank=True,
        null=True
    )
    offerref = models.IntegerField(db_column='OFFERREF', blank=True, null=True)
    offaltref = models.IntegerField(
        db_column='OFFALTREF', blank=True, null=True)
    typ = models.SmallIntegerField(
        db_column='TYP', blank=True, null=True)
    altnr = models.SmallIntegerField(
        db_column='ALTNR', blank=True, null=True)
    advancepaym = models.FloatField(
        db_column='ADVANCEPAYM', blank=True, null=True)
    trcurr = models.SmallIntegerField(
        db_column='TRCURR', blank=True, null=True)
    trrate = models.FloatField(
        db_column='TRRATE', blank=True, null=True)
    trnet = models.FloatField(
        db_column='TRNET', blank=True, null=True)
    paymenttype = models.SmallIntegerField(
        db_column='PAYMENTTYPE', blank=True, null=True)
    onlyonepayline = models.SmallIntegerField(
        db_column='ONLYONEPAYLINE', blank=True, null=True)
    opstat = models.SmallIntegerField(
        db_column='OPSTAT', blank=True, null=True)
    withpaytrans = models.SmallIntegerField(
        db_column='WITHPAYTRANS', blank=True, null=True)
    wflowcrdref = models.IntegerField(
        db_column='WFLOWCRDREF', blank=True, null=True)
    updtrcurr = models.SmallIntegerField(
        db_column='UPDTRCURR', blank=True, null=True)
    affectcollatrl = models.SmallIntegerField(
        db_column='AFFECTCOLLATRL', blank=True, null=True)
    pofferbegdt = models.DateTimeField(
        db_column='POFFERBEGDT', blank=True, null=True)
    pofferenddt = models.DateTimeField(
        db_column='POFFERENDDT', blank=True, null=True)
    revisnr = models.CharField(
        db_column='REVISNR', max_length=17, blank=True, null=True)
    lastrevision = models.SmallIntegerField(
        db_column='LASTREVISION', blank=True, null=True)
    checkamount = models.SmallIntegerField(
        db_column='CHECKAMOUNT', blank=True, null=True)
    slsopprref = models.IntegerField(
        db_column='SLSOPPRREF', blank=True, null=True)
    slsactref = models.IntegerField(
        db_column='SLSACTREF', blank=True, null=True)
    slscustref = models.IntegerField(
        db_column='SLSCUSTREF', blank=True, null=True)
    affectrisk = models.SmallIntegerField(
        db_column='AFFECTRISK', blank=True, null=True)
    totaladdtax = models.FloatField(
        db_column='TOTALADDTAX', blank=True, null=True)
    totalexaddtax = models.FloatField(
        db_column='TOTALEXADDTAX', blank=True, null=True)
    approve = models.SmallIntegerField(
        db_column='APPROVE', blank=True, null=True)
    approvedate = models.DateTimeField(
        db_column='APPROVEDATE', blank=True, null=True)
    checkprice = models.SmallIntegerField(
        db_column='CHECKPRICE', blank=True, null=True)
    transferwithpay = models.SmallIntegerField(
        db_column='TRANSFERWITHPAY', blank=True, null=True)
    fcstatusref = models.IntegerField(
        db_column='FCSTATUSREF', blank=True, null=True)
    checktotal = models.SmallIntegerField(
        db_column='CHECKTOTAL', blank=True, null=True)
    cantcrededuct = models.SmallIntegerField(
        db_column='CANTCREDEDUCT', blank=True, null=True)
    deductionpart1 = models.SmallIntegerField(
        db_column='DEDUCTIONPART1', blank=True, null=True)
    deductionpart2 = models.SmallIntegerField(
        db_column='DEDUCTIONPART2', blank=True, null=True)
    globalid = models.CharField(
        db_column='GLOBALID', max_length=51, blank=True, null=True)
    defaultfiche = models.SmallIntegerField(
        db_column='DEFAULTFICHE', blank=True, null=True)
    leasingref = models.IntegerField(
        db_column='LEASINGREF', blank=True, null=True)
    campaigncode = models.CharField(
        db_column='CAMPAIGNCODE', max_length=25, blank=True, null=True)
    addexpensesvat = models.FloatField(
        db_column='ADDEXPENSESVAT', blank=True, null=True)
    totalexpensesvat = models.FloatField(
        db_column='TOTALEXPENSESVAT', blank=True, null=True)
    devir = models.SmallIntegerField(
        db_column='DEVIR', blank=True, null=True)
    printdate = models.DateTimeField(
        db_column='PRINTDATE', blank=True, null=True)
    deliverycode = models.CharField(
        db_column='DELIVERYCODE', max_length=11, blank=True, null=True)
    vatexceptreason = models.CharField(
        db_column='VATEXCEPTREASON', max_length=201, blank=True, null=True)
    vatexceptcode = models.CharField(
        db_column='VATEXCEPTCODE', max_length=11, blank=True, null=True)
    ataxexceptcode = models.CharField(
        db_column='ATAXEXCEPTCODE', max_length=11, blank=True, null=True)
    taxfreechx = models.SmallIntegerField(
        db_column='TAXFREECHX', blank=True, null=True)
    ataxexceptreason = models.CharField(
        db_column='ATAXEXCEPTREASON', max_length=201, blank=True, null=True)
    einvoice = models.SmallIntegerField(
        db_column='EINVOICE', blank=True, null=True)
    einvoicetyp = models.SmallIntegerField(
        db_column='EINVOICETYP', blank=True, null=True)
    publicbnaccref = models.IntegerField(
        db_column='PUBLICBNACCREF', blank=True, null=True)
    insteadofdesp = models.SmallIntegerField(
        db_column='INSTEADOFDESP', blank=True, null=True)
    accepteinvpublic = models.SmallIntegerField(
        db_column='ACCEPTEINVPUBLIC', blank=True, null=True)
    orgdate = models.DateTimeField(
        db_column='ORGDATE', blank=True, null=True)
    adddiscountsvat = models.FloatField(
        db_column='ADDDISCOUNTSVAT', blank=True, null=True)
    actrenting = models.SmallIntegerField(
        db_column='ACTRENTING', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_ORFICHE'
        unique_together = (('trcode', 'ficheno'),)
        target_db = 'erp'
