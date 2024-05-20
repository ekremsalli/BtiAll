"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_SLTRANS(
    BaseLogical,
    BaseItem,
    BaseUnitSet,
    BaseAmount,
    BaseGUID,
    BaseWF,
    BaseSiteRec,
    BaseCancelled,
    BaseRef,
    models.Model):
    """
        Seri/lot hareketleri
    """
    stficheref = models.ForeignKey(
        "LG_STFICHE",
        db_column='STFICHEREF',
        blank=True,
        null=True,
        help_text='Stok fişi ref. -> STFICHE',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_stficheref"
    )
    sttransref = models.ForeignKey(
        "LG_STLINE",
        db_column='STTRANSREF',
        blank=True,
        null=True,
        help_text='Stok hareketi ref. -> STLINE',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_sttransref"
    )
    intransref = models.ForeignKey(
        "LG_STLINE",
        db_column='INTRANSREF',
        blank=True,
        null=True,
        help_text='Giriş stok hareketi ref. -> STLINE',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_intransref"
    )
    insltransref = models.IntegerField(
        db_column='INSLTRANSREF',
        blank=True,
        null=True,
        help_text='Giriş seri/lot/yerleşim hareketi ref. -> SLTRANS'
    )
    inslamount = models.FloatField(
        db_column='INSLAMOUNT',
        blank=True,
        null=True,
        help_text='Giriş hareketi biriminden miktar'
    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    iocode = models.SmallIntegerField(
        db_column='IOCODE',
        blank=True,
        null=True,
        choices=[
            (1, 'Giriş'),
            (2, 'Ambar giriş'),
            (3, 'Ambar çıkış'),
            (4, 'Çıkış')
        ],
        help_text='Giriş / çıkış kodu'
    )
    invenno = models.SmallIntegerField(
        db_column='INVENNO',
        blank=True,
        null=True,
        help_text='Ambar no'
    )
    fichetype = models.SmallIntegerField(
        db_column='FICHETYPE',
        blank=True,
        null=True,
        help_text='Bağlı olduğu stok fişi türü'
    )
    sltype = models.SmallIntegerField(
        db_column='SLTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Lot'),
            (2, 'Seri')
        ],
        help_text='Seri/lot türü'
    )
    slref = models.ForeignKey(
        "LG_SERILOTN",
        db_column='SLREF',
        blank=True,
        null=True,
        help_text='Seri/lot kaydı ref. -> SERILOTN',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_slref"
    )
    locref = models.ForeignKey(
        "LG_LOCATION",
        db_column='LOCREF',
        blank=True,
        null=True,
        help_text='Stok yeri kaydı ref. -> LOCATION',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_locref"
    )
    mainamount = models.FloatField(
        db_column='MAINAMOUNT',
        blank=True,
        null=True,
        help_text='Anabirim cinsinden miktar'
    )
    remamount = models.FloatField(
        db_column='REMAMOUNT',
        blank=True,
        null=True,
        help_text='Ana birim cinsinden kalan miktar'
    )
    remlnunitamnt = models.FloatField(
        db_column='REMLNUNITAMNT',
        blank=True,
        null=True,
        help_text='Satır birimi cinsninden kalan miktar'
    )
    uinfo1 = models.FloatField(db_column='UINFO1', blank=True, null=True,
        help_text='Çevrim katsayısı')
    uinfo2 = models.FloatField(db_column='UINFO2', blank=True, null=True,
        help_text='Çevrim katsayısı'
    )
    uinfo3 = models.FloatField(db_column='UINFO3', blank=True, null=True,
        help_text='Boyut katsayısı'
    )
    uinfo4 = models.FloatField(db_column='UINFO4', blank=True, null=True,
        help_text='Boyut katsayısı'
    )
    uinfo5 = models.FloatField(db_column='UINFO5', blank=True, null=True,
        help_text='Boyut katsayısı'
    )
    uinfo6 = models.FloatField(db_column='UINFO6', blank=True, null=True,
        help_text='Boyut katsayısı'
    )
    uinfo7 = models.FloatField(db_column='UINFO7', blank=True, null=True,
        help_text='Boyut katsayısı'
    )
    uinfo8 = models.FloatField(db_column='UINFO8', blank=True, null=True,
        help_text='Boyut katsayısı'
    )
    expdate = models.DateTimeField(
        db_column='EXPDATE',
        blank=True,
        null=True,
        help_text='Son kullanım tarihi'
    )
    ratescore = models.SmallIntegerField(
        db_column='RATESCORE',
        blank=True,
        null=True,
        help_text='Not'
    )
    outcost = models.FloatField(
        db_column='OUTCOST',
        blank=True,
        null=True,
        help_text='Çıkış fişleri çıkış maliyeti'
    )
    outcostcurr = models.FloatField(
        db_column='OUTCOSTCURR',
        blank=True,
        null=True,
        help_text='Çıkış fişleri dövizli çıkış maliyeti'
    )
    diffprcost = models.FloatField(
        db_column='DIFFPRCOST',
        blank=True,
        null=True,
        help_text='Fiyat farkı nedeniyle oluşan maliyet'
    )
    diffprcostcurr = models.FloatField(
        db_column='DIFFPRCOSTCURR',
        blank=True,
        null=True,
        help_text='Fiyat farkı nedeniyle oluşan dövizli maliyet'
    )
    seriqcok = models.SmallIntegerField(
        db_column='SERIQCOK',
        blank=True,
        null=True,
        choices=[
            (1, 'Uygun'),
            (2, 'Uygun değil')
        ],
        help_text='Kalite kontrol işlem uygunluğu'
    )
    lprodstat = models.SmallIntegerField(
        db_column='LPRODSTAT',
        blank=True,
        null=True,
        choices=[
            (0, 'Güncel'),
            (1, 'Planlanan')
        ],
        help_text='Durumu'
    )
    sourcetype = models.SmallIntegerField(
        db_column='SOURCETYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Ambar'),
            (1, 'İş istasyonu')
        ],
        help_text='Kaynak türü'
    )
    sourcewsref = models.ForeignKey(
        "LG_WORKSTAT",
        db_column='SOURCEWSREF',
        blank=True,
        null=True,
        help_text='Kaynak iş istasyonu -> WORKSTAT',
        on_delete=models.DO_NOTHING
    )
    distordref = models.IntegerField(
        db_column='DISTORDREF',
        blank=True,
        null=True,
    )
    distordlnref = models.IntegerField(
        db_column='DISTORDLNREF',
        blank=True,
        null=True
    )
    indordsltrnref = models.IntegerField(
        db_column='INDORDSLTRNREF',
        blank=True,
        null=True
    )
    grossuinfo1 = models.FloatField(
        db_column='GROSSUINFO1',
        blank=True,
        null=True
    )
    grossuinfo2 = models.FloatField(
        db_column='GROSSUINFO2',
        blank=True,
        null=True
    )
    ataxprcost = models.FloatField(
        db_column='ATAXPRCOST',
        blank=True,
        null=True
    )
    ataxprcostcurr = models.FloatField(
        db_column='ATAXPRCOSTCURR',
        blank=True,
        null=True
    )
    infidx = models.FloatField(
        db_column='INFIDX',
        blank=True,
        null=True
    )
    orglogoid = models.CharField(
        db_column='ORGLOGOID',
        max_length=25,
        blank=True,
        null=True
    )
    lineexp = models.CharField(
        db_column='LINEEXP',
        max_length=31,
        blank=True,
        null=True
    )
    eximfctype = models.SmallIntegerField(
        db_column='EXIMFCTYPE',
        blank=True,
        null=True
    )
    eximfileref = models.IntegerField(
        db_column='EXIMFILEREF',
        blank=True,
        null=True
    )
    eximprocnr = models.SmallIntegerField(
        db_column='EXIMPROCNR',
        blank=True,
        null=True
    )
    mainsllnref = models.IntegerField(
        db_column='MAINSLLNREF', blank=True, null=True)
    madeofshred = models.SmallIntegerField(
        db_column='MADEOFSHRED', blank=True, null=True)
    status = models.SmallIntegerField(
        db_column='STATUS', blank=True, null=True)
    variantref = models.IntegerField(
        db_column='VARIANTREF', blank=True, null=True)
    grpbegcode = models.CharField(
        db_column='GRPBEGCODE', max_length=101, blank=True, null=True)
    grpendcode = models.CharField(
        db_column='GRPENDCODE', max_length=101, blank=True, null=True)
    outcostufrs = models.FloatField(
        db_column='OUTCOSTUFRS', blank=True, null=True)
    outcostcurrufrs = models.FloatField(
        db_column='OUTCOSTCURRUFRS', blank=True, null=True)
    diffprcostufrs = models.FloatField(
        db_column='DIFFPRCOSTUFRS', blank=True, null=True)
    diffprcostcurrufrs = models.FloatField(
        db_column='DIFFPRCOSTCURRUFRS', blank=True, null=True)
    infidxufrs = models.FloatField(
        db_column='INFIDXUFRS', blank=True, null=True)
    adjprcostufrs = models.FloatField(
        db_column='ADJPRCOSTUFRS', blank=True, null=True)
    adjprcostcurrufrs = models.FloatField(
        db_column='ADJPRCOSTCURRUFRS', blank=True, null=True)
    prdordref = models.IntegerField(
        db_column='PRDORDREF', blank=True, null=True)
    prdordslplnreserve = models.SmallIntegerField(
        db_column='PRDORDSLPLNRESERVE', blank=True, null=True)
    inplnsltransref = models.IntegerField(
        db_column='INPLNSLTRANSREF', blank=True, null=True)
    notshipped = models.SmallIntegerField(
        db_column='NOTSHIPPED', blank=True, null=True)
    qctransferamnt = models.FloatField(
        db_column='QCTRANSFERAMNT', blank=True, null=True)
    qctransferref = models.IntegerField(
        db_column='QCTRANSFERREF', blank=True, null=True)

    class Meta:
        managed = False
        unique_together = (('siteid', 'orglogicref', 'logicalref'),)
        db_table = f'LG_{Active.namespace}_{Active.period}_SLTRANS'
        target_db = 'erp'
