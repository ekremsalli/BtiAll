"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_ORFLINE(
    BaseLogical,
    BaseClient,
    BaseCenter,
    BaseAccount,
    BaseAmount,
    BaseVAT,
    BaseUnit,
    BaseSalesMan,
    BaseSiteRec,
    BaseWF,
    BaseCancelled,
    BaseTextINC,
    BaseProject,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        ORFLINE tablosunda sipariş fişlerinin satırlarına ait kayıtlar
        bulunmaktadır. Sipariş fişlerinin stok, indirim, masraf ve promosyon
        satırları bu tabloda birer kayıt olarak yer almaktadır. Sipariş fişinin
        başlık bilgilerine ORDFICHE tablosundan ulalılabilir.
    """
    stockref = models.ForeignKey(
        "LG_ITEMS",
        db_column='STOCKREF',
        blank=True,
        null=True,
        help_text='Malzeme kartı ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_stockref"
    )
    ordficheref = models.ForeignKey(
        "LG_ORFICHE",
        db_column='ORDFICHEREF',
        blank=True,
        null=True,
        help_text='Sipariş fişi ref. -> ORFICHE',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_ordficheref"
    )
    linetype = models.SmallIntegerField(
        db_column='LINETYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Stok satırı'),
            (1, 'Promosyon'),
            (2, 'İndirim'),
            (3, 'Masraf'),
            (4, 'Hizmet'),
            (5, 'Depozito'),
            (6, 'Karma koli detayları'),
            (7, 'Sabit kıymet satırı')
        ],
        help_text='Satır tipi'
    )
    prevlineref = models.IntegerField(
        db_column='PREVLINEREF',
        blank=True,
        null=True,
        help_text='Üst malzeme sınıfı satır ref.'
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
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Malzeme sınıfı detay satırı'
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Alınan siparişler'),
            (2, 'Verilen siparişler')
        ],
        help_text='Fiş türü'
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
    globtrans = models.SmallIntegerField(
        db_column='GLOBTRANS',
        blank=True,
        null=True,
        choices=[
            (0, 'Satırda'),
            (1, 'Genelde')
        ],
        help_text='İndirim/Masraf ve Promosyon satırları'
    )
    calctype = models.SmallIntegerField(
        db_column='CALCTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Yüzde %'),
            (1, 'Fonksiyon f(x)'),
            (2, 'Tutar (TL)')
        ],
        help_text='Hesaplama türü'
    )
    vataccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='VATACCREF',
        blank=True,
        null=True,
        help_text='KDV muhasebe hesabı ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_vataccref",
    )
    vatcenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='VATCENTERREF',
        blank=True,
        null=True,
        help_text='KDV masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_vatcenterref"
    )
    praccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='PRACCREF',
        blank=True,
        null=True,
        help_text='Promosyon muhasebe ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_praccref"
    )
    prcenterref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='PRCENTERREF',
        blank=True,
        null=True,
        help_text='Promosyon masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_prcenterref"
    )
    prvataccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='PRVATACCREF',
        blank=True,
        null=True,
        help_text='Promosyon KDV\' sinin muhasebe ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_prvataccref"
    )
    prvatcenref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='PRVATCENREF',
        blank=True,
        null=True,
        help_text='Promosyon KDV\' sinin masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_prvatcenref"
    )
    promref = models.ForeignKey(
        "LG_PRCARDS",
        db_column='PROMREF',
        blank=True,
        null=True,
        help_text='Promosyon kartı ref. -> PRCARD',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_promref"
    )
    specode = models.CharField(
        db_column='SPECODE',
        max_length=17,
        blank=True,
        null=True,
        help_text='Özel kod'
    )
    delvrycode = models.CharField(
        db_column='DELVRYCODE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Teslimat kodu'
    )
    price = models.FloatField(
        db_column='PRICE',
        blank=True,
        null=True,
        help_text='Fiyat'
    )
    total = models.FloatField(
        db_column='TOTAL',
        blank=True,
        null=True,
        help_text='Toplam'
    )
    shippedamount = models.FloatField(
        db_column='SHIPPEDAMOUNT',
        blank=True,
        null=True,
        help_text='Sevk edilen miktar'
    )
    discper = models.FloatField(
        db_column='DISCPER',
        blank=True,
        null=True,
        help_text='İndirim yüzdesi'
    )
    distcost = models.FloatField(
        db_column='DISTCOST',
        blank=True,
        null=True,
        help_text='Satıra dağıtılan maliyet (karma koli)'
    )
    distdisc = models.FloatField(
        db_column='DISTDISC',
        blank=True,
        null=True,
        help_text='Satıra dağıtılan indirim (karma koli)'
    )
    distexp = models.FloatField(
        db_column='DISTEXP',
        blank=True,
        null=True,
        help_text='Satıra dağıtılan masraf (karma koli)'
    )
    distprom = models.FloatField(
        db_column='DISTPROM',
        blank=True,
        null=True,
        help_text='Satıra dağıtılan promosyon (karma koli)'
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
        help_text='KDV matrahı'
    )
    lineexp = models.CharField(
        db_column='LINEEXP',
        max_length=251,
        blank=True,
        null=True,
        help_text='Satır açıklaması'
    )
    vatinc = models.SmallIntegerField(
        db_column='VATINC',
        blank=True,
        null=True,
        help_text='KDV dahil / hariç'
    )
    closed = models.SmallIntegerField(
        db_column='CLOSED',
        blank=True,
        null=True,
        help_text='Sipariş kapalı (E/H)'
    )
    doreserve = models.SmallIntegerField(
        db_column='DORESERVE',
        blank=True,
        null=True,
        help_text='Mal rezerve edilecek (E/H)'
    )
    inuse = models.SmallIntegerField(
        db_column='INUSE',
        blank=True,
        null=True,
        help_text='Kullanılıyor (E/H)'
    )
    duedate = models.DateTimeField(
        db_column='DUEDATE',
        blank=True,
        null=True,
        help_text='Teslim tarihi'
    )
    prcurr = models.SmallIntegerField(
        db_column='PRCURR',
        blank=True,
        null=True,
        help_text='Fiyatlandırma döviz kuru'
    )
    prprice = models.FloatField(
        db_column='PRPRICE',
        blank=True,
        null=True,
        help_text='Fiyatlandırma döviz tutarı'
    )
    reportrate = models.FloatField(
        db_column='REPORTRATE',
        blank=True,
        null=True,
        help_text='Raporlama döviz tutarı'
    )
    billeditem = models.IntegerField(
        db_column='BILLEDITEM',
        blank=True,
        null=True,
        help_text='Faturalanması gereken mal'
    )
    paydefref = models.IntegerField(
        db_column='PAYDEFREF',
        blank=True,
        null=True,
        help_text='Ödeme planı ref. -> PAYPLANS'
    )
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ek dosya ref.'
    )
    cpstflag = models.SmallIntegerField(
        db_column='CPSTFLAG',
        blank=True,
        null=True,
        help_text='Karma koli satırı (E/H)'
    )
    sourceindex = models.SmallIntegerField(
        db_column='SOURCEINDEX',
        blank=True,
        null=True,
        help_text='Ambar numarası'
    )
    sourcecostgrp = models.SmallIntegerField(
        db_column='SOURCECOSTGRP',
        blank=True,
        null=True,
        help_text='Ambar maliyet grubu'
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
    linenet = models.FloatField(
        db_column='LINENET',
        blank=True,
        null=True,
        help_text='Net satır tutarı'
    )
    status = models.SmallIntegerField(
        db_column='STATUS',
        blank=True,
        null=True,
        choices=[
            (1, 'Öneri'),
            (2, 'Sevkedilemez'),
            (4, 'Sevkedilebilir')
        ],
        help_text='Onay bilgisi'
    )
    dref = models.IntegerField(
        db_column='DREF',
        blank=True,
        null=True,
        help_text='Satıra ait dağıtım şablonu kaydı ref. -> DISTTEMP'
    )
    trgflag = models.SmallIntegerField(
        db_column='TRGFLAG',
        blank=True,
        null=True,
        choices=[
            (0, 'Trigger kullanılacak'),
            (1, 'Trigger kullanılmayacak')
        ],
        help_text='Trigger bayrağı'
    )
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika no'
    )
    netdiscflag = models.SmallIntegerField(
        db_column='NETDISCFLAG', blank=True, null=True)
    netdiscperc = models.FloatField(
        db_column='NETDISCPERC', blank=True, null=True)
    netdiscamnt = models.FloatField(
        db_column='NETDISCAMNT', blank=True, null=True)
    conditionref = models.IntegerField(
        db_column='CONDITIONREF', blank=True, null=True)
    distreserved = models.FloatField(
        db_column='DISTRESERVED', blank=True, null=True)
    onvehicle = models.FloatField(
        db_column='ONVEHICLE', blank=True, null=True)
    campaignrefs1 = models.IntegerField(
        db_column='CAMPAIGNREFS1', blank=True, null=True)
    campaignrefs2 = models.IntegerField(
        db_column='CAMPAIGNREFS2', blank=True, null=True)
    campaignrefs3 = models.IntegerField(
        db_column='CAMPAIGNREFS3', blank=True, null=True)
    campaignrefs4 = models.IntegerField(
        db_column='CAMPAIGNREFS4', blank=True, null=True)
    campaignrefs5 = models.IntegerField(
        db_column='CAMPAIGNREFS5', blank=True, null=True)
    pointcampref = models.IntegerField(
        db_column='POINTCAMPREF', blank=True, null=True)
    camppoint = models.FloatField(
        db_column='CAMPPOINT', blank=True, null=True)
    promclasitemref = models.IntegerField(
        db_column='PROMCLASITEMREF', blank=True, null=True)
    reasonfornotshp = models.SmallIntegerField(
        db_column='REASONFORNOTSHP', blank=True, null=True)
    cmpglineref = models.IntegerField(
        db_column='CMPGLINEREF', blank=True, null=True)
    prrate = models.FloatField(
        db_column='PRRATE', blank=True, null=True)
    grossuinfo1 = models.FloatField(
        db_column='GROSSUINFO1', blank=True, null=True)
    grossuinfo2 = models.FloatField(
        db_column='GROSSUINFO2', blank=True, null=True)
    dempeggedamnt = models.FloatField(
        db_column='DEMPEGGEDAMNT', blank=True, null=True)
    offerref = models.IntegerField(
        db_column='OFFERREF', blank=True, null=True)
    orderparam = models.SmallIntegerField(
        db_column='ORDERPARAM', blank=True, null=True)
    itemasgref = models.IntegerField(
        db_column='ITEMASGREF', blank=True, null=True)
    eximamount = models.FloatField(
        db_column='EXIMAMOUNT', blank=True, null=True)
    offtransref = models.IntegerField(
        db_column='OFFTRANSREF', blank=True, null=True)
    orderedamount = models.FloatField(
        db_column='ORDEREDAMOUNT', blank=True, null=True)
    orglogoid = models.CharField(
        db_column='ORGLOGOID', max_length=25, blank=True, null=True)
    trcurr = models.SmallIntegerField(
        db_column='TRCURR', blank=True, null=True)
    trrate = models.FloatField(
        db_column='TRRATE', blank=True, null=True)
    withpaytrans = models.SmallIntegerField(
        db_column='WITHPAYTRANS', blank=True, null=True)
    pointcamprefs1 = models.IntegerField(
        db_column='POINTCAMPREFS1', blank=True, null=True)
    pointcamprefs2 = models.IntegerField(
        db_column='POINTCAMPREFS2', blank=True, null=True)
    pointcamprefs3 = models.IntegerField(
        db_column='POINTCAMPREFS3', blank=True, null=True)
    pointcamprefs4 = models.IntegerField(
        db_column='POINTCAMPREFS4', blank=True, null=True)
    camppoints1 = models.FloatField(
        db_column='CAMPPOINTS1', blank=True, null=True)
    camppoints2 = models.FloatField(
        db_column='CAMPPOINTS2', blank=True, null=True)
    camppoints3 = models.FloatField(
        db_column='CAMPPOINTS3', blank=True, null=True)
    camppoints4 = models.FloatField(
        db_column='CAMPPOINTS4', blank=True, null=True)
    cmpglinerefs1 = models.IntegerField(
        db_column='CMPGLINEREFS1', blank=True, null=True)
    cmpglinerefs2 = models.IntegerField(
        db_column='CMPGLINEREFS2', blank=True, null=True)
    cmpglinerefs3 = models.IntegerField(
        db_column='CMPGLINEREFS3', blank=True, null=True)
    cmpglinerefs4 = models.IntegerField(
        db_column='CMPGLINEREFS4', blank=True, null=True)
    prclistref = models.IntegerField(
        db_column='PRCLISTREF', blank=True, null=True)
    affectcollatrl = models.SmallIntegerField(
        db_column='AFFECTCOLLATRL', blank=True, null=True)
    fctyp = models.SmallIntegerField(
        db_column='FCTYP', blank=True, null=True)
    purchoffnr = models.SmallIntegerField(
        db_column='PURCHOFFNR', blank=True, null=True)
    demficheref = models.IntegerField(
        db_column='DEMFICHEREF', blank=True, null=True)
    demtransref = models.IntegerField(
        db_column='DEMTRANSREF', blank=True, null=True)
    altpromflag = models.SmallIntegerField(
        db_column='ALTPROMFLAG', blank=True, null=True)
    variantref = models.IntegerField(
        db_column='VARIANTREF', blank=True, null=True)
    reflvataccref = models.IntegerField(
        db_column='REFLVATACCREF', blank=True, null=True)
    reflvatothaccref = models.IntegerField(
        db_column='REFLVATOTHACCREF', blank=True, null=True)
    priority = models.SmallIntegerField(
        db_column='PRIORITY', blank=True, null=True)
    affectrisk = models.SmallIntegerField(
        db_column='AFFECTRISK', blank=True, null=True)
    bomref = models.IntegerField(
        db_column='BOMREF', blank=True, null=True)
    bomrevref = models.IntegerField(
        db_column='BOMREVREF', blank=True, null=True)
    routingref = models.IntegerField(
        db_column='ROUTINGREF', blank=True, null=True)
    operationref = models.IntegerField(
        db_column='OPERATIONREF', blank=True, null=True)
    wsref = models.IntegerField(
        db_column='WSREF', blank=True, null=True)
    addtaxrate = models.FloatField(
        db_column='ADDTAXRATE', blank=True, null=True)
    addtaxconvfact = models.FloatField(
        db_column='ADDTAXCONVFACT', blank=True, null=True)
    addtaxamount = models.FloatField(
        db_column='ADDTAXAMOUNT', blank=True, null=True)
    addtaxaccref = models.IntegerField(
        db_column='ADDTAXACCREF', blank=True, null=True)
    addtaxcenterref = models.IntegerField(
        db_column='ADDTAXCENTERREF', blank=True, null=True)
    addtaxamntisupd = models.SmallIntegerField(
        db_column='ADDTAXAMNTISUPD', blank=True, null=True)
    addtaxdiscamount = models.FloatField(
        db_column='ADDTAXDISCAMOUNT', blank=True, null=True)
    exaddtaxrate = models.FloatField(
        db_column='EXADDTAXRATE', blank=True, null=True)
    exaddtaxconvf = models.FloatField(
        db_column='EXADDTAXCONVF', blank=True, null=True)
    exaddtaxamnt = models.FloatField(
        db_column='EXADDTAXAMNT', blank=True, null=True)
    euvatstatus = models.IntegerField(
        db_column='EUVATSTATUS', blank=True, null=True)
    addtaxvatmatrah = models.FloatField(
        db_column='ADDTAXVATMATRAH', blank=True, null=True)
    camppaydefref = models.IntegerField(
        db_column='CAMPPAYDEFREF', blank=True, null=True)
    rprice = models.FloatField(
        db_column='RPRICE', blank=True, null=True)
    orgduedate = models.DateTimeField(
        db_column='ORGDUEDATE', blank=True, null=True)
    orgamount = models.FloatField(
        db_column='ORGAMOUNT', blank=True, null=True)
    orgprice = models.FloatField(
        db_column='ORGPRICE', blank=True, null=True)
    specode2 = models.CharField(
        db_column='SPECODE2', max_length=41, blank=True, null=True)
    reservedate = models.DateTimeField(
        db_column='RESERVEDATE', blank=True, null=True)
    candeduct = models.SmallIntegerField(
        db_column='CANDEDUCT', blank=True, null=True)
    underdeductlimit = models.SmallIntegerField(
        db_column='UNDERDEDUCTLIMIT', blank=True, null=True)
    globalid = models.CharField(
        db_column='GLOBALID', max_length=51, blank=True, null=True)
    deductionpart1 = models.SmallIntegerField(
        db_column='DEDUCTIONPART1', blank=True, null=True)
    deductionpart2 = models.SmallIntegerField(
        db_column='DEDUCTIONPART2', blank=True, null=True)
    parentlnref = models.IntegerField(
        db_column='PARENTLNREF', blank=True, null=True)
    distexpvat = models.FloatField(
        db_column='DISTEXPVAT', blank=True, null=True)
    shippedamntsugg = models.FloatField(
        db_column='SHIPPEDAMNTSUGG', blank=True, null=True)
    reserveamount = models.FloatField(
        db_column='RESERVEAMOUNT', blank=True, null=True)
    deductcode = models.CharField(
        db_column='DEDUCTCODE', max_length=11, blank=True, null=True)
    bomtype = models.SmallIntegerField(
        db_column='BOMTYPE', blank=True, null=True)
    devir = models.SmallIntegerField(
        db_column='DEVIR', blank=True, null=True)
    faregref = models.IntegerField(
        db_column='FAREGREF', blank=True, null=True)
    cpacode = models.CharField(
        db_column='CPACODE', max_length=25, blank=True, null=True)
    gtipcode = models.CharField(
        db_column='GTIPCODE', max_length=25, blank=True, null=True)
    publiccountryref = models.IntegerField(
        db_column='PUBLICCOUNTRYREF', blank=True, null=True)
    ataxexceptreason = models.CharField(
        db_column='ATAXEXCEPTREASON', max_length=201, blank=True, null=True)
    vatexceptcode = models.CharField(
        db_column='VATEXCEPTCODE', max_length=11, blank=True, null=True)
    vatexceptreason = models.CharField(
        db_column='VATEXCEPTREASON', max_length=201, blank=True, null=True)
    ataxexceptcode = models.CharField(
        db_column='ATAXEXCEPTCODE', max_length=11, blank=True, null=True)
    distdiscvat = models.FloatField(
        db_column='DISTDISCVAT', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_ORFLINE'
        unique_together = (('orglogicref', 'logicalref', 'siteid'),)
        target_db = 'erp'

