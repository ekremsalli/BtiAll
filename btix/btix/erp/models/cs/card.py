"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_CSCARD(
    BaseLogical,
    BaseCode,
    BaseInfo,
    BaseAmount,
    BaseSiteRec,
    BaseWF,
    BaseGUID,
    BaseProject,
    BaseCancelled,
    BaseTextINC,
    BaseSalesMan,
    BaseTrading,
    BaseRef,
    models.Model):
    """
        Çek / Senet kartları
        CSCARD tablosunda çek ya da senedin üzerinde bulunan bilgiler
        tutulmaktadır. Çek ve senetlerin veri tabanına sadece bordrolarla
        kaydolduğu ve yapılan ilgili her işlemin yine bordrolar aracılığı
        ile kaydedildiği unutulmamalıdır. Her çek ya da senet için
        yapılan işlemde o çek ya da senet için bir çek senet
        hareketi oluşmalıdır.
    """
    doc = models.SmallIntegerField(
        db_column='DOC',
        blank=True,
        null=True,
        choices=[
            (1, 'Müşteri çeki'),
            (2, 'Müşteri senedi'),
            (3, 'Kendi çekimiz'),
            (4, 'Borç senedimiz')
        ],
        help_text='Çek / senet türü')
    currstat = models.SmallIntegerField(
        db_column='CURRSTAT',
        blank=True,
        null=True,
        help_text="""
            Şimdiki statüsü
            doc=1 ise;
                1 -> Müşteriye iade
                2 -> Portföyden tahsil
                3 -> Bankada tahsil
                4 -> Portföyde karşılıksız
                5 -> Bankada karşılıksız
                6 -> Müşteriden portföye iade
                7 -> Bankadan portföye iade
                8 -> Müşteriden karşılıksız iade
                9 -> Cirodan tahsil
                A(10) -> Tahsil edilemiyor
            doc=2 ise;
                1 -> Müşteriye iade
                2 -> Portföyden tahsil
                3 -> Bankada tahsil
                4 -> Portföyde protestolu
                5 -> Bankada protestolu
                6 -> Müşteriden portföye iade
                7 -> Bankadan protföye iade
                8 -> Müşteriden protestolu iade
                9 -> Cirodan tahsil
                A(10) -> Tahsil edilemiyor
            doc=3 ise;
                1 -> Müşteriden iade
                2 -> Müşteride tahsil
            doc=4 ise;
                1 -> Müşteriden iade
                2 -> Müşteride tahsil
                3 -> Müşteride protesto
                4 -> Tahsil edilemiyor
        """
    )
    ourbankref = models.ForeignKey(
        "LG_BNCARD",
        db_column='OURBANKREF',
        blank=True,
        null=True,
        help_text='Yazılan çekin ait olduğu banka -> BNCARD',
        on_delete=models.DO_NOTHING
    )
    portfoyno = models.CharField(
        db_column='PORTFOYNO',
        max_length=9,
        blank=True,
        null=True,
        help_text='Portföy numarası'
    )
    serino = models.CharField(
        db_column='SERINO',
        max_length=25,
        blank=True,
        null=True,
        help_text='Çek numarası'
    )
    bankname = models.CharField(
        db_column='BANKNAME',
        max_length=21,
        blank=True,
        null=True,
        help_text='Banka adı'
    )
    city = models.CharField(
        db_column='CITY',
        max_length=16,
        blank=True,
        null=True,
        help_text='Şehir (Ödeme yeri)'
    )
    owing = models.CharField(
        db_column='OWING',
        max_length=201,
        blank=True,
        null=True,
        help_text='Çek ya da senetin borçlusu')
    kefil = models.CharField(
        db_column='KEFIL',
        max_length=31,
        blank=True,
        null=True,
        help_text='Kefil'
    )
    muhabir = models.CharField(
        db_column='MUHABIR',
        max_length=31,
        blank=True,
        null=True,
        help_text='Muhabir şube'
    )
    branch = models.SmallIntegerField(
        db_column='BRANCH',
        blank=True,
        null=True,
        help_text='Şube'
    )
    duedate = models.DateTimeField(
        db_column='DUEDATE',
        blank=True,
        null=True,
        help_text='Vade'
    )
    setdate = models.DateTimeField(
        db_column='SETDATE',
        blank=True,
        null=True,
        help_text='Tanzim tarihi'
    )
    stamp = models.FloatField(
        db_column='STAMP',
        blank=True,
        null=True,
        help_text='Pul'
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
        help_text='İşlem tutarı'
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
        help_text='Raporlama döviz tutarı'
    )
    riskupdate = models.SmallIntegerField(
        db_column='RISKUPDATE',
        blank=True,
        null=True,
        help_text='Riskten düşülecek E/H'
    )
    devir = models.SmallIntegerField(
        db_column='DEVIR',
        blank=True,
        null=True,
        help_text='Devir'
    )
    inuse = models.SmallIntegerField(
        db_column='INUSE',
        blank=True,
        null=True,
        help_text='Kullanımda'
    )
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ekstra dosya ref.'
    )
    collreprate = models.FloatField(
        db_column='COLLREPRATE',
        blank=True,
        null=True,
        help_text='Tahsil edildiğindeki raporlama döviz kuru'
    )
    colltrrate = models.FloatField(
        db_column='COLLTRRATE',
        blank=True,
        null=True,
        help_text='Tahsilat edildiğindeki raporlama döviz kuru'
    )
    lineexctyp = models.SmallIntegerField(
        db_column='LINEEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (satır)'
    )
    bnbranchno = models.CharField(db_column='BNBRANCHNO', max_length=51,
        blank=True, null=True, help_text='Banka şubesi numarası')
    bnaccountno = models.CharField(db_column='BNACCOUNTNO', max_length=51,
        blank=True, null=True, help_text='Banka hesabı numarası')
    deptaddr1 = models.CharField(db_column='DEPTADDR1', max_length=51,
        blank=True, null=True, help_text='Borçlu adresi (1)')
    deptaddr2 = models.CharField(db_column='DEPTADDR2', max_length=51,
        blank=True, null=True, help_text='Borçlu adresi (2)')
    deptcity = models.CharField(db_column='DEPTCITY', max_length=21,
        blank=True, null=True, help_text='Borçlu şehir')
    deptcitycode = models.CharField(db_column='DEPTCITYCODE', max_length=13,
        blank=True, null=True, help_text='Borçlu şehir kodu')
    deptcountry = models.CharField(db_column='DEPTCOUNTRY', max_length=21,
        blank=True, null=True, help_text='')
    deptcountrycode = models.CharField(db_column='DEPTCOUNTRYCODE',
        max_length=13, blank=True, null=True, help_text='Borçlu ülke kodu')
    deptpostcode = models.CharField(db_column='DEPTPOSTCODE', max_length=11,
        blank=True, null=True, help_text='Borçlu posta kodu')
    depttelnrs1 = models.CharField(db_column='DEPTTELNRS1', max_length=16,
        blank=True, null=True, help_text='Borçlu telefon numarası (1)')
    depttelnrs2 = models.CharField(db_column='DEPTTELNRS2', max_length=16,
        blank=True, null=True, help_text='Borçlu telefon numarası (2)')
    deptfaxnr = models.CharField(db_column='DEPTFAXNR', max_length=16,
        blank=True, null=True, help_text='Borçlu faks numarası')
    depttown = models.CharField(db_column='DEPTTOWN', max_length=51,
        blank=True, null=True, help_text='Borçlu ilçe açıklaması')
    depttowncode = models.CharField(db_column='DEPTTOWNCODE', max_length=13,
        blank=True, null=True, help_text='Borçlu ilçe kodu')
    deptdistrict = models.CharField(db_column='DEPTDISTRICT', max_length=51,
        blank=True, null=True, help_text='Borçlu semt açıklaması')
    deptdistrictcode = models.CharField(db_column='DEPTDISTRICTCODE',
        max_length=13, blank=True, null=True, help_text='Borçlu semt kodu')
    opstat = models.SmallIntegerField(db_column='OPSTAT', blank=True,
        null=True, help_text='Hareket durumu')
    printcnt = models.SmallIntegerField(db_column='PRINTCNT', blank=True,
        null=True, help_text='Basılmış olanların sayısı')
    newserino = models.CharField(db_column='NEWSERINO', max_length=31,
        blank=True, null=True, help_text='Yeni seri numarası')
    telcodes1 = models.CharField(db_column='TELCODES1', max_length=9,
        blank=True, null=True)
    telcodes2 = models.CharField(db_column='TELCODES2', max_length=9,
        blank=True, null=True)
    faxcode = models.CharField(db_column='FAXCODE', max_length=9,
        blank=True, null=True)
    affectcollatrl = models.SmallIntegerField(db_column='AFFECTCOLLATRL',
        blank=True, null=True)
    collatrollref = models.IntegerField(db_column='COLLATROLLREF',
        blank=True, null=True)
    collatcardref = models.IntegerField(db_column='COLLATCARDREF',
        blank=True, null=True)
    affectrisk = models.SmallIntegerField(db_column='AFFECTRISK',
        blank=True, null=True)
    giroreprate = models.FloatField(db_column='GIROREPRATE',
        blank=True, null=True)
    girotrrate = models.FloatField(db_column='GIROTRRATE',
        blank=True, null=True)
    orglogoid = models.CharField(db_column='ORGLOGOID', max_length=25,
        blank=True, null=True)
    giroamount = models.FloatField(db_column='GIROAMOUNT',
        blank=True, null=True)
    girorepnet = models.FloatField(db_column='GIROREPNET',
        blank=True, null=True)
    usegirorate = models.SmallIntegerField(db_column='USEGIRORATE',
        blank=True, null=True)
    taxnr = models.CharField(db_column='TAXNR', max_length=51,
        blank=True, null=True)
    iban = models.CharField(db_column='IBAN', max_length=51,
        blank=True, null=True)
    useraisedval = models.SmallIntegerField(db_column='USERAISEDVAL',
        blank=True, null=True)
    raisedvalamount = models.FloatField(db_column='RAISEDVALAMOUNT',
        blank=True, null=True)
    raisedvalrepnet = models.FloatField(db_column='RAISEDVALREPNET',
        blank=True, null=True)
    subduration = models.IntegerField(db_column='SUBDURATION',
        blank=True, null=True)
    degactive = models.SmallIntegerField(db_column='DEGACTIVE',
        blank=True, null=True)
    degcurr = models.SmallIntegerField(db_column='DEGCURR',
        blank=True, null=True)
    degcurrrate = models.FloatField(db_column='DEGCURRRATE',
        blank=True, null=True)
    ciro = models.SmallIntegerField(db_column='CIRO',
        blank=True, null=True)
    kefil2 = models.CharField(db_column='KEFIL2',
        max_length=31, blank=True, null=True)
    offerref = models.IntegerField(db_column='OFFERREF',
        blank=True, null=True)
    printdate = models.DateTimeField(db_column='PRINTDATE', blank=True,
        null=True)
    status = models.SmallIntegerField(db_column='STATUS',
        blank=True, null=True)
    bncreref = models.IntegerField(db_column='BNCREREF',
        blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (('doc', 'portfoyno'),)
        db_table = f'LG_{Active.namespace}_{Active.period}_CSCARD'
        target_db = 'erp'

    # rels -> L_BANKACC, L_PROJECT
