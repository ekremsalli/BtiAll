"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_EMFLINE(
    BaseLogical,
    BaseCancelled,
    BaseSign,
    BaseAccount,
    BaseCenter,
    BaseSiteRec,
    BaseGUID,
    BaseProject,
    BaseRef,
    models.Model):
    """
        Muhasebe hareketleri
        EMFLINE tablosunda muhasebe fişlerinin satur bilgileri tutulmaktadır.
        Muhasebe fişlerinin her bir satırı için birer satır oluşmaktadır.
        Muhasebe fiş başlık kaydı için ise EMFICHE tablosu okunmalıdır.
    """
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )

    accficheref = models.ForeignKey(
        "LG_EMFICHE",
        db_column='ACCFICHEREF',
        blank=True,
        null=True,
        help_text='Muhasebe fişi ref. -> EMFICHE',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_accficheref"        
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Açılış'),
            (2, 'Tahsil'),
            (3, 'Tediye'),
            (4, 'Mahsup'),
            (5, 'Özel'),
            (6, 'Kur farkı hesabı')
        ],
        help_text='Fiş türü'
    )
    branch = models.SmallIntegerField(
        db_column='BRANCH',
        blank=True,
        null=True,
        help_text='İş yeri'
    )
    kebircode = models.CharField(
        db_column='KEBIRCODE',
        max_length=101,
        blank=True,
        null=True,
        help_text='Kebir kodu'
    )
    accountcode = models.CharField(
        db_column='ACCOUNTCODE',
        max_length=101,
        blank=True,
        null=True,
        help_text='Muhasebe kodu'
    )
    specode = models.CharField(
        db_column='SPECODE',
        max_length=17,
        blank=True,
        null=True,
        help_text='Özel kod'
    )
    debit = models.FloatField(
        db_column='DEBIT',
        blank=True,
        null=True,
        help_text='Borç'
    )
    credit = models.FloatField(
        db_column='CREDIT',
        blank=True,
        null=True,
        help_text='Alacak'
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    lineexp = models.CharField(
        db_column='LINEEXP',
        max_length=251,
        blank=True,
        null=True,
        help_text='Satır açıklaması'
    )
    trcurr = models.SmallIntegerField(
        db_column='TRCURR',
        blank=True,
        null=True,
        help_text='İşlem döviz türü'
    )
    currdiffcalc = models.SmallIntegerField(
        db_column='CURRDIFFCALC',
        blank=True,
        null=True,
        help_text='Kur farkı hesabı'
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
        help_text='İşlem dövizi kuru'
    )
    trnet = models.FloatField(
        db_column='TRNET',
        blank=True,
        null=True,
        help_text='İşlem döviz tutarı'
    )
    amnt = models.FloatField(
        db_column='AMNT',
        blank=True,
        null=True,
        help_text='Miktar'
    )
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ekstra dosya ref.'
    )
    emudebit = models.FloatField(
        db_column='EMUDEBIT',
        blank=True,
        null=True,
        help_text='Borç (EURO)'
    )
    emucredit = models.FloatField(
        db_column='EMUCREDIT',
        blank=True,
        null=True,
        help_text='Alacak (EURO)'
    )
    lineexctyp = models.SmallIntegerField(
        db_column='LINEEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (satır)'
    )
    crosscode = models.CharField(
        db_column='CROSSCODE', max_length=101, blank=True, null=True)

    infidx = models.FloatField(db_column='INFIDX', blank=True, null=True)
    notinflated = models.SmallIntegerField(
        db_column='NOTINFLATED', blank=True, null=True)
    notcalculated = models.SmallIntegerField(
        db_column='NOTCALCULATED', blank=True, null=True)
    fromwhere = models.SmallIntegerField(
        db_column='FROMWHERE', blank=True, null=True)
    owneraccref = models.IntegerField(
        db_column='OWNERACCREF', blank=True, null=True)
    department = models.SmallIntegerField(
        db_column='DEPARTMENT', blank=True, null=True)
    bdgtlinetype = models.SmallIntegerField(
        db_column='BDGTLINETYPE', blank=True, null=True)
    status = models.SmallIntegerField(
        db_column='STATUS', blank=True, null=True)
    bdgtfctype = models.SmallIntegerField(
        db_column='BDGTFCTYPE', blank=True, null=True)
    bdgtfcref = models.IntegerField(
        db_column='BDGTFCREF', blank=True, null=True)
    bdgtfclnref = models.IntegerField(
        db_column='BDGTFCLNREF', blank=True, null=True)
    bdgtfcprdref = models.IntegerField(
        db_column='BDGTFCPRDREF', blank=True, null=True)
    fromdemtype = models.SmallIntegerField(
        db_column='FROMDEMTYPE', blank=True, null=True)
    emdemfcref = models.IntegerField(
        db_column='EMDEMFCREF', blank=True, null=True)
    emdemlnref = models.IntegerField(
        db_column='EMDEMLNREF', blank=True, null=True)
    parentlnref = models.IntegerField(
        db_column='PARENTLNREF', blank=True, null=True)
    paidtotal = models.FloatField(
        db_column='PAIDTOTAL', blank=True, null=True)
    closed = models.SmallIntegerField(
        db_column='CLOSED', blank=True, null=True)
    outfctype = models.SmallIntegerField(
        db_column='OUTFCTYPE', blank=True, null=True)
    outfcref = models.IntegerField(
        db_column='OUTFCREF', blank=True, null=True)
    createbdgtln = models.SmallIntegerField(
        db_column='CREATEBDGTLN', blank=True, null=True)
    month_field = models.SmallIntegerField(
        db_column='MONTH_', blank=True, null=True)
    year_field = models.SmallIntegerField(
        db_column='YEAR_', blank=True, null=True)
    grpfirmtrans = models.SmallIntegerField(
        db_column='GRPFIRMTRANS', blank=True, null=True)
    invoiceno = models.CharField(
        db_column='INVOICENO', max_length=17, blank=True, null=True)
    cldef = models.CharField(
        db_column='CLDEF', max_length=201, blank=True, null=True)
    taxnr = models.CharField(
        db_column='TAXNR', max_length=12, blank=True, null=True)
    fortaxdecl = models.SmallIntegerField(
        db_column='FORTAXDECL', blank=True, null=True)
    docdate = models.DateTimeField(
        db_column='DOCDATE', blank=True, null=True)
    ufrslnref = models.IntegerField(
        db_column='UFRSLNREF', blank=True, null=True)
    ufrsnetamnt = models.FloatField(
        db_column='UFRSNETAMNT', blank=True, null=True)
    globlineno = models.IntegerField(
        db_column='GLOBLINENO', blank=True, null=True)
    linetype = models.SmallIntegerField(
        db_column='LINETYPE', blank=True, null=True)
    coderef = models.IntegerField(
        db_column='CODEREF', blank=True, null=True)
    specode2 = models.CharField(
        db_column='SPECODE2', max_length=17, blank=True, null=True)
    sourcefref = models.IntegerField(
        db_column='SOURCEFREF', blank=True, null=True)
    clcode = models.CharField(
        db_column='CLCODE', max_length=17, blank=True, null=True)
    sourceflnref = models.IntegerField(
        db_column='SOURCEFLNREF', blank=True, null=True)
    disttempref = models.IntegerField(
        db_column='DISTTEMPREF', blank=True, null=True)
    tckno = models.CharField(
        db_column='TCKNO', max_length=16, blank=True, null=True)
    cashline = models.SmallIntegerField(
        db_column='CASHLINE', blank=True, null=True)
    mnthcount = models.SmallIntegerField(
        db_column='MNTHCOUNT', blank=True, null=True)
    mnthsourceref = models.IntegerField(
        db_column='MNTHSOURCEREF', blank=True, null=True)
    mnthline = models.SmallIntegerField(
        db_column='MNTHLINE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_EMFLINE'
        target_db = 'erp'
