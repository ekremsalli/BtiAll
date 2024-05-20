"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_DEMANDLINE(
    BaseLogical,
    BaseUnit,
    BaseBranch,
    BaseCode,
    BaseSiteRec,
    BaseWF,
    BaseGUID,
    BaseAccount,
    BaseProject,
    BaseCenter,
    models.Model):
    """
        Talep fişi detayı
    """
    demandficheref = models.IntegerField(
        db_column='DEMANDFICHEREF',
        blank=True,
        null=True,
        help_text='Talep fişi ref.'
    )
    itemref = models.IntegerField(db_column='ITEMREF', blank=True,
        null=True, help_text='Malzeme ref.')
    clientref = models.IntegerField(db_column='CLIENTREF', blank=True,
        null=True, help_text='Müşteri kartı ref.')
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True,
        help_text='Tutar'
    )
    meetamnt = models.FloatField(db_column='MEETAMNT', blank=True,
        null=True, help_text='Sevkedilen miktar')
    cancamount = models.FloatField(db_column='CANCAMOUNT',
        blank=True, null=True, help_text='Birim seti log ref.')
    meettype = models.SmallIntegerField(db_column='MEETTYPE', blank=True,
        null=True,
        help_text="""
            Teslimat şekli;
            0 -> Alış siparişi
            1 -> Üretim emri
            2 -> Ambar fişi
        """
    )
    procuredate = models.DateTimeField(db_column='PROCUREDATE', blank=True,
        null=True, help_text='Temin tarihi')
    sourceindex = models.SmallIntegerField(db_column='SOURCEINDEX', blank=True,
        null=True, help_text='Kaynak ambar numarası')
    factorynr = models.SmallIntegerField(db_column='FACTORYNR', blank=True,
        null=True, help_text='Fabrika numarası')
    bommasterref = models.IntegerField(db_column='BOMMASTERREF', blank=True,
        null=True, help_text='Bom master log ref.')
    bomrevref = models.IntegerField(db_column='BOMREVREF', blank=True,
        null=True, help_text='Ürün reçetesi revizyon ref.')
    lineexp = models.CharField(db_column='LINEEXP', max_length=251,
        blank=True, null=True, help_text='Satır açıklaması')
    status = models.SmallIntegerField(db_column='STATUS', blank=True,
        null=True, help_text='Durumu')
    orglogicref = models.IntegerField(db_column='ORGLOGICREF', blank=True,
        null=True, help_text='Orjinal kayıt ref.')
    paydefref = models.IntegerField(db_column='PAYDEFREF', blank=True,
        null=True, help_text='Ödeme planı ref.')
    linetype = models.SmallIntegerField(db_column='LINETYPE',
        blank=True, null=True, help_text='Satır tipi')
    cpstflag = models.SmallIntegerField(db_column='CPSTFLAG',
        blank=True, null=True, help_text='Karma koli satırı')
    detline = models.SmallIntegerField(db_column='DETLINE',
        blank=True, null=True, help_text='Detay satırı')
    prevlineref = models.IntegerField(db_column='PREVLINEREF',
        blank=True, null=True, help_text='Malzemeler ref.')
    prevlineno = models.SmallIntegerField(db_column='PREVLINENO',
        blank=True, null=True, help_text='Üst mzelzeme sınıfı satır numarası')
    lineno_field = models.SmallIntegerField(db_column='LINENO_',
        blank=True, null=True, help_text='Satır numarası')
    username = models.CharField(db_column='USERNAME', max_length=25,
        blank=True, null=True, help_text='Kullanıcı adı')
    fichedate = models.DateTimeField(db_column='FICHEDATE',
        blank=True, null=True, help_text='Fiş tarihi')
    mrplineref = models.IntegerField(db_column='MRPLINEREF', blank=True,
        null=True, help_text='MRPLINEREF ref.')
    mrpheadref = models.IntegerField(db_column='MRPHEADREF', blank=True,
        null=True, help_text='MRPHEADREF ref.')
    altitemuse = models.SmallIntegerField(db_column='ALTITEMUSE', blank=True,
        null=True, help_text='Alternatif malzeme kullanımı')
    mrpheadtype = models.SmallIntegerField(db_column='MRPHEADTYPE',
        blank=True, null=True,
        help_text="""
            Talep / teklf planlama türü,
            1 -> MPS,
            2 -> MRP
        """
    )
    ordpeguse = models.SmallIntegerField(db_column='ORDPEGUSE',
        blank=True, null=True, help_text='Verilen sipariş bağlantıları')
    ordpegamount = models.FloatField(db_column='ORDPEGAMOUNT', blank=True,
        null=True, help_text='Verilen sipariş bağlantıları miktarı')
    price = models.FloatField(db_column='PRICE', blank=True,
        null=True, help_text='Birim fiyat')
    procuretime = models.IntegerField(db_column='PROCURETIME',
        blank=True, null=True, help_text='Temin tarihi')
    invuseparam = models.SmallIntegerField(db_column='INVUSEPARAM',
        blank=True, null=True,
        help_text="""
            0 -> Tüm ambarlar kontrol edilecek
            1 -> Seçilen ambarlar kontrol edilecek
        """
    )
    prodordref = models.IntegerField(db_column='PRODORDREF',
        blank=True, null=True, help_text='Üretim emirleri ref.')
    polineref = models.IntegerField(db_column='POLINEREF', blank=True,
        null=True, help_text='Üretim emri satırları ref.')
    displineref = models.IntegerField(db_column='DISPLINEREF', blank=True,
        null=True, help_text='İş emirleri ref.')
    plnstfcref = models.IntegerField(db_column='PLNSTFCREF', blank=True,
        null=True, help_text='Malzeme fişleri ref.')
    plnstlref = models.IntegerField(db_column='PLNSTLREF', blank=True,
        null=True, help_text='Malzeme hareketleri ref.')

    department = models.SmallIntegerField(
        db_column='DEPARTMENT',
        blank=True,
        null=True
    )

    plnficheper = models.SmallIntegerField(db_column='PLNFICHEPER',
        blank=True, null=True, help_text='Planlanan fiş periyodu')
    realsrcindex = models.SmallIntegerField(db_column='REALSRCINDEX',
        blank=True, null=True, help_text='Talep satırı kaynak ambarı')
    crsaccountref = models.IntegerField(db_column='CRSACCOUNTREF',
        blank=True, null=True)
    crscenterref = models.IntegerField(db_column='CRSCENTERREF',
        blank=True, null=True)
    crsprojectref = models.IntegerField(db_column='CRSPROJECTREF',
        blank=True, null=True)
    prcurr = models.SmallIntegerField(db_column='PRCURR',
        blank=True, null=True)
    prprice = models.FloatField(db_column='PRPRICE', blank=True, null=True)
    variantref = models.IntegerField(db_column='VARIANTREF',
        blank=True, null=True)
    meetwithstock = models.SmallIntegerField(db_column='MEETWITHSTOCK',
        blank=True, null=True)
    fichetype = models.SmallIntegerField(db_column='FICHETYPE',
        blank=True, null=True)
    prodordtyp = models.SmallIntegerField(db_column='PRODORDTYP',
        blank=True, null=True)
    bomtype = models.SmallIntegerField(db_column='BOMTYPE',
        blank=True, null=True)
    prclistref = models.IntegerField(db_column='PRCLISTREF',
        blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_DEMANDLINE'
        target_db = 'erp'

    # rels -> -


class LG_DEMANDFICHE(
    BaseLogical,
    BaseCode,
    BaseBranch,
    BaseSiteRec,
    BaseWF,
    BaseInfo,
    BasePrint,
    BaseTextINC,
    BaseWFlowTask,
    BaseProject,
    BaseGUID,
    BaseRef,
    models.Model):
    ficheno = models.CharField(db_column='FICHENO', max_length=17, blank=True, null=True)
    date_field = models.DateTimeField(db_column='DATE_', blank=True, null=True)
    time_field = models.IntegerField(db_column='TIME_', blank=True, null=True)
    docode = models.CharField(db_column='DOCODE', max_length=33, blank=True, null=True)
    status = models.SmallIntegerField(db_column='STATUS', blank=True, null=True)
    sourceindex = models.SmallIntegerField(db_column='SOURCEINDEX', blank=True, null=True)
    factorynr = models.SmallIntegerField(db_column='FACTORYNR', blank=True, null=True)
    demandtype = models.SmallIntegerField(db_column='DEMANDTYPE', blank=True, null=True)
    demandref = models.IntegerField(db_column='DEMANDREF', blank=True, null=True)
    userno = models.SmallIntegerField(db_column='USERNO', blank=True, null=True)
    perref = models.IntegerField(db_column='PERREF', blank=True, null=True)
    printdate = models.DateTimeField(db_column='PRINTDATE', blank=True, null=True)
    department = models.SmallIntegerField(db_column='DEPARTMENT', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_DEMANDFICHE'
        unique_together = (('demandtype', 'ficheno'),)
        target_db = 'erp'


##
class LG_DEMANDPEGGING(
    BaseLogical,
    BaseSiteRec,
    BaseProject,
    BaseRef,
    models.Model
    ):
    demandlineref = models.IntegerField(db_column='DEMANDLINEREF', blank=True, null=True)
    demandficheref = models.IntegerField(db_column='DEMANDFICHEREF', blank=True, null=True)
    parenttype = models.SmallIntegerField(db_column='PARENTTYPE', blank=True, null=True)
    parentref = models.IntegerField(db_column='PARENTREF', blank=True, null=True)
    childtype = models.SmallIntegerField(db_column='CHILDTYPE', blank=True, null=True)
    childref = models.IntegerField(db_column='CHILDREF', blank=True, null=True)
    itemalter = models.SmallIntegerField(db_column='ITEMALTER', blank=True, null=True)
    itemref = models.IntegerField(db_column='ITEMREF', blank=True, null=True)
    unitref = models.IntegerField(db_column='UNITREF', blank=True, null=True)
    mainitemref = models.IntegerField(db_column='MAINITEMREF', blank=True, null=True)
    mainunitref = models.IntegerField(db_column='MAINUNITREF', blank=True, null=True)
    meetamnt = models.FloatField(db_column='MEETAMNT', blank=True, null=True)
    mainmeetamnt = models.FloatField(db_column='MAINMEETAMNT', blank=True, null=True)
    ordperiod = models.IntegerField(db_column='ORDPERIOD', blank=True, null=True)
    clientref = models.IntegerField(db_column='CLIENTREF', blank=True, null=True)
    bommasterref = models.IntegerField(db_column='BOMMASTERREF', blank=True, null=True)
    bomrevref = models.IntegerField(db_column='BOMREVREF', blank=True, null=True)
    linetype = models.SmallIntegerField(db_column='LINETYPE', blank=True, null=True)
    detline = models.SmallIntegerField(db_column='DETLINE', blank=True, null=True)
    prevlineref = models.IntegerField(db_column='PREVLINEREF', blank=True, null=True)
    prevlineno = models.SmallIntegerField(db_column='PREVLINENO', blank=True, null=True)
    lineno_field = models.SmallIntegerField(db_column='LINENO_', blank=True, null=True)
    payplanref = models.IntegerField(db_column='PAYPLANREF', blank=True, null=True)
    price = models.FloatField(db_column='PRICE', blank=True, null=True)
    variantref = models.IntegerField(db_column='VARIANTREF', blank=True, null=True)
    mainvariantref = models.IntegerField(db_column='MAINVARIANTREF', blank=True, null=True)
    fichetype = models.SmallIntegerField(db_column='FICHETYPE', blank=True, null=True)
    bomtype = models.SmallIntegerField(db_column='BOMTYPE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_DEMANDPEGGING'
        target_db = 'erp'