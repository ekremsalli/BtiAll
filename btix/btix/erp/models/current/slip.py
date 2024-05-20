"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_CLFLINE(
    BaseLogical,
    BaseCode,
    BaseInfo,
    BaseSiteRec,
    BaseBranch,
    BaseAccounted,
    BaseAmount,
    BaseSign,
    BaseGUID,
    BasePrint,
    BaseCancelled,
    BaseTrading,
    BaseSalesMan,
    models.Model):
    """
        Cari hesap hareketleri
        CLFLINE tablosunda cari hesap fişleri ile cari hesabı borçlandıran
        ya da alacaklandıran fatura, çek/senet, bordrosu, banka havale
        fişi gibi fişlerden sonra oluşan cari hesap hareketi
        kayıtları yer almaktadır. Belli bir ayın belli bir aralığına
        ait cari hesap toplamı almak için ay içerisinde belirtilen
        aralığa ait tarihlerdeki kayıtlar incelenmelidir.
    """
    clientref = models.ForeignKey(
        "LG_CLCARD",
        db_column='CLIENTREF',
        blank=True,
        null=True,
        help_text='Cari hesap ref. -> CLCARD',
        on_delete=models.DO_NOTHING
    )
    claccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='CLACCREF',
        blank=True,
        null=True,
        help_text='Cari hesap muhasebe hesabı ref. -> EMUHACC',
        on_delete=models.DO_NOTHING
    )
    clcenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='CLCENTERREF',
        blank=True,
        null=True,
        help_text='Cari hesap masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_clcenterref"
    )
    cashcenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='CASHCENTERREF',
        blank=True,
        null=True,
        help_text='Kasa masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_cashcenterref"
    )
    cashaccountref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='CASHACCOUNTREF',
        blank=True,
        null=True,
        help_text='Kasa muhasebe hesabı ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_cashaccountref"
    )
    virmanref = models.IntegerField(
        db_column='VIRMANREF',
        blank=True,
        null=True,
        help_text='Virman satırı ref.'
    )
    sourcefref = models.IntegerField(
        db_column='SOURCEFREF',
        blank=True,
        null=True,
        help_text='İlgili modüldeki ilgili fişin ref.'
    )
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
            (10, 'Kasa')
        ],
        help_text='Modül numarası'
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Nakit tahsilat'),
            (2, 'Nakit ödeme'),
            (3, 'Borç dekontu'),
            (4, 'Alacak dekontu'),
            (5, 'Virman işlemi'),
            (6, 'Kur farkı işlemi'),
            (12, 'Özel işlem'),
            (20, 'Gelen havaleler'),
            (21, 'Gönderilen havaleler'),
            (31, 'Mal alım faturası'),
            (32, 'Perakende satış iade'),
            (33, 'Toptan satış iade'),
            (34, 'Alınan hizmet faturası'),
            (35, 'Alınan proforma fatura'),
            (36, 'Alım iade faturası'),
            (37, 'Perakende satış faturası'),
            (38, 'Toptan satış faturası'),
            (39, 'Verilen hizmet faturası'),
            (40, 'Verilen proforma fatura'),
            (41, 'Verilen vade farkı faturası'),
            (42, 'Alınan vade farkı faturası'),
            (43, 'Alınan fiyat farkı faturası'),
            (44, 'Verilen fiyat farkı faturası'),
            (56, 'Müstahsil makbuzu'),
            (61, 'Çek girişi'),
            (62, 'Senet girişi'),
            (63, 'Çek çıkış cari hesaba'),
            (64, 'Senet çıkış cari hesaba')
        ],
        help_text='Hareket türü'
    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Hareket türü virman (E/H)'
    )
    tranno = models.CharField(
        db_column='TRANNO',
        max_length=17,
        blank=True,
        null=True,
        help_text='İşlem no'
    )
    docode = models.CharField(
        db_column='DOCODE',
        max_length=33,
        blank=True,
        null=True,
        help_text='Belge numarası'
    )
    lineexp = models.CharField(
        db_column='LINEEXP',
        max_length=251,
        blank=True,
        null=True,
        help_text='Hareket açıklaması'
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
        help_text='İşlem dövizi kuru'
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
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ekstra dosya ref.'
    )
    paydefref = models.ForeignKey(
        "LG_PAYPLANS",
        db_column='PAYDEFREF',
        blank=True,
        null=True,
        help_text='Ödeme planı ref. -> PAYPLANS',
        on_delete=models.DO_NOTHING
    )
    accficheref = models.ForeignKey(
        "LG_EMFICHE",
        db_column='ACCFICHEREF',
        blank=True,
        null=True,
        help_text='Muhasebe fişi ref. -> EMFICHE',
        on_delete=models.DO_NOTHING
    )
    trgflag = models.SmallIntegerField(
        db_column='TRGFLAG', blank=True,
        null=True,
        choices=[
            (0, 'Trigger kullanılacak'),
            (1, 'Trigger kullanılmayacak')
        ],
        help_text="Trigger bayrağı"
    )
    lineexctyp = models.SmallIntegerField(
        db_column='LINEEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (satırı)'
    )
    department = models.SmallIntegerField(
        db_column='DEPARTMENT',
        blank=True,
        null=True
    )

    onlyonepayline = models.SmallIntegerField(db_column='ONLYONEPAYLINE',
        blank=True, null=True, help_text='Tek satırlı ödeme planı')
    discflag = models.SmallIntegerField(db_column='DISCFLAG',
        blank=True, null=True, help_text='İndirim satırı işareti')
    discrate = models.FloatField(db_column='DISCRATE', blank=True, null=True,
        help_text='İndirim oranı'
    )
    vatrate = models.FloatField(db_column='VATRATE', blank=True, null=True,
        help_text='KDV oranı'
    )
    cashamount = models.FloatField(db_column='CASHAMOUNT', blank=True,
        null=True, help_text='Nakit (İndirimli)')
    discaccref = models.IntegerField(db_column='DISCACCREF', blank=True,
        null=True, help_text='İndirim genel muhasebe hesabı ref.')
    disccenref = models.IntegerField(db_column='DISCCENREF', blank=True,
        null=True, help_text='İndirim masraf merkezi ref.')
    vatraccref = models.IntegerField(db_column='VATRACCREF', blank=True,
        null=True, help_text='KDV muhasebe hesabı ref.')
    vatrcenref = models.IntegerField(db_column='VATRCENREF', blank=True,
        null=True, help_text='KDV masraf merkezi ref.')
    paymentref = models.IntegerField(db_column='PAYMENTREF', blank=True,
        null=True, help_text='Ödeme planı ref.')
    vatamount = models.FloatField(db_column='VATAMOUNT', blank=True,
        null=True, help_text='KDV tutarı')
    orglogicref = models.IntegerField(db_column='ORGLOGICREF', blank=True,
        null=True, help_text='Orjinal kayıt ref.')
    infidx = models.FloatField(db_column='INFIDX', blank=True,
        null=True, help_text='Enflasyon endeksi')
    poscommaccref = models.IntegerField(db_column='POSCOMMACCREF',
        blank=True, null=True, help_text='Genel muhasebe hesapları ref.')
    poscommcenref = models.IntegerField(db_column='POSCOMMCENREF',
        blank=True, null=True, help_text='Masraf merkezi ref.')
    pointcommaccref = models.IntegerField(db_column='POINTCOMMACCREF',
        blank=True, null=True, help_text='Genel muhasebe hesapları ref.')
    pointcommcenref = models.IntegerField(db_column='POINTCOMMCENREF',
        blank=True, null=True, help_text='Masraf merkezi ref.')
    cheqinfo = models.CharField(db_column='CHEQINFO', max_length=121,
        blank=True, null=True, help_text='Çek bilgisi (1)')
    creditcno = models.CharField(db_column='CREDITCNO', max_length=25,
        blank=True, null=True, help_text='Çek bilgisi (2)')
    clprjref = models.IntegerField(db_column='CLPRJREF', blank=True,
        null=True, help_text='Proje ref.')
    status = models.SmallIntegerField(db_column='STATUS', blank=True,
        null=True)
    eximfileref = models.IntegerField(db_column='EXIMFILEREF', blank=True,
        null=True)
    eximprocnr = models.SmallIntegerField(db_column='EXIMPROCNR', blank=True,
        null=True)
    month_field = models.SmallIntegerField(db_column='MONTH_', blank=True,
        null=True)
    year_field = models.SmallIntegerField(db_column='YEAR_', blank=True,
        null=True)
    fundsharerat = models.FloatField(db_column='FUNDSHARERAT', blank=True,
        null=True)
    affectcollatrl = models.SmallIntegerField(db_column='AFFECTCOLLATRL',
        blank=True, null=True)
    grpfirmtrans = models.SmallIntegerField(db_column='GRPFIRMTRANS',
        blank=True, null=True)
    reflvataccref = models.IntegerField(db_column='REFLVATACCREF',
        blank=True, null=True)
    reflvatothaccref = models.IntegerField(db_column='REFLVATOTHACCREF',
        blank=True, null=True)
    affectrisk = models.SmallIntegerField(db_column='AFFECTRISK',
        blank=True, null=True)
    batchnr = models.IntegerField(db_column='BATCHNR',
        blank=True, null=True)
    approvenr = models.IntegerField(db_column='APPROVENR',
        blank=True, null=True)
    batchnum = models.CharField(db_column='BATCHNUM', max_length=17,
        blank=True, null=True)
    approvenum = models.CharField(db_column='APPROVENUM', max_length=17,
        blank=True, null=True)
    euvatstatus = models.IntegerField(db_column='EUVATSTATUS',
        blank=True, null=True)
    orglogoid = models.CharField(db_column='ORGLOGOID', max_length=25,
        blank=True, null=True)
    eximtype = models.SmallIntegerField(db_column='EXIMTYPE',
        blank=True, null=True)
    eidistflnnr = models.SmallIntegerField(db_column='EIDISTFLNNR',
        blank=True, null=True)
    eisrvdsttyp = models.SmallIntegerField(db_column='EISRVDSTTYP',
        blank=True, null=True)
    eximdisttyp = models.SmallIntegerField(db_column='EXIMDISTTYP',
        blank=True, null=True)
    bankaccref = models.IntegerField(db_column='BANKACCREF',
        blank=True, null=True)
    bnaccref = models.IntegerField(db_column='BNACCREF',
        blank=True, null=True)
    bncenterref = models.IntegerField(db_column='BNCENTERREF',
        blank=True, null=True)
    devirprocdate = models.DateTimeField(db_column='DEVIRPROCDATE',
        blank=True, null=True)
    docdate = models.DateTimeField(db_column='DOCDATE',
        blank=True, null=True)
    instalref = models.IntegerField(db_column='INSTALREF', blank=True,
        null=True)
    devir = models.SmallIntegerField(db_column='DEVIR', blank=True, null=True)
    devirmodulenr = models.IntegerField(db_column='DEVIRMODULENR', blank=True,
        null=True)
    ftime = models.IntegerField(db_column='FTIME', blank=True, null=True)
    offerref = models.IntegerField(db_column='OFFERREF', blank=True, null=True)
    retccfcref = models.IntegerField(db_column='RETCCFCREF',
        blank=True, null=True)
    emflineref = models.IntegerField(db_column='EMFLINEREF',
        blank=True, null=True)
    fromexchdiff = models.SmallIntegerField(db_column='FROMEXCHDIFF',
        blank=True, null=True)
    candeduct = models.SmallIntegerField(db_column='CANDEDUCT',
        blank=True, null=True)
    deductionpart1 = models.SmallIntegerField(db_column='DEDUCTIONPART1',
        blank=True, null=True)
    deductionpart2 = models.SmallIntegerField(db_column='DEDUCTIONPART2',
        blank=True, null=True)
    underdeductlimit = models.SmallIntegerField(db_column='UNDERDEDUCTLIMIT',
        blank=True, null=True)
    vatdeductrate = models.FloatField(db_column='VATDEDUCTRATE',
        blank=True, null=True)
    vatdeductaccref = models.IntegerField(db_column='VATDEDUCTACCREF',
        blank=True, null=True)
    vatdeductothaccref = models.IntegerField(db_column='VATDEDUCTOTHACCREF',
        blank=True, null=True)
    vatdeductcenref = models.IntegerField(db_column='VATDEDUCTCENREF',
        blank=True, null=True)
    vatdeductothcenref = models.IntegerField(db_column='VATDEDUCTOTHCENREF',
        blank=True, null=True)
    cantcrededuct = models.SmallIntegerField(db_column='CANTCREDEDUCT',
        blank=True, null=True)
    paidincash = models.SmallIntegerField(db_column='PAIDINCASH',
        blank=True, null=True)
    brutamount = models.FloatField(db_column='BRUTAMOUNT',
        blank=True, null=True)
    netamount = models.FloatField(db_column='NETAMOUNT',
        blank=True, null=True)
    brutamounttr = models.FloatField(db_column='BRUTAMOUNTTR',
        blank=True, null=True)
    netamounttr = models.FloatField(db_column='NETAMOUNTTR',
        blank=True, null=True)
    brutamountrep = models.FloatField(db_column='BRUTAMOUNTREP',
        blank=True, null=True)
    netamountrep = models.FloatField(db_column='NETAMOUNTREP',
        blank=True, null=True)
    bnlntrcurr = models.SmallIntegerField(db_column='BNLNTRCURR',
        blank=True, null=True)
    bnlntrrate = models.FloatField(db_column='BNLNTRRATE',
        blank=True, null=True)
    bnlntrnet = models.FloatField(db_column='BNLNTRNET',
        blank=True, null=True)
    printdate = models.DateTimeField(db_column='PRINTDATE',
        blank=True, null=True)
    incdeductamnt = models.SmallIntegerField(db_column='INCDEDUCTAMNT',
        blank=True, null=True)
    affectcost = models.SmallIntegerField(db_column='AFFECTCOST',
        blank=True, null=True)
    forexim = models.SmallIntegerField(db_column='FOREXIM',
        blank=True, null=True)
    eximfilecodeclf = models.CharField(db_column='EXIMFILECODECLF',
        max_length=25, blank=True, null=True)
    specode2 = models.CharField(db_column='SPECODE2', max_length=41,
        blank=True, null=True)
    servreasondef = models.CharField(db_column='SERVREASONDEF',
        max_length=251, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_CLFLINE'
        target_db = 'erp'