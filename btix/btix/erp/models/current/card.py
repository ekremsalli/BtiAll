"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class BankGroup(models.Model):
    bankbranchs1 = models.CharField(db_column='BANKBRANCHS1', max_length=17,
        blank=True, null=True, help_text='Banka şube numarası (1)')
    bankbranchs2 = models.CharField(db_column='BANKBRANCHS2', max_length=17,
        blank=True, null=True, help_text='Banka şube numarası (2)')
    bankaccounts1 = models.CharField(db_column='BANKACCOUNTS1', max_length=51,
        blank=True, null=True, help_text='Banka hesabı numarası (1)')
    bankaccounts2 = models.CharField(db_column='BANKACCOUNTS2', max_length=51,
        blank=True, null=True, help_text='Banka hesabı numarası (2)')
    banknames1 = models.CharField(db_column='BANKNAMES1', max_length=51,
        blank=True, null=True)
    banknames2 = models.CharField(db_column='BANKNAMES2', max_length=51,
        blank=True, null=True)
    bankibans1 = models.CharField(db_column='BANKIBANS1', max_length=51,
        blank=True, null=True)
    bankibans2 = models.CharField(db_column='BANKIBANS2', max_length=51,
        blank=True, null=True)
    bankbics1 = models.CharField(db_column='BANKBICS1', max_length=25,
        blank=True, null=True)
    bankbics2 = models.CharField(db_column='BANKBICS2', max_length=25,
        blank=True, null=True)
    bankbcurrency1 = models.CharField(db_column='BANKBCURRENCY1', max_length=4,
        blank=True, null=True)
    bankbcurrency2 = models.CharField(db_column='BANKBCURRENCY2', max_length=4,
        blank=True, null=True)
    dbslimit1 = models.FloatField(db_column='DBSLIMIT1', blank=True, null=True)
    dbslimit2 = models.FloatField(db_column='DBSLIMIT2', blank=True, null=True)
    dbstotal1 = models.FloatField(db_column='DBSTOTAL1', blank=True, null=True)
    dbstotal2 = models.FloatField(db_column='DBSTOTAL2', blank=True, null=True)
    dbsbankno1 = models.SmallIntegerField(db_column='DBSBANKNO1', blank=True,
        null=True)
    dbsbankno2 = models.SmallIntegerField(db_column='DBSBANKNO2', blank=True,
        null=True)
    dbsriskcntrl1 = models.SmallIntegerField(db_column='DBSRISKCNTRL1',
        blank=True, null=True)
    dbsriskcntrl2 = models.SmallIntegerField(db_column='DBSRISKCNTRL2',
        blank=True, null=True)
    dbsbankcurrency1 = models.SmallIntegerField(db_column='DBSBANKCURRENCY1',
        blank=True, null=True)
    dbsbankcurrency2 = models.SmallIntegerField(db_column='DBSBANKCURRENCY2',
        blank=True, null=True)
    bankcorrpacc1 = models.CharField(db_column='BANKCORRPACC1', max_length=51,
        blank=True, null=True)
    bankcorrpacc2 = models.CharField(db_column='BANKCORRPACC2', max_length=51,
        blank=True, null=True)
    bankvoen1 = models.CharField(db_column='BANKVOEN1', max_length=51,
        blank=True, null=True)
    bankvoen2 = models.CharField(db_column='BANKVOEN2', max_length=51,
        blank=True, null=True)

    class Meta:
        abstract = True

