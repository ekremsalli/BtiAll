"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_STLINE(
    BaseLogical,
    BaseUnit,
    BaseVAT,
    BaseSiteRec,
    BaseAmount,
    BaseGUID,
    BaseCenter,
    BaseCancelled,
    BaseClient,
    BaseSalesMan,
    BaseProject,
    BaseAccount,
    BaseWF,
    BaseTextINC,
    BaseRef,
    models.Model):
    """
        Fatura, irsaliye ve stok fişlerinin satırlarının tutulduğu tablo.
        Fişlerin satırlarında bulunan indirim, masraf promosyon gibi
        stok hareketinin dışındaki satır türleri de stok
        hareketleri tablosunda ayrı satırlar halinde kaydedilmektedir.
    """
    stockref = models.ForeignKey(
        "LG_ITEMS",
        db_column='STOCKREF',
        blank=True,
        null=True,
        help_text='Malzeme kartı ref. -> ITEMS (linetype=0,1,5,6,7,9,10)',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_stockref'
    )
    linetype = models.SmallIntegerField(db_column='LINETYPE', blank=True,
        null=True,
        choices=[
            (0, 'Malzeme'),
            (1, 'Promosyon'),
            (2, 'İndirim'),
            (3, 'Masraf'),
            (4, 'Hizmet'),
            (5, 'Depozito'),
            (6, 'Karma koli'),
            (7, 'Karma koli kalemi'),
            (8, 'Sabit kıymet'),
            (9, 'Ek malzeme'),
            (10, 'Malzeme sınıfı'),
            (11, 'Fason')
        ],
        help_text="""
            Satır türü;
            0 -> Malzeme
            1 -> Promosyon
            2 -> İndirim
            3 -> Masraf
            4 -> Hizmet
            5 -> Depozito
            6 -> Karma koli
            7 -> Karma koli kalemi
            8 -> Sabit kıymet
            9 -> Ek malzeme
            10 -> Malzeme sınıfı
            11 -> Fason
        """
    )
    prevlineref = models.ForeignKey(
        'LG_ITEMS',
        db_column='PREVLINEREF',
        blank=True,
        null=True,
        help_text='Üst malzeme sınıfı satır ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_prevlineref'
    )
    prevlineno = models.SmallIntegerField(
        db_column='PREVLINENO',
        blank=True,
        null=True,
        help_text='Üst malzeme sınıfı satır numarası'
    )
    detline = models.SmallIntegerField(
        db_column='DETLINE',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text="""
            Malzeme sınıf detay satırı
            1 -> Evet
            0 -> Hayır
        """
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        help_text="""
            Bağlı olduğu fiş türü;
            15, 16, 17, 18, 19 -> Kullanıcı tanımlı giriş fişi
            20, 21, 22, 23, 24 -> Kullanıcı tanımlı çıkış fişi
            30, 31, 32, 33, 34 -> Kullanıcı tanımlı satın alma irsaliyesi
            35, 36, 37, 38, 39 -> Kullanıcı tanımlı satış irsaliyesi
        """
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Fiş tarihi'
    )
    ftime = models.IntegerField(
        db_column='FTIME',
        blank=True,
        null=True,
        help_text='Fiş zamanı'
    )
    globtrans = models.SmallIntegerField(
        db_column='GLOBTRANS',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text="""
            İndirim, masraf, promosyon satırları için;
            Fiş geneline uygulanan
            1 -> Evet
            0 -> Hayır
        """
    )
    calctype = models.SmallIntegerField(
        db_column='CALCTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Yüzde'),
            (2, 'Miktar'),
            (3, 'Formül')
        ],

        help_text="""
            İndirim, masraf
            Promosyon satırları için
            Hesaplama türü;
            0 -> Yüzde
            1 -> Miktar
            2 -> Formül
        """
    )
    prodorderref = models.ForeignKey(
        "LG_PRODORD",
        db_column='PRODORDERREF',
        blank=True,
        null=True,
        help_text="Üretim emri ref. -> PRODORD",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_prodorderref'
    )
    sourcetype = models.SmallIntegerField(
        db_column='SOURCETYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Ambar'),
            (1, 'İş istasyonu')
        ],
        help_text="Kaynak türü (0 -> Ambar, 1-> İş istasyonu)"
    )
    sourceindex = models.SmallIntegerField(
        db_column='SOURCEINDEX',
        blank=True,
        null=True,
        help_text="Kaynak ambar numarası"
    )
    sourcecostgrp = models.SmallIntegerField(
        db_column='SOURCECOSTGRP',
        blank=True,
        null=True,
        help_text="Kaynak ambar maliyet grubu"
    )
    sourcewsref = models.ForeignKey(
        "LG_WORKSTAT",
        db_column='SOURCEWSREF',
        blank=True,
        null=True,
        help_text="Kaynak iş istasyonu ref. -> WORKSTAT",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_sourcewsref'
    )
    sourcepolnref = models.ForeignKey(
        "LG_DISPLINE",
        db_column='SOURCEPOLNREF',
        blank=True,
        null=True,
        help_text="Kaynak iş emri ref. -> DISPLINE",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_sourcepolnref'
    )
    desttype = models.SmallIntegerField(
        db_column='DESTTYPE',
        blank=True, null=True,
        choices=[
            (0, 'Ambar'),
            (1, 'İş istasyonu')
        ],
        help_text="Hedef türü (0 -> Ambar, 1 -> İş istasyonu)"
    )
    destindex = models.SmallIntegerField(
        db_column='DESTINDEX',
        blank=True,
        null=True,
        help_text='Hedef ambar numarası'
    )
    destcostgrp = models.SmallIntegerField(
        db_column='DESTCOSTGRP',
        blank=True,
        null=True,
        help_text='Hedef ambar maliyet grubu'
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
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika numarası'
    )
    iocode = models.SmallIntegerField(
        db_column='IOCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Giriş'),
            (2, 'Ambar giriş'),
            (3, 'Ambar çıkış'),
            (4, 'Çıkış')
        ],
        help_text="""
            Giriş / Çıkış kodu;
            1 -> Giriş
            2 -> Ambar giriş
            3 -> Ambar çıkış
            4 -> Çıkış
        """
    )
    stficheref = models.ForeignKey(
        "LG_STFICHE",
        db_column='STFICHEREF',
        blank=True,
        null=True,
        help_text="Stok fişi ref. -> STFICHE",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_stficheref'
    )
    stfichelnno = models.SmallIntegerField(
        db_column='STFICHELNNO',
        blank=True,
        null=True,
        help_text="Stok fişi satır no"
    )
    invoiceref = models.ForeignKey(
        "LG_INVOICE",
        db_column='INVOICEREF',
        blank=True,
        null=True,
        help_text="Fatura ref. -> INVOICE",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_invoiceref'
    )
    invoicelnno = models.SmallIntegerField(
        db_column='INVOICELNNO',
        blank=True,
        null=True,
        help_text="Fatura satır numarası"
    )
    ordtransref = models.ForeignKey(
        "LG_ORFLINE",
        db_column='ORDTRANSREF',
        blank=True,
        null=True,
        help_text="Sipariş fiş satırı ref. -> ORFLINE",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_ordtransref'
    )
    ordficheref = models.ForeignKey(
        "LG_ORFICHE",
        db_column='ORDFICHEREF',
        blank=True,
        null=True,
        help_text="Sipariş fişi ref. -> ORFICHE",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_ordficheref'
    )
    vataccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='VATACCREF',
        blank=True,
        null=True,
        help_text="KDV Hesabı ref. -> EMUHACC",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_vataccref'
    )
    vatcenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='VATCENTERREF',
        blank=True,
        null=True,
        help_text="KDV masraf merkezi ref. -> EMCENTER",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_vatcenterref'
    )
    praccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='PRACCREF',
        blank=True,
        null=True,
        help_text="Promosyon hesabı ref. -> EMUHACC",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_praccref'
    )
    prcenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='PRCENTERREF',
        blank=True,
        null=True,
        help_text="Promosyon masraf merkezi ref. -> EMCENTER",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_prcenterref'
    )
    prvataccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='PRVATACCREF',
        blank=True,
        null=True,
        help_text="Promosyon KDV'si muhasebe hesabı ref. -> EMUHACC",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_prvataccref'
    )
    prvatcenref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='PRVATCENREF',
        blank=True,
        null=True,
        help_text="Promosyon KDV'si masraf merkezi ref. -> EMCENTER",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_prvatcenref'
    )
    promref = models.ForeignKey(
        "LG_PRCARDS",
        db_column='PROMREF',
        blank=True,
        null=True,
        help_text="Promosyon kartı ref. -> PRCARD",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_promref'
    )
    paydefref = models.ForeignKey(
        "LG_PAYPLANS",
        db_column='PAYDEFREF',
        blank=True,
        null=True,
        help_text="Ödeme planı ref. -> PAYPLANS",
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_paydefref'
    )
    specode = models.CharField(
        db_column='SPECODE',
        max_length=17,
        blank=True,
        null=True, help_text="Özel kod"
    )
    delvrycode = models.CharField(
        db_column='DELVRYCODE',
        max_length=11,
        blank=True,
        null=True,
        help_text="Teslimat kodu"
    )
    price = models.FloatField(
        db_column='PRICE',
        blank=True,
        null=True,
        help_text='Birim fiyat'
    )
    total = models.FloatField(
        db_column='TOTAL',
        blank=True,
        null=True,
        help_text='Toplam'
    )
    prcurr = models.SmallIntegerField(
        db_column='PRCURR',
        blank=True,
        null=True,
        help_text='İşlem döviz kuru'
    )
    prprice = models.FloatField(
        db_column='PRPRICE',
        blank=True,
        null=True,
        help_text='Fiyat işlem dövizi'
    )
    trcurr = models.SmallIntegerField(
        db_column='TRCURR',
        blank=True,
        null=True,
        help_text='Hareket dövizi türü'
    )
    trrate = models.FloatField(
        db_column='TRRATE',
        blank=True,
        null=True,
        help_text='Hareket dövizi kuru'
    )
    reportrate = models.FloatField(
        db_column='REPORTRATE',
        blank=True,
        null=True,
        help_text='Raporlama dövizi kuru'
    )
    distcost = models.FloatField(
        db_column='DISTCOST',
        blank=True,
        null=True,
        help_text='Satıra dağıtılan maliyet'
    )
    distdisc = models.FloatField(
        db_column='DISTDISC',
        blank=True,
        null=True,
        help_text='Satıra dağıtılan indirim'
    )
    distexp = models.FloatField(
        db_column='DISTEXP',
        blank=True,
        null=True,
        help_text='Satıra dağıtılan masraf'
    )
    distprom = models.FloatField(
        db_column='DISTPROM',
        blank=True,
        null=True,
        help_text='Satıra dağıtılan promosyon'
    )
    discper = models.FloatField(
        db_column='DISCPER',
        blank=True,
        null=True,
        help_text='İndirim yüzdesi'
    )
    lineexp = models.CharField(
        db_column='LINEEXP',
        max_length=251,
        blank=True,
        null=True,
        help_text='Satır açıklaması'
    )

    plnamount = models.FloatField(
        db_column='PLNAMOUNT',
        blank=True,
        null=True,
        help_text='Planlanan miktar'
    )
    vatinc = models.SmallIntegerField(
        db_column='VATINC',
        blank=True, null=True,
        choices=[
            (0, 'Hariç'),
            (1, 'Dahil')
        ],
        help_text='KDV Dahil / Hariç'
    )
    vatamnt = models.FloatField(
        db_column='VATAMNT',
        blank=True,
        null=True,
        help_text='KDV net tutarı'
    )
    vatmatrah = models.FloatField(
        db_column='VATMATRAH',
        blank=True,
        null=True,
        help_text='KDV Matrahı'
    )
    billeditem = models.IntegerField(
        db_column='BILLEDITEM',
        blank=True,
        null=True,
        help_text='Faturalanması gereken mal'
    )
    billed = models.SmallIntegerField(
        db_column='BILLED',
        blank=True,
        null=True,
        help_text='Faturalanmış E/H'
    )
    cpstflag = models.SmallIntegerField(
        db_column='CPSTFLAG',
        blank=True,
        null=True,
        help_text='Karma koli satırı'
    )
    retcosttype = models.SmallIntegerField(
        db_column='RETCOSTTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Çıkış'),
            (1, 'O anki'),
            (2, 'Tutar')
        ],
        help_text="""
            İade hareketi maliyet türü
            0 -> Çıkış
            1 -> O anki
            2 -> Tutar
        """
    )
    sourcelink = models.ForeignKey(
        "LG_STLINE",
        db_column='SOURCELINK',
        blank=True,
        null=True,
        help_text='İadelerde kaynak hareket bağlantısı -> STLINE',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_sourcelink'
    )
    retcost = models.FloatField(
        db_column='RETCOST',
        blank=True,
        null=True,
        help_text='İade fişleri için iade maliyeti'
    )
    retcostcurr = models.FloatField(
        db_column='RETCOSTCURR',
        blank=True,
        null=True,
        help_text='İade fişleri için dövizli iade maliyeti'
    )
    outcost = models.FloatField(
        db_column='OUTCOST',
        blank=True,
        null=True,
        help_text='Çıkış fişleri çıkış maliyeti'
    )
    outcostcurr = models.FloatField(
        db_column='OUTCOSTCURR',
        blank=True,
        null=True,
        help_text='Çıkış fişleri dövizli çıkış maliyeti'
    )
    retamount = models.FloatField(
        db_column='RETAMOUNT',
        blank=True,
        null=True,
        help_text='İade miktarı'
    )
    faregref = models.ForeignKey(
        "LG_FAREGIST",
        db_column='FAREGREF',
        blank=True,
        null=True,
        help_text='Demirbaş kayıt ref.',
        on_delete=models.DO_NOTHING
    )
    faattrib = models.SmallIntegerField(
        db_column='FAATTRIB',
        blank=True,
        null=True,
        help_text='Demirbaş kayıt ilişki türü'
    )
    linenet = models.FloatField(
        db_column='LINENET',
        blank=True,
        null=True,
        help_text='Satır net tutarı'
    )
    distaddexp = models.FloatField(
        db_column='DISTADDEXP',
        blank=True,
        null=True,
        help_text='Satıra dağıtılan ek masraf'
    )
    fadaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='FADACCREF',
        blank=True,
        null=True,
        help_text='Sabit kıymet birikmiş amortisman hesabı -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_fadaccref'
    )
    fadcenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='FADCENTERREF',
        blank=True,
        null=True,
        help_text='Sabit kıymet birikmiş amortisman masraf merkezi ref. -> EMCENTER',
        related_name='%(app_label)s_%(class)s_fadcenterref',
        on_delete=models.DO_NOTHING
    )
    faraccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='FARACCREF',
        blank=True,
        null=True,
        help_text='Sabit kıymet yeniden değerleme hesabı -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_faraccref'
    )
    farcenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='FARCENTERREF',
        blank=True,
        null=True,
        help_text='Sabit kıymet yeniden değerleme amortisman maraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_farcenterref'
    )
    diffprice = models.FloatField(
        db_column='DIFFPRICE',
        blank=True,
        null=True,
        help_text='Fiyat farkı tutarı'
    )
    diffprcost = models.FloatField(
        db_column='DIFFPRCOST',
        blank=True,
        null=True,
        help_text='Fiyat farkı nedeniyle oluşan maliyet'
    )
    decprdiff = models.SmallIntegerField(
        db_column='DECPRDIFF',
        blank=True,
        null=True,
        choices=[
            (0, 'Azaltıcı'),
            (1, 'Arttırıcı')
        ],
        help_text='Fiyat farkı (0 -> azaltıcı, 1-> arttırıcı)')
    lprodstat = models.SmallIntegerField(
        db_column='LPRODSTAT',
        choices=[
            (0, 'Güncel'),
            (1, 'Planlanan')
        ],
        blank=True, null=True, help_text='Durumu')
    prdexptotal = models.FloatField(
        db_column='PRDEXPTOTAL',
        blank=True,
        null=True,
        help_text='Üretimden girişe katılan masraf fişi tutarı'
    )
    diffrepprice = models.FloatField(
        db_column='DIFFREPPRICE',
        blank=True,
        null=True,
        help_text='Fiyat farkı raporlama döviz tutarı'
    )
    diffprcrcost = models.FloatField(
        db_column='DIFFPRCRCOST',
        blank=True,
        null=True,
        help_text='Fiyat farkıyla oluşan RD maliyeti'
    )
    faplaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='FAPLACCREF',
        blank=True,
        null=True,
        help_text='Sabit kıymet kar/zarar hesabı -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_faplaccref'
    )
    faplcenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='FAPLCENTERREF',
        blank=True,
        null=True,
        help_text='Sabit kıymet kar/zarar masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_faplcenterref'
    )
    outputidcode = models.CharField(
        db_column='OUTPUTIDCODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Çıkış izleme kodu'
    )
    dref = models.ForeignKey(
        "LG_DISTTEMP",
        db_column='DREF',
        blank=True,
        null=True,
        help_text='Dağıtım şablonu ref. -> DISTTEMP',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_dref'
    )
    costrate = models.FloatField(
        db_column='COSTRATE',
        blank=True,
        null=True,
        help_text='Üretimden giriş fişi satır maliyeti yüzdesi'
    )
    xpriceupd = models.SmallIntegerField(
        db_column='XPRICEUPD',
        blank=True,
        null=True,
        help_text='İç kullanım'
    )
    xprice = models.FloatField(
        db_column='XPRICE',
        blank=True,
        null=True,
        help_text='İç kullanım'
    )
    xreprate = models.FloatField(
        db_column='XREPRATE',
        blank=True,
        null=True,
        help_text='İç kullanım'
    )
    distcoef = models.FloatField(
        db_column='DISTCOEF',
        blank=True,
        null=True,
        help_text='Fiyat farkı dağıtım katsayısı'
    )
    transqcok = models.SmallIntegerField(
        db_column='TRANSQCOK',
        choices=[
            (1, 'Uygun'),
            (0, 'Uygun değil')
        ],
        blank=True,
        null=True,
        help_text='Kalite kontrol işlem uygunluğu'
    )
    polineref = models.IntegerField(
        db_column='POLINEREF',
        blank=True,
        null=True,
        help_text='Üretim emri satır ref.'
    )
    plnsttransref = models.IntegerField(
        db_column='PLNSTTRANSREF',
        blank=True,
        null=True,
        help_text='Planlanan malzeme hareti ref.'
    )
    netdiscflag = models.SmallIntegerField(
        db_column='NETDISCFLAG',
        blank=True,
        null=True,
        help_text='Net indirim satırı ve tutar işareti (evet/hayır)'
    )
    netdiscperc = models.FloatField(
        db_column='NETDISCPERC',
        blank=True,
        null=True,
        help_text='Net indirim oranı (%)'
    )
    netdiscamnt = models.FloatField(
        db_column='NETDISCAMNT',
        blank=True,
        null=True,
        help_text='Net indirim tutarı'
    )
    vatcalcdiff = models.FloatField(
        db_column='VATCALCDIFF',
        blank=True,
        null=True,
        help_text='Alım faturasında KDV farkı'
    )
    conditionref = models.IntegerField(
        db_column='CONDITIONREF',
        blank=True,
        null=True,
        help_text='Satınalma / satış koşulları ref.'
    )
    distorderref = models.IntegerField(
        db_column='DISTORDERREF',
        blank=True,
        null=True,
        help_text='Dağıtım emri ref.'
    )
    distordlineref = models.IntegerField(
        db_column='DISTORDLINEREF',
        blank=True,
        null=True,
        help_text='Dağıtım emri satırı ref.'
    )
    campaignrefs1 = models.IntegerField(
        db_column='CAMPAIGNREFS1',
        blank=True,
        null=True,
        help_text='Kampanya kartı ref. 1'
    )
    campaignrefs2 = models.IntegerField(
        db_column='CAMPAIGNREFS2',
        blank=True,
        null=True,
        help_text='Kampanya kartı ref. 2'
    )
    campaignrefs3 = models.IntegerField(
        db_column='CAMPAIGNREFS3',
        blank=True,
        null=True,
        help_text='Kampanya kartı ref. 3'
    )
    campaignrefs4 = models.IntegerField(
        db_column='CAMPAIGNREFS4',
        blank=True,
        null=True,
        help_text='Kampanya kartı ref. 4'
    )
    campaignrefs5 = models.IntegerField(
        db_column='CAMPAIGNREFS5',
        blank=True,
        null=True,
        help_text='Kampanya kartı ref. 5'
    )
    pointcampref = models.IntegerField(
        db_column='POINTCAMPREF',
        blank=True,
        null=True,
        help_text='Kampanya puanı ref.'
    )
    camppoint = models.FloatField(
        db_column='CAMPPOINT',
        blank=True,
        null=True,
        help_text='Kampanya puanı'
    )
    promclasitemref = models.IntegerField(
        db_column='PROMCLASITEMREF',
        blank=True,
        null=True,
        help_text='Promosyon sınırlı ref. (kampanyadan)'
    )
    cmpglineref = models.IntegerField(
        db_column='CMPGLINEREF',
        blank=True,
        null=True,
        help_text='?'
    )
    plnsttranspernr = models.IntegerField(
        db_column='PLNSTTRANSPERNR',
        blank=True,
        null=True,
        help_text='Planlanan malzeme hareketi periy num.'
    )
    pordclsplnamnt = models.FloatField(
        db_column='PORDCLSPLNAMNT',
        blank=True,
        null=True,
        help_text='Planlanan kapanış miktarı'
    )
    vendcomm = models.FloatField(
        db_column='VENDCOMM',
        blank=True,
        null=True,
        help_text='Komisyon oranı'
    )
    previousoutcost = models.FloatField(
        db_column='PREVIOUSOUTCOST',
        blank=True,
        null=True,
        help_text='Önceki çıkış maliyeti'
    )
    costofsaleaccref = models.IntegerField(
        db_column='COSTOFSALEACCREF',
        blank=True,
        null=True,
        help_text='Satış maliyeti muhasebe hesabı ref.'
    )
    purchaccref = models.IntegerField(
        db_column='PURCHACCREF',
        blank=True,
        null=True,
        help_text='Satınalma muhasebe hesabı ref.'
    )
    costofsalecntref = models.IntegerField(
        db_column='COSTOFSALECNTREF',
        blank=True,
        null=True,
        help_text='Satış maliyeti masraf merkezi ref.'
    )
    purchcentref = models.IntegerField(
        db_column='PURCHCENTREF',
        blank=True,
        null=True,
        help_text='Satınalma masraf merkezi ref.'
    )
    prevoutcostcurr = models.FloatField(
        db_column='PREVOUTCOSTCURR',
        blank=True,
        null=True,
        help_text='Önceki çıkış maliyeti (döviz)'
    )
    abvatamount = models.FloatField(
        db_column='ABVATAMOUNT',
        blank=True,
        null=True,
        help_text='AB kdv tutarı'
    )
    abvatstatus = models.IntegerField(
        db_column='ABVATSTATUS',
        blank=True,
        null=True,
        help_text='KDV hesaplama durumu'
    )
    prrate = models.FloatField(
        db_column='PRRATE',
        blank=True,
        null=True,
        help_text='Fiyatlandırma dövizi kuru'
    )
    addtaxrate = models.FloatField(
        db_column='ADDTAXRATE',
        blank=True,
        null=True,
        help_text='Ek vergi oranı'
    )
    addtaxconvfact = models.FloatField(
        db_column='ADDTAXCONVFACT',
        blank=True,
        null=True,
        help_text='Ek vergi çevrim katsayısı'
    )
    addtaxamount = models.FloatField(
        db_column='ADDTAXAMOUNT',
        blank=True,
        null=True,
        help_text='Ek vergi tutarı'
    )
    addtaxprcost = models.FloatField(
        db_column='ADDTAXPRCOST',
        blank=True,
        null=True,
        help_text='Ek vergi maliyeti'
    )
    addtaxretcost = models.FloatField(
        db_column='ADDTAXRETCOST',
        blank=True,
        null=True,
        help_text='Ek vergi iade maliyeti'
    )
    addtaxretcostcurr = models.FloatField(
        db_column='ADDTAXRETCOSTCURR',
        blank=True,
        null=True,
        help_text='Ek vergi iade maliyetli (RD)'
    )
    grossuinfo1 = models.FloatField(
        db_column='GROSSUINFO1',
        blank=True,
        null=True,
        help_text='Brüt birim çevrim katsayısı 1'
    )
    grossuinfo2 = models.FloatField(
        db_column='GROSSUINFO2',
        blank=True,
        null=True,
        help_text='Brüt birim çevrim katsayısı 2'
    )
    addtaxprcostcurr = models.FloatField(
        db_column='ADDTAXPRCOSTCURR',
        blank=True,
        null=True,
        help_text='Ek vergi maliyeti'
    )
    addtaxaccref = models.IntegerField(
        db_column='ADDTAXACCREF',
        blank=True,
        null=True,
        help_text='Ek vergi genel muh. hesabı ref.'
    )
    addtaxcenterref = models.IntegerField(
        db_column='ADDTAXCENTERREF',
        blank=True,
        null=True,
        help_text='Ek vergi genel muh. hesabı ref.'
    )
    addtaxamntisupd = models.SmallIntegerField(
        db_column='ADDTAXAMNTISUPD',
        blank=True,
        null=True,
        help_text='Güncel ek vergi tutarı'
    )
    infidx = models.FloatField(
        db_column='INFIDX',
        blank=True,
        null=True,
        help_text='Enflasyon endeksi'
    )
    addtaxcosaccref = models.IntegerField(
        db_column='ADDTAXCOSACCREF',
        blank=True,
        null=True,
        help_text='İndirilecek ÖTV muhasebe hesabı ref.'
    )
    addtaxcoscntref = models.IntegerField(
        db_column='ADDTAXCOSCNTREF',
        blank=True,
        null=True,
        help_text='İndirilecek ÖTV masraf merkezi ref.'
    )
    previousataxprcost = models.FloatField(
        db_column='PREVIOUSATAXPRCOST',
        blank=True,
        null=True,
        help_text='Önceki ek vergi maliyeti'
    )
    prevataxprcostcurr = models.FloatField(
        db_column='PREVATAXPRCOSTCURR',
        blank=True,
        null=True,
        help_text='Önceki ek vergi maliyeti (RD)'
    )
    prdordtotcoef = models.FloatField(
        db_column='PRDORDTOTCOEF',
        blank=True,
        null=True,
        help_text='Üretimden girişler toplamı (miktar * maliyet katsayısı)'
    )
    dempeggedamnt = models.FloatField(
        db_column='DEMPEGGEDAMNT',
        blank=True,
        null=True,
        help_text='Talep karşılamada kullanılan miktar'
    )
    stdunitcost = models.FloatField(
        db_column='STDUNITCOST',
        blank=True,
        null=True,
        help_text='Standart malzeme maliyeti'
    )
    stdrpunitcost = models.FloatField(
        db_column='STDRPUNITCOST',
        blank=True,
        null=True,
        help_text='Standart malzeme maliyeti (RD)'
    )
    costdiffaccref = models.IntegerField(
        db_column='COSTDIFFACCREF',
        blank=True,
        null=True,
        help_text='Ayrıntılı açıklama içerir'
    )
    costdiffcenref = models.IntegerField(
        db_column='COSTDIFFCENREF',
        blank=True,
        null=True,
        help_text='?'
    )
    addtaxdiscamount = models.FloatField(
        db_column='ADDTAXDISCAMOUNT',
        blank=True,
        null=True,
        help_text='Ek vergi indirim tutarı'
    )
    orglogoid = models.CharField(
        db_column='ORGLOGOID',
        max_length=25,
        blank=True,
        null=True,
        help_text='Veri merkezi'
    )
    eximficheno = models.CharField(
        db_column='EXIMFICHENO',
        max_length=31,
        blank=True,
        null=True,
        help_text='İthalat / İhracat dosya numarası'
    )
    eximfctype = models.SmallIntegerField(
        db_column='EXIMFCTYPE',
        blank=True,
        null=True,
        help_text='İhtalat / İhracat fiş türü'
    )
    transexpline = models.SmallIntegerField(
        db_column='TRANSEXPLINE',
        blank=True,
        null=True,
        help_text='Navlun'
    )
    insexpline = models.SmallIntegerField(
        db_column='INSEXPLINE',
        blank=True,
        null=True,
        help_text='Sigorta masrafı'
    )
    eximwhfcref = models.IntegerField(
        db_column='EXIMWHFCREF',
        blank=True,
        null=True,
        help_text='İthalat / İhracat ambar fişi ref.'
    )
    eximwhlnref = models.IntegerField(
        db_column='EXIMWHLNREF',
        blank=True,
        null=True,
        help_text='İthalat / İhracat ambar hareket ref.'
    )
    eximfileref = models.IntegerField(
        db_column='EXIMFILEREF',
        blank=True,
        null=True,
        help_text='INVEXIMINFO ref.'
    )
    eximprocnr = models.SmallIntegerField(
        db_column='EXIMPROCNR',
        blank=True,
        null=True,
        help_text='İthalat / İhracat hareket emri'
    )
    eisrvdsttyp = models.SmallIntegerField(
        db_column='EISRVDSTTYP',
        blank=True,
        null=True,
        help_text='Hizmet dağıtım türü; 0 -> Ambarlara göre, 1 -> Genel'
    )
    mainstlnref = models.IntegerField(
        db_column='MAINSTLNREF',
        blank=True,
        null=True,
        help_text='Malzeme hareketleri ref.'
    )
    madeofshred = models.SmallIntegerField(
        db_column='MADEOFSHRED',
        blank=True,
        null=True,
        help_text="""
            Parçalama yoluyla oluşmuş
            0 -> Hayır
            1 -> Evet
        """
    )
    fromordwithpay = models.SmallIntegerField(
        db_column='FROMORDWITHPAY',
        blank=True,
        null=True,
        help_text='Ödemeli / ödemesiz sipariş'
    )
    status = models.SmallIntegerField(
        db_column='STATUS',
        blank=True,
        null=True,
        help_text='Durum'
    )
    doreserve = models.SmallIntegerField(db_column='DORESERVE',
        blank=True, null=True)
    pointcamprefs1 = models.IntegerField(db_column='POINTCAMPREFS1',
        blank=True, null=True)
    pointcamprefs2 = models.IntegerField(db_column='POINTCAMPREFS2',
        blank=True, null=True)
    pointcamprefs3 = models.IntegerField(db_column='POINTCAMPREFS3',
        blank=True, null=True)
    pointcamprefs4 = models.IntegerField(db_column='POINTCAMPREFS4',
        blank=True, null=True)
    camppoints1 = models.FloatField(db_column='CAMPPOINTS1',
        blank=True, null=True)
    camppoints2 = models.FloatField(db_column='CAMPPOINTS2',
        blank=True, null=True)
    camppoints3 = models.FloatField(db_column='CAMPPOINTS3',
        blank=True, null=True)
    camppoints4 = models.FloatField(db_column='CAMPPOINTS4',
        blank=True, null=True)
    cmpglinerefs1 = models.IntegerField(db_column='CMPGLINEREFS1',
        blank=True, null=True)
    cmpglinerefs2 = models.IntegerField(db_column='CMPGLINEREFS2',
        blank=True, null=True)
    cmpglinerefs3 = models.IntegerField(db_column='CMPGLINEREFS3',
        blank=True, null=True)
    cmpglinerefs4 = models.IntegerField(db_column='CMPGLINEREFS4',
        blank=True, null=True)
    prclistref = models.IntegerField(db_column='PRCLISTREF',
        blank=True, null=True)
    pordsymoutln = models.SmallIntegerField(db_column='PORDSYMOUTLN',
        blank=True, null=True)
    month_field = models.SmallIntegerField(db_column='MONTH_',
        blank=True, null=True)
    year_field = models.SmallIntegerField(db_column='YEAR_',
        blank=True, null=True)
    exaddtaxrate = models.FloatField(db_column='EXADDTAXRATE',
        blank=True, null=True)
    exaddtaxconvf = models.FloatField(db_column='EXADDTAXCONVF',
        blank=True, null=True)
    exaddtaxaref = models.IntegerField(db_column='EXADDTAXAREF',
        blank=True, null=True)
    exaddtaxcref = models.IntegerField(db_column='EXADDTAXCREF',
        blank=True, null=True)
    othraddtaxaref = models.IntegerField(db_column='OTHRADDTAXAREF',
        blank=True, null=True)
    othraddtaxcref = models.IntegerField(db_column='OTHRADDTAXCREF',
        blank=True, null=True)
    exaddtaxamnt = models.FloatField(db_column='EXADDTAXAMNT',
        blank=True, null=True)
    affectcollatrl = models.SmallIntegerField(db_column='AFFECTCOLLATRL',
        blank=True, null=True)
    altpromflag = models.SmallIntegerField(db_column='ALTPROMFLAG',
        blank=True, null=True)
    eidistflnnr = models.SmallIntegerField(db_column='EIDISTFLNNR',
        blank=True, null=True)
    eximtype = models.SmallIntegerField(db_column='EXIMTYPE',
        blank=True, null=True)
    variantref = models.IntegerField(db_column='VARIANTREF',
        blank=True, null=True)
    candeduct = models.SmallIntegerField(db_column='CANDEDUCT',
        blank=True, null=True)
    outremamnt = models.FloatField(db_column='OUTREMAMNT',
        blank=True, null=True)
    outremcost = models.FloatField(db_column='OUTREMCOST',
        blank=True, null=True)
    outremcostcurr = models.FloatField(db_column='OUTREMCOSTCURR',
        blank=True, null=True)
    reflvataccref = models.IntegerField(db_column='REFLVATACCREF',
        blank=True, null=True)
    reflvatothaccref = models.IntegerField(db_column='REFLVATOTHACCREF',
        blank=True, null=True)
    parentlnref = models.IntegerField(db_column='PARENTLNREF',
        blank=True, null=True)
    affectrisk = models.SmallIntegerField(db_column='AFFECTRISK',
        blank=True, null=True)
    ineffectivecost = models.SmallIntegerField(db_column='INEFFECTIVECOST',
        blank=True, null=True)
    addtaxvatmatrah = models.FloatField(db_column='ADDTAXVATMATRAH',
        blank=True, null=True)
    reflaccref = models.IntegerField(db_column='REFLACCREF',
        blank=True, null=True)
    reflothaccref = models.IntegerField(db_column='REFLOTHACCREF',
        blank=True, null=True)
    camppaydefref = models.IntegerField(db_column='CAMPPAYDEFREF',
        blank=True, null=True)
    faregbinddate = models.DateTimeField(db_column='FAREGBINDDATE',
        blank=True, null=True)
    reltranslnref = models.IntegerField(db_column='RELTRANSLNREF',
        blank=True, null=True)
    fromtransfer = models.SmallIntegerField(db_column='FROMTRANSFER',
        blank=True, null=True)
    costdistprice = models.FloatField(db_column='COSTDISTPRICE',
        blank=True, null=True)
    costdistrepprice = models.FloatField(db_column='COSTDISTREPPRICE',
        blank=True, null=True)
    diffpriceufrs = models.FloatField(db_column='DIFFPRICEUFRS',
        blank=True, null=True)
    diffreppriceufrs = models.FloatField(db_column='DIFFREPPRICEUFRS',
        blank=True, null=True)
    outcostufrs = models.FloatField(db_column='OUTCOSTUFRS',
        blank=True, null=True)
    outcostcurrufrs = models.FloatField(db_column='OUTCOSTCURRUFRS',
        blank=True, null=True)
    diffprcostufrs = models.FloatField(db_column='DIFFPRCOSTUFRS',
        blank=True, null=True)
    diffprcrcostufrs = models.FloatField(db_column='DIFFPRCRCOSTUFRS',
        blank=True, null=True)
    retcostufrs = models.FloatField(db_column='RETCOSTUFRS',
        blank=True, null=True)
    retcostcurrufrs = models.FloatField(db_column='RETCOSTCURRUFRS',
        blank=True, null=True)
    outremcostufrs = models.FloatField(db_column='OUTREMCOSTUFRS',
        blank=True, null=True)
    outremcostcurrufrs = models.FloatField(db_column='OUTREMCOSTCURRUFRS',
        blank=True, null=True)
    infidxufrs = models.FloatField(db_column='INFIDXUFRS',
        blank=True, null=True)
    adjpriceufrs = models.FloatField(db_column='ADJPRICEUFRS',
        blank=True, null=True)
    adjreppriceufrs = models.FloatField(db_column='ADJREPPRICEUFRS',
        blank=True, null=True)
    adjprcostufrs = models.FloatField(db_column='ADJPRCOSTUFRS',
        blank=True, null=True)
    adjprcrcostufrs = models.FloatField(db_column='ADJPRCRCOSTUFRS',
        blank=True, null=True)
    costdistpriceufrs = models.FloatField(db_column='COSTDISTPRICEUFRS',
        blank=True, null=True)
    costdistreppriceufrs = models.FloatField(db_column='COSTDISTREPPRICEUFRS',
        blank=True, null=True)
    purchaccrefufrs = models.IntegerField(db_column='PURCHACCREFUFRS',
        blank=True, null=True)
    purchcentrefufrs = models.IntegerField(db_column='PURCHCENTREFUFRS',
        blank=True, null=True)
    cosaccrefufrs = models.IntegerField(db_column='COSACCREFUFRS',
        blank=True, null=True)
    coscntrefufrs = models.IntegerField(db_column='COSCNTREFUFRS',
        blank=True, null=True)
    proutcostufrsdiff = models.FloatField(db_column='PROUTCOSTUFRSDIFF',
        blank=True, null=True)
    proutcostcrufrsdiff = models.FloatField(db_column='PROUTCOSTCRUFRSDIFF',
        blank=True, null=True)
    underdeductlimit = models.SmallIntegerField(db_column='UNDERDEDUCTLIMIT',
        blank=True, null=True)
    globalid = models.CharField(db_column='GLOBALID', max_length=51,
        blank=True, null=True)
    deductionpart1 = models.SmallIntegerField(db_column='DEDUCTIONPART1',
        blank=True, null=True)
    deductionpart2 = models.SmallIntegerField(db_column='DEDUCTIONPART2',
        blank=True, null=True)
    specode2 = models.CharField(db_column='SPECODE2',
        max_length=41, blank=True, null=True)
    offerref = models.IntegerField(db_column='OFFERREF', blank=True, null=True)
    offtransref = models.IntegerField(db_column='OFFTRANSREF',
        blank=True, null=True)
    vatexceptreason = models.CharField(db_column='VATEXCEPTREASON',
        max_length=201, blank=True, null=True)
    plndefserilotno = models.CharField(db_column='PLNDEFSERILOTNO',
        max_length=101, blank=True, null=True)
    plnunrsrvamount = models.FloatField(db_column='PLNUNRSRVAMOUNT',
        blank=True, null=True)
    pordclsplnunrsrvamnt = models.FloatField(db_column='PORDCLSPLNUNRSRVAMNT',
        blank=True, null=True)
    lprodrsrvstat = models.SmallIntegerField(db_column='LPRODRSRVSTAT',
        blank=True, null=True)
    falinktype = models.SmallIntegerField(db_column='FALINKTYPE',
        blank=True, null=True)
    deductcode = models.CharField(db_column='DEDUCTCODE',
        max_length=11, blank=True, null=True)
    updthisline = models.SmallIntegerField(db_column='UPDTHISLINE',
        blank=True, null=True)
    vatexceptcode = models.CharField(db_column='VATEXCEPTCODE',
        max_length=11, blank=True, null=True)
    porderficheno = models.CharField(db_column='PORDERFICHENO',
        max_length=17, blank=True, null=True)
    qprodfcref = models.IntegerField(db_column='QPRODFCREF',
        blank=True, null=True)
    reltransfcref = models.IntegerField(db_column='RELTRANSFCREF',
        blank=True, null=True)
    ataxexceptreason = models.CharField(db_column='ATAXEXCEPTREASON',
        max_length=201, blank=True, null=True)
    ataxexceptcode = models.CharField(db_column='ATAXEXCEPTCODE',
        max_length=11, blank=True, null=True)
    prodordertyp = models.SmallIntegerField(db_column='PRODORDERTYP',
        blank=True, null=True)
    subcontorderref = models.IntegerField(db_column='SUBCONTORDERREF',
        blank=True, null=True)
    qprodfctyp = models.SmallIntegerField(db_column='QPRODFCTYP',
        blank=True, null=True)
    prdordslplnreserve = models.SmallIntegerField(db_column='PRDORDSLPLNRESERVE',
        blank=True, null=True)
    infdate = models.DateTimeField(db_column='INFDATE',
        blank=True, null=True)
    deststatus = models.SmallIntegerField(db_column='DESTSTATUS',
        blank=True, null=True)
    regtypref = models.IntegerField(db_column='REGTYPREF',
        blank=True, null=True)
    faprofitaccref = models.IntegerField(db_column='FAPROFITACCREF',
        blank=True, null=True)
    faprofitcentref = models.IntegerField(db_column='FAPROFITCENTREF',
        blank=True, null=True)
    falossaccref = models.IntegerField(db_column='FALOSSACCREF',
        blank=True, null=True)
    falosscentref = models.IntegerField(db_column='FALOSSCENTREF',
        blank=True, null=True)
    futmonthbegdate = models.IntegerField(db_column='FUTMONTHBEGDATE',
        blank=True, null=True)
    qctransferref = models.IntegerField(db_column='QCTRANSFERREF',
        blank=True, null=True)
    qctransferamnt = models.FloatField(db_column='QCTRANSFERAMNT',
        blank=True, null=True)
    gtipcode = models.CharField(db_column='GTIPCODE',
        max_length=25, blank=True, null=True)
    cpacode = models.CharField(db_column='CPACODE',
        max_length=25, blank=True, null=True)
    publiccountryref = models.IntegerField(db_column='PUBLICCOUNTRYREF',
        blank=True, null=True)
    futmonthcnt = models.SmallIntegerField(db_column='FUTMONTHCNT',
        blank=True, null=True)
    qproditemtype = models.SmallIntegerField(db_column='QPRODITEMTYPE',
        blank=True, null=True)
    futmonthenddate = models.DateTimeField(db_column='FUTMONTHENDDATE',
        blank=True, null=True)
    kkegvatcentref = models.IntegerField(db_column='KKEGVATCENTREF',
        blank=True, null=True)
    kkegvataccref = models.IntegerField(db_column='KKEGVATACCREF',
        blank=True, null=True)
    markingtagno = models.CharField(db_column='MARKINGTAGNO',
        max_length=21, blank=True, null=True)
    tcktaxnr = models.CharField(db_column='TCKTAXNR',
        max_length=16, blank=True, null=True)
    owner = models.CharField(db_column='OWNER',
        max_length=201, blank=True, null=True)
    mntorderfref = models.IntegerField(db_column='MNTORDERFREF',
        blank=True, null=True)
    kkegcentref = models.IntegerField(db_column='KKEGCENTREF',
        blank=True, null=True)
    kkegaccref = models.IntegerField(db_column='KKEGACCREF',
        blank=True, null=True)
    fakkegamount = models.FloatField(db_column='FAKKEGAMOUNT',
        blank=True, null=True)
    exprcntrref = models.IntegerField(db_column='EXPRCNTRREF',
        blank=True, null=True)
    expraccref = models.IntegerField(db_column='EXPRACCREF',
        blank=True, null=True)
    middlemanexptyp = models.SmallIntegerField(db_column='MIDDLEMANEXPTYP',
        blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_STLINE'
        unique_together = (
            ('faregref', 'date_field', 'logicalref'),
            (
                'detline', 'cancelled', 'offtransref',
                'trcode', 'logicalref',
                'amount', 'uinfo1', 'uinfo2'
            )
        )
        target_db = "erp"