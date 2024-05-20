"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_DISPLINE(
    BaseLogical,
    BaseSiteRec,
    BaseCode,
    BaseWF,
    BasePrint,
    BaseProject,
    BaseGUID,
    BaseClient,
    BaseItem,
    BaseRef,
    models.Model):
    """
        İş emirleri
    """
    prodordref = models.IntegerField(
        db_column='PRODORDREF',
        blank=True,
        null=True,
        help_text='Üretim emri ref.'
    )
    bomlevel = models.SmallIntegerField(
        db_column='BOMLEVEL',
        blank=True,
        null=True,
        help_text='Ürün reçetesi seviyesi'
    )
    revref = models.IntegerField(
        db_column='REVREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi revizyonu ref.'
    )
    lineno_field = models.CharField(
        db_column='LINENO_',
        max_length=25,
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    routlineref = models.ForeignKey(
        "LG_ROUTING",
        db_column='ROUTLINEREF',
        blank=True,
        null=True,
        help_text='Üretim rota satırı ref. -> ROUTING',
        on_delete=models.DO_NOTHING
    )
    operationref = models.IntegerField(
        db_column='OPERATIONREF',
        blank=True,
        null=True,
        help_text='İşlem ref. -> OPERATION'
    )
    qcopok = models.SmallIntegerField(
        db_column='QCOPOK',
        blank=True,
        null=True,
        help_text='Kalite kontrol sonucu uygun'
    )
    opreqref = models.IntegerField(
        db_column='OPREQREF',
        blank=True,
        null=True,
        help_text='Operasyon ihtiyaçları ref. -> OPREQREF'
    )
    wsref = models.ForeignKey(
        "LG_WORKSTAT",
        db_column='WSREF',
        blank=True,
        null=True,
        help_text='İş istasyonu ref. -> WORKSTAT',
        on_delete=models.DO_NOTHING
    )
    wsdailyoptime = models.FloatField(db_column='WSDAILYOPTIME',
        blank=True, null=True, help_text='İş istasyonu günlük çalışma saati')
    wsworkingdays = models.SmallIntegerField(db_column='WSWORKINGDAYS',
        blank=True, null=True, help_text='İş istasyonu çalışma günleri')
    scheduled = models.SmallIntegerField(db_column='SCHEDULED', blank=True,
        null=True, help_text='Çizelgelenmiş')
    released = models.SmallIntegerField(db_column='RELEASED', blank=True,
        null=True, help_text='Serbest bırakılmış')
    setuptime = models.IntegerField(db_column='SETUPTIME', blank=True,
        null=True, help_text='Hazırlık süresi')
    queuetime = models.IntegerField(db_column='QUEUETIME', blank=True,
        null=True, help_text='Kuyruk süresi')
    runbatch = models.FloatField(db_column='RUNBATCH', blank=True,
        null=True, help_text='İşlem partisi')
    runtime = models.IntegerField(db_column='RUNTIME', blank=True,
        null=True, help_text='İşlem süresi')
    movebatch = models.FloatField(db_column='MOVEBATCH', blank=True,
        null=True, help_text='Taşıma partisi')
    movetime = models.IntegerField(db_column='MOVETIME', blank=True,
        null=True, help_text='Taşıma süresi')
    insptime = models.IntegerField(db_column='INSPTIME', blank=True,
        null=True, help_text='Kontrol zamanı')
    headtime = models.IntegerField(db_column='HEADTIME', blank=True,
        null=True, help_text='Operasyon öncesi bekleme süresi')
    tailtime = models.IntegerField(db_column='TAILTIME',
        blank=True, null=True, help_text='Operasyon sonrası bekleme süresi')
    opbegdate = models.DateTimeField(db_column='OPBEGDATE',
        blank=True, null=True, help_text='Planlanan işlem başlangıç tarihi')
    opbegtime = models.IntegerField(db_column='OPBEGTIME', blank=True,
        null=True, help_text='Planlanan işlem başlangıç zamanı')
    opduedate = models.DateTimeField(db_column='OPDUEDATE',
        blank=True, null=True, help_text='Planlanan işlem bitiş tarihi')
    opduetime = models.IntegerField(db_column='OPDUETIME',
        blank=True, null=True, help_text='Planlanan işlem bitiş saati')
    plnduration = models.FloatField(db_column='PLNDURATION', blank=True,
        null=True, help_text='Planlanan süre')
    actbegdate = models.DateTimeField(db_column='ACTBEGDATE',
        blank=True, null=True, help_text='Gerçekleşen işlem başlangıç tarihi')
    actbegtime = models.IntegerField(db_column='ACTBEGTIME',
        blank=True, null=True, help_text='Gerçekleşen işlem başlangıç zamanı')
    actduedate = models.DateTimeField(db_column='ACTDUEDATE',
        blank=True, null=True, help_text='Gerçekleşen işlem bitiş tarihi')
    actduetime = models.IntegerField(db_column='ACTDUETIME',
        blank=True, null=True, help_text='Gerçekleşen işlem bitiş zamanı')
    actduration = models.FloatField(db_column='ACTDURATION',
        blank=True, null=True, help_text='Gerçekleşen süre')
    linestatus = models.SmallIntegerField(
        db_column='LINESTATUS',
        blank=True,
        null=True,
        choices=[
            (0, 'Başlamadı'),
            (1, 'Devam ediyor'),
            (2, 'Durduruldu'),
            (3, 'Tamamlandı'),
            (4, 'Kapandı')
        ],
        help_text='Satır durumu'
    )
    stdmaterialcost = models.FloatField(db_column='STDMATERIALCOST',
        blank=True, null=True, help_text='Standart malzeme maliyeti')
    stdequiptcost = models.FloatField(db_column='STDEQUIPTCOST',
        blank=True, null=True, help_text='Standart araç maliyeti')
    stdwscost = models.FloatField(db_column='STDWSCOST',
        blank=True, null=True, help_text='Standart iş istasyonu maliyeti')
    stdlaborcost = models.FloatField(db_column='STDLABORCOST',
        blank=True, null=True, help_text='Standart işgücü maliyeti')
    stdoverhcost = models.FloatField(db_column='STDOVERHCOST',
        blank=True, null=True, help_text='Standart genel gider payı')
    stdtotalcost = models.FloatField(db_column='STDTOTALCOST',
        blank=True, null=True, help_text='Standart toplam maliyet')
    stdmaterialrpcost = models.FloatField(db_column='STDMATERIALRPCOST',
        blank=True, null=True, help_text='RD standart malzeme maliyeti')
    stdequiptrpcost = models.FloatField(db_column='STDEQUIPTRPCOST',
        blank=True, null=True, help_text='RD standart araç maliyeti	')
    stdwsrpcost = models.FloatField(db_column='STDWSRPCOST',
        blank=True, null=True, help_text='RD standart iş istasyonu maliyeti')
    stdlaborrpcost = models.FloatField(db_column='STDLABORRPCOST',
        blank=True, null=True, help_text='RD standart işgücü maliyeti')
    stdoverhrpcost = models.FloatField(db_column='STDOVERHRPCOST',
        blank=True, null=True, help_text='RD standart genel gider payı')
    stdtotalrpcost = models.FloatField(db_column='STDTOTALRPCOST',
        blank=True, null=True, help_text='RD standart toplam maliyet')
    actmaterialcost = models.FloatField(db_column='ACTMATERIALCOST',
        blank=True, null=True, help_text='Gerçekleşen malzeme maliyeti')
    actequiptcost = models.FloatField(db_column='ACTEQUIPTCOST',
        blank=True, null=True, help_text='Gerçekleşen araç maliyeti')
    actwscost = models.FloatField(db_column='ACTWSCOST',
        blank=True, null=True, help_text='Gerçekleşen iş istasyonu maliyeti')
    actlaborcost = models.FloatField(db_column='ACTLABORCOST',
        blank=True, null=True, help_text='Gerçekleşen çalışan maliyeti')
    actoverhcost = models.FloatField(db_column='ACTOVERHCOST',
        blank=True, null=True, help_text='Gerçekleşen genel gider payı')
    acttotalcost = models.FloatField(db_column='ACTTOTALCOST',
        blank=True, null=True, help_text='Gerçekleşen toplam maliyet')
    actmaterialrpcost = models.FloatField(db_column='ACTMATERIALRPCOST',
        blank=True, null=True,
        help_text='Raporlama dövizi gerçekleşen malzeme maliyeti')
    actequiptrpcost = models.FloatField(db_column='ACTEQUIPTRPCOST',
        blank=True, null=True,
        help_text='Raporlama dövizi gerçekleşen araç maliyeti')
    actwsrpcost = models.FloatField(db_column='ACTWSRPCOST',
        blank=True, null=True,
        help_text='Raporlama dövizi gerçekleşen ambar maliyeti')
    actlaborrpcost = models.FloatField(db_column='ACTLABORRPCOST',
        blank=True, null=True,
        help_text='Raporlama dövizi gerçekleşen işgücü maliyeti')
    actoverhrpcost = models.FloatField(db_column='ACTOVERHRPCOST',
        blank=True, null=True,
        help_text='Raporlama dövizi gerçekleşen genel gider payı')
    acttotalrpcost = models.FloatField(db_column='ACTTOTALRPCOST',
        blank=True, null=True,
        help_text='Raporlama dövizi gerçekleşen toplam maliyet')
    stdovhdformula = models.CharField(db_column='STDOVHDFORMULA',
        max_length=121, blank=True, null=True,
        help_text='Standart genel gider formülü')
    stdovhdrpformula = models.CharField(db_column='STDOVHDRPFORMULA',
        max_length=121, blank=True, null=True,
        help_text='RD standart genel gider formülü')
    actovhdformula = models.CharField(db_column='ACTOVHDFORMULA',
        max_length=121, blank=True, null=True,
        help_text='Gerçekleşen genel gider formülü'
    )
    actovhdrpformula = models.CharField(db_column='ACTOVHDRPFORMULA',
        max_length=121, blank=True, null=True,
        help_text='Raporlama dövizi gerçekleşen genel gider formülü'
    )
    opwsbegdate = models.DateTimeField(db_column='OPWSBEGDATE', blank=True,
        null=True, help_text='İş istasyonu başlangıç tarihi')
    bommasterref = models.IntegerField(db_column='BOMMASTERREF',
        blank=True, null=True, help_text='Ürün Reçetesi ref.')
    stpduration = models.FloatField(db_column='STPDURATION', blank=True,
        null=True, help_text='Durma süresi')
    stpcostduration = models.FloatField(db_column='STPCOSTDURATION',
        blank=True, null=True, help_text='Durma süresi maliyeti')
    docode = models.CharField(db_column='DOCODE', max_length=33,
        blank=True, null=True, help_text='Belge numarası')
    docounting = models.SmallIntegerField(db_column='DOCOUNTING',
        blank=True, null=True)
    variantref = models.IntegerField(db_column='VARIANTREF',
        blank=True, null=True)
    ufrsmaterialcost = models.FloatField(db_column='UFRSMATERIALCOST',
        blank=True, null=True)
    ufrsequiptcost = models.FloatField(db_column='UFRSEQUIPTCOST',
        blank=True, null=True)
    ufrswscost = models.FloatField(db_column='UFRSWSCOST',
        blank=True, null=True)
    ufrslaborcost = models.FloatField(db_column='UFRSLABORCOST',
        blank=True, null=True)
    ufrsoverhcost = models.FloatField(db_column='UFRSOVERHCOST',
        blank=True, null=True)
    ufrstotalcost = models.FloatField(db_column='UFRSTOTALCOST',
        blank=True, null=True)
    ufrsmaterialrpcost = models.FloatField(db_column='UFRSMATERIALRPCOST',
        blank=True, null=True)
    ufrsequiptrpcost = models.FloatField(db_column='UFRSEQUIPTRPCOST',
        blank=True, null=True)
    ufrswsrpcost = models.FloatField(db_column='UFRSWSRPCOST',
        blank=True, null=True)
    ufrslaborrpcost = models.FloatField(db_column='UFRSLABORRPCOST',
        blank=True, null=True)
    ufrsoverhrpcost = models.FloatField(db_column='UFRSOVERHRPCOST',
        blank=True, null=True)
    ufrstotalrpcost = models.FloatField(db_column='UFRSTOTALRPCOST',
        blank=True, null=True)
    stdoverhcostg1 = models.FloatField(db_column='STDOVERHCOSTG1',
        blank=True, null=True)
    stdoverhcostg2 = models.FloatField(db_column='STDOVERHCOSTG2',
        blank=True, null=True)
    stdoverhcostg3 = models.FloatField(db_column='STDOVERHCOSTG3',
        blank=True, null=True)
    stdoverhcostg4 = models.FloatField(db_column='STDOVERHCOSTG4',
        blank=True, null=True)
    stdoverhcostg5 = models.FloatField(db_column='STDOVERHCOSTG5',
        blank=True, null=True)
    stdoverhcostg6 = models.FloatField(db_column='STDOVERHCOSTG6',
        blank=True, null=True)
    stdoverhcostg7 = models.FloatField(db_column='STDOVERHCOSTG7',
        blank=True, null=True)
    stdoverhcostg8 = models.FloatField(db_column='STDOVERHCOSTG8',
        blank=True, null=True)
    stdoverhcostg9 = models.FloatField(db_column='STDOVERHCOSTG9',
        blank=True, null=True)
    stdoverhcostg10 = models.FloatField(db_column='STDOVERHCOSTG10',
        blank=True, null=True)
    stdoverhrpcostg1 = models.FloatField(db_column='STDOVERHRPCOSTG1',
        blank=True, null=True)
    stdoverhrpcostg2 = models.FloatField(db_column='STDOVERHRPCOSTG2',
        blank=True, null=True)
    stdoverhrpcostg3 = models.FloatField(db_column='STDOVERHRPCOSTG3',
        blank=True, null=True)
    stdoverhrpcostg4 = models.FloatField(db_column='STDOVERHRPCOSTG4',
        blank=True, null=True)
    stdoverhrpcostg5 = models.FloatField(db_column='STDOVERHRPCOSTG5',
        blank=True, null=True)
    stdoverhrpcostg6 = models.FloatField(db_column='STDOVERHRPCOSTG6',
        blank=True, null=True)
    stdoverhrpcostg7 = models.FloatField(db_column='STDOVERHRPCOSTG7',
        blank=True, null=True)
    stdoverhrpcostg8 = models.FloatField(db_column='STDOVERHRPCOSTG8',
        blank=True, null=True)
    stdoverhrpcostg9 = models.FloatField(db_column='STDOVERHRPCOSTG9',
        blank=True, null=True)
    stdoverhrpcostg10 = models.FloatField(db_column='STDOVERHRPCOSTG10',
        blank=True, null=True)
    actoverhcostg1 = models.FloatField(db_column='ACTOVERHCOSTG1',
        blank=True, null=True)
    actoverhcostg2 = models.FloatField(db_column='ACTOVERHCOSTG2',
        blank=True, null=True)
    actoverhcostg3 = models.FloatField(db_column='ACTOVERHCOSTG3',
        blank=True, null=True)
    actoverhcostg4 = models.FloatField(db_column='ACTOVERHCOSTG4',
        blank=True, null=True)
    actoverhcostg5 = models.FloatField(db_column='ACTOVERHCOSTG5',
        blank=True, null=True)
    actoverhcostg6 = models.FloatField(db_column='ACTOVERHCOSTG6',
        blank=True, null=True)
    actoverhcostg7 = models.FloatField(db_column='ACTOVERHCOSTG7',
        blank=True, null=True)
    actoverhcostg8 = models.FloatField(db_column='ACTOVERHCOSTG8',
        blank=True, null=True)
    actoverhcostg9 = models.FloatField(db_column='ACTOVERHCOSTG9',
        blank=True, null=True)
    actoverhcostg10 = models.FloatField(db_column='ACTOVERHCOSTG10',
        blank=True, null=True)
    actoverhrpcostg1 = models.FloatField(db_column='ACTOVERHRPCOSTG1',
        blank=True, null=True)
    actoverhrpcostg2 = models.FloatField(db_column='ACTOVERHRPCOSTG2',
        blank=True, null=True)
    actoverhrpcostg3 = models.FloatField(db_column='ACTOVERHRPCOSTG3',
        blank=True, null=True)
    actoverhrpcostg4 = models.FloatField(db_column='ACTOVERHRPCOSTG4',
        blank=True, null=True)
    actoverhrpcostg5 = models.FloatField(db_column='ACTOVERHRPCOSTG5',
        blank=True, null=True)
    actoverhrpcostg6 = models.FloatField(db_column='ACTOVERHRPCOSTG6',
        blank=True, null=True)
    actoverhrpcostg7 = models.FloatField(db_column='ACTOVERHRPCOSTG7',
        blank=True, null=True)
    actoverhrpcostg8 = models.FloatField(db_column='ACTOVERHRPCOSTG8',
        blank=True, null=True)
    actoverhrpcostg9 = models.FloatField(db_column='ACTOVERHRPCOSTG9',
        blank=True, null=True)
    actoverhrpcostg10 = models.FloatField(db_column='ACTOVERHRPCOSTG10',
        blank=True, null=True)
    ufrsoverhcostg1 = models.FloatField(db_column='UFRSOVERHCOSTG1',
        blank=True, null=True)
    ufrsoverhcostg2 = models.FloatField(db_column='UFRSOVERHCOSTG2',
        blank=True, null=True)
    ufrsoverhcostg3 = models.FloatField(db_column='UFRSOVERHCOSTG3',
        blank=True, null=True)
    ufrsoverhcostg4 = models.FloatField(db_column='UFRSOVERHCOSTG4',
        blank=True, null=True)
    ufrsoverhcostg5 = models.FloatField(db_column='UFRSOVERHCOSTG5',
        blank=True, null=True)
    ufrsoverhcostg6 = models.FloatField(db_column='UFRSOVERHCOSTG6',
        blank=True, null=True)
    ufrsoverhcostg7 = models.FloatField(db_column='UFRSOVERHCOSTG7',
        blank=True, null=True)
    ufrsoverhcostg8 = models.FloatField(db_column='UFRSOVERHCOSTG8',
        blank=True, null=True)
    ufrsoverhcostg9 = models.FloatField(db_column='UFRSOVERHCOSTG9',
        blank=True, null=True)
    ufrsoverhcostg10 = models.FloatField(db_column='UFRSOVERHCOSTG10',
        blank=True, null=True)
    ufrsoverhrpcostg1 = models.FloatField(db_column='UFRSOVERHRPCOSTG1',
        blank=True, null=True)
    ufrsoverhrpcostg2 = models.FloatField(db_column='UFRSOVERHRPCOSTG2',
        blank=True, null=True)
    ufrsoverhrpcostg3 = models.FloatField(db_column='UFRSOVERHRPCOSTG3',
        blank=True, null=True)
    ufrsoverhrpcostg4 = models.FloatField(db_column='UFRSOVERHRPCOSTG4',
        blank=True, null=True)
    ufrsoverhrpcostg5 = models.FloatField(db_column='UFRSOVERHRPCOSTG5',
        blank=True, null=True)
    ufrsoverhrpcostg6 = models.FloatField(db_column='UFRSOVERHRPCOSTG6',
        blank=True, null=True)
    ufrsoverhrpcostg7 = models.FloatField(db_column='UFRSOVERHRPCOSTG7',
        blank=True, null=True)
    ufrsoverhrpcostg8 = models.FloatField(db_column='UFRSOVERHRPCOSTG8',
        blank=True, null=True)
    ufrsoverhrpcostg9 = models.FloatField(db_column='UFRSOVERHRPCOSTG9',
        blank=True, null=True)
    ufrsoverhrpcostg10 = models.FloatField(db_column='UFRSOVERHRPCOSTG10',
        blank=True, null=True)
    rollupmaterialcost = models.FloatField(db_column='ROLLUPMATERIALCOST',
        blank=True, null=True)
    rollupequiptcost = models.FloatField(db_column='ROLLUPEQUIPTCOST',
        blank=True, null=True)
    rollupwscost = models.FloatField(db_column='ROLLUPWSCOST',
        blank=True, null=True)
    rolluplaborcost = models.FloatField(db_column='ROLLUPLABORCOST',
        blank=True, null=True)
    rollupoverhcost = models.FloatField(db_column='ROLLUPOVERHCOST',
        blank=True, null=True)
    rolluptotalcost = models.FloatField(db_column='ROLLUPTOTALCOST',
        blank=True, null=True)
    rollupmaterialrpcost = models.FloatField(db_column='ROLLUPMATERIALRPCOST',
        blank=True, null=True)
    rollupequiptrpcost = models.FloatField(db_column='ROLLUPEQUIPTRPCOST',
        blank=True, null=True)
    rollupwsrpcost = models.FloatField(
        db_column='ROLLUPWSRPCOST', blank=True, null=True)
    rolluplaborrpcost = models.FloatField(db_column='ROLLUPLABORRPCOST',
        blank=True, null=True)
    rollupoverhrpcost = models.FloatField(db_column='ROLLUPOVERHRPCOST',
        blank=True, null=True)
    rolluptotalrpcost = models.FloatField(db_column='ROLLUPTOTALRPCOST',
        blank=True, null=True)
    rollupoverhcostg1 = models.FloatField(db_column='ROLLUPOVERHCOSTG1',
        blank=True, null=True)
    rollupoverhcostg2 = models.FloatField(db_column='ROLLUPOVERHCOSTG2',
        blank=True, null=True)
    rollupoverhcostg3 = models.FloatField(db_column='ROLLUPOVERHCOSTG3',
        blank=True, null=True)
    rollupoverhcostg4 = models.FloatField(db_column='ROLLUPOVERHCOSTG4',
        blank=True, null=True)
    rollupoverhcostg5 = models.FloatField(db_column='ROLLUPOVERHCOSTG5',
        blank=True, null=True)
    rollupoverhcostg6 = models.FloatField(db_column='ROLLUPOVERHCOSTG6',
        blank=True, null=True)
    rollupoverhcostg7 = models.FloatField(db_column='ROLLUPOVERHCOSTG7',
        blank=True, null=True)
    rollupoverhcostg8 = models.FloatField(db_column='ROLLUPOVERHCOSTG8',
        blank=True, null=True)
    rollupoverhcostg9 = models.FloatField(db_column='ROLLUPOVERHCOSTG9',
        blank=True, null=True)
    rollupoverhcostg10 = models.FloatField(db_column='ROLLUPOVERHCOSTG10',
        blank=True, null=True)
    rollupoverhrpcostg1 = models.FloatField(db_column='ROLLUPOVERHRPCOSTG1',
        blank=True, null=True)
    rollupoverhrpcostg2 = models.FloatField(db_column='ROLLUPOVERHRPCOSTG2',
        blank=True, null=True)
    rollupoverhrpcostg3 = models.FloatField(db_column='ROLLUPOVERHRPCOSTG3',
        blank=True, null=True)
    rollupoverhrpcostg4 = models.FloatField(db_column='ROLLUPOVERHRPCOSTG4',
        blank=True, null=True)
    rollupoverhrpcostg5 = models.FloatField(db_column='ROLLUPOVERHRPCOSTG5',
        blank=True, null=True)
    rollupoverhrpcostg6 = models.FloatField(db_column='ROLLUPOVERHRPCOSTG6',
        blank=True, null=True)
    rollupoverhrpcostg7 = models.FloatField(db_column='ROLLUPOVERHRPCOSTG7',
        blank=True, null=True)
    rollupoverhrpcostg8 = models.FloatField(db_column='ROLLUPOVERHRPCOSTG8',
        blank=True, null=True)
    rollupoverhrpcostg9 = models.FloatField(db_column='ROLLUPOVERHRPCOSTG9',
        blank=True, null=True)
    rollupoverhrpcostg10 = models.FloatField(db_column='ROLLUPOVERHRPCOSTG10',
        blank=True, null=True)
    waitbatch = models.FloatField(db_column='WAITBATCH', blank=True, null=True)
    waittime = models.IntegerField(db_column='WAITTIME', blank=True, null=True)
    prodordtyp = models.SmallIntegerField(db_column='PRODORDTYP',
        blank=True, null=True)
    manueledit = models.SmallIntegerField(db_column='MANUELEDIT',
        blank=True, null=True)
    rework = models.SmallIntegerField(db_column='REWORK',
        blank=True, null=True)
    parting = models.SmallIntegerField(db_column='PARTING',
        blank=True, null=True)
    printdate = models.DateTimeField(db_column='PRINTDATE',
        blank=True, null=True)
    entrytype = models.SmallIntegerField(db_column='ENTRYTYPE',
        blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_DISPLINE'
        target_db = 'erp'