class LG_CLCARD(
    BaseLogical,
    BaseActive,
    LowLevelCodes10,
    BankGroup,
    BaseCode,
    BaseSiteRec,
    BaseInfo,
    BaseAddress,
    BaseContact,
    BaseTrading,
    BaseWF,
    BasePayment,
    BaseTax,
    BaseBlocked,
    BaseTextINC,
    BaseRef,
    models.Model):
    """
        Cari hesap kartı
        CLCARD tablosunda firmanın çalıştığı alıcı ve satıcı firmalar ile
        borç / alacak ilişkisi içinde olduğu diğer firmaları düzenli
        olarak izlemek için gerekli olan cari hesap kartları bilgileri
        bulunmaktadır.
            Cari hesap toplamlarına ulaşmak için CLTOTFIL,
            Cari hesap istihbarat bilgilerine ulaşmak için CLINTEL
            Cari hesap risk bilgilerine ulaşmal için CLRNUMS
            Cari hesap hareklerine ulaşmak için ise CLFLINE tabloları
                okunmalıdır.
    """
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True,
        help_text='Cari hesap kart türü'
    )
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=17,
        blank=True,
        null=True,
        help_text='Cari hesap kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=201,
        blank=True,
        null=True,
        help_text='Cari hesap ünvanı'
    )
    incharge = models.CharField(
        db_column='INCHARGE',
        max_length=21,
        blank=True,
        null=True,
        help_text='İlgili'
    )
    discrate = models.FloatField(
        db_column='DISCRATE',
        blank=True,
        null=True,
        help_text='İndirim yüzdesi'
    )
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ekstra dosya ref.'
    )
    webaddr = models.CharField(
        db_column='WEBADDR',
        max_length=101,
        blank=True,
        null=True,
        help_text='WEB adresi'
    )
    warnmethod = models.SmallIntegerField(
        db_column='WARNMETHOD',
        blank=True,
        null=True,
        help_text='İhtar metodu'
    )
    warnemailaddr = models.CharField(
        db_column='WARNEMAILADDR',
        max_length=251,
        blank=True,
        null=True,
        help_text='E-posta adresi (İhtar)'
    )
    warnfaxnr = models.CharField(
        db_column='WARNFAXNR',
        max_length=16,
        blank=True,
        null=True,
        help_text='Faks numarası (İhtar)'
    )
    clanguage = models.SmallIntegerField(
        db_column='CLANGUAGE',
        blank=True,
        null=True,
        help_text='Yazışma dili'
    )
    deliverymethod = models.CharField(
        db_column='DELIVERYMETHOD',
        max_length=13,
        blank=True,
        null=True,
        help_text='Sevkiyat yöntemi'
    )
    deliveryfirm = models.CharField(
        db_column='DELIVERYFIRM',
        max_length=13,
        blank=True,
        null=True,
        help_text='Taşıyıcı firma'
    )
    ccurrency = models.SmallIntegerField(
        db_column='CCURRENCY',
        blank=True,
        null=True,
        help_text='Döviz türü'
    )
    edino = models.CharField(
        db_column='EDINO',
        max_length=25,
        blank=True,
        null=True,
        help_text='Veri aktarım no'
    )
    paymentproc = models.SmallIntegerField(
        db_column='PAYMENTPROC',
        blank=True,
        null=True,
        choices=[
            (0, 'Döviz'),
            (1, 'Karma')
        ],
        help_text='Borç izleme; 0 -> Döviz, 1-> Karma'
    )
    cratediffproc = models.SmallIntegerField(db_column='CRATEDIFFPROC',
        blank=True, null=True, help_text='Belirsiz')
    ppgroupcode = models.CharField(db_column='PPGROUPCODE', max_length=17,
        blank=True, null=True, help_text='Ödeme planları grup kodu')
    ppgroupref = models.IntegerField(db_column='PPGROUPREF', blank=True,
        null=True, help_text='Ödeme planı grup kodu')
    taxoffcode = models.CharField(db_column='TAXOFFCODE', max_length=31,
        blank=True, null=True, help_text='Vergi dairesi kodu')
    towncode = models.CharField(db_column='TOWNCODE', max_length=13,
        blank=True, null=True, help_text='İlçe kodu')
    districtcode = models.CharField(db_column='DISTRICTCODE', max_length=13,
        blank=True, null=True, help_text='Semt kodu')
    citycode = models.CharField(db_column='CITYCODE', max_length=13,
        blank=True, null=True, help_text='Şehir kodu')
    countrycode = models.CharField(db_column='COUNTRYCODE', max_length=13,
        blank=True, null=True, help_text='Ülke kodu')
    ordsendmethod = models.SmallIntegerField(db_column='ORDSENDMETHOD',
        blank=True, null=True, help_text='Sipariş formu gönderim metodu')
    ordsendemailaddr = models.CharField(db_column='ORDSENDEMAILADDR',
        max_length=251, blank=True, null=True,
        help_text='Sipariş formu gönderimi (E-posta ile)')
    ordsendfaxnr = models.CharField(db_column='ORDSENDFAXNR', max_length=16,
        blank=True, null=True, help_text='Sipariş formu gönderimi (faks ile)')
    dspsendmethod = models.SmallIntegerField(db_column='DSPSENDMETHOD',
        blank=True, null=True, help_text='İrsaliye form gönderimi metodu')
    dspsendemailaddr = models.CharField(db_column='DSPSENDEMAILADDR',
        max_length=251, blank=True, null=True,
        help_text='İrsaliye form gönderdimi (E-posta ile)')
    dspsendfaxnr = models.CharField(db_column='DSPSENDFAXNR', max_length=16,
        blank=True, null=True, help_text='İrsaliye form gönderimi (Faks ile)')
    invsendmethod = models.SmallIntegerField(db_column='INVSENDMETHOD',
        blank=True, null=True, help_text='Fatura gönderim metodu')
    invsendemailaddr = models.CharField(db_column='INVSENDEMAILADDR',
        max_length=251, blank=True, null=True,
        help_text='Fatura gönderimi (E-posta ile)')
    invsendfaxnr = models.CharField(db_column='INVSENDFAXNR', max_length=16,
        blank=True, null=True, help_text='Fatura gönderimi (Faks ile)')
    subscriberstat = models.SmallIntegerField(db_column='SUBSCRIBERSTAT',
        blank=True, null=True, help_text='Abone durumu')
    subscriberext = models.CharField(db_column='SUBSCRIBEREXT', max_length=17,
        blank=True, null=True, help_text='Abone ek bilgi')
    autopaidbank = models.CharField(db_column='AUTOPAIDBANK', max_length=25,
        blank=True, null=True, help_text='Otomatik ödeme banka kodu')
    paymenttype = models.SmallIntegerField(db_column='PAYMENTTYPE',
        blank=True, null=True, help_text='Ödeme türü')
    lastsendremlev = models.IntegerField(db_column='LASTSENDREMLEV',
        blank=True, null=True, help_text='İhtar işlemleri seviyesi')
    extaccessflags = models.IntegerField(
        db_column='EXTACCESSFLAGS',
        blank=True,
        null=True,
        choices=[
            (1, 'E-iş ortamında erişebilir'),
            (2, 'Satış noktalarında erişebilir')
        ],
        help_text="""
            1 -> E-iş ortamında erişebilir
            2 -> Satış noktalarında erişebilir
        """
    )
    ordsendformat = models.SmallIntegerField(db_column='ORDSENDFORMAT',
        blank=True, null=True, help_text='Sipariş formu gönderim formatı')
    dspsendformat = models.SmallIntegerField(db_column='DSPSENDFORMAT',
        blank=True, null=True, help_text='İrsaliye formu gönderim formatı')
    invsendformat = models.SmallIntegerField(db_column='INVSENDFORMAT',
        blank=True, null=True, help_text='Fatura gönderim formatı')
    remsendformat = models.SmallIntegerField(db_column='REMSENDFORMAT',
        blank=True, null=True, help_text='İhtar formu gönderim formatı')
    storecreditcardno = models.CharField(db_column='STORECREDITCARDNO',
        max_length=17, blank=True, null=True,
        help_text='Mahaza kredi kartı numarası')
    clordfreq = models.SmallIntegerField(db_column='CLORDFREQ', blank=True,
        null=True, help_text='Sipariş sıklığı (gün)')
    ordday = models.SmallIntegerField(db_column='ORDDAY', blank=True,
        null=True, help_text='Sipariş günleri')
    logoid = models.CharField(db_column='LOGOID', max_length=25,
        blank=True, null=True, help_text='Logo ID')
    lidconfirmed = models.SmallIntegerField(db_column='LIDCONFIRMED',
        blank=True, null=True,
        help_text="Logo ID onaylansın mı?(Evet / Hayır)")
    expregno = models.CharField(db_column='EXPREGNO', max_length=25,
        blank=True, null=True, help_text="İhracat birlik plaka numarası")
    expdocno = models.CharField(db_column='EXPDOCNO', max_length=33,
        blank=True, null=True, help_text="İhracat belge numarası")
    expbustypref = models.IntegerField(db_column='EXPBUSTYPREF', blank=True,
        null=True, help_text="İhracat liman izni")
    invprintcnt = models.SmallIntegerField(db_column='INVPRINTCNT',
        blank=True, null=True, help_text="Fatura basım sayısı")
    pieceordinflict = models.SmallIntegerField(db_column='PIECEORDINFLICT',
        blank=True, null=True, help_text="Parçalı sipariş teslimatı")
    collectinvoicing = models.SmallIntegerField(db_column='COLLECTINVOICING',
        blank=True, null=True, help_text="Toplu faturalam")
    ebusdatasendtype = models.SmallIntegerField(db_column='EBUSDATASENDTYPE',
        blank=True, null=True,
        help_text="E-İş veri gönderim bilgileri")
    inistatusflags = models.IntegerField(db_column='INISTATUSFLAGS',
        blank=True, null=True,
        help_text="Banka fişi ve satış faturaları için öndeğer")
    slsorderstatus = models.SmallIntegerField(db_column='SLSORDERSTATUS',
        blank=True, null=True,
        help_text="""
            Cari hesaptan LDX aracılığıyla gelen sipariş
            hareketlerinin içeriye hangi statüde alınacağını belirler
        """
    )
    slsorderprice = models.SmallIntegerField(db_column='SLSORDERPRICE',
        blank=True, null=True)
    ltrsendmethod = models.SmallIntegerField(db_column='LTRSENDMETHOD',
        blank=True, null=True, help_text="Mektup yollama metodu")
    ltrsendemailaddr = models.CharField(db_column='LTRSENDEMAILADDR',
        max_length=251, blank=True, null=True, help_text="E-posta adresi")
    ltrsendfaxnr = models.CharField(db_column='LTRSENDFAXNR', max_length=16,
        blank=True, null=True, help_text="Faks numarası")
    ltrsendformat = models.SmallIntegerField(db_column='LTRSENDFORMAT',
        blank=True, null=True, help_text="Mektup yollama formatı")
    imageinc = models.SmallIntegerField(db_column='IMAGEINC',
        blank=True, null=True, help_text="Resim")
    cellphone = models.CharField(db_column='CELLPHONE', max_length=18,
        blank=True, null=True, help_text="GSM numarası")
    sameitemcodeuse = models.SmallIntegerField(db_column='SAMEITEMCODEUSE',
        blank=True, null=True, help_text="Aynı malzeme kodları kullanılacak")
    statecode = models.CharField(db_column='STATECODE', max_length=13,
        blank=True, null=True, help_text="Eyalet kodu")
    statename = models.CharField(db_column='STATENAME', max_length=41,
        blank=True, null=True, help_text="Eyalet ismi")
    wflowcrdref = models.IntegerField(db_column='WFLOWCRDREF',
        blank=True, null=True, help_text="İş akı kartı ref.")
    parentclref = models.IntegerField(db_column='PARENTCLREF', blank=True,
        null=True)
    telcodes1 = models.CharField(db_column='TELCODES1', max_length=9,
        blank=True, null=True)
    telcodes2 = models.CharField(db_column='TELCODES2', max_length=9,
        blank=True, null=True)
    faxcode = models.CharField(db_column='FAXCODE', max_length=9,
        blank=True, null=True)
    purchbrws = models.SmallIntegerField(db_column='PURCHBRWS',
        blank=True, null=True)
    salesbrws = models.SmallIntegerField(db_column='SALESBRWS',
        blank=True, null=True)
    impbrws = models.SmallIntegerField(db_column='IMPBRWS',
        blank=True, null=True)
    expbrws = models.SmallIntegerField(db_column='EXPBRWS',
        blank=True, null=True)
    finbrws = models.SmallIntegerField(db_column='FINBRWS',
        blank=True, null=True)
    orglogoid = models.CharField(db_column='ORGLOGOID', max_length=25,
        blank=True, null=True)
    addtoreflist = models.SmallIntegerField(db_column='ADDTOREFLIST',
        blank=True, null=True)
    textreftr = models.SmallIntegerField(db_column='TEXTREFTR',
        blank=True, null=True)
    tckno = models.CharField(db_column='TCKNO', max_length=16, blank=True,
        null=True)
    isperscomp = models.SmallIntegerField(db_column='ISPERSCOMP', blank=True,
        null=True)
    cashref = models.IntegerField(db_column='CASHREF', blank=True, null=True)
    usedinperiods = models.SmallIntegerField(db_column='USEDINPERIODS',
        blank=True, null=True)
    accepteinv = models.SmallIntegerField(db_column='ACCEPTEINV',
        blank=True, null=True)
    einvoiceid = models.CharField(db_column='EINVOICEID', max_length=41,
        blank=True, null=True)
    profileid = models.SmallIntegerField(db_column='PROFILEID',
        blank=True, null=True)
    purcorderstatus = models.SmallIntegerField(db_column='PURCORDERSTATUS',
        blank=True, null=True)
    purcorderprice = models.SmallIntegerField(db_column='PURCORDERPRICE',
        blank=True, null=True)
    isforeign = models.SmallIntegerField(db_column='ISFOREIGN', blank=True,
        null=True)
    einvoicetype = models.SmallIntegerField(db_column='EINVOICETYPE',
        blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=31,
        blank=True, null=True)
    surname = models.CharField(db_column='SURNAME',
        max_length=31, blank=True, null=True)
    ispercurr = models.SmallIntegerField(db_column='ISPERCURR',
        blank=True, null=True)
    einvoicetyp = models.SmallIntegerField(db_column='EINVOICETYP',
        blank=True, null=True)

    acceptedesp = models.SmallIntegerField(
        db_column='ACCEPTEDESP', blank=True, null=True)
    profileiddesp = models.SmallIntegerField(
        db_column='PROFILEIDDESP', blank=True, null=True)


    class Meta:
        managed = False
        unique_together = (
            ('active', 'code'),
            (
                'lowlevelcodes1',
                'lowlevelcodes2',
                'lowlevelcodes3',
                'lowlevelcodes4',
                'lowlevelcodes5',
                'lowlevelcodes6',
                'lowlevelcodes7',
                'logicalref'
            ),
            ('purchbrws', 'active', 'code'),
            ('salesbrws', 'active', 'code'),
            ('impbrws', 'active', 'code'),
            ('expbrws', 'active', 'code'),
            ('finbrws', 'active', 'code'),
        )
        db_table = f'LG_{Active.namespace}_CLCARD'
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.definition_field}"

    # rel -> L_PAYPLAN, L_PERMFILE, L_WFTASK
