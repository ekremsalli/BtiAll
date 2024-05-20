"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_BNFICHE(
    BaseLogical,
    BaseAccounted,
    BaseCancelled,
    BaseInfo,
    BaseCode,
    BaseGenexp,
    BaseSiteRec,
    BaseGUID,
    BaseSign,
    BasePrint,
    BaseWF,
    BaseSalesMan,
    BaseTextINC,
    BaseProject,
    BaseBranch,
    BaseDepartment,
    models.Model):
    """
        Banka fişleri
        BNFICHE tablosunda banka fişlerinin başlık kayıtları tutulmaktadır.
        Banka fişlerinin satırlarına ulaşabilmek için BNFLINE tablosu
        okunmalıdır.
    """
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    ficheno = models.CharField(
        db_column='FICHENO',
        max_length=17,
        blank=True,
        null=True,
        help_text='Fiş numarası'
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Banka işlem fişi'),
            (2, 'Virman fişi'),
            (3, 'Gelen havaleler'),
            (4, 'Gönderilen havaleler')
        ],
        help_text='İşlem türü'
    )
    modulenr = models.SmallIntegerField(
        db_column='MODULENR',
        blank=True,
        null=True,
        help_text="Modül numarası"
    )
    sourcefref = models.IntegerField(
        db_column='SOURCEFREF',
        blank=True,
        null=True,
        help_text='Bağlı fiş ref.'
    )
    debittot = models.FloatField(
        db_column='DEBITTOT',
        blank=True,
        null=True,
        help_text='Borç toplamı'
    )
    credittot = models.FloatField(
        db_column='CREDITTOT',
        blank=True,
        null=True,
        help_text='Alacak toplamı'
    )
    cancelledacc = models.SmallIntegerField(
        db_column='CANCELLEDACC',
        blank=True,
        null=True,
        help_text='Muhasebeleştirme İşlemi İptal Edilmiş'
    )
    accficheref = models.IntegerField(
        db_column='ACCFICHEREF',
        blank=True,
        null=True,
        help_text='Muhasebe fiş ref.'
    )
    genexctyp = models.SmallIntegerField(
        db_column='GENEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (Genel)'
    )
    lineexctyp = models.SmallIntegerField(
        db_column='LINEEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (Satır)'
    )
    orglogicref = models.IntegerField(
        db_column='ORGLOGICREF',
        blank=True,
        null=True,
        help_text='Orjinal kayıt ref.'
    )
    repdebit = models.FloatField(
        db_column='REPDEBIT',
        blank=True,
        null=True,
        help_text='Borç (RD)')
    repcredit = models.FloatField(
        db_column='REPCREDIT',
        blank=True,
        null=True,
        help_text='Alacak (RD)'
    )
    crcardwzd = models.SmallIntegerField(db_column='CRCARDWZD', blank=True,
        null=True,
        help_text="""
            Ödeme oto oluşturuldu,
                0->Hayır
                1->Oto+kredi kartı
                2->Oto+kred kartı slipi
        """)
    bnaccountref = models.IntegerField(
        db_column='BNACCOUNTREF',
        blank=True,
        null=True,
        help_text='Banka hesapları ref.'
    )
    trangrpno = models.CharField(
        db_column='TRANGRPNO',
        max_length=17,
        blank=True,
        null=True,
        help_text='Hareket grup numarası (fiş)'
    )
    collatrollref = models.IntegerField(
        db_column='COLLATROLLREF',
        blank=True,
        null=True
    )
    collattrnref = models.IntegerField(
        db_column='COLLATTRNREF',
        blank=True,
        null=True
    )
    bncrref = models.IntegerField(
        db_column='BNCRREF',
        blank=True,
        null=True
    )
    orglogoid = models.CharField(
        db_column='ORGLOGOID',
        max_length=25,
        blank=True,
        null=True
    )
    reflected = models.SmallIntegerField(
        db_column='REFLECTED',
        blank=True,
        null=True
    )
    reflaccficheref = models.IntegerField(
        db_column='REFLACCFICHEREF',
        blank=True,
        null=True
    )
    cancelledreflacc = models.SmallIntegerField(
        db_column='CANCELLEDREFLACC',
        blank=True,
        null=True
    )
    approve = models.SmallIntegerField(
        db_column='APPROVE',
        blank=True,
        null=True
    )
    approvedate = models.DateTimeField(
        db_column='APPROVEDATE',
        blank=True,
        null=True
    )
    collatcardref = models.IntegerField(
        db_column='COLLATCARDREF',
        blank=True,
        null=True
    )
    crcardwzdper = models.SmallIntegerField(
        db_column='CRCARDWZDPER',
        blank=True,
        null=True
    )
    leasingref = models.IntegerField(
        db_column='LEASINGREF',
        blank=True,
        null=True
    )
    offerref = models.IntegerField(
        db_column='OFFERREF',
        blank=True,
        null=True
    )
    crcardfcref = models.IntegerField(
        db_column='CRCARDFCREF',
        blank=True,
        null=True
    )
    fromcreditclose = models.SmallIntegerField(
        db_column='FROMCREDITCLOSE',
        blank=True,
        null=True
    )
    fromcurdiffproc = models.SmallIntegerField(
        db_column='FROMCURDIFFPROC',
        blank=True,
        null=True
    )
    printdate = models.DateTimeField(
        db_column='PRINTDATE',
        blank=True,
        null=True
    )
    ftime = models.IntegerField(
        db_column='FTIME',
        blank=True,
        null=True
    )
    fromcrstruct = models.SmallIntegerField(
        db_column='FROMCRSTRUCT',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        unique_together = (
            ('trcode', 'ficheno'), ('date_field', 'trcode', 'ficheno'),
        )
        db_table = f'LG_{Active.namespace}_{Active.period}_BNFICHE'
        target_db = 'erp'

    #rels -> L_EMFICHE, L_BNCARD