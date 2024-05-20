"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_CLRNUMS(
    BaseLogical,
    models.Model):
    """
        Cari hesap risk rakamları portu
        CLRNUMS tablosunda cari hesaba ait risk bilgileri ve o cari
        hesaba ait ödenmeyen ya da protesto olan çek ya da senetlerinin
        toplamını gösteren bilgiler bulunmaktadır.
    """
    clcardref = models.OneToOneField(
        "LG_CLCARD",
        db_column='CLCARDREF',
        unique=True,
        blank=True,
        null=True,
        help_text='Cari hesap ref. -> CLCARD',
        on_delete=models.DO_NOTHING
    )
    risktype = models.SmallIntegerField(
        db_column='RISKTYPE',
        blank=True,
        null=True,
        help_text='Risk türü'
    )
    riskover = models.SmallIntegerField(
        db_column='RISKOVER',
        blank=True,
        null=True,
        help_text='Risk kontrol'
    )
    ps = models.FloatField(
        db_column='PS',
        blank=True,
        null=True,
        help_text='Protestolu senetler'
    )
    kc = models.FloatField(
        db_column='KC',
        blank=True,
        null=True,
        help_text='Karşılıksız çekler'
    )
    risktotal = models.FloatField(db_column='RISKTOTAL', blank=True,
        null=True, help_text='Risk toplamı')
    desprisktotal = models.FloatField(db_column='DESPRISKTOTAL',
        blank=True, null=True, help_text='İrsaliye risk toplamı')
    risklimit = models.FloatField(db_column='RISKLIMIT', blank=True,
        null=True, help_text='Risk limiti')
    riskbalanced = models.FloatField(db_column='RISKBALANCED',
        blank=True, null=True, help_text='Sevkedilen (ayarlanan) risk')
    cekriskfactor = models.FloatField(db_column='CEKRISKFACTOR', blank=True,
        null=True, help_text='Çek risk faktörü')
    senetriskfactor = models.FloatField(db_column='SENETRISKFACTOR',
        blank=True, null=True, help_text='Senet risk faktörü')
    cek0_debit = models.FloatField(db_column='CEK0_DEBIT', blank=True,
        null=True, help_text='Çek (Borç)')
    cek0_credit = models.FloatField(db_column='CEK0_CREDIT', blank=True,
        null=True, help_text='Çek (Alacak)')
    cek1_debit = models.FloatField(db_column='CEK1_DEBIT', blank=True,
        null=True, help_text='Çek (Borç)')
    cek1_credit = models.FloatField(db_column='CEK1_CREDIT', blank=True,
        null=True, help_text='Çek (Alacak)')
    senet0_debit = models.FloatField(db_column='SENET0_DEBIT', blank=True,
        null=True, help_text='Senet - Borç')
    senet0_credit = models.FloatField(db_column='SENET0_CREDIT', blank=True,
        null=True, help_text='Senet - Alacak')
    senet1_debit = models.FloatField(db_column='SENET1_DEBIT', blank=True,
        null=True, help_text='Senet - Borç')
    senet1_credit = models.FloatField(db_column='SENET1_CREDIT', blank=True,
        null=True, help_text='Senet - Alacak')
    cekcurr0_debit = models.FloatField(db_column='CEKCURR0_DEBIT',
        blank=True, null=True, help_text='Çek (Borç)')
    cekcurr0_credit = models.FloatField(db_column='CEKCURR0_CREDIT',
        blank=True, null=True, help_text='Çek (Alacak)')
    cekcurr1_debit = models.FloatField(db_column='CEKCURR1_DEBIT',
        blank=True, null=True, help_text='Çek (Borç)')
    cekcurr1_credit = models.FloatField(db_column='CEKCURR1_CREDIT',
        blank=True, null=True, help_text='Çek (Alacak)')
    senetcurr0_debit = models.FloatField(db_column='SENETCURR0_DEBIT',
        blank=True, null=True, help_text='Senet (Borç)')
    senetcurr0_credit = models.FloatField(db_column='SENETCURR0_CREDIT',
        blank=True, null=True, help_text='Senet (Alacak)')
    senetcurr1_debit = models.FloatField(db_column='SENETCURR1_DEBIT',
        blank=True, null=True, help_text='Senet (Borç)')
    senetcurr1_credit = models.FloatField(db_column='SENETCURR1_CREDIT',
        blank=True, null=True, help_text='Senet (Alacak)')
    ordriskover = models.SmallIntegerField(db_column='ORDRISKOVER',
        blank=True, null=True, help_text='Sipariş risk aşımı')
    despriskover = models.SmallIntegerField(db_column='DESPRISKOVER',
        blank=True, null=True, help_text='İrsaliye risk aşımı')
    usereprisk = models.SmallIntegerField(db_column='USEREPRISK',
        blank=True, null=True, help_text='Risk takibinde kullanılacak')
    reprisktotal = models.FloatField(db_column='REPRISKTOTAL', blank=True,
        null=True, help_text='RD risk toplamı')
    repdesprisktotal = models.FloatField(db_column='REPDESPRISKTOTAL',
        blank=True, null=True, help_text='RS irsaliye risk toplamı')
    reprisklimit = models.FloatField(db_column='REPRISKLIMIT', blank=True,
        null=True, help_text='RS risk limiti')
    repriskbalanced = models.FloatField(db_column='REPRISKBALANCED',
        blank=True, null=True, help_text='RD ayarlanmış risk')
    repps = models.FloatField(db_column='REPPS', blank=True,
        null=True, help_text='RD ayarlanmış risk')
    repkc = models.FloatField(db_column='REPKC', blank=True,
        null=True, help_text='RD protestolu senetler')
    ordrisktotal = models.FloatField(db_column='ORDRISKTOTAL', blank=True,
        null=True, help_text='Sipariş risk limiti')
    ordrisktotalsugg = models.FloatField(db_column='ORDRISKTOTALSUGG',
        blank=True, null=True, help_text='Sipariş risk limiti (öneri)')
    repordrisktotal = models.FloatField(db_column='REPORDRISKTOTAL',
        blank=True, null=True, help_text='RD sipariş risk toplamı')
    repordrisktotalsugg = models.FloatField(db_column='REPORDRISKTOTALSUGG',
        blank=True, null=True, help_text='RD sipariş risk toplamı (öneri)')
    risktypes1 = models.SmallIntegerField(db_column='RISKTYPES1',
        blank=True, null=True)
    risktypes2 = models.SmallIntegerField(db_column='RISKTYPES2',
        blank=True, null=True)
    risktypes3 = models.SmallIntegerField(db_column='RISKTYPES3',
        blank=True, null=True)
    risktypes4 = models.SmallIntegerField(db_column='RISKTYPES4',
        blank=True, null=True)
    risktypes5 = models.SmallIntegerField(db_column='RISKTYPES5',
        blank=True, null=True)
    cstcekriskfactor = models.FloatField(db_column='CSTCEKRISKFACTOR',
        blank=True, null=True)
    cstsenetriskfactor = models.FloatField(db_column='CSTSENETRISKFACTOR',
        blank=True, null=True)
    riskgrpcontrol = models.SmallIntegerField(db_column='RISKGRPCONTROL',
        blank=True, null=True)
    accriskover = models.SmallIntegerField(db_column='ACCRISKOVER',
        blank=True, null=True)
    cstcsriskover = models.SmallIntegerField(db_column='CSTCSRISKOVER',
        blank=True, null=True)
    mycsriskover = models.SmallIntegerField(db_column='MYCSRISKOVER',
        blank=True, null=True)
    riskctrltype = models.SmallIntegerField(db_column='RISKCTRLTYPE',
        blank=True, null=True)
    accrisktotal = models.FloatField(db_column='ACCRISKTOTAL',
        blank=True, null=True)
    repaccrisktotal = models.FloatField(db_column='REPACCRISKTOTAL',
        blank=True, null=True)
    cstcsrisktotal = models.FloatField(db_column='CSTCSRISKTOTAL',
        blank=True, null=True)
    repcstcsrisktotal = models.FloatField(db_column='REPCSTCSRISKTOTAL',
        blank=True, null=True)
    mycsrisktotal = models.FloatField(db_column='MYCSRISKTOTAL',
        blank=True, null=True)
    repmycsrisktotal = models.FloatField(db_column='REPMYCSRISKTOTAL',
        blank=True, null=True)
    accrisklimit = models.FloatField(db_column='ACCRISKLIMIT',
        blank=True, null=True)
    repaccrisklimit = models.FloatField(db_column='REPACCRISKLIMIT',
        blank=True, null=True)
    cstcsrisklimit = models.FloatField(db_column='CSTCSRISKLIMIT',
        blank=True, null=True)
    repcstcsrisklimit = models.FloatField(db_column='REPCSTCSRISKLIMIT',
        blank=True, null=True)
    mycsrisklimit = models.FloatField(db_column='MYCSRISKLIMIT',
        blank=True, null=True)
    repmycsrisklimit = models.FloatField(db_column='REPMYCSRISKLIMIT',
        blank=True, null=True)
    desprisklimit = models.FloatField(db_column='DESPRISKLIMIT',
        blank=True, null=True)
    repdesprisklimit = models.FloatField(db_column='REPDESPRISKLIMIT',
        blank=True, null=True)
    ordrisklimit = models.FloatField(db_column='ORDRISKLIMIT',
        blank=True, null=True)
    repordrisklimit = models.FloatField(db_column='REPORDRISKLIMIT',
        blank=True, null=True)
    ordrisklimitsugg = models.FloatField(db_column='ORDRISKLIMITSUGG',
        blank=True, null=True)
    repordrisklimitsugg = models.FloatField(db_column='REPORDRISKLIMITSUGG',
        blank=True, null=True)
    accrskblnced = models.FloatField(db_column='ACCRSKBLNCED',
        blank=True, null=True)
    repaccrskblnced = models.FloatField(db_column='REPACCRSKBLNCED',
        blank=True, null=True)
    cstcsrskblnced = models.FloatField(db_column='CSTCSRSKBLNCED',
        blank=True, null=True)
    repcstcsrskblnced = models.FloatField(db_column='REPCSTCSRSKBLNCED',
        blank=True, null=True)
    mycsrskblnced = models.FloatField(db_column='MYCSRSKBLNCED',
        blank=True, null=True)
    repmycsrskblnced = models.FloatField(db_column='REPMYCSRSKBLNCED',
        blank=True, null=True)
    desprskblnced = models.FloatField(db_column='DESPRSKBLNCED',
        blank=True, null=True)
    repdesprskblnced = models.FloatField(db_column='REPDESPRSKBLNCED',
        blank=True, null=True)
    ordrskblnced = models.FloatField(db_column='ORDRSKBLNCED',
        blank=True, null=True)
    repordrskblnced = models.FloatField(db_column='REPORDRSKBLNCED',
        blank=True, null=True)
    ordrskblncedsug = models.FloatField(db_column='ORDRSKBLNCEDSUG',
        blank=True, null=True)
    repordrskblncedsug = models.FloatField(db_column='REPORDRSKBLNCEDSUG',
        blank=True, null=True)
    ordriskoversugg = models.SmallIntegerField(db_column='ORDRISKOVERSUGG',
        blank=True, null=True)
    csdownsrisk = models.SmallIntegerField(db_column='CSDOWNSRISK',
        blank=True, null=True)
    cstcsciroriskover = models.SmallIntegerField(
        db_column='CSTCSCIRORISKOVER', blank=True, null=True)
    cstcirocekriskfac = models.FloatField(
        db_column='CSTCIROCEKRISKFAC', blank=True, null=True)
    cstcirosenetriskfac = models.FloatField(
        db_column='CSTCIROSENETRISKFAC', blank=True, null=True)
    cscirodownsrisk = models.SmallIntegerField(
        db_column='CSCIRODOWNSRISK', blank=True, null=True)
    cstcscirorisklimit = models.FloatField(
        db_column='CSTCSCIRORISKLIMIT', blank=True, null=True)
    repcstcscirorisklim = models.FloatField(
        db_column='REPCSTCSCIRORISKLIM', blank=True, null=True)
    cstcscirorskblnced = models.FloatField(
        db_column='CSTCSCIRORSKBLNCED', blank=True, null=True)
    repcstcscirorskbln = models.FloatField(
        db_column='REPCSTCSCIRORSKBLN', blank=True, null=True)
    cstcsownrisktotal = models.FloatField(
        db_column='CSTCSOWNRISKTOTAL', blank=True, null=True)
    repcstcsownrisktot = models.FloatField(
        db_column='REPCSTCSOWNRISKTOT', blank=True, null=True)
    cstcscirorisktotal = models.FloatField(
        db_column='CSTCSCIRORISKTOTAL', blank=True, null=True)
    repcstcscirorisktot = models.FloatField(
        db_column='REPCSTCSCIRORISKTOT', blank=True, null=True)
    despriskoversug = models.SmallIntegerField(
        db_column='DESPRISKOVERSUG', blank=True, null=True)
    desprisklimitsug = models.FloatField(
        db_column='DESPRISKLIMITSUG', blank=True, null=True)
    repdesprisklimitsug = models.FloatField(
        db_column='REPDESPRISKLIMITSUG', blank=True, null=True)
    desprisktotalsug = models.FloatField(
        db_column='DESPRISKTOTALSUG', blank=True, null=True)
    repdesprisktotalsug = models.FloatField(
        db_column='REPDESPRISKTOTALSUG', blank=True, null=True)
    desprskblncedsug = models.FloatField(
        db_column='DESPRSKBLNCEDSUG', blank=True, null=True)
    repdesprskblncedsug = models.FloatField(
        db_column='REPDESPRSKBLNCEDSUG', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_CLRNUMS'
        target_db = 'erp'
    # rels -> L_CLCARD
