"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_BNFLINE(
    BaseLogical,
    BaseCode,
    BaseClient,
    BaseAccount,
    BaseCenter,
    BaseBranch,
    BaseAmount,
    BaseSign,
    BaseAccounted,
    BaseProject,
    BasePrint,
    BaseCancelled,
    BaseSiteRec,
    BaseSalesMan,
    BaseGUID,
    BaseTrading,
    models.Model):
    """
        Banka hareketleri
    """
    bankref = models.ForeignKey(
        "LG_BNCARD",
        db_column='BANKREF',
        blank=True,
        null=True,
        help_text='Banka ref. -> BNCARD',
        on_delete=models.DO_NOTHING
    )
    bnaccref = models.ForeignKey(
        "LG_BANKACC",
        db_column='BNACCREF',
        blank=True,
        null=True,
        help_text='Banka hesabı ref. -> BANKACC',
        on_delete=models.DO_NOTHING
    )
    bnaccountref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='BNACCOUNTREF',
        blank=True,
        null=True,
        help_text='Banka muhasebe kodu ref. -> EMUHACC',
        on_delete=models.DO_NOTHING
    )
    bncenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='BNCENTERREF',
        blank=True,
        null=True,
        help_text='Banka masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING
    )
    virmanref = models.IntegerField(
        db_column='VIRMANREF',
        blank=True,
        null=True,
        help_text='Virman satırı ref.'
    )
    sourcefref = models.ForeignKey(
        "LG_BNFICHE",
        db_column='SOURCEFREF',
        blank=True,
        null=True,
        help_text='İlgili satırdaki ilgili fişin ref. -> BNFICHE',
        on_delete=models.DO_NOTHING
    )
    transtype = models.SmallIntegerField(
        db_column='TRANSTYPE',
        blank=True,
        null=True,
        help_text="""
            Hareket türü;
            Ticari hesap ->
                1. Cari hesap
                2. Takas senetleri
                3. Takas çekleri
                4. Kesilen çekler
            Kredi hesabı
                1. Teminat senetleri
                2. Teminat çekleri
                3. Senet karşılığı kredi
                4. Çek karşılığı kredi
        """
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
            (1, 'Banka işlem'),
            (2, 'Virman işlemi'),
            (3, 'Gelen havale'),
            (4, 'Gönderilen havale'),
            (5, 'Açılış işlemi')
        ],
        help_text='İşlem türü')
    modulenr = models.SmallIntegerField(
        db_column='MODULENR',
        blank=True,
        null=True,
        choices=[
            (6, 'Çek/Senet'),
            (7, 'Banka'),
            (10, 'Kasa')
        ],
        help_text="Hareket türü"

    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    tranno = models.CharField(
        db_column='TRANNO',
        max_length=17,
        blank=True,
        null=True,
        help_text='Hareket numarası'
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
        max_length=201,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    trcurr = models.SmallIntegerField(
        db_column='TRCURR',
        blank=True,
        null=True,
        help_text='Hareket dövizi'
    )
    trrate = models.FloatField(
        db_column='TRRATE',
        blank=True,
        null=True,
        help_text='Hareket dövizi kuru'
    )
    trnet = models.FloatField(
        db_column='TRNET',
        blank=True,
        null=True,
        help_text='Hareket dövizi tutarı')
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
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ekstra dosya ref.'
    )
    accficheref = models.ForeignKey(
        "LG_EMFICHE",
        db_column='ACCFICHEREF',
        blank=True,
        null=True,
        help_text='Muhasebe fişi ref. -> EMFICHE',
        on_delete=models.DO_NOTHING
    )
    clbnbranchno = models.CharField(
        db_column='CLBNBRANCHNO',
        max_length=17,
        blank=True,
        null=True,
        help_text='Cari hesap banka numarası'
    )
    clbnaccountno = models.CharField(
        db_column='CLBNACCOUNTNO',
        max_length=51,
        blank=True,
        null=True,
        help_text='Cari hesap banka hesap numarası'
    )
    bntrackingno = models.CharField(
        db_column='BNTRACKINGNO',
        max_length=51,
        blank=True,
        null=True,
        help_text='Banka izleme numarası'
    )
    trnstate = models.SmallIntegerField(
        db_column='TRNSTATE',
        blank=True,
        null=True,
        help_text='İşlem durumu'
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
    discflag = models.SmallIntegerField(db_column='DISCFLAG', blank=True,
        null=True, help_text='İndirim satırı (Evet/Hayır)')
    discrate = models.FloatField(db_column='DISCRATE', blank=True,
        null=True, help_text='İndirim oranı')
    vatrate = models.FloatField(db_column='VATRATE', blank=True,
        null=True, help_text='KDV Oranı')
    arcloseamount = models.FloatField(db_column='ARCLOSEAMOUNT', blank=True,
        null=True, help_text='?')
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
    bankproctype = models.SmallIntegerField(db_column='BANKPROCTYPE',
        blank=True, null=True, help_text='Banka hareket türü')
    bankproccode = models.SmallIntegerField(db_column='BANKPROCCODE',
        blank=True, null=True, help_text='Banka hareket kodu')
    transduedate = models.DateTimeField(db_column='TRANSDUEDATE', blank=True,
        null=True, help_text='Hareket tarihi')
    orglogicref = models.IntegerField(db_column='ORGLOGICREF', blank=True,
        null=True, help_text='Orjinal kayıt ref.')
    opstat = models.SmallIntegerField(db_column='OPSTAT', blank=True,
        null=True, help_text='Hareket durumu')
    infidx = models.FloatField(db_column='INFIDX', blank=True,
        null=True, help_text='Enflasyon endeksi')
    eximficheno = models.CharField(db_column='EXIMFICHENO', max_length=31,
        blank=True, null=True, help_text='İthalat/İhracat fiş numarası')
    bntranvatinc = models.SmallIntegerField(db_column='BNTRANVATINC',
        blank=True, null=True, help_text='KDV dahil/hariç')
    bntranvatrat = models.FloatField(db_column='BNTRANVATRAT', blank=True,
        null=True, help_text='KDV oranı')
    bntranvataccref = models.IntegerField(db_column='BNTRANVATACCREF',
        blank=True, null=True, help_text='KDV muhasebe hesabı ref.')
    bntranvatcenref = models.IntegerField(db_column='BNTRANVATCENREF',
        blank=True, null=True, help_text='KDV masraf merkezi ref.')
    bntranvattot = models.FloatField(db_column='BNTRANVATTOT', blank=True,
        null=True, help_text='KDV tutarı')
    cheqinfo = models.CharField(db_column='CHEQINFO', max_length=121,
        blank=True, null=True, help_text='Çek bilgisi')
    eximinforef = models.IntegerField(db_column='EXIMINFOREF', blank=True,
        null=True, help_text='INVEXINFO ref.')
    eximinfopar = models.FloatField(db_column='EXIMINFOPAR', blank=True,
        null=True, help_text='Eximbank kredisi paritesi')
    excreref = models.IntegerField(db_column='EXCREREF', blank=True,
        null=True, help_text='İhracat kredisi ref.')
    crcardwzd = models.SmallIntegerField(db_column='CRCARDWZD', blank=True,
        null=True,
        help_text="""
            Ödeme oto oluşturuldu,
                0->Hayır
                1->Oto+kredi kartı
                2->Oto+kred kartı slipi
        """
    )
    comstype = models.SmallIntegerField(db_column='COMSTYPE', blank=True,
        null=True,
        help_text="""
            Komisyon türü;
            1 -> Puan komisyonu
            2 -> Hizmet komisyonu

        """
    )
    provisionref = models.IntegerField(db_column='PROVISIONREF', blank=True,
        null=True, help_text='?')
    trangrplineno = models.SmallIntegerField(db_column='TRANGRPLINENO',
        blank=True, null=True, help_text='Hareket grup numarası (fiş satırı)')
    trangrpdate = models.DateTimeField(db_column='TRANGRPDATE', blank=True,
        null=True, help_text='Hareket grup tarihi')
    trangrpno = models.CharField(db_column='TRANGRPNO', max_length=17,
        blank=True, null=True, help_text='Hareket grup numrası (öndeğer)')
    bankrefnr = models.CharField(db_column='BANKREFNR', max_length=25,
        blank=True, null=True, help_text='Banka referans numarası')
    customdocnr = models.CharField(db_column='CUSTOMDOCNR', max_length=17,
        blank=True, null=True)
    dablnref = models.IntegerField(db_column='DABLNREF', blank=True, null=True)
    transref = models.IntegerField(db_column='TRANSREF', blank=True, null=True)
    affectcollatrl = models.SmallIntegerField(db_column='AFFECTCOLLATRL',
        blank=True, null=True)
    collatrollref = models.IntegerField(db_column='COLLATROLLREF', blank=True,
        null=True)
    collattrnref = models.IntegerField(db_column='COLLATTRNREF', blank=True,
        null=True)
    collatcardref = models.IntegerField(db_column='COLLATCARDREF', blank=True,
        null=True)
    grpfirmtrans = models.SmallIntegerField(db_column='GRPFIRMTRANS',
        blank=True, null=True)
    affectrisk = models.SmallIntegerField(db_column='AFFECTRISK', blank=True,
        null=True)
    bncrsource = models.SmallIntegerField(db_column='BNCRSOURCE', blank=True,
        null=True)
    bncrref = models.IntegerField(db_column='BNCRREF', blank=True, null=True)
    bncrlntype = models.SmallIntegerField(db_column='BNCRLNTYPE', blank=True,
        null=True)
    orglogoid = models.CharField(db_column='ORGLOGOID', max_length=25,
        blank=True, null=True)
    cstransref = models.IntegerField(db_column='CSTRANSREF', blank=True,
        null=True)
    reflected = models.SmallIntegerField(db_column='REFLECTED', blank=True,
        null=True)
    reflaccficheref = models.IntegerField(db_column='REFLACCFICHEREF',
        blank=True, null=True)
    iban = models.CharField(db_column='IBAN', max_length=51,
        blank=True, null=True)
    bankbranchs = models.CharField(db_column='BANKBRANCHS', max_length=25,
        blank=True, null=True)
    bankaccounts = models.CharField(db_column='BANKACCOUNTS', max_length=51,
        blank=True, null=True)
    costowner = models.SmallIntegerField(db_column='COSTOWNER',
        blank=True, null=True)
    costaccount = models.CharField(db_column='COSTACCOUNT', max_length=25,
        blank=True, null=True)
    costaccref = models.IntegerField(db_column='COSTACCREF',
        blank=True, null=True)
    costtot = models.FloatField(db_column='COSTTOT', blank=True, null=True)
    bsmvtot = models.FloatField(db_column='BSMVTOT', blank=True, null=True)
    bntrcostaccref = models.IntegerField(db_column='BNTRCOSTACCREF',
        blank=True, null=True)
    bntrcostcenref = models.IntegerField(db_column='BNTRCOSTCENREF',
        blank=True, null=True)
    bnbsmvaccref = models.IntegerField(db_column='BNBSMVACCREF',
        blank=True, null=True)
    bnbsmvcenref = models.IntegerField(db_column='BNBSMVCENREF',
        blank=True, null=True)
    repcosttot = models.FloatField(db_column='REPCOSTTOT',
        blank=True, null=True)
    repbsmvtot = models.FloatField(db_column='REPBSMVTOT',
        blank=True, null=True)
    trcosttot = models.FloatField(db_column='TRCOSTTOT', blank=True, null=True)
    trbsmvtot = models.FloatField(db_column='TRBSMVTOT', blank=True, null=True)
    cltrcurr = models.SmallIntegerField(db_column='CLTRCURR',
        blank=True, null=True)
    cltrrate = models.FloatField(db_column='CLTRRATE', blank=True, null=True)
    cltrnet = models.FloatField(db_column='CLTRNET', blank=True, null=True)
    bnintaccref = models.IntegerField(db_column='BNINTACCREF',
        blank=True, null=True)
    bnintcenref = models.IntegerField(db_column='BNINTCENREF',
        blank=True, null=True)
    bnkkdfaccref = models.IntegerField(db_column='BNKKDFACCREF',
        blank=True, null=True)
    bnkkdfcenref = models.IntegerField(db_column='BNKKDFCENREF', blank=True,
        null=True)
    bnfincostaccref = models.IntegerField(db_column='BNFINCOSTACCREF',
        blank=True, null=True)
    bnfincostcenref = models.IntegerField(db_column='BNFINCOSTCENREF',
        blank=True, null=True)
    dbs = models.SmallIntegerField(db_column='DBS', blank=True, null=True)
    clflineref = models.IntegerField(db_column='CLFLINEREF', blank=True,
        null=True)
    kkblockedref = models.IntegerField(db_column='KKBLOCKEDREF', blank=True,
        null=True)
    clficheref = models.IntegerField(db_column='CLFICHEREF', blank=True,
        null=True)
    creletterref = models.IntegerField(db_column='CRELETTERREF', blank=True,
        null=True)
    offerref = models.IntegerField(db_column='OFFERREF', blank=True, null=True)
    bntrancosttotinc = models.SmallIntegerField(db_column='BNTRANCOSTTOTINC',
        blank=True, null=True)
    crcardfcref = models.IntegerField(db_column='CRCARDFCREF', blank=True,
        null=True)
    ccpaytrref = models.IntegerField(db_column='CCPAYTRREF', blank=True,
        null=True)
    emflineref = models.IntegerField(db_column='EMFLINEREF', blank=True,
        null=True)
    docdate = models.DateTimeField(db_column='DOCDATE', blank=True, null=True)
    bntrcostaccref2 = models.IntegerField(db_column='BNTRCOSTACCREF2',
        blank=True, null=True)
    bncrtrrate = models.FloatField(db_column='BNCRTRRATE', blank=True,
        null=True)
    printdate = models.DateTimeField(db_column='PRINTDATE', blank=True,
        null=True)
    processaccref = models.IntegerField(db_column='PROCESSACCREF', blank=True,
        null=True)
    processcenref = models.IntegerField(db_column='PROCESSCENREF', blank=True,
        null=True)
    custtitle = models.CharField(db_column='CUSTTITLE', max_length=201,
        blank=True, null=True)
    bngpaddr = models.CharField(db_column='BNGPADDR', max_length=201,
        blank=True, null=True)
    bngpplate = models.CharField(db_column='BNGPPLATE', max_length=17,
        blank=True, null=True)
    bngptaxaccref = models.IntegerField(db_column='BNGPTAXACCREF', blank=True,
        null=True)
    bngptaxcenref = models.IntegerField(db_column='BNGPTAXCENREF', blank=True,
        null=True)
    bngpfundaccref = models.IntegerField(db_column='BNGPFUNDACCREF', blank=True,
        null=True)
    bngpfundcenref = models.IntegerField(db_column='BNGPFUNDCENREF',
        blank=True, null=True)
    bngpoptype = models.SmallIntegerField(db_column='BNGPOPTYPE', blank=True,
        null=True)
    bngpincometaxrat = models.FloatField(db_column='BNGPINCOMETAXRAT',
        blank=True, null=True)
    bngpfundsharerat = models.FloatField(db_column='BNGPFUNDSHARERAT',
        blank=True, null=True)
    typecode = models.CharField(db_column='TYPECODE', max_length=5,
        blank=True, null=True)
    fundquantity = models.FloatField(db_column='FUNDQUANTITY',
        blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (
            ('transtype', 'ccpaytrref', 'bankproctype', 'logicalref', 'trnet'),
            ('bnaccref', 'logicalref', 'sourcefref'),
        )
        db_table = f'LG_{Active.namespace}_{Active.period}_BNFLINE'
        target_db = 'erp'