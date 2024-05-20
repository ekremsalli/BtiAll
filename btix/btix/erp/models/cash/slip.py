"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_KSLINES(
    BaseLogical,
    BaseCode,
    BaseAccounted,
    BaseCancelled,
    BasePrint,
    BaseInfo,
    BaseSign,
    BaseTrading,
    BaseTextINC,
    BaseAmount,
    BaseSiteRec,
    BaseWF,
    BaseProject,
    BaseSalesMan,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Kasa hareketi
        KSLINES tablosunda kasadan yapılan cari hesap, banka, fatura,
        çek/senet ya da kasa işlemleri gibi işlemlerden sonra oluşan
        hareketler tutulmaktadır.
    """
    cardref = models.ForeignKey(
        "LG_KSCARD",
        db_column='CARDREF',
        blank=True,
        null=True,
        help_text='Kasa kart ref. -> KSCARD',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_cardref"
    )
    vcardref = models.ForeignKey(
        'LG_KSCARD',
        db_column='VCARDREF',
        blank=True,
        null=True,
        help_text='Virman yapılan kasa kart ref. -> KSCARD',
        on_delete=models.DO_NOTHING
    )
    transref = models.IntegerField(
        db_column='TRANSREF',
        blank=True,
        null=True,
        help_text='İlgili modulun ilgili işlem ref.'
    )
    accref = models.ForeignKey(
        'LG_EMUHACC',
        db_column='ACCREF',
        blank=True,
        null=True,
        help_text='Muhasebe hesabı ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_accref"
    )
    centerref = models.ForeignKey(
        'LG_EMCENTER',
        db_column='CENTERREF',
        blank=True,
        null=True,
        help_text='Masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_centerref"
    )
    csaccref = models.ForeignKey(
        'LG_EMUHACC',
        db_column='CSACCREF',
        blank=True,
        null=True,
        help_text='Karşı kasanın muhasebe ref. -> EMUHACC',
        on_delete=models.DO_NOTHING
    )
    cscenterref = models.ForeignKey(
        'LG_EMCENTER',
        db_column='CSCENTERREF',
        blank=True,
        null=True,
        help_text='Karşı kasanın masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    hour_field = models.SmallIntegerField(
        db_column='HOUR_',
        blank=True,
        null=True,
        help_text='Saat'
    )
    minute_field = models.SmallIntegerField(
        db_column='MINUTE_',
        blank=True,
        null=True,
        help_text='Dakika'
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (11, 'Cari hesap tahsilat'),
            (12, 'Cari hesap ödeme'),
            (21, 'Banka'),
            (22, 'Banka'),
            (31, 'Fatura'),
            (32, 'Fatura'),
            (33, 'Fatura'),
            (34, 'Fatura'),
            (35, 'Fatura'),
            (36, 'Fatura'),
            (37, 'Fatura'),
            (38, 'Fatura'),
            (39, 'Fatura'),
            (61, 'Çek/senet'),
            (62, 'Çek/senet'),
            (63, 'Çek/senet'),
            (64, 'Çek/senet'),
            (71, 'Kasa'),
            (72, 'Kasa'),
            (73, 'Kasa'),
            (74, 'Kasa')
        ],
        help_text='İşlem türü'
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
    destbranch = models.SmallIntegerField(
        db_column='DESTBRANCH',
        blank=True,
        null=True,
        help_text='Gönderilen iş yeri'
    )
    destdepartment = models.SmallIntegerField(
        db_column='DESTDEPARTMENT',
        blank=True,
        null=True,
        help_text='Gönderilen bölüm'
    )
    ficheno = models.CharField(
        db_column='FICHENO',
        max_length=17,
        blank=True,
        null=True,
        help_text='Fiş numarası'
    )
    custtitle = models.CharField(
        db_column='CUSTTITLE',
        max_length=51,
        blank=True,
        null=True,
        help_text='Kasa açıklaması'
    )
    lineexp = models.CharField(
        db_column='LINEEXP',
        max_length=201,
        blank=True,
        null=True
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
    trrate = models.FloatField(
        db_column='TRRATE',
        blank=True,
        null=True,
        help_text='İşlem döviz kuru'
    )
    trnet = models.FloatField(
        db_column='TRNET',
        blank=True,
        null=True,
        help_text='İşlem döviz tutarı'
    )
    trcurr = models.SmallIntegerField(
        db_column='TRCURR',
        blank=True,
        null=True,
        help_text='İşlem döviz türü'
    )
    accficheref = models.ForeignKey(
        "LG_EMFICHE",
        db_column='ACCFICHEREF',
        blank=True,
        null=True,
        help_text='Muhasebe fiş ref. -> EMFICHE',
        on_delete=models.DO_NOTHING
    )
    cancelledacc = models.SmallIntegerField(
        db_column='CANCELLEDACC',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Muhasebeleştirme iptal'
    )
    genexctyp = models.SmallIntegerField(
        db_column='GENEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (genel)'
    )
    lineexctyp = models.SmallIntegerField(
        db_column='LINEEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (satır)'
    )
    gpoptype = models.SmallIntegerField(
        db_column='GPOPTYPE',
        blank=True,
        null=True
    )
    gpincometacrat = models.FloatField(
        db_column='GPINCOMETACRAT',
        blank=True,
        null=True
    )
    gpfundsharerat = models.FloatField(
        db_column='GPFUNDSHARERAT',
        blank=True,
        null=True
    )
    gpplate = models.CharField(
        db_column='GPPLATE',
        max_length=17,
        blank=True,
        null=True
    )
    gptaxacc = models.IntegerField(
        db_column='GPTAXACC',
        blank=True,
        null=True
    )
    gpfundacc = models.IntegerField(
        db_column='GPFUNDACC',
        blank=True,
        null=True
    )
    gpaddr = models.CharField(
        db_column='GPADDR',
        max_length=51,
        blank=True,
        null=True
    )
    smmvatrate = models.FloatField(
        db_column='SMMVATRATE',
        blank=True,
        null=True
    )
    smmvatacref = models.IntegerField(
        db_column='SMMVATACREF', blank=True, null=True)
    smmvatcentref = models.IntegerField(
        db_column='SMMVATCENTREF', blank=True, null=True)
    smmdocode = models.CharField(
        db_column='SMMDOCODE', max_length=33, blank=True, null=True)
    infidx = models.FloatField(
        db_column='INFIDX', blank=True, null=True)
    trangrpno = models.CharField(
        db_column='TRANGRPNO', max_length=17, blank=True, null=True)
    trangrplineno = models.SmallIntegerField(
        db_column='TRANGRPLINENO', blank=True, null=True)
    orglogoid = models.CharField(
        db_column='ORGLOGOID', max_length=25, blank=True, null=True)
    vatinc = models.SmallIntegerField(
        db_column='VATINC', blank=True, null=True)
    vatrat = models.FloatField(
        db_column='VATRAT', blank=True, null=True)
    vataccref = models.IntegerField(
        db_column='VATACCREF', blank=True, null=True)
    vattot = models.FloatField(
        db_column='VATTOT', blank=True, null=True)
    cstransref = models.IntegerField(
        db_column='CSTRANSREF', blank=True, null=True)
    status = models.SmallIntegerField(
        db_column='STATUS', blank=True, null=True)
    wflowcrdref = models.IntegerField(
        db_column='WFLOWCRDREF', blank=True, null=True)
    affectcollatrl = models.SmallIntegerField(
        db_column='AFFECTCOLLATRL', blank=True, null=True)
    grpfirmtrans = models.SmallIntegerField(
        db_column='GRPFIRMTRANS', blank=True, null=True)
    tranno = models.CharField(
        db_column='TRANNO', max_length=17, blank=True, null=True)
    docode = models.CharField(
        db_column='DOCODE', max_length=33, blank=True, null=True)
    affectrisk = models.SmallIntegerField(
        db_column='AFFECTRISK', blank=True, null=True)
    reflected = models.SmallIntegerField(
        db_column='REFLECTED', blank=True, null=True)
    reflaccficheref = models.IntegerField(
        db_column='REFLACCFICHEREF', blank=True, null=True)
    cancelledreflacc = models.SmallIntegerField(
        db_column='CANCELLEDREFLACC', blank=True, null=True)
    taxnr = models.CharField(
        db_column='TAXNR', max_length=12, blank=True, null=True)
    approve = models.SmallIntegerField(
        db_column='APPROVE', blank=True, null=True)
    approvedate = models.DateTimeField(
        db_column='APPROVEDATE', blank=True, null=True)
    tckno = models.CharField(
        db_column='TCKNO', max_length=12, blank=True, null=True)
    isperscomp = models.SmallIntegerField(
        db_column='ISPERSCOMP', blank=True, null=True)
    eximtype = models.SmallIntegerField(
        db_column='EXIMTYPE', blank=True, null=True)
    eximfileref = models.IntegerField(
        db_column='EXIMFILEREF', blank=True, null=True)
    eximprocnr = models.SmallIntegerField(
        db_column='EXIMPROCNR', blank=True, null=True)
    eidistflnnr = models.SmallIntegerField(
        db_column='EIDISTFLNNR', blank=True, null=True)
    eisrvdsttyp = models.SmallIntegerField(
        db_column='EISRVDSTTYP', blank=True, null=True)
    eximdisttyp = models.SmallIntegerField(
        db_column='EXIMDISTTYP', blank=True, null=True)
    salesmanref = models.IntegerField(
        db_column='SALESMANREF', blank=True, null=True)
    docdate = models.DateTimeField(
        db_column='DOCDATE', blank=True, null=True)
    offerref = models.IntegerField(
        db_column='OFFERREF', blank=True, null=True)
    emflineref = models.IntegerField(
        db_column='EMFLINEREF', blank=True, null=True)
    candeduct = models.SmallIntegerField(
        db_column='CANDEDUCT', blank=True, null=True)
    deductionpart1 = models.SmallIntegerField(
        db_column='DEDUCTIONPART1', blank=True, null=True)
    deductionpart2 = models.SmallIntegerField(
        db_column='DEDUCTIONPART2', blank=True, null=True)
    underdeductlimit = models.SmallIntegerField(
        db_column='UNDERDEDUCTLIMIT', blank=True, null=True)
    vatdeductrate = models.FloatField(
        db_column='VATDEDUCTRATE', blank=True, null=True)
    vatdeductaccref = models.IntegerField(
        db_column='VATDEDUCTACCREF', blank=True, null=True)
    vatdeductothaccref = models.IntegerField(
        db_column='VATDEDUCTOTHACCREF', blank=True, null=True)
    vatdeductcenref = models.IntegerField(
        db_column='VATDEDUCTCENREF', blank=True, null=True)
    vatdeductothcenref = models.IntegerField(
        db_column='VATDEDUCTOTHCENREF', blank=True, null=True)
    cantcrededuct = models.SmallIntegerField(
        db_column='CANTCREDEDUCT', blank=True, null=True)
    cltrcurr = models.SmallIntegerField(
        db_column='CLTRCURR', blank=True, null=True)
    cltrrate = models.FloatField(
        db_column='CLTRRATE', blank=True, null=True)
    cltrnet = models.FloatField(
        db_column='CLTRNET', blank=True, null=True)
    brutamount = models.FloatField(
        db_column='BRUTAMOUNT', blank=True, null=True)
    netamount = models.FloatField(
        db_column='NETAMOUNT', blank=True, null=True)
    brutamounttr = models.FloatField(
        db_column='BRUTAMOUNTTR', blank=True, null=True)
    netamounttr = models.FloatField(
        db_column='NETAMOUNTTR', blank=True, null=True)
    brutamountrep = models.FloatField(
        db_column='BRUTAMOUNTREP', blank=True, null=True)
    netamountrep = models.FloatField(
        db_column='NETAMOUNTREP', blank=True, null=True)
    crcardwzd = models.SmallIntegerField(
        db_column='CRCARDWZD', blank=True, null=True)
    smmserialcode = models.CharField(
        db_column='SMMSERIALCODE', max_length=17, blank=True, null=True)
    cashaccref = models.IntegerField(
        db_column='CASHACCREF', blank=True, null=True)
    cashcenref = models.IntegerField(
        db_column='CASHCENREF', blank=True, null=True)
    printdate = models.DateTimeField(
        db_column='PRINTDATE', blank=True, null=True)
    incdeductamnt = models.SmallIntegerField(
        db_column='INCDEDUCTAMNT', blank=True, null=True)
    affectcost = models.SmallIntegerField(
        db_column='AFFECTCOST', blank=True, null=True)
    custtitle2 = models.CharField(
        db_column='CUSTTITLE2', max_length=51, blank=True, null=True)
    typecode = models.CharField(
        db_column='TYPECODE', max_length=5, blank=True, null=True)
    einvoice = models.SmallIntegerField(
        db_column='EINVOICE', blank=True, null=True)
    time_field = models.IntegerField(
        db_column='TIME_', blank=True, null=True)
    deductcode = models.CharField(
        db_column='DEDUCTCODE', max_length=11, blank=True, null=True)
    servreasondef = models.CharField(
        db_column='SERVREASONDEF', max_length=251, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_KSLINES'
        unique_together = (
            ('cardref', 'date_field', 'hour_field', 'minute_field', 'ficheno'),
            ('cardref', 'ficheno'),
        )
        target_db = 'erp'
