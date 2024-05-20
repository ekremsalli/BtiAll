"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_STFICHE(
    BaseLogical,
    BaseClient,
    BaseAccount,
    BaseCenter,
    BaseBranch,
    BaseCode,
    BaseCancelled,
    BaseAccounted,
    BaseGenexp,
    BasePrint,
    BaseInfo,
    BaseSalesMan,
    BaseTrading,
    BaseSiteRec,
    BaseWF,
    BaseGUID,
    BaseProject,
    BaseTextINC,
    BaseRef,
    models.Model):
    """
        Stok fişleri
        Ambar fişi, giriş çıkış fişleri ve irsaliye kayıtlarının başlık bilgileri
        STFICHE tablosunda tutulmaktadır.
        Stok hareketlerine ulaşmak için STLINE tablosunun okunması gerekir.
    """
    grpcode = models.SmallIntegerField(
        db_column='GRPCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Satınalma'),
            (2, 'Satış'),
            (3, 'Malzeme yönetimi')
        ],
        help_text="""
            Grup kodu;
            1 -> Satınalma
            2 -> Satış
            3 -> Malzeme yönetimi
        """
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Mal alım irsaliyesi'),
            (2, 'Per. sat. iade irs.'),
            (3, 'Topt. sat. iade irs.'),
            (4, 'Kons. çıkış iade irs.'),
            (5, 'Konsinye giriş irs.'),
            (6, 'Alım iade irs.'),
            (7, 'Perakende satış irs.'),
            (8, 'Toptan satış irsaliyesi'),
            (9, 'Konsinye çıkış irsaliyesi'),
            (10, 'Konsinye giriş iade irs.'),
            (11, 'Fire fişi'),
            (12, 'Sarf fişi'),
            (13, 'Üretimden giriş fişi'),
            (14, 'Devir fişi'),
            (25, 'Ambar fişi'),
            (26, 'Mustahsil irs.'),
            (50, 'Sayım fazlası fişi'),
            (51, 'Sayım eksiği fişi')
        ],
        help_text="""
            Fiş türü;
            1 -> Mal alım irsaliyesi
            2 -> Per. sat. iade irs.
            3 -> Topt. sat. iade irs.
            4 -> Kons. çıkış iade irs.
            5 -> Konsinye giriş irs.
            6 -> Alım iade irs.
            7 -> Perakende satış irs.
            8 -> Toptan satış irsaliyesi
            9 -> Konsinye çıkış irsaliyesi
            10 -> Konsinye giriş iade irs.
            11 -> Fire fişi
            12 -> Sarf fişi
            13 -> Üretimden giriş fişi
            14 -> Devir fişi
            25 -> Ambar fişi
            26 -> Mustahsil irs.
            50 -> Sayım fazlası fişi
            51 -> Sayım eksiği fişi
        """
    )
    iocode = models.SmallIntegerField(
        db_column='IOCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Girdi'),
            (2, 'Ambar'),
            (3, 'Çıktı')
        ],
        help_text="""
            Giriş Çıkış kodu;
            1 -> Girdi (TRCODE=1,2,34,5,13,14,15,16,17,18,19,26,30,31,32,33,34,50)
            2 -> Ambar (TRCODE=25)
            3 -> Çıktı (TRCODE=6,7,8,9,10,11,12,20,21,22,23,24,35,36,37,38,39,51)
        """
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
    ftime = models.IntegerField(
        db_column='FTIME',
        blank=True,
        null=True,
        help_text='Fiş zamanı'
    )
    docode = models.CharField(
        db_column='DOCODE',
        max_length=33,
        blank=True,
        null=True,
        help_text='Belge numarası'
    )
    invno = models.CharField(
        db_column='INVNO',
        max_length=17,
        blank=True,
        null=True,
        help_text='Fatura numarası'
    )

    invoiceref = models.ForeignKey(
        "LG_INVOICE",
        db_column='INVOICEREF',
        blank=True,
        null=True,
        help_text='Fatura ref. -> INVOICE',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_invoiceref'
    )

    recvref = models.ForeignKey(
        "LG_CLCARD",
        db_column='RECVREF',
        blank=True,
        null=True,
        help_text='Alıcı cari hesap ref. -> CLCARD',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_recvref'
    )
    prodorderref = models.ForeignKey(
        "LG_PRODORD",
        db_column='PRODORDERREF',
        blank=True,
        null=True,
        help_text='Üretim emri ref. -> PRODORD',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_prodorderref'
    )
    porderficheno = models.CharField(
        db_column='PORDERFICHENO',
        max_length=17,
        blank=True,
        null=True,
        help_text='Üretim emri fiş numarası'
    )
    sourcetype = models.SmallIntegerField(
        db_column='SOURCETYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Ambar'),
            (2, 'İş istasyonu')
        ],
        help_text="""
            Kaynak türü;
            1 -> Ambar
            2 -> İş istasyonu
        """
    )
    sourceindex = models.SmallIntegerField(
        db_column='SOURCEINDEX',
        blank=True,
        null=True,
        help_text='Çıkış (kaynak) ambar numarası'
    )
    sourcewsref = models.ForeignKey(
        "LG_WORKSTAT",
        db_column='SOURCEWSREF',
        blank=True,
        null=True,
        help_text='Kaynak iş istasyonu ref. -> WORKSTAT',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_sourcewsref'
    )
    sourcepolnref = models.ForeignKey(
        "LG_DISPLINE",
        db_column='SOURCEPOLNREF',
        blank=True,
        null=True,
        help_text='Kaynak iş emri ref. -> DISPLINE',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_sourcepolnref'
    )
    sourcecostgrp = models.SmallIntegerField(
        db_column='SOURCECOSTGRP',
        blank=True,
        null=True,
        help_text='Kaynak ambar maliyet grubu'
    )
    desttype = models.SmallIntegerField(
        db_column='DESTTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Ambar'),
            (1, 'İş istasyonu')
        ],
        help_text="""
            Hedef türü;
            0 -> Ambar
            1 -> İş istasyonu
        """
    )
    destindex = models.SmallIntegerField(
        db_column='DESTINDEX',
        blank=True,
        null=True,
        help_text='Giriş (hedef) ambar numarası'
    )
    destwsref = models.ForeignKey(
        "LG_WORKSTAT",
        db_column='DESTWSREF',
        blank=True,
        null=True,
        help_text='Hedef iş istasyonu ref. -> WORKSTAT',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_destwsref'
    )
    destpolnref = models.ForeignKey(
        "LG_DISPLINE",
        db_column='DESTPOLNREF',
        blank=True,
        null=True,
        help_text='Hedef iş emri ref. -> DISPLINE',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_destpolnref'
    )
    destcostgrp = models.SmallIntegerField(
        db_column='DESTCOSTGRP',
        blank=True,
        null=True,
        help_text='Hedef ambar maliyet grubu'
    )
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika'
    )
    compbranch = models.SmallIntegerField(
        db_column='COMPBRANCH',
        blank=True,
        null=True,
        help_text='Giriş işyeri (Ambar fişleri)'
    )
    compdepartment = models.SmallIntegerField(
        db_column='COMPDEPARTMENT',
        blank=True,
        null=True,
        help_text='Giriş bölüm (Ambar fişleri)'
    )
    compfactory = models.SmallIntegerField(
        db_column='COMPFACTORY',
        blank=True,
        null=True,
        help_text='Giriş fabrika (Ambar fişleri)'
    )
    prodstat = models.SmallIntegerField(
        db_column='PRODSTAT',
        blank=True,
        null=True,
        choices=[
            (0, 'Güncel'),
            (1, 'Planlanan')
        ],
        help_text='Fiş durumu'
    )
    department = models.SmallIntegerField(
        db_column='DEPARTMENT',
        blank=True,
        null=True
    )

    devir = models.SmallIntegerField(db_column='DEVIR', blank=True,
        null=True, help_text='Devir (E/H)')
    billed = models.SmallIntegerField(db_column='BILLED',
        blank=True, null=True, help_text='Faturalanmış')
    updcurr = models.SmallIntegerField(db_column='UPDCURR',
        blank=True, null=True, help_text='İç kullanım')
    inuse = models.SmallIntegerField(db_column='INUSE',
        blank=True, null=True, help_text='Kullanılıyor (E/H)')
    invkind = models.SmallIntegerField(db_column='INVKIND',
        blank=True, null=True, help_text='Fatura türü')
    adddiscounts = models.FloatField(db_column='ADDDISCOUNTS',
        blank=True, null=True, help_text='Ek indirimler')
    totaldiscounts = models.FloatField(db_column='TOTALDISCOUNTS',
        blank=True, null=True, help_text='Toplam indirimler')
    totaldiscounted = models.FloatField(db_column='TOTALDISCOUNTED',
        blank=True, null=True, help_text='Satır indirimleri düşülmüş tutar')
    addexpenses = models.FloatField(db_column='ADDEXPENSES',
        blank=True, null=True, help_text='Ek masraflar')
    totalexpenses = models.FloatField(db_column='TOTALEXPENSES',
        blank=True, null=True, help_text='Toplam masraflar')
    totaldepozito = models.FloatField(db_column='TOTALDEPOZITO',
        blank=True, null=True, help_text='Toplam depozito')
    totalpromotions = models.FloatField(db_column='TOTALPROMOTIONS',
        blank=True, null=True, help_text='Toplam promosyonlar')
    totalvat = models.FloatField(db_column='TOTALVAT',
        blank=True, null=True, help_text='Toplam KDV')
    grosstotal = models.FloatField(db_column='GROSSTOTAL',
        blank=True, null=True, help_text='Toplam')
    nettotal = models.FloatField(db_column='NETTOTAL',
        blank=True, null=True, help_text='Net toplam')
    reportrate = models.FloatField(db_column='REPORTRATE',
        blank=True, null=True, help_text='Raporlama döviz kuru')
    reportnet = models.FloatField(db_column='REPORTNET',
        blank=True, null=True, help_text='Raporlama döviz tutarı')
    extenref = models.IntegerField(db_column='EXTENREF',
        blank=True, null=True, help_text='Ek dosya ref.')
    paydefref = models.ForeignKey(
        "LG_PAYPLANS",
        db_column='PAYDEFREF',
        blank=True,
        null=True,
        help_text='Ödeme planı ref. -> PAYPLANS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_paydefref"

    )
    fichecnt = models.SmallIntegerField(db_column='FICHECNT',
        blank=True, null=True, help_text='Faturalanın kaçıncı irsaliyesi')
    accficheref = models.ForeignKey(
        "LG_EMFICHE",
        db_column='ACCFICHEREF',
        blank=True,
        null=True,
        help_text='Muhasebe fişi ref. -> EMFICHE',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_accficheref"
    )
    cancelledacc = models.SmallIntegerField(db_column='CANCELLEDACC',
        blank=True, null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Muhasebeleştirme iptal')
    shptypcod = models.CharField(db_column='SHPTYPCOD', max_length=13,
        blank=True, null=True, help_text='Sevkiyet türü')
    shpagncod = models.CharField(db_column='SHPAGNCOD', max_length=13,
        blank=True, null=True, help_text='Taşıyıcı kodu')
    tracknr = models.CharField(db_column='TRACKNR', max_length=65,
        blank=True, null=True, help_text='Paket/Koli no')
    genexctyp = models.SmallIntegerField(db_column='GENEXCTYP',
        blank=True, null=True, help_text='Döviz türü (genel)')
    lineexctyp = models.SmallIntegerField(db_column='LINEEXCTYP',
        blank=True, null=True, help_text='Döviz türü (satır)')
    shipinforef = models.ForeignKey(
        "LG_SHIPINFO",
        db_column='SHIPINFOREF',
        blank=True,
        null=True,
        help_text='Teslimat bilgisi ref.',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_shipinforef"
    )
    distorderref = models.IntegerField(
        db_column='DISTORDERREF',
        blank=True,
        null=True,
        help_text='Dağıtım emri ref.',
    )
    sendcnt = models.SmallIntegerField(db_column='SENDCNT',
        blank=True, null=True, help_text='Gönderilenlerin sayısı')
    dlvclient = models.SmallIntegerField(db_column='DLVCLIENT',
        blank=True, null=True, help_text='Teslimat adresi müşteri tipi')
    doctrackingnr = models.CharField(db_column='DOCTRACKINGNR',
        max_length=21, blank=True, null=True, help_text='Belge izleme numarası')
    addtaxcalc = models.SmallIntegerField(db_column='ADDTAXCALC',
        blank=True, null=True, help_text='Hesaplanan ek vergi')
    totaladdtax = models.FloatField(db_column='TOTALADDTAX', blank=True,
        null=True, help_text='Ek vergi toplamı')
    ugirtrackingno = models.CharField(db_column='UGIRTRACKINGNO',
        max_length=17, blank=True, null=True,
        help_text='Üretimden giriş fişi bağlantılı izleme numarası')
    qprodfcref = models.IntegerField(db_column='QPRODFCREF',
        blank=True, null=True, help_text='Malzeme fişleri ref.')
    vaaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='VAACCREF',
        blank=True,
        null=True,
        help_text='Genel muhasebe hesapları ref.',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_vaaccref"
    )
    vacenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='VACENTERREF',
        blank=True,
        null=True,
        help_text='Masraf merkezi ref.',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_vacenterref"
    )
    orglogoid = models.CharField(db_column='ORGLOGOID', max_length=25,
        blank=True, null=True, help_text='Veri merkezi')
    fromexim = models.SmallIntegerField(db_column='FROMEXIM',
        blank=True, null=True, help_text='İthalat - ihracat ilişkisi')
    frgtypcod = models.CharField(db_column='FRGTYPCOD', max_length=13,
        blank=True, null=True,
        help_text='Nakliyet türü kodu (İthalat / İhracat)')
    trcurr = models.SmallIntegerField(db_column='TRCURR',
        blank=True, null=True, help_text='ID türü')
    trrate = models.FloatField(db_column='TRRATE', blank=True,
        null=True, help_text='ID kuru')
    trnet = models.FloatField(db_column='TRNET', blank=True,
        null=True, help_text='ID net tutar')
    eximwhfcref = models.IntegerField(db_column='EXIMWHFCREF',
        blank=True, null=True,
        help_text='İthalat / ihracat ambar fişi referansı')
    eximfctype = models.SmallIntegerField(db_column='EXIMFCTYPE',
        blank=True, null=True, help_text='İthalat / ihracat fiş türü')
    mainstfcref = models.IntegerField(db_column='MAINSTFCREF', blank=True,
        null=True, help_text='Ana malzeme fiş türü')
    fromordwithpay = models.SmallIntegerField(db_column='FROMORDWITHPAY',
        blank=True, null=True, help_text='Ödemeli / ödemesiz sipariş')
    wflowcrdref = models.IntegerField(db_column='WFLOWCRDREF',
        blank=True, null=True, help_text='İş akış kartı ref.')
    status = models.SmallIntegerField(db_column='STATUS',
        blank=True, null=True, help_text='Durum')
    updtrcurr = models.SmallIntegerField(db_column='UPDTRCURR',
        blank=True, null=True, help_text='Güncellenen işlem dövizi')
    totalexaddtax = models.FloatField(db_column='TOTALEXADDTAX',
        blank=True, null=True)
    affectcollatrl = models.SmallIntegerField(db_column='AFFECTCOLLATRL',
        blank=True, null=True)
    deductionpart1 = models.SmallIntegerField(db_column='DEDUCTIONPART1',
        blank=True, null=True)
    deductionpart2 = models.SmallIntegerField(db_column='DEDUCTIONPART2',
        blank=True, null=True)
    grpfirmtrans = models.SmallIntegerField(db_column='GRPFIRMTRANS',
        blank=True, null=True)
    affectrisk = models.SmallIntegerField(db_column='AFFECTRISK',
        blank=True, null=True)
    dispstatus = models.SmallIntegerField(db_column='DISPSTATUS',
        blank=True, null=True)
    approve = models.SmallIntegerField(db_column='APPROVE',
        blank=True, null=True)
    approvedate = models.DateTimeField(db_column='APPROVEDATE',
        blank=True, null=True)
    cantcrededuct = models.SmallIntegerField(db_column='CANTCREDEDUCT',
        blank=True, null=True)
    shipdate = models.DateTimeField(db_column='SHIPDATE',
        blank=True, null=True)
    shiptime = models.IntegerField(db_column='SHIPTIME',
        blank=True, null=True)
    entrustdevir = models.SmallIntegerField(db_column='ENTRUSTDEVIR',
        blank=True, null=True)
    reltransfcref = models.IntegerField(db_column='RELTRANSFCREF',
        blank=True, null=True)
    fromtransfer = models.SmallIntegerField(db_column='FROMTRANSFER',
        blank=True, null=True)
    globalid = models.CharField(db_column='GLOBALID', max_length=51,
        blank=True, null=True)
    compstfcref = models.IntegerField(db_column='COMPSTFCREF',
        blank=True, null=True)
    compinvref = models.IntegerField(db_column='COMPINVREF',
        blank=True, null=True)
    totalservices = models.FloatField(db_column='TOTALSERVICES',
        blank=True, null=True)
    campaigncode = models.CharField(db_column='CAMPAIGNCODE', max_length=25,
        blank=True, null=True)
    offerref = models.IntegerField(db_column='OFFERREF', blank=True,
        null=True)
    einvoicetyp = models.SmallIntegerField(db_column='EINVOICETYP',
        blank=True, null=True)
    einvoice = models.SmallIntegerField(db_column='EINVOICE',
        blank=True, null=True)
    nocalculate = models.SmallIntegerField(db_column='NOCALCULATE',
        blank=True, null=True)
    prodordertyp = models.SmallIntegerField(db_column='PRODORDERTYP',
        blank=True, null=True)
    qprodfctyp = models.SmallIntegerField(db_column='QPRODFCTYP',
        blank=True, null=True)
    printdate = models.DateTimeField(db_column='PRINTDATE',
        blank=True, null=True)
    prdordslplnreserve = models.SmallIntegerField(
        db_column='PRDORDSLPLNRESERVE', blank=True, null=True)
    controlinfo = models.SmallIntegerField(db_column='CONTROLINFO',
        blank=True, null=True)
    edespatch = models.SmallIntegerField(db_column='EDESPATCH',
        blank=True, null=True)
    docdate = models.DateTimeField(db_column='DOCDATE',
        blank=True, null=True)
    doctime = models.IntegerField(db_column='DOCTIME', blank=True, null=True)
    edespstatus = models.SmallIntegerField(db_column='EDESPSTATUS',
        blank=True, null=True)
    profileid = models.SmallIntegerField(db_column='PROFILEID',
        blank=True, null=True)
    deliverycode = models.CharField(db_column='DELIVERYCODE',
        max_length=11, blank=True, null=True)
    deststatus = models.SmallIntegerField(db_column='DESTSTATUS',
        blank=True, null=True)
    cancelexp = models.CharField(db_column='CANCELEXP', max_length=251,
        blank=True, null=True)
    undoexp = models.CharField(db_column='UNDOEXP', max_length=251,
        blank=True, null=True)
    canceldate = models.DateTimeField(db_column='CANCELDATE',
        blank=True, null=True)
    ataxexceptcode = models.CharField(db_column='ATAXEXCEPTCODE',
        max_length=11, blank=True, null=True)
    vatexceptreason = models.CharField(db_column='VATEXCEPTREASON',
        max_length=201, blank=True, null=True)
    taxfreechx = models.SmallIntegerField(db_column='TAXFREECHX', blank=True,
        null=True)
    ataxexceptreason = models.CharField(db_column='ATAXEXCEPTREASON',
        max_length=201, blank=True, null=True)
    publicbnaccref = models.IntegerField(db_column='PUBLICBNACCREF',
        blank=True, null=True)
    createwhere = models.SmallIntegerField(db_column='CREATEWHERE',
        blank=True, null=True)
    vatexceptcode = models.CharField(db_column='VATEXCEPTCODE',
        max_length=11, blank=True, null=True)
    accepteinvpublic = models.SmallIntegerField(db_column='ACCEPTEINVPUBLIC',
        blank=True, null=True)
    mntorderfref = models.IntegerField(db_column='MNTORDERFREF', blank=True,
        null=True)
    printeddespfcno = models.CharField(db_column='PRINTEDDESPFCNO',
        max_length=17, blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (
            ('grpcode', 'trcode', 'ficheno'),
            ('trcode', 'ficheno'),
            ('orglogicref', 'logicalref', 'siteid'),
        )
        db_table = f'LG_{Active.namespace}_{Active.period}_STFICHE'
        target_db = 'erp'
