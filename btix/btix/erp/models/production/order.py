"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_PRODORD(
    BaseLogical,
    BaseItem,
    BasePriority,
    BaseSiteRec,
    BaseActive,
    BaseInfo,
    BaseCenter,
    BaseAccount,
    BasePrint,
    BaseWF,
    BaseClient,
    BaseCode,
    BaseCancelled,
    BaseGenexp,
    BaseGUID,
    BaseProject,
    BaseApproved,
    BaseTextINC,
    BaseRef,
    models.Model):
    """
        Üretim emirleri
    """
    fichetype = models.SmallIntegerField(
        db_column='FICHETYPE',
        blank=True,
        null=True,
        help_text='Fiş tipi'
    )
    ficheno = models.CharField(
        db_column='FICHENO',
        max_length=17,
        blank=True,
        null=True,
        help_text='Fiş no'
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Fiş tarihi'
    )
    released = models.SmallIntegerField(
        db_column='RELEASED',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Serbest bırakılmış'
    )
    method = models.SmallIntegerField(
        db_column='METHOD',
        blank=True,
        null=True,
        choices=[
            (0, 'Geri'),
            (1, 'İleri')
        ],
        help_text='Metod'
    )
    scheduled = models.SmallIntegerField(
        db_column='SCHEDULED',
        blank=True,
        null=True,
        help_text='Planlanan'
    )
    partialdel = models.SmallIntegerField(
        db_column='PARTIALDEL',
        blank=True,
        null=True,
        help_text='Ambardan parçalı malzeme çekişi'
    )
    diffwhouseuse = models.SmallIntegerField(
        db_column='DIFFWHOUSEUSE',
        blank=True,
        null=True,
        help_text='Safha takibi yapılacaktır'
    )
    automtrissue = models.SmallIntegerField(
        db_column='AUTOMTRISSUE',
        blank=True,
        null=True,
        help_text='Otomatik malzeme çekişi'
    )
    rework = models.SmallIntegerField(
        db_column='REWORK',
        blank=True,
        null=True,
        help_text='Yeniden çalışabilir'
    )
    routingref = models.ForeignKey(
        "LG_ROUTING",
        db_column='ROUTINGREF',
        blank=True,
        null=True,
        help_text='Üretim rotaları kartı -> ROUTING',
        on_delete=models.DO_NOTHING
    )
    masterref = models.ForeignKey(
        "LG_BOMASTER",
        db_column='MASTERREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi ref. -> BOMASTER',
        on_delete=models.DO_NOTHING
    )
    revref = models.ForeignKey(
        "LG_BOMREVSN",
        db_column='REVREF',
        blank=True,
        null=True,
        help_text='Revizyon ref. -> BOMREVSN',
        on_delete=models.DO_NOTHING
    )
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika no'
    )
    plnamount = models.FloatField(
        db_column='PLNAMOUNT',
        blank=True,
        null=True,
        help_text='Planlanan miktar'
    )
    actamount = models.FloatField(
        db_column='ACTAMOUNT',
        blank=True,
        null=True,
        help_text='Gerçekleşen miktar'
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
    duedate = models.DateTimeField(
        db_column='DUEDATE',
        blank=True,
        null=True,
        help_text='Vade tarihi'
    )
    stopdate = models.DateTimeField(
        db_column='STOPDATE',
        blank=True,
        null=True,
        help_text='Durma tarihi'
    )
    startdate = models.DateTimeField(
        db_column='STARTDATE',
        blank=True,
        null=True,
        help_text='Yeniden başlama tarihi'
    )
    plnbegdate = models.DateTimeField(
        db_column='PLNBEGDATE',
        blank=True,
        null=True,
        help_text='Planlanan başlangıç tarihi'
    )
    plnenddate = models.DateTimeField(
        db_column='PLNENDDATE',
        blank=True,
        null=True,
        help_text='Planlanan bitiş tarihi'
    )
    plnduration = models.FloatField(
        db_column='PLNDURATION',
        blank=True,
        null=True,
        help_text='Planlanan süre'
    )
    actbegdate = models.DateTimeField(
        db_column='ACTBEGDATE',
        blank=True,
        null=True,
        help_text='Gerçekleşen bitiş tarihi'
    )
    actenddate = models.DateTimeField(
        db_column='ACTENDDATE',
        blank=True,
        null=True,
        help_text='Gerçekleşen bitiş tarihi'
    )
    actduration = models.FloatField(
        db_column='ACTDURATION',
        blank=True,
        null=True,
        help_text='Gerçekleşen süre'
    )
    status = models.SmallIntegerField(
        db_column='STATUS',
        blank=True,
        null=True,
        help_text='Durum'
    )
    stdmaterialcost = models.FloatField(
        db_column='STDMATERIALCOST',
        blank=True,
        null=True,
        help_text='Standart malzeme maliyeti'
    )
    stdequiptcost = models.FloatField(
        db_column='STDEQUIPTCOST',
        blank=True,
        null=True,
        help_text='Standart ekipman maliyeti'
    )
    stdwscost = models.FloatField(
        db_column='STDWSCOST',
        blank=True,
        null=True,
        help_text='Standart iş istasyonu maliyeti'
    )
    stdlaborcost = models.FloatField(
        db_column='STDLABORCOST',
        blank=True,
        null=True,
        help_text='Standart çalışma (emek) maliyeti'
    )
    stdoverhcost = models.FloatField(
        db_column='STDOVERHCOST',
        blank=True,
        null=True,
        help_text='Standart genel gider payı'
    )
    stdtotalcost = models.FloatField(
        db_column='STDTOTALCOST',
        blank=True,
        null=True,
        help_text='Standart toplam maliyet'
    )
    stdmaterialrpcost = models.FloatField(
        db_column='STDMATERIALRPCOST',
        blank=True,
        null=True
    )
    stdequiptrpcost = models.FloatField(
        db_column='STDEQUIPTRPCOST',
        blank=True,
        null=True
    )
    stdwsrpcost = models.FloatField(
        db_column='STDWSRPCOST',
        blank=True,
        null=True
    )
    stdlaborrpcost = models.FloatField(
        db_column='STDLABORRPCOST',
        blank=True,
        null=True
    )
    stdoverhrpcost = models.FloatField(
        db_column='STDOVERHRPCOST',
        blank=True,
        null=True
    )
    stdtotalrpcost = models.FloatField(
        db_column='STDTOTALRPCOST',
        blank=True,
        null=True
    )
    actmaterialcost = models.FloatField(
        db_column='ACTMATERIALCOST',
        blank=True,
        null=True,
        help_text='Gerçekleşen malzeme maliyeti'
    )
    actequiptcost = models.FloatField(
        db_column='ACTEQUIPTCOST',
        blank=True,
        null=True,
        help_text='Gerçekleşen ekipman maliyeti'
    )
    actwscost = models.FloatField(
        db_column='ACTWSCOST',
        blank=True,
        null=True,
        help_text='Gerçek iş istasyonu maliyeti'
    )
    actlaborcost = models.FloatField(
        db_column='ACTLABORCOST',
        blank=True,
        null=True,
        help_text='Gerçekleşen çalışma(emek) maliyeti'
    )
    actoverhcost = models.FloatField(
        db_column='ACTOVERHCOST',
        blank=True,
        null=True,
        help_text='Gerçekleşen genel gider payı'
    )
    acttotalcost = models.FloatField(
        db_column='ACTTOTALCOST',
        blank=True,
        null=True,
        help_text='Gerçekleşen total maliyet'
    )
    actmaterialrpcost = models.FloatField(
        db_column='ACTMATERIALRPCOST',
        blank=True,
        null=True
    )
    actequiptrpcost = models.FloatField(
        db_column='ACTEQUIPTRPCOST',
        blank=True,
        null=True
    )
    actwsrpcost = models.FloatField(
        db_column='ACTWSRPCOST',
        blank=True,
        null=True
    )
    actlaborrpcost = models.FloatField(
        db_column='ACTLABORRPCOST',
        blank=True,
        null=True
    )
    actoverhrpcost = models.FloatField(
        db_column='ACTOVERHRPCOST',
        blank=True,
        null=True
    )
    acttotalrpcost = models.FloatField(
        db_column='ACTTOTALRPCOST',
        blank=True,
        null=True
    )
    orglogicref = models.IntegerField(
        db_column='ORGLOGICREF',
        blank=True,
        null=True,
        help_text='Orjinal kayıt ref.'
    )
    needrelease = models.SmallIntegerField(
        db_column='NEEDRELEASE',
        blank=True,
        null=True
    )
    uomref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UOMREF',
        blank=True,
        null=True,
        help_text='Birim ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_uomref"
    )
    uinfo1 = models.FloatField(
        db_column='UINFO1',
        blank=True,
        null=True,
        help_text='Çevrim katsayısı'
    )
    uinfo2 = models.FloatField(
        db_column='UINFO2',
        blank=True,
        null=True,
        help_text='Çevrim katsayısı'
    )
    uinfo3 = models.FloatField(
        db_column='UINFO3',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    uinfo4 = models.FloatField(
        db_column='UINFO4',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    uinfo5 = models.FloatField(
        db_column='UINFO5',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    uinfo6 = models.FloatField(
        db_column='UINFO6',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    uinfo7 = models.FloatField(
        db_column='UINFO7',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    uinfo8 = models.FloatField(
        db_column='UINFO8',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    needprocure = models.SmallIntegerField(
        db_column='NEEDPROCURE', blank=True, null=True)
    procured = models.SmallIntegerField(
        db_column='PROCURED', blank=True, null=True)
    begtime = models.IntegerField(
        db_column='BEGTIME', blank=True, null=True)
    endtime = models.IntegerField(
        db_column='ENDTIME', blank=True, null=True)
    plnbegtime = models.IntegerField(
        db_column='PLNBEGTIME', blank=True, null=True)
    plnendtime = models.IntegerField(
        db_column='PLNENDTIME', blank=True, null=True)
    actbegtime = models.IntegerField(
        db_column='ACTBEGTIME', blank=True, null=True)
    actendtime = models.IntegerField(
        db_column='ACTENDTIME', blank=True, null=True)
    stdaccounted = models.SmallIntegerField(
        db_column='STDACCOUNTED', blank=True, null=True)
    actaccounted = models.SmallIntegerField(
        db_column='ACTACCOUNTED', blank=True, null=True)
    grossuinfo1 = models.FloatField(
        db_column='GROSSUINFO1', blank=True, null=True)
    grossuinfo2 = models.FloatField(
        db_column='GROSSUINFO2', blank=True, null=True)
    chkrescap = models.SmallIntegerField(
        db_column='CHKRESCAP', blank=True, null=True)
    advicews = models.SmallIntegerField(
        db_column='ADVICEWS', blank=True, null=True)
    duetime = models.IntegerField(
        db_column='DUETIME', blank=True, null=True)
    approve = models.SmallIntegerField(
        db_column='APPROVE', blank=True, null=True)
    approvedate = models.DateTimeField(
        db_column='APPROVEDATE', blank=True, null=True)
    ufrsmaterialcost = models.FloatField(
        db_column='UFRSMATERIALCOST', blank=True, null=True)
    ufrsequiptcost = models.FloatField(
        db_column='UFRSEQUIPTCOST', blank=True, null=True)
    ufrswscost = models.FloatField(
        db_column='UFRSWSCOST', blank=True, null=True)
    ufrslaborcost = models.FloatField(
        db_column='UFRSLABORCOST', blank=True, null=True)
    ufrsoverhcost = models.FloatField(
        db_column='UFRSOVERHCOST', blank=True, null=True)
    ufrstotalcost = models.FloatField(
        db_column='UFRSTOTALCOST', blank=True, null=True)
    ufrsmaterialrpcost = models.FloatField(
        db_column='UFRSMATERIALRPCOST', blank=True, null=True)
    ufrsequiptrpcost = models.FloatField(
        db_column='UFRSEQUIPTRPCOST', blank=True, null=True)
    ufrswsrpcost = models.FloatField(
        db_column='UFRSWSRPCOST', blank=True, null=True)
    ufrslaborrpcost = models.FloatField(
        db_column='UFRSLABORRPCOST', blank=True, null=True)
    ufrsoverhrpcost = models.FloatField(
        db_column='UFRSOVERHRPCOST', blank=True, null=True)
    ufrstotalrpcost = models.FloatField(
        db_column='UFRSTOTALRPCOST', blank=True, null=True)
    ufrsaccounted = models.SmallIntegerField(
        db_column='UFRSACCOUNTED', blank=True, null=True)
    stdoverhcostg1 = models.FloatField(
        db_column='STDOVERHCOSTG1', blank=True, null=True)
    stdoverhcostg2 = models.FloatField(
        db_column='STDOVERHCOSTG2', blank=True, null=True)
    stdoverhcostg3 = models.FloatField(
        db_column='STDOVERHCOSTG3', blank=True, null=True)
    stdoverhcostg4 = models.FloatField(
        db_column='STDOVERHCOSTG4', blank=True, null=True)
    stdoverhcostg5 = models.FloatField(
        db_column='STDOVERHCOSTG5', blank=True, null=True)
    stdoverhcostg6 = models.FloatField(
        db_column='STDOVERHCOSTG6', blank=True, null=True)
    stdoverhcostg7 = models.FloatField(
        db_column='STDOVERHCOSTG7', blank=True, null=True)
    stdoverhcostg8 = models.FloatField(
        db_column='STDOVERHCOSTG8', blank=True, null=True)
    stdoverhcostg9 = models.FloatField(
        db_column='STDOVERHCOSTG9', blank=True, null=True)
    stdoverhcostg10 = models.FloatField(
        db_column='STDOVERHCOSTG10', blank=True, null=True)
    stdoverhrpcostg1 = models.FloatField(
        db_column='STDOVERHRPCOSTG1', blank=True, null=True)
    stdoverhrpcostg2 = models.FloatField(
        db_column='STDOVERHRPCOSTG2', blank=True, null=True)
    stdoverhrpcostg3 = models.FloatField(
        db_column='STDOVERHRPCOSTG3', blank=True, null=True)
    stdoverhrpcostg4 = models.FloatField(
        db_column='STDOVERHRPCOSTG4', blank=True, null=True)
    stdoverhrpcostg5 = models.FloatField(
        db_column='STDOVERHRPCOSTG5', blank=True, null=True)
    stdoverhrpcostg6 = models.FloatField(
        db_column='STDOVERHRPCOSTG6', blank=True, null=True)
    stdoverhrpcostg7 = models.FloatField(
        db_column='STDOVERHRPCOSTG7', blank=True, null=True)
    stdoverhrpcostg8 = models.FloatField(
        db_column='STDOVERHRPCOSTG8', blank=True, null=True)
    stdoverhrpcostg9 = models.FloatField(
        db_column='STDOVERHRPCOSTG9', blank=True, null=True)
    stdoverhrpcostg10 = models.FloatField(
        db_column='STDOVERHRPCOSTG10', blank=True, null=True)
    actoverhcostg1 = models.FloatField(
        db_column='ACTOVERHCOSTG1', blank=True, null=True)
    actoverhcostg2 = models.FloatField(
        db_column='ACTOVERHCOSTG2', blank=True, null=True)
    actoverhcostg3 = models.FloatField(
        db_column='ACTOVERHCOSTG3', blank=True, null=True)
    actoverhcostg4 = models.FloatField(
        db_column='ACTOVERHCOSTG4', blank=True, null=True)
    actoverhcostg5 = models.FloatField(
        db_column='ACTOVERHCOSTG5', blank=True, null=True)
    actoverhcostg6 = models.FloatField(
        db_column='ACTOVERHCOSTG6', blank=True, null=True)
    actoverhcostg7 = models.FloatField(
        db_column='ACTOVERHCOSTG7', blank=True, null=True)
    actoverhcostg8 = models.FloatField(
        db_column='ACTOVERHCOSTG8', blank=True, null=True)
    actoverhcostg9 = models.FloatField(
        db_column='ACTOVERHCOSTG9', blank=True, null=True)
    actoverhcostg10 = models.FloatField(
        db_column='ACTOVERHCOSTG10', blank=True, null=True)
    actoverhrpcostg1 = models.FloatField(
        db_column='ACTOVERHRPCOSTG1', blank=True, null=True)
    actoverhrpcostg2 = models.FloatField(
        db_column='ACTOVERHRPCOSTG2', blank=True, null=True)
    actoverhrpcostg3 = models.FloatField(
        db_column='ACTOVERHRPCOSTG3', blank=True, null=True)
    actoverhrpcostg4 = models.FloatField(
        db_column='ACTOVERHRPCOSTG4', blank=True, null=True)
    actoverhrpcostg5 = models.FloatField(
        db_column='ACTOVERHRPCOSTG5', blank=True, null=True)
    actoverhrpcostg6 = models.FloatField(
        db_column='ACTOVERHRPCOSTG6', blank=True, null=True)
    actoverhrpcostg7 = models.FloatField(
        db_column='ACTOVERHRPCOSTG7', blank=True, null=True)
    actoverhrpcostg8 = models.FloatField(
        db_column='ACTOVERHRPCOSTG8', blank=True, null=True)
    actoverhrpcostg9 = models.FloatField(
        db_column='ACTOVERHRPCOSTG9', blank=True, null=True)
    actoverhrpcostg10 = models.FloatField(
        db_column='ACTOVERHRPCOSTG10', blank=True, null=True)
    ufrsoverhcostg1 = models.FloatField(
        db_column='UFRSOVERHCOSTG1', blank=True, null=True)
    ufrsoverhcostg2 = models.FloatField(
        db_column='UFRSOVERHCOSTG2', blank=True, null=True)
    ufrsoverhcostg3 = models.FloatField(
        db_column='UFRSOVERHCOSTG3', blank=True, null=True)
    ufrsoverhcostg4 = models.FloatField(
        db_column='UFRSOVERHCOSTG4', blank=True, null=True)
    ufrsoverhcostg5 = models.FloatField(
        db_column='UFRSOVERHCOSTG5', blank=True, null=True)
    ufrsoverhcostg6 = models.FloatField(
        db_column='UFRSOVERHCOSTG6', blank=True, null=True)
    ufrsoverhcostg7 = models.FloatField(
        db_column='UFRSOVERHCOSTG7', blank=True, null=True)
    ufrsoverhcostg8 = models.FloatField(
        db_column='UFRSOVERHCOSTG8', blank=True, null=True)
    ufrsoverhcostg9 = models.FloatField(
        db_column='UFRSOVERHCOSTG9', blank=True, null=True)
    ufrsoverhcostg10 = models.FloatField(
        db_column='UFRSOVERHCOSTG10', blank=True, null=True)
    ufrsoverhrpcostg1 = models.FloatField(
        db_column='UFRSOVERHRPCOSTG1', blank=True, null=True)
    ufrsoverhrpcostg2 = models.FloatField(
        db_column='UFRSOVERHRPCOSTG2', blank=True, null=True)
    ufrsoverhrpcostg3 = models.FloatField(
        db_column='UFRSOVERHRPCOSTG3', blank=True, null=True)
    ufrsoverhrpcostg4 = models.FloatField(
        db_column='UFRSOVERHRPCOSTG4', blank=True, null=True)
    ufrsoverhrpcostg5 = models.FloatField(
        db_column='UFRSOVERHRPCOSTG5', blank=True, null=True)
    ufrsoverhrpcostg6 = models.FloatField(
        db_column='UFRSOVERHRPCOSTG6', blank=True, null=True)
    ufrsoverhrpcostg7 = models.FloatField(
        db_column='UFRSOVERHRPCOSTG7', blank=True, null=True)
    ufrsoverhrpcostg8 = models.FloatField(
        db_column='UFRSOVERHRPCOSTG8', blank=True, null=True)
    ufrsoverhrpcostg9 = models.FloatField(
        db_column='UFRSOVERHRPCOSTG9', blank=True, null=True)
    ufrsoverhrpcostg10 = models.FloatField(
        db_column='UFRSOVERHRPCOSTG10', blank=True, null=True)
    rollupmaterialcost = models.FloatField(
        db_column='ROLLUPMATERIALCOST', blank=True, null=True)
    rollupequiptcost = models.FloatField(
        db_column='ROLLUPEQUIPTCOST', blank=True, null=True)
    rollupwscost = models.FloatField(
        db_column='ROLLUPWSCOST', blank=True, null=True)
    rolluplaborcost = models.FloatField(
        db_column='ROLLUPLABORCOST', blank=True, null=True)
    rollupoverhcost = models.FloatField(
        db_column='ROLLUPOVERHCOST', blank=True, null=True)
    rolluptotalcost = models.FloatField(
        db_column='ROLLUPTOTALCOST', blank=True, null=True)
    rollupmaterialrpcost = models.FloatField(
        db_column='ROLLUPMATERIALRPCOST', blank=True, null=True)
    rollupequiptrpcost = models.FloatField(
        db_column='ROLLUPEQUIPTRPCOST', blank=True, null=True)
    rollupwsrpcost = models.FloatField(
        db_column='ROLLUPWSRPCOST', blank=True, null=True)
    rolluplaborrpcost = models.FloatField(
        db_column='ROLLUPLABORRPCOST', blank=True, null=True)
    rollupoverhrpcost = models.FloatField(
        db_column='ROLLUPOVERHRPCOST', blank=True, null=True)
    rolluptotalrpcost = models.FloatField(
        db_column='ROLLUPTOTALRPCOST', blank=True, null=True)
    rollupoverhcostg1 = models.FloatField(
        db_column='ROLLUPOVERHCOSTG1', blank=True, null=True)
    rollupoverhcostg2 = models.FloatField(
        db_column='ROLLUPOVERHCOSTG2', blank=True, null=True)
    rollupoverhcostg3 = models.FloatField(
        db_column='ROLLUPOVERHCOSTG3', blank=True, null=True)
    rollupoverhcostg4 = models.FloatField(
        db_column='ROLLUPOVERHCOSTG4', blank=True, null=True)
    rollupoverhcostg5 = models.FloatField(
        db_column='ROLLUPOVERHCOSTG5', blank=True, null=True)
    rollupoverhcostg6 = models.FloatField(
        db_column='ROLLUPOVERHCOSTG6', blank=True, null=True)
    rollupoverhcostg7 = models.FloatField(
        db_column='ROLLUPOVERHCOSTG7', blank=True, null=True)
    rollupoverhcostg8 = models.FloatField(
        db_column='ROLLUPOVERHCOSTG8', blank=True, null=True)
    rollupoverhcostg9 = models.FloatField(
        db_column='ROLLUPOVERHCOSTG9', blank=True, null=True)
    rollupoverhcostg10 = models.FloatField(
        db_column='ROLLUPOVERHCOSTG10', blank=True, null=True)
    rollupoverhrpcostg1 = models.FloatField(
        db_column='ROLLUPOVERHRPCOSTG1', blank=True, null=True)
    rollupoverhrpcostg2 = models.FloatField(
        db_column='ROLLUPOVERHRPCOSTG2', blank=True, null=True)
    rollupoverhrpcostg3 = models.FloatField(
        db_column='ROLLUPOVERHRPCOSTG3', blank=True, null=True)
    rollupoverhrpcostg4 = models.FloatField(
        db_column='ROLLUPOVERHRPCOSTG4', blank=True, null=True)
    rollupoverhrpcostg5 = models.FloatField(
        db_column='ROLLUPOVERHRPCOSTG5', blank=True, null=True)
    rollupoverhrpcostg6 = models.FloatField(
        db_column='ROLLUPOVERHRPCOSTG6', blank=True, null=True)
    rollupoverhrpcostg7 = models.FloatField(
        db_column='ROLLUPOVERHRPCOSTG7', blank=True, null=True)
    rollupoverhrpcostg8 = models.FloatField(
        db_column='ROLLUPOVERHRPCOSTG8', blank=True, null=True)
    rollupoverhrpcostg9 = models.FloatField(
        db_column='ROLLUPOVERHRPCOSTG9', blank=True, null=True)
    rollupoverhrpcostg10 = models.FloatField(
        db_column='ROLLUPOVERHRPCOSTG10', blank=True, null=True)
    doplnreserve = models.SmallIntegerField(
        db_column='DOPLNRESERVE', blank=True, null=True)
    actcostcalculated = models.SmallIntegerField(
        db_column='ACTCOSTCALCULATED', blank=True, null=True)
    hasparallelwsload = models.SmallIntegerField(
        db_column='HASPARALLELWSLOAD', blank=True, null=True)
    createwhfiche = models.SmallIntegerField(
        db_column='CREATEWHFICHE', blank=True, null=True)
    printdate = models.DateTimeField(
        db_column='PRINTDATE', blank=True, null=True)
    doslplnreserve = models.SmallIntegerField(
        db_column='DOSLPLNRESERVE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_PRODORD'
        unique_together = (
            ('ficheno', 'fichetype'),
            ('date_field', 'ficheno', 'fichetype'),
        )
        target_db = 'erp'
