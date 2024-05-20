"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_FAREGIST(
    BaseLogical,
    BaseCenter,
    BaseGUID,
    BaseProject,
    BaseInfo,
    BaseSiteRec,
    BaseCancelled,
    BaseBranch,
    models.Model):
    """
        Sabit kıymet kayıtları
    """
    regcode = models.CharField(
        db_column='REGCODE',
        unique=True,
        max_length=17,
        blank=True,
        null=True,
        help_text='Kayıt kodu'
    )
    department = models.SmallIntegerField(
        db_column='DEPARTMENT',
        blank=True,
        null=True,
        help_text='Bölüm'
    )
    transfer = models.SmallIntegerField(
        db_column='TRANSFER',
        blank=True,
        null=True,
        choices=[
            (1, 'Devir'),
            (0, 'Yeni kayıt')
        ],
        help_text='1 -> Devir, 0 -> Yeni kayıt'
    )
    crdref = models.ForeignKey(
        "LG_ITEMS",
        db_column='CRDREF',
        blank=True,
        null=True,
        help_text='Kayıt ref. -> ITEMS',
        on_delete=models.DO_NOTHING
    )
    ficheref = models.ForeignKey(
        "LG_STFICHE",
        db_column='FICHEREF',
        blank=True,
        null=True,
        help_text='Hareket ref. (stok fişi / irsaliye) -> STFICHE',
        on_delete=models.DO_NOTHING
    )
    datein = models.DateTimeField(
        db_column='DATEIN',
        blank=True,
        null=True,
        help_text='Alım tarihi'
    )
    dateofdepr = models.DateTimeField(
        db_column='DATEOFDEPR',
        blank=True,
        null=True,
        help_text='Amortisman başlangıçı'
    )
    quantity = models.FloatField(
        db_column='QUANTITY',
        blank=True,
        null=True,
        help_text='Miktar'
    )
    totout = models.FloatField(
        db_column='TOTOUT',
        blank=True,
        null=True,
        help_text='Düşülen miktar'
    )
    invalue = models.FloatField(
        db_column='INVALUE',
        blank=True,
        null=True,
        help_text='Giriş maliyeti'
    )
    vatamount = models.FloatField(
        db_column='VATAMOUNT',
        blank=True,
        null=True,
        help_text='Ödenecek KDV'
    )
    vatdur = models.SmallIntegerField(
        db_column='VATDUR',
        blank=True,
        null=True,
        help_text='KDV ödeme süresi'
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
    deprtype = models.SmallIntegerField(
        db_column='DEPRTYPE',
        blank=True,
        null=True,
        help_text='Amortisman türü'
    )
    revflag = models.SmallIntegerField(
        db_column='REVFLAG',
        blank=True,
        null=True,
        help_text='Yeniden değerlenecek (E/H)'
    )
    revdepflag = models.SmallIntegerField(
        db_column='REVDEPFLAG',
        blank=True,
        null=True,
        help_text='Değerleme amortismanı (E/H)'
    )
    partdep = models.SmallIntegerField(
        db_column='PARTDEP',
        blank=True,
        null=True,
        help_text='Kıst amotismanı'
    )
    reportrate = models.FloatField(
        db_column='REPORTRATE',
        blank=True,
        null=True,
        help_text='Raporlama döviz kuru'
    )
    invaluex = models.FloatField(
        db_column='INVALUEX',
        blank=True,
        null=True,
        help_text='Giriş maliyeti (Rap. Döv.)'
    )
    exptotal = models.FloatField(
        db_column='EXPTOTAL',
        blank=True,
        null=True,
        help_text='Gider toplamı'
    )
    accumdepr = models.FloatField(
        db_column='ACCUMDEPR',
        blank=True,
        null=True,
        help_text='Toplam amortisman'
    )
    accumreval = models.FloatField(
        db_column='ACCUMREVAL',
        blank=True,
        null=True,
        help_text='Toplam yeniden değerleme'
    )
    exptotalx = models.FloatField(
        db_column='EXPTOTALX',
        blank=True,
        null=True,
        help_text='Gider toplamı (Rap. döv.)'
    )
    accumdeprx = models.FloatField(
        db_column='ACCUMDEPRX',
        blank=True,
        null=True,
        help_text='Birikmiş amortisman (Rap. döv.)'
    )
    accumrevalx = models.FloatField(
        db_column='ACCUMREVALX',
        blank=True,
        null=True,
        help_text='Yeniden değerleme (Rap. döv.)'
    )
    deprtype2 = models.SmallIntegerField(
        db_column='DEPRTYPE2',
        blank=True,
        null=True,
        help_text='Alternatif amortisman türü'
    )
    deprrate2 = models.FloatField(
        db_column='DEPRRATE2',
        blank=True,
        null=True,
        help_text='Alternatif amortisman oranı'
    )
    deprdur2 = models.SmallIntegerField(
        db_column='DEPRDUR2',
        blank=True,
        null=True,
        help_text='Alternatif amortisman süresi'
    )
    revalflag2 = models.SmallIntegerField(
        db_column='REVALFLAG2',
        blank=True,
        null=True,
        help_text='Alt. yeniden değerlenecek (E/H)'
    )
    revdeprflag2 = models.SmallIntegerField(
        db_column='REVDEPRFLAG2',
        blank=True,
        null=True,
        help_text='Alt. değerleme amortismanı (E/H)'
    )
    begreval = models.FloatField(
        db_column='BEGREVAL', blank=True, null=True)
    begdepr = models.FloatField(
        db_column='BEGDEPR', blank=True, null=True)
    begrevdepr = models.FloatField(
        db_column='BEGREVDEPR', blank=True, null=True)
    begrevalx = models.FloatField(
        db_column='BEGREVALX', blank=True, null=True)
    begdeprx = models.FloatField(
        db_column='BEGDEPRX', blank=True, null=True)
    begrevdeprx = models.FloatField(
        db_column='BEGREVDEPRX', blank=True, null=True)
    opvals_begreval = models.FloatField(
        db_column='OPVALS_BEGREVAL', blank=True, null=True)
    opvals_begdepr = models.FloatField(
        db_column='OPVALS_BEGDEPR', blank=True, null=True)
    opvals_begrevdepr = models.FloatField(
        db_column='OPVALS_BEGREVDEPR', blank=True, null=True)
    opvalsx_begreval = models.FloatField(
        db_column='OPVALSX_BEGREVAL', blank=True, null=True)
    opvalsx_begdepr = models.FloatField(
        db_column='OPVALSX_BEGDEPR', blank=True, null=True)
    opvalsx_begrevdepr = models.FloatField(
        db_column='OPVALSX_BEGREVDEPR', blank=True, null=True)
    dateofdepr2 = models.IntegerField(
        db_column='DATEOFDEPR2', blank=True, null=True)
    partdep2 = models.SmallIntegerField(
        db_column='PARTDEP2', blank=True, null=True)
    orglogicref = models.IntegerField(db_column='ORGLOGICREF',
        blank=True, null=True, help_text='Orjinal kayıt ref.')
    deprtype3 = models.SmallIntegerField(
        db_column='DEPRTYPE3', blank=True, null=True)
    deprrate3 = models.FloatField(db_column='DEPRRATE3', blank=True, null=True)
    deprdur3 = models.SmallIntegerField(db_column='DEPRDUR3',
        blank=True, null=True)
    partdep3 = models.SmallIntegerField(db_column='PARTDEP3',
        blank=True, null=True)
    dateofdepr3 = models.DateTimeField(db_column='DATEOFDEPR3',
        blank=True, null=True)
    opvalsinf_begreval = models.FloatField(
        db_column='OPVALSINF_BEGREVAL', blank=True, null=True)
    opvalsinf_begdepr = models.FloatField(
        db_column='OPVALSINF_BEGDEPR', blank=True, null=True)
    opvalsinf_begrevdepr = models.FloatField(
        db_column='OPVALSINF_BEGREVDEPR', blank=True, null=True)
    opvalsinfx_begreval = models.FloatField(
        db_column='OPVALSINFX_BEGREVAL', blank=True, null=True)
    opvalsinfx_begdepr = models.FloatField(
        db_column='OPVALSINFX_BEGDEPR', blank=True, null=True)
    opvalsinfx_begrevdepr = models.FloatField(
        db_column='OPVALSINFX_BEGREVDEPR', blank=True, null=True)
    diffprice = models.FloatField(
        db_column='DIFFPRICE', blank=True, null=True)
    diffrepprice = models.FloatField(
        db_column='DIFFREPPRICE', blank=True, null=True)
    infidx = models.FloatField(
        db_column='INFIDX', blank=True, null=True)
    invdiscincl = models.SmallIntegerField(
        db_column='INVDISCINCL', blank=True, null=True)
    invdiscrate = models.FloatField(
        db_column='INVDISCRATE', blank=True, null=True)
    annualdistval = models.SmallIntegerField(
        db_column='ANNUALDISTVAL', blank=True, null=True)
    inflbasedvalue = models.FloatField(
        db_column='INFLBASEDVALUE', blank=True, null=True)
    regdefinition = models.CharField(
        db_column='REGDEFINITION', max_length=51, blank=True, null=True)
    deprtype4 = models.SmallIntegerField(
        db_column='DEPRTYPE4', blank=True, null=True)
    deprrate4 = models.FloatField(
        db_column='DEPRRATE4', blank=True, null=True)
    deprdur4 = models.SmallIntegerField(
        db_column='DEPRDUR4', blank=True, null=True)
    partdep4 = models.SmallIntegerField(
        db_column='PARTDEP4', blank=True, null=True)
    dateofdepr4 = models.DateTimeField(
        db_column='DATEOFDEPR4', blank=True, null=True)
    opvalsinf2_begreval = models.FloatField(
        db_column='OPVALSINF2_BEGREVAL', blank=True, null=True)
    opvalsinf2_begdepr = models.FloatField(
        db_column='OPVALSINF2_BEGDEPR', blank=True, null=True)
    opvalsinf2_begrevdepr = models.FloatField(
        db_column='OPVALSINF2_BEGREVDEPR', blank=True, null=True)
    opvalsinfx2_begreval = models.FloatField(
        db_column='OPVALSINFX2_BEGREVAL', blank=True, null=True)
    opvalsinfx2_begdepr = models.FloatField(
        db_column='OPVALSINFX2_BEGDEPR', blank=True, null=True)
    opvalsinfx2_begrevdepr = models.FloatField(
        db_column='OPVALSINFX2_BEGREVDEPR', blank=True, null=True)
    infidx2 = models.FloatField(
        db_column='INFIDX2', blank=True, null=True)
    annualdistval2 = models.SmallIntegerField(
        db_column='ANNUALDISTVAL2', blank=True, null=True)
    inflbasedvalue2 = models.FloatField(
        db_column='INFLBASEDVALUE2', blank=True, null=True)
    dateactive = models.DateTimeField(
        db_column='DATEACTIVE', blank=True, null=True)
    taxexprate2 = models.FloatField(
        db_column='TAXEXPRATE2', blank=True, null=True)
    taxaccflag = models.SmallIntegerField(
        db_column='TAXACCFLAG', blank=True, null=True)
    accficheref = models.IntegerField(
        db_column='ACCFICHEREF', blank=True, null=True)
    regtypcod = models.CharField(
        db_column='REGTYPCOD', max_length=25, blank=True, null=True)
    regtypdef = models.CharField(
        db_column='REGTYPDEF', max_length=51, blank=True, null=True)
    regexpenscod = models.CharField(
        db_column='REGEXPENSCOD', max_length=25, blank=True, null=True)
    regexpensdef = models.CharField(
        db_column='REGEXPENSDEF', max_length=51, blank=True, null=True)
    deprstpreasn = models.SmallIntegerField(
        db_column='DEPRSTPREASN', blank=True, null=True)
    deprstpdate = models.DateTimeField(
        db_column='DEPRSTPDATE', blank=True, null=True)
    prodcapacity = models.FloatField(
        db_column='PRODCAPACITY', blank=True, null=True)
    capacityunit = models.CharField(
        db_column='CAPACITYUNIT', max_length=51, blank=True, null=True)
    taxexptyp2 = models.SmallIntegerField(
        db_column='TAXEXPTYP2', blank=True, null=True)
    currtype = models.SmallIntegerField(
        db_column='CURRTYPE', blank=True, null=True)
    cyphcode = models.CharField(
        db_column='CYPHCODE', max_length=11, blank=True, null=True)
    approve = models.SmallIntegerField(
        db_column='APPROVE', blank=True, null=True)
    approvedate = models.DateTimeField(
        db_column='APPROVEDATE', blank=True, null=True)
    dateofdepr5 = models.IntegerField(
        db_column='DATEOFDEPR5', blank=True, null=True)
    deprrate5 = models.FloatField(
        db_column='DEPRRATE5', blank=True, null=True)
    deprdur5 = models.SmallIntegerField(
        db_column='DEPRDUR5', blank=True, null=True)
    deprtype5 = models.SmallIntegerField(
        db_column='DEPRTYPE5', blank=True, null=True)
    revalflag5 = models.SmallIntegerField(
        db_column='REVALFLAG5', blank=True, null=True)
    revdeprflag5 = models.SmallIntegerField(
        db_column='REVDEPRFLAG5', blank=True, null=True)
    partdep5 = models.SmallIntegerField(
        db_column='PARTDEP5', blank=True, null=True)
    opvalsinf3_begreval = models.FloatField(
        db_column='OPVALSINF3_BEGREVAL', blank=True, null=True)
    opvalsinf3_begdepr = models.FloatField(
        db_column='OPVALSINF3_BEGDEPR', blank=True, null=True)
    opvalsinf3_begrevdepr = models.FloatField(
        db_column='OPVALSINF3_BEGREVDEPR', blank=True, null=True)
    opvalsinfx3_begreval = models.FloatField(
        db_column='OPVALSINFX3_BEGREVAL', blank=True, null=True)
    opvalsinfx3_begdepr = models.FloatField(
        db_column='OPVALSINFX3_BEGDEPR', blank=True, null=True)
    opvalsinfx3_begrevdepr = models.FloatField(
        db_column='OPVALSINFX3_BEGREVDEPR', blank=True, null=True)
    deprdurtype2 = models.SmallIntegerField(
        db_column='DEPRDURTYPE2', blank=True, null=True)
    deprdurtype5 = models.SmallIntegerField(
        db_column='DEPRDURTYPE5', blank=True, null=True)
    tfrsvalue = models.FloatField(
        db_column='TFRSVALUE', blank=True, null=True)
    sourceindex = models.SmallIntegerField(
        db_column='SOURCEINDEX', blank=True, null=True)
    totrevamount = models.FloatField(
        db_column='TOTREVAMOUNT', blank=True, null=True)
    fausefullifecode5 = models.CharField(
        db_column='FAUSEFULLIFECODE5', max_length=11, blank=True, null=True)
    totrevamountx = models.FloatField(
        db_column='TOTREVAMOUNTX', blank=True, null=True)
    figscostopx = models.FloatField(
        db_column='FIGSCOSTOPX', blank=True, null=True)
    figscostop = models.FloatField(
        db_column='FIGSCOSTOP', blank=True, null=True)
    fausefullifecode = models.CharField(
        db_column='FAUSEFULLIFECODE', max_length=11, blank=True, null=True)
    centerref = models.IntegerField(
        db_column='CENTERREF', blank=True, null=True)
    fausefullifecode2 = models.CharField(
        db_column='FAUSEFULLIFECODE2', max_length=11, blank=True, null=True)
    fausefullifecode4 = models.CharField(
        db_column='FAUSEFULLIFECODE4', max_length=11, blank=True, null=True)
    fausefullifecode3 = models.CharField(
        db_column='FAUSEFULLIFECODE3', max_length=11, blank=True, null=True)
    mainttype = models.SmallIntegerField(
        db_column='MAINTTYPE', blank=True, null=True)
    maintlifeasratio = models.SmallIntegerField(
        db_column='MAINTLIFEASRATIO', blank=True, null=True)
    maintlife = models.FloatField(
        db_column='MAINTLIFE', blank=True, null=True)
    maintperunit = models.SmallIntegerField(
        db_column='MAINTPERUNIT', blank=True, null=True)
    maintperiod = models.FloatField(
        db_column='MAINTPERIOD', blank=True, null=True)
    maintbegdate = models.DateTimeField(
        db_column='MAINTBEGDATE', blank=True, null=True)
    maintusagelife = models.FloatField(
        db_column='MAINTUSAGELIFE', blank=True, null=True)
    maintlifetracktype = models.SmallIntegerField(
        db_column='MAINTLIFETRACKTYPE', blank=True, null=True)
    wsref = models.IntegerField(
        db_column='WSREF', blank=True, null=True)
    maintlifetype = models.SmallIntegerField(
        db_column='MAINTLIFETYPE', blank=True, null=True)
    maintnumber = models.IntegerField(
        db_column='MAINTNUMBER', blank=True, null=True)
    maintfactor = models.SmallIntegerField(
        db_column='MAINTFACTOR', blank=True, null=True)
    otvamount = models.FloatField(db_column='OTVAMOUNT', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_FAREGIST'
        target_db = 'erp'
