"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_BANKACC(
    BaseLogical,
    BaseActive,
    BaseWF,
    BaseBank,
    BaseInfo,
    BaseCode,
    BaseTextINC,
    BaseSiteRec,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Banka hesapları
    """
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Ticari hesap'),
            (2, 'Kredi hesabı'),
            (3, 'Dövizli ticari'),
            (4, 'Dövizli kredi')
        ],
        help_text="Kart tipi"
    )
    code = models.CharField(
        db_column='CODE',
        max_length=17,
        blank=True,
        null=True,
        help_text='Banka hesabı kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=51,
        blank=True,
        null=True,
        help_text='Banka hesabı açıklaması'
    )
    checkmargin = models.FloatField(
        db_column='CHECKMARGIN',
        blank=True,
        null=True,
        help_text='Çek kredi marjı'
    )
    notemargin = models.FloatField(
        db_column='NOTEMARGIN',
        blank=True,
        null=True,
        help_text='Senet kredi marjı'
    )
    checklimit = models.FloatField(
        db_column='CHECKLIMIT',
        blank=True,
        null=True,
        help_text='Çek kredi limiti'
    )
    notelimit = models.FloatField(
        db_column='NOTELIMIT',
        blank=True,
        null=True,
        help_text='Senet kredi limiti'
    )
    custinterest = models.FloatField(
        db_column='CUSTINTEREST',
        blank=True,
        null=True,
        help_text='Cari hesap faizi (yıllık)'
    )
    skinterest = models.FloatField(
        db_column='SKINTEREST',
        blank=True,
        null=True,
        help_text='Senet karşılığı kredi (aylık)'
    )
    ckinterest = models.FloatField(
        db_column='CKINTEREST',
        blank=True,
        null=True,
        help_text='Çek karşılığı kredi (aylık)'
    )
    stopajper = models.FloatField(
        db_column='STOPAJPER',
        blank=True,
        null=True,
        help_text='Stopaj oranı'
    )
    fonper = models.FloatField(
        db_column='FONPER',
        blank=True,
        null=True,
        help_text='Fon oranı'
    )
    currency = models.SmallIntegerField(
        db_column='CURRENCY',
        blank=True,
        null=True,
        help_text='Hesap dövizi'
    )
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ekstra dosya ref.'
    )
    accountno = models.CharField(
        db_column='ACCOUNTNO',
        max_length=51,
        blank=True,
        null=True,
        help_text='Muhasebe hesabı numarası'
    )
    kkusage = models.SmallIntegerField(
        db_column='KKUSAGE',
        blank=True,
        null=True,
        help_text='Kredi kartı hareketleri'
    )
    collatrllimit = models.FloatField(
        db_column='COLLATRLLIMIT',
        blank=True,
        null=True
    )
    curratetype = models.SmallIntegerField(
        db_column='CURRATETYPE',
        blank=True,
        null=True
    )
    wthcltrlinterest = models.FloatField(db_column='WTHCLTRLINTEREST',
        blank=True, null=True)
    wthcltrllimit = models.FloatField(db_column='WTHCLTRLLIMIT', blank=True,
        null=True)
    usedinperiods = models.SmallIntegerField(db_column='USEDINPERIODS',
        blank=True, null=True)
    iban = models.CharField(db_column='IBAN',
        max_length=51, blank=True, null=True)
    cutoffday = models.SmallIntegerField(db_column='CUTOFFDAY', blank=True,
        null=True)
    lastpaymentday = models.SmallIntegerField(db_column='LASTPAYMENTDAY',
        blank=True, null=True)
    creditcardlimit = models.FloatField(db_column='CREDITCARDLIMIT',
        blank=True, null=True)
    creditcardno = models.CharField(db_column='CREDITCARDNO',
        max_length=25, blank=True, null=True)
    glbbankbranch = models.CharField(db_column='GLBBANKBRANCH',
        max_length=17, blank=True, null=True)
    defbnaccref = models.IntegerField(db_column='DEFBNACCREF',
        blank=True, null=True)
    batchnum = models.CharField(db_column='BATCHNUM', max_length=17,
        blank=True, null=True)
    posterminalnum = models.CharField(db_column='POSTERMINALNUM',
        max_length=17, blank=True, null=True)
    defksref = models.IntegerField(db_column='DEFKSREF',
        blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (
            ('bankref', 'cardtype', 'code'), ('cardtype', 'code'),
            ('bankref', 'active', 'cardtype', 'code'),
        )
        db_table = f'LG_{Active.namespace}_BANKACC'
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.definition_field}"

    # rels -> L_BNCARD