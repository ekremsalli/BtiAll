"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_CHARASGN(
    BaseLogical,
    BaseItem,
    BasePriority,
    models.Model):
    """
        Malzeme özellik ataması
    """
    charcoderef = models.ForeignKey(
        'LG_CHARCODE',
        db_column='CHARCODEREF',
        blank=True,
        null=True,
        help_text='Malzeme özellik kodu ref.',
        on_delete=models.DO_NOTHING
    )
    charvalref = models.ForeignKey(
        'LG_CHARVAL',
        db_column='CHARVALREF',
        blank=True,
        null=True,
        help_text='Malzeme özellik değeri ref.',
        on_delete=models.DO_NOTHING
    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    matrixloc = models.SmallIntegerField(
        db_column='MATRIXLOC',
        blank=True, null=True,
        choices=[
            (0, 'Satır'),
            (1, 'Sütun')
        ],
        help_text='Matris stok yeri bilgisi; 0-> Satır, 1-> Sütun'
    )

    class Meta:
        managed = False
        unique_together = (
            ('itemref', 'charcoderef', 'charvalref'),
            ('charcoderef', 'charvalref', 'itemref'),
            ('charvalref', 'charcoderef', 'itemref'),
            ('charcoderef', 'itemref', 'charvalref'),
        )
        db_table = f'LG_{Active.namespace}_CHARASGN'
        target_db = 'erp'

class LG_CHARCODE(
    BaseLogical,
    BaseCode,
    BaseSiteRec,
    BaseTextINC,
    BaseInfo,
    BaseWF,
    BaseGUID,
    BaseApproved,
    BaseRef,
    models.Model):
    """
        Özellik kodları
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=25,
        blank=True,
        null=True,
        help_text='Özellik kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Özellik açıklaması'
    )
    name2 = models.CharField(db_column='NAME2', max_length=201, blank=True,
        null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_CHARCODE'
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"

class LG_CHARVAL(
    BaseLogical,
    models.Model):
    """
        Özellik değerleri
    """
    charcoderef = models.IntegerField(
        db_column='CHARCODEREF',
        blank=True,
        null=True,
        help_text='Özellik kodu ref.'
    )
    valno = models.IntegerField(
        db_column='VALNO',
        blank=True,
        null=True,
        help_text='Değer numarası'
    )
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Değer kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Değer açıklaması'
    )
    name2 = models.CharField(
        db_column='NAME2',
        max_length=201,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        unique_together = (('charcoderef', 'code'),)
        db_table = f'LG_{Active.namespace}_CHARVAL'
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"

class LG_ITEMS(
    BaseLogical,
    BasePayment,
    BaseWFlowTask,
    BaseVAT,
    BaseAddTax,
    BaseApproved,
    LowLevelCodes10,
    BaseWF,
    BaseInfo,
    BaseSiteRec,
    BaseTextINC,
    BaseCode,
    BaseActive,
    BaseRef,
    models.Model):
    """
        Malzemeler
    """
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Ticari mal'),
            (2, 'Karma koli'),
            (3, 'Depozitolu mal'),
            (4, 'Sabit kıymet'),
            (10, 'Hammadde'),
            (11, 'Yarımamül'),
            (12, 'Mamül'),
            (13, 'Tüketim malı'),
            (20, 'M. sınıfı (genel)'),
            (21, 'M. sınıfı (tablolu)'),
            (22, 'Firma dosyaları oluşturulurken default olarak eklenen malzeme sınıfı')
        ],
        help_text='Kart türü'
    )
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=25,
        blank=True,
        null=True,
        help_text='Malzeme kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Malzeme açıklaması'
    )
    stgrpcode = models.CharField(
        db_column='STGRPCODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Malzeme grup kodu'
    )
    producercode = models.CharField(
        db_column='PRODUCERCODE',
        max_length=101,
        blank=True,
        null=True,
        help_text='Üretici kodu'
    )
    classtype = models.SmallIntegerField(
        db_column='CLASSTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Malzeme'),
            (20, 'Malzeme sınıfı')
        ],
        help_text='Sınıf tipi'
    )
    purchbrws = models.SmallIntegerField(
        db_column='PURCHBRWS',
        blank=True,
        null=True,
        help_text='Kullanım yeri satınalma'
    )
    salesbrws = models.SmallIntegerField(
        db_column='SALESBRWS',
        blank=True,
        null=True,
        help_text='Kullanım yeri satış'
    )
    mtrlbrws = models.SmallIntegerField(
        db_column='MTRLBRWS',
        blank=True,
        null=True,
        help_text='Kullanım yeri malzeme yönetimi'
    )
    tracktype = models.SmallIntegerField(
        db_column='TRACKTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'İzleme yapılmayacak'),
            (1, 'Lot(parti) numarası'),
            (2, 'Seri numarası')
        ],
        help_text='İzleme yöntemi'
    )
    loctracking = models.SmallIntegerField(
        db_column='LOCTRACKING',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text='Stok yeri takibi'
    )
    tool = models.SmallIntegerField(
        db_column='TOOL',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text='Araç'
    )
    autoincsl = models.SmallIntegerField(
        db_column='AUTOINCSL',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text='Lot / seri no otomatik arttırılacak'
    )
    divlotsize = models.SmallIntegerField(
        db_column='DIVLOTSIZE',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text='Lot büyüklükleri bölünebilir'
    )
    shelflife = models.FloatField(
        db_column='SHELFLIFE',
        blank=True,
        null=True,
        help_text='Raf ömrü'
    )
    shelfdate = models.SmallIntegerField(
        db_column='SHELFDATE',
        blank=True,
        null=True,
        choices=[
            (0, 'Gün'),
            (1, 'Hafta'),
            (2, 'Ay'),
            (3, 'Yıl')
        ],
        help_text='Raf ömür periyotu'
    )
    dominantrefs1 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS1',
        blank=True,
        null=True,
        help_text='Genel bilgileri kullanılan üst malzeme sınıfı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs1"
    )
    dominantrefs2 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS2',
        blank=True,
        null=True,
        help_text='Ambar parametreleri kullanılan üst malzeme sınıfı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs2"
    )
    dominantrefs3 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS3',
        blank=True,
        null=True,
        help_text='Fabrika parametreleri kullanılan üst malzeme sınıfı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs3"
    )
    dominantrefs4 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS4',
        blank=True,
        null=True,
        help_text='İş istasyonu parametreleri kullanılan üst malzeme sınıfı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs4"
    )
    dominantrefs5 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS5',
        blank=True,
        null=True,
        help_text='Birimleri kullanılan üst malzeme sınıfı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs5"
    )
    dominantrefs6 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS6',
        blank=True,
        null=True,
        help_text='Fiyatları kullanılan üst malzeme sınıfı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs6"
    )
    dominantrefs7 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS7',
        blank=True,
        null=True,
        help_text='(kullanılmıyor)',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs7"
    )
    dominantrefs8 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS8',
        blank=True,
        null=True,
        help_text='Müşteri / tedarikçi bağlantıları kullanılan üst malzeme sınıfı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs8"
    )
    dominantrefs9 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS9',
        blank=True,
        null=True,
        help_text='Muhasebe kodları kullanılan üst malzeme sınıfı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs9"
    )
    dominantrefs10 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS10',
        blank=True,
        null=True,
        help_text='Kalite kontrol kriterleri kullanılan üst malzeme sınıfı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs10"
    )
    dominantrefs11 = models.ForeignKey(
        "LG_ITEMS",
        db_column='DOMINANTREFS11',
        blank=True,
        null=True,
        help_text='Ürün reçetesi ilişkisi kullanılan üst malzeme sınıfı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_dominantrefs11"
    )
    dominantrefs12 = models.IntegerField(
        db_column='DOMINANTREFS12',
        blank=True,
        null=True,
        help_text='(kullanılmıyor)'
    )
    imageinc = models.SmallIntegerField(
        db_column='IMAGEINC',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text='Resim var'
    )
    deprtype = models.SmallIntegerField(
        db_column='DEPRTYPE',
        blank=True,
        null=True,
        help_text='Amortisman türü'
    )
    deprrate = models.FloatField(
        db_column='DEPRRATE',
        blank=True,
        null=True,
        help_text='Amortisman oranı'
    )
    deprdur = models.SmallIntegerField(
        db_column='DEPRDUR',
        blank=True,
        null=True,
        help_text='Amortisman süresi'
    )
    salvageval = models.FloatField(
        db_column='SALVAGEVAL',
        blank=True,
        null=True,
        help_text='Hurda değeri'
    )
    revalflag = models.SmallIntegerField(
        db_column='REVALFLAG',
        blank=True,
        null=True,
        help_text='Değerlenebilir'
    )
    revdeprflag = models.SmallIntegerField(
        db_column='REVDEPRFLAG',
        blank=True,
        null=True,
        help_text='Değerleme amortismanı'
    )
    partdep = models.SmallIntegerField(
        db_column='PARTDEP',
        blank=True,
        null=True,
        help_text='Kıst. amortisman durumu'
    )
    deprtype2 = models.SmallIntegerField(
        db_column='DEPRTYPE2',
        blank=True,
        null=True,
        help_text='Ulusal amortisman türü'
    )
    deprrate2 = models.FloatField(
        db_column='DEPRRATE2',
        blank=True,
        null=True,
        help_text='Ulusal amortisman oranı'
    )
    deprdur2 = models.SmallIntegerField(
        db_column='DEPRDUR2',
        blank=True,
        null=True,
        help_text='Ulusal amortisman süresi'
    )
    revalflag2 = models.SmallIntegerField(
        db_column='REVALFLAG2',
        blank=True,
        null=True,
        help_text='Ulusal değerleme'
    )
    revdeprflag2 = models.SmallIntegerField(
        db_column='REVDEPRFLAG2',
        blank=True,
        null=True,
        help_text='Ulusal değerleme amortismanı'
    )
    partdep2 = models.SmallIntegerField(
        db_column='PARTDEP2',
        blank=True,
        null=True,
        help_text='Ulusal kıst. amortisman'
    )
    unitsetref = models.ForeignKey(
        "LG_UNITSETF",
        db_column='UNITSETREF',
        blank=True,
        null=True,
        help_text='Birim seti kaydı ref. -> UNITSETF',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_unitsetref"
    )
    qccsetref = models.ForeignKey(
        "LG_QCSET",
        db_column='QCCSETREF',
        blank=True,
        null=True,
        help_text='KKK seti ref. -> QCSET',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_qccsetref"
    )
    distamount = models.FloatField(
        db_column='DISTAMOUNT',
        blank=True,
        null=True,
        help_text='Tablolu malz. sınıfı dağıtım miktarı'
    )
    univid = models.CharField(
        db_column='UNIVID',
        max_length=25,
        blank=True,
        null=True,
        help_text='Kayıt kodu (yabancı dil)'
    )
    distlotunits = models.SmallIntegerField(
        db_column='DISTLOTUNITS',
        blank=True,
        null=True,
        help_text='Lot birimleri dağıtılabilir'
    )
    comblotunits = models.SmallIntegerField(
        db_column='COMBLOTUNITS',
        blank=True,
        null=True,
        help_text='Lot birimleri birleştirebilir'
    )
    distpoint = models.FloatField(
        db_column='DISTPOINT',
        blank=True,
        null=True,
        help_text='Dağıtım noktası'
    )
    camppoint = models.FloatField(
        db_column='CAMPPOINT',
        blank=True,
        null=True,
        help_text='Campaign point'
    )
    canuseintrns = models.SmallIntegerField(
        db_column='CANUSEINTRNS',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text='This can be used in transactions'
    )
    isonr = models.CharField(
        db_column='ISONR',
        max_length=11,
        blank=True,
        null=True,
        help_text='ISO numarası'
    )
    groupnr = models.CharField(
        db_column='GROUPNR', max_length=9, blank=True, null=True)
    prodcountry = models.CharField(
        db_column='PRODCOUNTRY', max_length=13, blank=True, null=True)
    qprodamnt = models.FloatField(
        db_column='QPRODAMNT', blank=True, null=True)
    qproduom = models.IntegerField(
        db_column='QPRODUOM', blank=True, null=True)
    qprodsrcindex = models.SmallIntegerField(
        db_column='QPRODSRCINDEX', blank=True, null=True)
    extaccessflags = models.IntegerField(
        db_column='EXTACCESSFLAGS', blank=True, null=True)
    packet = models.SmallIntegerField(
        db_column='PACKET', blank=True, null=True)
    salvageval2 = models.FloatField(
        db_column='SALVAGEVAL2', blank=True, null=True)
    sellvat = models.FloatField(
        db_column='SELLVAT', blank=True, null=True)
    returnvat = models.FloatField(
        db_column='RETURNVAT', blank=True, null=True)
    logoid = models.CharField(
        db_column='LOGOID', max_length=25, blank=True, null=True)
    lidconfirmed = models.SmallIntegerField(
        db_column='LIDCONFIRMED', blank=True, null=True)
    gtipcode = models.CharField(
        db_column='GTIPCODE', max_length=25, blank=True, null=True)
    expctgno = models.CharField(
        db_column='EXPCTGNO', max_length=25, blank=True, null=True)
    b2ccode = models.CharField(
        db_column='B2CCODE', max_length=25, blank=True, null=True)
    markref = models.IntegerField(db_column='MARKREF', blank=True, null=True)
    image2inc = models.SmallIntegerField(
        db_column='IMAGE2INC', blank=True, null=True)
    avrwhduration = models.FloatField(
        db_column='AVRWHDURATION', blank=True, null=True)
    extcardflags = models.IntegerField(
        db_column='EXTCARDFLAGS',
        blank=True,
        null=True)
    minordamount = models.FloatField(
        db_column='MINORDAMOUNT',
        blank=True, null=True)
    freightplace = models.CharField(
        db_column='FREIGHTPLACE',
        max_length=51, blank=True, null=True)
    freighttypcode1 = models.CharField(
        db_column='FREIGHTTYPCODE1', max_length=13, blank=True, null=True)
    freighttypcode2 = models.CharField(
        db_column='FREIGHTTYPCODE2', max_length=13, blank=True, null=True)
    freighttypcode3 = models.CharField(
        db_column='FREIGHTTYPCODE3', max_length=13, blank=True, null=True)
    freighttypcode4 = models.CharField(
        db_column='FREIGHTTYPCODE4', max_length=13, blank=True, null=True)
    freighttypcode5 = models.CharField(
        db_column='FREIGHTTYPCODE5', max_length=13, blank=True, null=True)
    freighttypcode6 = models.CharField(
        db_column='FREIGHTTYPCODE6', max_length=13, blank=True, null=True)
    freighttypcode7 = models.CharField(
        db_column='FREIGHTTYPCODE7', max_length=13, blank=True, null=True)
    freighttypcode8 = models.CharField(
        db_column='FREIGHTTYPCODE8', max_length=13, blank=True, null=True)
    freighttypcode9 = models.CharField(
        db_column='FREIGHTTYPCODE9', max_length=13, blank=True, null=True)
    freighttypcode10 = models.CharField(
        db_column='FREIGHTTYPCODE10', max_length=13, blank=True, null=True)
    statecode = models.CharField(
        db_column='STATECODE', max_length=13, blank=True, null=True)
    statename = models.CharField(
        db_column='STATENAME', max_length=41, blank=True, null=True)
    expcategory = models.CharField(
        db_column='EXPCATEGORY', max_length=25, blank=True, null=True)
    lostfactor = models.FloatField(
        db_column='LOSTFACTOR', blank=True, null=True)
    textinceng = models.SmallIntegerField(
        db_column='TEXTINCENG', blank=True, null=True)
    eanbarcode = models.CharField(
        db_column='EANBARCODE', max_length=25, blank=True, null=True)
    deprclasstype = models.CharField(
        db_column='DEPRCLASSTYPE', max_length=31, blank=True, null=True)
    sellprvat = models.FloatField(
        db_column='SELLPRVAT', blank=True, null=True)
    returnprvat = models.FloatField(
        db_column='RETURNPRVAT', blank=True, null=True)
    orglogoid = models.CharField(
        db_column='ORGLOGOID', max_length=25, blank=True, null=True)
    qproddepart = models.SmallIntegerField(
        db_column='QPRODDEPART', blank=True, null=True)
    canconfigure = models.SmallIntegerField(
        db_column='CANCONFIGURE', blank=True, null=True)
    charsetref = models.IntegerField(
        db_column='CHARSETREF', blank=True, null=True)
    candeduct = models.SmallIntegerField(
        db_column='CANDEDUCT', blank=True, null=True)
    conscoderef = models.IntegerField(
        db_column='CONSCODEREF', blank=True, null=True)
    specode2 = models.CharField(
        db_column='SPECODE2', max_length=11, blank=True, null=True)
    specode3 = models.CharField(
        db_column='SPECODE3', max_length=11, blank=True, null=True)
    specode4 = models.CharField(
        db_column='SPECODE4', max_length=11, blank=True, null=True)
    specode5 = models.CharField(
        db_column='SPECODE5', max_length=11, blank=True, null=True)
    expense = models.SmallIntegerField(
        db_column='EXPENSE', blank=True, null=True)
    origin = models.CharField(
        db_column='ORIGIN', max_length=25, blank=True, null=True)
    name2 = models.CharField(
        db_column='NAME2', max_length=51, blank=True, null=True)
    compkdvuse = models.SmallIntegerField(
        db_column='COMPKDVUSE', blank=True, null=True)
    usedinperiods = models.SmallIntegerField(
        db_column='USEDINPERIODS', blank=True, null=True)
    eximtax1 = models.FloatField(db_column='EXIMTAX1', blank=True, null=True)
    eximtax2 = models.FloatField(db_column='EXIMTAX2', blank=True, null=True)
    eximtax3 = models.FloatField(db_column='EXIMTAX3', blank=True, null=True)
    eximtax4 = models.FloatField(db_column='EXIMTAX4', blank=True, null=True)
    eximtax5 = models.FloatField(db_column='EXIMTAX5', blank=True, null=True)
    productlevel = models.SmallIntegerField(
        db_column='PRODUCTLEVEL', blank=True, null=True)
    appspevatmatrah = models.SmallIntegerField(
        db_column='APPSPEVATMATRAH', blank=True, null=True)
    name3 = models.CharField(
        db_column='NAME3', max_length=201, blank=True, null=True)
    facostkeys = models.SmallIntegerField(
        db_column='FACOSTKEYS', blank=True, null=True)
    kklinesdisable = models.SmallIntegerField(
        db_column='KKLINESDISABLE', blank=True, null=True)
    approve = models.SmallIntegerField(
        db_column='APPROVE', blank=True, null=True)
    approvedate = models.DateTimeField(
        db_column='APPROVEDATE', blank=True, null=True)
    globalid = models.CharField(
        db_column='GLOBALID', max_length=51, blank=True, null=True)
    saledeductpart1 = models.SmallIntegerField(
        db_column='SALEDEDUCTPART1', blank=True, null=True)
    saledeductpart2 = models.SmallIntegerField(
        db_column='SALEDEDUCTPART2', blank=True, null=True)
    purcdeductpart1 = models.SmallIntegerField(
        db_column='PURCDEDUCTPART1', blank=True, null=True)
    purcdeductpart2 = models.SmallIntegerField(
        db_column='PURCDEDUCTPART2', blank=True, null=True)
    categoryid = models.CharField(
        db_column='CATEGORYID', max_length=51, blank=True, null=True)
    categoryname = models.CharField(
        db_column='CATEGORYNAME', max_length=256, blank=True, null=True)
    keyword1 = models.CharField(
        db_column='KEYWORD1', max_length=121, blank=True, null=True)
    keyword2 = models.CharField(
        db_column='KEYWORD2', max_length=121, blank=True, null=True)
    keyword3 = models.CharField(
        db_column='KEYWORD3', max_length=121, blank=True, null=True)
    keyword4 = models.CharField(
        db_column='KEYWORD4', max_length=121, blank=True, null=True)
    keyword5 = models.CharField(
        db_column='KEYWORD5', max_length=121, blank=True, null=True)
    guid = models.CharField(
        db_column='GUID', max_length=37, blank=True, null=True)
    demandmeetsortfld1 = models.CharField(
        db_column='DEMANDMEETSORTFLD1', max_length=51, blank=True, null=True)
    demandmeetsortfld2 = models.CharField(
        db_column='DEMANDMEETSORTFLD2', max_length=51, blank=True, null=True)
    demandmeetsortfld3 = models.CharField(
        db_column='DEMANDMEETSORTFLD3', max_length=51, blank=True, null=True)
    demandmeetsortfld4 = models.CharField(
        db_column='DEMANDMEETSORTFLD4', max_length=51, blank=True, null=True)
    demandmeetsortfld5 = models.CharField(
        db_column='DEMANDMEETSORTFLD5', max_length=51, blank=True, null=True)
    deductcode = models.CharField(
        db_column='DEDUCTCODE', max_length=11, blank=True, null=True)
    projectref = models.IntegerField(
        db_column='PROJECTREF', blank=True, null=True)
    name4 = models.CharField(
        db_column='NAME4', max_length=201, blank=True, null=True)
    qprodsubamnt = models.FloatField(
        db_column='QPRODSUBAMNT', blank=True, null=True)
    qprodsubuom = models.IntegerField(
        db_column='QPRODSUBUOM', blank=True, null=True)
    qprodsubsrcindex = models.SmallIntegerField(
        db_column='QPRODSUBSRCINDEX', blank=True, null=True)
    qprodsubdepart = models.SmallIntegerField(
        db_column='QPRODSUBDEPART', blank=True, null=True)
    pordamnttolerance = models.FloatField(
        db_column='PORDAMNTTOLERANCE', blank=True, null=True)
    sordamnttolerance = models.FloatField(
        db_column='SORDAMNTTOLERANCE', blank=True, null=True)
    multiaddtax = models.SmallIntegerField(
        db_column='MULTIADDTAX', blank=True, null=True)
    fausefullifecode = models.CharField(
        db_column='FAUSEFULLIFECODE', max_length=11, blank=True, null=True)
    fausefullifecode2 = models.CharField(
        db_column='FAUSEFULLIFECODE2', max_length=11, blank=True, null=True)
    cpacode = models.CharField(
        db_column='CPACODE', max_length=25, blank=True, null=True)
    publiccountryref = models.IntegerField(
        db_column='PUBLICCOUNTRYREF', blank=True, null=True)
    moldmainttype = models.SmallIntegerField(
        db_column='MOLDMAINTTYPE', blank=True, null=True)
    moldlifeasratio = models.SmallIntegerField(
        db_column='MOLDLIFEASRATIO', blank=True, null=True)
    moldmaintlife = models.FloatField(
        db_column='MOLDMAINTLIFE', blank=True, null=True)
    moldmaintperunit = models.SmallIntegerField(
        db_column='MOLDMAINTPERUNIT', blank=True, null=True)
    moldmaintperiod = models.FloatField(
        db_column='MOLDMAINTPERIOD', blank=True, null=True)
    moldmaintbegdate = models.DateTimeField(
        db_column='MOLDMAINTBEGDATE', blank=True, null=True)
    moldusagelife = models.FloatField(
        db_column='MOLDUSAGELIFE', blank=True, null=True)
    moldlifetracktype = models.SmallIntegerField(
        db_column='MOLDLIFETRACKTYPE', blank=True, null=True)
    mold = models.SmallIntegerField(
        db_column='MOLD', blank=True, null=True)
    moldmaintlifetype = models.SmallIntegerField(
        db_column='MOLDMAINTLIFETYPE', blank=True, null=True)
    moldmaintnumber = models.IntegerField(
        db_column='MOLDMAINTNUMBER', blank=True, null=True)
    moldfactor = models.SmallIntegerField(
        db_column='MOLDFACTOR', blank=True, null=True)
    obtaintype = models.SmallIntegerField(
        db_column='OBTAINTYPE', blank=True, null=True)
    gaintype = models.SmallIntegerField(
        db_column='GAINTYPE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ITEMS'
        unique_together = (
            ('classtype', 'dominantrefs5', 'logicalref'),
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
        )
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"

class LG_ITEMSUBS(
    BaseLogical,
    BasePriority,
    BaseSiteRec,
    BaseRef,
    models.Model):
    """
        Malzeme alternatifleri
    """
    mainitemref = models.ForeignKey(
        "LG_ITEMS",
        db_column='MAINITEMREF',
        blank=True,
        null=True,
        help_text='Ana malzeme sınıfı ref.',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_mainitemref"
    )
    subitemref = models.ForeignKey(
        "LG_ITEMS",
        db_column='SUBITEMREF',
        blank=True,
        null=True,
        help_text='Alt malzeme sınıfı ref.',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_subitemref"
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    convfact1 = models.FloatField(
        db_column='CONVFACT1',
        blank=True,
        null=True,
        help_text='Çarpan 1'
    )
    convfact2 = models.FloatField(
        db_column='CONVFACT2',
        blank=True,
        null=True,
        help_text='Çarpan 2'
    )
    maxquantity = models.FloatField(
        db_column='MAXQUANTITY',
        blank=True,
        null=True,
        help_text='Azami miktar'
    )
    minquantity = models.FloatField(
        db_column='MINQUANTITY',
        blank=True,
        null=True,
        help_text='Asgari miktar'
    )
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True,
        help_text='Başlangıç tarihi'
    )
    enddate = models.DateTimeField(
        db_column='ENDDATE',
        blank=True,
        null=True,
        help_text='Bitiş tarihi'
    )
    mainvrntref = models.IntegerField(
        db_column='MAINVRNTREF',
        blank=True,
        null=True
    )
    subvrntref = models.IntegerField(
        db_column='SUBVRNTREF',
        blank=True,
        null=True
    )
    sourceindex = models.SmallIntegerField(
        db_column='SOURCEINDEX',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_ITEMSUBS'
        target_db = 'erp'

