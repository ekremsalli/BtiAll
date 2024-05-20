"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_BOMASTER(
    BaseLogical,
    BaseInfo,
    BaseCode,
    BaseSiteRec,
    BaseVariable,
    BaseActive,
    BaseWF,
    BaseClient,
    BaseTextINC,
    BasePrint,
    BaseGUID,
    BaseApproved,
    BaseRef,
    models.Model):
    """
        Ürün reçeteleri
    """
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Ürün reçetesi kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Ürün reçetesi açıklama'
    )
    validrevref = models.IntegerField(
        db_column='VALIDREVREF',
        blank=True,
        null=True,
        help_text='Geçerli revizyon ref. -> BOMREVSN'
    )
    mainprodref = models.ForeignKey(
        "LG_ITEMS",
        db_column='MAINPRODREF',
        blank=True,
        null=True,
        help_text='Ana ürün ref. -> ITEMS',
        on_delete=models.DO_NOTHING,
    )
    demontaj = models.SmallIntegerField(
        db_column='DEMONTAJ',
        blank=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        null=True,
        help_text='Demontaj'
    )
    routingref = models.ForeignKey(
        "LG_ROUTING",
        db_column='ROUTINGREF',
        blank=True,
        null=True,
        help_text='Üretim rotası ref.',
        on_delete=models.DO_NOTHING
    )
    productlineref = models.IntegerField(
        db_column='PRODUCTLINEREF',
        blank=True,
        null=True,
        help_text='Üretim satırı ref.',
    )
    bomtype = models.SmallIntegerField(
        db_column='BOMTYPE',
        blank=True,
        null=True
    )
    printdate = models.DateTimeField(
        db_column='PRINTDATE',
        blank=True,
        null=True
    )
    specode2 = models.CharField(
        db_column='SPECODE2',
        max_length=11,
        blank=True,
        null=True
    )
    name2 = models.CharField(
        db_column='NAME2',
        max_length=201,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        unique_together = (('bomtype', 'code'), ('active', 'bomtype', 'code'),)
        db_table = f'LG_{Active.namespace}_BOMASTER'
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"

class LG_BOMLINE(
    BaseLogical,
    BaseUnit,
    BaseAmount,
    BaseSiteRec,
    BaseItem,
    BaseWF,
    BaseRef,
    models.Model):
    """
        Ürün reçete detayları
    """
    bomrevref = models.ForeignKey(
        "LG_BOMASTER",
        db_column='BOMREVREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi ref. -> BOMASTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_bomrefrev"
    )
    linetype = models.SmallIntegerField(
        db_column='LINETYPE',
        blank=True,
        null=True,
        help_text='Satır tipi'
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    outitemref = models.IntegerField(
        db_column='OUTITEMREF',
        blank=True,
        null=True,
        help_text='Koşul malzeme sınıf kul. ref.'
    )
    scrapfact = models.FloatField(
        db_column='SCRAPFACT',
        blank=True,
        null=True,
        help_text='Fire faktörü'
    )
    scrapcalc = models.SmallIntegerField(
        db_column='SCRAPCALC',
        blank=True,
        null=True,
        help_text='Fire hesaplama yöntemi'
    )
    scalable = models.SmallIntegerField(
        db_column='SCALABLE',
        blank=True,
        null=True,
        help_text='Ölçeklenebilir'
    )
    altitemuse = models.SmallIntegerField(
        db_column='ALTITEMUSE',
        blank=True,
        null=True,
        help_text='Alternatif malzeme kullanımı'
    )
    tempinuse = models.SmallIntegerField(
        db_column='TEMPINUSE',
        blank=True,
        null=True,
        help_text='Konsiye kullanımı'
    )
    nextlevelbomref = models.ForeignKey(
        "LG_BOMASTER",
        db_column='NEXTLEVELBOMREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi ref. -> BOMASTER',
        on_delete=models.DO_NOTHING
    )
    specode = models.CharField(
        db_column='SPECODE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Özel kod'
    )
    bomlineexp = models.CharField(
        db_column='BOMLINEEXP',
        max_length=51,
        blank=True,
        null=True,
        help_text='Ürün reçetesi satır açıklaması'
    )
    invenno = models.SmallIntegerField(
        db_column='INVENNO',
        blank=True,
        null=True,
        help_text='Ambar numarası'
    )
    engineering = models.SmallIntegerField(
        db_column='ENGINEERING',
        blank=True,
        null=True,
        help_text='Mühendislik'
    )
    production = models.SmallIntegerField(
        db_column='PRODUCTION',
        blank=True,
        null=True,
        help_text='Üretim'
    )
    cost = models.SmallIntegerField(
        db_column='COST',
        blank=True,
        null=True,
        help_text='Maliyet'
    )
    costrate = models.FloatField(
        db_column='COSTRATE',
        blank=True,
        null=True,
        help_text='Maliyet oranı'
    )
    formula = models.CharField(
        db_column='FORMULA',
        max_length=251,
        blank=True,
        null=True,
        help_text='Formül'
    )
    bommasterref = models.IntegerField(
        db_column='BOMMASTERREF',
        blank=True,
        null=True,
        help_text='Ürün reçete ref.'
    )
    lineclstype = models.SmallIntegerField(
        db_column='LINECLSTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Malzeme'),
            (10, 'Malzeme sınıfı')
        ],
        help_text='Satır tipi; 0 -> Malzeme, 10-> Malzeme sınıfı'
    )
    detline = models.SmallIntegerField(
        db_column='DETLINE',
        blank=True,
        null=True,
        help_text='Detay satırı'
    )
    prevlineref = models.IntegerField(
        db_column='PREVLINEREF',
        blank=True,
        null=True,
        help_text='Üst malzeme satırı ref.'
    )
    routlineref = models.IntegerField(
        db_column='ROUTLINEREF',
        blank=True,
        null=True,
        help_text='Üretim rota satırı ref.'
    )
    operationref = models.IntegerField(
        db_column='OPERATIONREF',
        blank=True,
        null=True,
        help_text='İşlem ref.'
    )
    formulaitemref = models.IntegerField(
        db_column='FORMULAITEMREF',
        blank=True,
        null=True,
        help_text='Malzeme formül ref.'
    )
    nextlevrevref = models.IntegerField(
        db_column='NEXTLEVREVREF',
        blank=True,
        null=True,
        help_text='Reçete revizyon ref. sonraki seviye'
    )
    effectoptime = models.SmallIntegerField(
        db_column='EFFECTOPTIME',
        blank=True,
        null=True,
        help_text='Operasyon süresini etkiler'
    )
    dref = models.IntegerField(
        db_column='DREF',
        blank=True,
        null=True,
        help_text='Dağıtım şablonu ref.'
    )
    bydefaultexists = models.SmallIntegerField(
        db_column='BYDEFAULTEXISTS',
        blank=True,
        null=True,
        help_text='?'
    )
    grossuinfo1 = models.FloatField(
        db_column='GROSSUINFO1',
        blank=True,
        null=True,
        help_text='Brüt çevrim katsayısı 1'
    )
    grossuinfo2 = models.FloatField(
        db_column='GROSSUINFO2',
        blank=True,
        null=True,
        help_text='Brüt çevrim katsayısı 2'
    )
    usestdcost = models.SmallIntegerField(
        db_column='USESTDCOST',
        blank=True,
        null=True,
        help_text='Standart malitet kullanımı'
    )
    overlapwith = models.SmallIntegerField(
        db_column='OVERLAPWITH',
        blank=True,
        null=True
    )
    overlapmethod = models.SmallIntegerField(
        db_column='OVERLAPMETHOD',
        blank=True,
        null=True
    )
    overlaptype = models.SmallIntegerField(
        db_column='OVERLAPTYPE',
        blank=True,
        null=True
    )
    overlapvalue = models.FloatField(
        db_column='OVERLAPVALUE',
        blank=True,
        null=True
    )
    overlapunit = models.SmallIntegerField(
        db_column='OVERLAPUNIT',
        blank=True,
        null=True
    )
    bomtype = models.SmallIntegerField(
        db_column='BOMTYPE',
        blank=True,
        null=True
    )
    nextlevbomtype = models.SmallIntegerField(
        db_column='NEXTLEVBOMTYPE',
        blank=True,
        null=True
    )
    variantref = models.IntegerField(
        db_column='VARIANTREF',
        blank=True,
        null=True
    )
    optional = models.SmallIntegerField(
        db_column='OPTIONAL',
        blank=True,
        null=True
    )
    defcosttype = models.SmallIntegerField(
        db_column='DEFCOSTTYPE',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_BOMLINE'
        target_db = 'erp'

class LG_BOMPARAM(
    BaseLogical,
    models.Model):
    """
        Ürün reçetesi parametreleri
    """
    paramref = models.IntegerField(
        db_column='PARAMREF',
        blank=True,
        null=True,
        help_text='Parametre ref.'
    )
    bommasterref = models.IntegerField(
        db_column='BOMMASTERREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi ref.'
    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    paramdefault = models.FloatField(
        db_column='PARAMDEFAULT',
        blank=True,
        null=True,
        help_text='Ürün reçetesi sabiti öndeğeri'
    )

    class Meta:
        managed = False
        unique_together = (('bommasterref', 'paramref'),)
        db_table = f'LG_{Active.namespace}_BOMPARAM'
        target_db = 'erp'

class LG_BOMREVSN(
    BaseLogical,
    BasePrint,
    BaseGUID,
    BaseActive,
    BaseWF,
    BaseSiteRec,
    BaseClient,
    LowLevelCodes10,
    BaseRef,
    models.Model):
    """
        Ürün reçetesi revizyonları
    """
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Revizyon kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Revizyon açıklaması'
    )
    bommasterref = models.ForeignKey(
        "LG_BOMASTER",
        db_column='BOMMASTERREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi ref. -> BOMASTER',
        on_delete=models.DO_NOTHING
    )
    routingref = models.ForeignKey(
        "LG_ROUTING",
        db_column='ROUTINGREF',
        blank=True,
        null=True,
        help_text='Üretim rotası ref. -> ROUTING',
        on_delete=models.DO_NOTHING
    )
    engchgref = models.ForeignKey(
        "LG_ENGCLINE",
        db_column='ENGCHGREF',
        blank=True,
        null=True,
        help_text='Mühendislik ref. -> ENGCLINE',
        on_delete=models.DO_NOTHING
    )
    revdate = models.DateTimeField(
        db_column='REVDATE',
        blank=True,
        null=True,
        help_text='Geçerlilik tarihi'
    )
    qtydepttime = models.IntegerField(
        db_column='QTYDEPTTIME',
        blank=True,
        null=True,
        help_text='Kullanımda değil'
    )
    qtyundepttime = models.IntegerField(
        db_column='QTYUNDEPTTIME',
        blank=True,
        null=True,
        help_text='Kullanımda değil'
    )
    stdovhdformula = models.CharField(
        db_column='STDOVHDFORMULA',
        max_length=121,
        blank=True, null=True,
        help_text='Standart genel gider maliyet formülü'
    )
    stdovhdrpformula = models.CharField(
        db_column='STDOVHDRPFORMULA',
        max_length=121,
        blank=True,
        null=True,
        help_text='Standart genel gider maliyet formülü (RD)')
    qtydepduration = models.FloatField(
        db_column='QTYDEPDURATION',
        blank=True,
        null=True,
        help_text='Zamana bağlımlı miktar (saat)'
    )
    qtyindepduration = models.FloatField(
        db_column='QTYINDEPDURATION',
        blank=True,
        null=True,
        help_text='Zaman bağımsız miktar (saat)'
    )
    overlaptype = models.SmallIntegerField(
        db_column='OVERLAPTYPE',
        blank=True,
        null=True,
        help_text='Örtüşme tipi'
    )
    overlapamnt = models.FloatField(
        db_column='OVERLAPAMNT',
        blank=True,
        null=True,
        help_text='Örtüşme miktarı'
    )
    overlapperc = models.FloatField(
        db_column='OVERLAPPERC',
        blank=True,
        null=True,
        help_text='Örtüşme oranı'
    )
    stdovhdformula2 = models.CharField(
        db_column='STDOVHDFORMULA2',
        max_length=121,
        blank=True,
        null=True
    )
    stdovhdrpformula2 = models.CharField(
        db_column='STDOVHDRPFORMULA2',
        max_length=121,
        blank=True,
        null=True
    )
    stdovhdformula3 = models.CharField(
        db_column='STDOVHDFORMULA3',
        max_length=121,
        blank=True,
        null=True
    )
    stdovhdrpformula3 = models.CharField(
        db_column='STDOVHDRPFORMULA3',
        max_length=121,
        blank=True,
        null=True
    )
    stdovhdformula4 = models.CharField(
        db_column='STDOVHDFORMULA4',
        max_length=121,
        blank=True,
        null=True
    )
    stdovhdrpformula4 = models.CharField(
        db_column='STDOVHDRPFORMULA4',
        max_length=121,
        blank=True,
        null=True
    )
    stdovhdformula5 = models.CharField(db_column='STDOVHDFORMULA5',
        max_length=121, blank=True, null=True)
    stdovhdrpformula5 = models.CharField(db_column='STDOVHDRPFORMULA5',
        max_length=121, blank=True, null=True)
    bomtype = models.SmallIntegerField(db_column='BOMTYPE', blank=True,
        null=True)
    withoutrouting = models.SmallIntegerField(db_column='WITHOUTROUTING',
        blank=True, null=True)
    usedepttimeforprd = models.SmallIntegerField(db_column='USEDEPTTIMEFORPRD',
        blank=True, null=True)
    pegtype = models.SmallIntegerField(db_column='PEGTYPE', blank=True,
        null=True)
    pegguid = models.CharField(db_column='PEGGUID', max_length=37,
        blank=True, null=True)
    usewsforprd = models.SmallIntegerField(db_column='USEWSFORPRD',
        blank=True, null=True)
    wsref = models.IntegerField(db_column='WSREF', blank=True, null=True)
    opreqref = models.IntegerField(db_column='OPREQREF', blank=True, null=True)
    printdate = models.DateTimeField(db_column='PRINTDATE', blank=True,
        null=True)
    wstype = models.SmallIntegerField(db_column='WSTYPE', blank=True,
        null=True)
    stdovhdformula6 = models.CharField(db_column='STDOVHDFORMULA6',
        max_length=121, blank=True, null=True)
    stdovhdrpformula6 = models.CharField(db_column='STDOVHDRPFORMULA6',
        max_length=121, blank=True, null=True)
    stdovhdformula7 = models.CharField(db_column='STDOVHDFORMULA7',
        max_length=121, blank=True, null=True)
    stdovhdrpformula7 = models.CharField(db_column='STDOVHDRPFORMULA7',
        max_length=121, blank=True, null=True)
    stdovhdformula8 = models.CharField(db_column='STDOVHDFORMULA8',
        max_length=121, blank=True, null=True)
    stdovhdrpformula8 = models.CharField(db_column='STDOVHDRPFORMULA8',
        max_length=121, blank=True, null=True)
    stdovhdformula9 = models.CharField(db_column='STDOVHDFORMULA9',
        max_length=121, blank=True, null=True)
    stdovhdrpformula9 = models.CharField(db_column='STDOVHDRPFORMULA9',
        max_length=121, blank=True, null=True)
    stdovhdformula10 = models.CharField(db_column='STDOVHDFORMULA10',
        max_length=121, blank=True, null=True)
    stdovhdrpformula10 = models.CharField(db_column='STDOVHDRPFORMULA10',
        max_length=121, blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (('bommasterref', 'code'),)
        db_table = f'LG_{Active.namespace}_BOMREVSN'
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"

class LG_COPRDBOM(
    BaseLogical,
    BaseSiteRec,
    BaseWF,
    BaseRef,
    models.Model):
    """
        Reçete ek ürün ataması
    """
    bommasterref = models.ForeignKey(
        "LG_BOMASTER",
        db_column='BOMMASTERREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi ref. -> BOMASTER',
        on_delete=models.DO_NOTHING
    )
    bomrevref = models.ForeignKey(
        "LG_BOMREVSN",
        db_column='BOMREVREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi revizyon ref. -> BOMREVSN',
        on_delete=models.DO_NOTHING
    )
    coprodref = models.ForeignKey(
        "LG_ITEMS",
        db_column='COPRODREF',
        blank=True,
        null=True,
        help_text='Yan ürün ref. -> ITEMS',
        on_delete=models.DO_NOTHING
    )
    coprodvrntref = models.IntegerField(
        db_column='COPRODVRNTREF',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        unique_together = (
            ('bommasterref', 'bomrevref', 'coprodref', 'coprodvrntref'),
            ('coprodref', 'coprodvrntref', 'bommasterref', 'bomrevref'),
        )
        db_table = f'LG_{Active.namespace}_COPRDBOM'
        target_db = 'erp'