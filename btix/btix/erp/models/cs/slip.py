"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_CSTRANS(
    BaseLogical,
    BaseAccounted,
    BaseSiteRec,
    BaseGUID,
    BaseCancelled,
    BaseRef,
    models.Model):
    """
        Çek / senet hareketleri
        Çek ya da senetlerle ilgili işlemler bordrolar aracılığı ile
        yapıldığında her çek ya da senet için o anki akıbetini belirten
        bir çek ya da senet hareketi oluşmaktadır.
    """
    date_field = models.DateTimeField(
        db_column='DATE_',
        blank=True,
        null=True,
        help_text='Tarih'
    )
    csref = models.ForeignKey(
        "LG_CSCARD",
        db_column='CSREF',
        blank=True,
        null=True,
        help_text='Çek / senet kartı ref. -> CSCARD',
        on_delete=models.DO_NOTHING
    )
    rollref = models.ForeignKey(
        "LG_CSROLL",
        db_column='ROLLREF',
        blank=True,
        null=True,
        help_text='Bordro ref. -> CSROLL',
        on_delete=models.DO_NOTHING
    )
    trcode = models.SmallIntegerField(
        db_column='TRCODE',
        blank=True,
        null=True,
        help_text='İşlem türü (1-12)'
    )
    devir = models.SmallIntegerField(
        db_column='DEVIR',
        blank=True,
        null=True,
        help_text='Devir'
    )
    status = models.SmallIntegerField(
        db_column='STATUS',
        blank=True,
        null=True,
        choices=[
            (1, 'Portföyde'),
            (2, 'Ciro edildi'),
            (3, 'Teminata verildi'),
            (4, 'Tahsile verildi'),
            (5, 'Protestolu tahsile verildi'),
            (6, 'İade edildi'),
            (7, 'Protesto edildi'),
            (8, 'Tahsil edildi'),
            (9, 'Kendi çekimiz'),
            (10, 'Borç senedimiz'),
            (11, 'Karşılığı yok'),
            (12, 'Tahsil edilemiyor')
        ],
        help_text='Durumu'
    )
    cardmd = models.SmallIntegerField(
        db_column='CARDMD',
        blank=True,
        null=True,
        help_text="""
            Kart modül numarası;
            1-4 Cari hesap (5),
            5-8 Banka hesabı (7)
        """
    )
    cardref = models.IntegerField(
        db_column='CARDREF',
        blank=True,
        null=True,
        help_text='Kart ref.'
    )
    statno = models.SmallIntegerField(
        db_column='STATNO',
        blank=True,
        null=True,
        help_text='Kaçıncı statü'
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Bordronun kaçıncı satır'
    )
    accref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='ACCREF',
        blank=True,
        null=True,
        help_text='Muhasebe hesabı ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_accref",
    )
    costref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='COSTREF',
        blank=True,
        null=True,
        help_text='Masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_costref"
    )
    crsaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='CRSACCREF',
        blank=True,
        null=True,
        help_text='Karşı hesabın muhasebe hesabı ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_crsaccref"
    )
    crscostref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='CRSCOSTREF',
        blank=True,
        null=True,
        help_text='Karşı hesabın masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_crscostref"
    )
    fromcash = models.SmallIntegerField(
        db_column='FROMCASH',
        blank=True,
        null=True,
        help_text='Kasadan işlem yapılmış (E/H)'
    )
    lineexctyp = models.SmallIntegerField(
        db_column='LINEEXCTYP',
        blank=True,
        null=True,
        help_text='Döviz türü (satır)'
    )
    opstat = models.SmallIntegerField(db_column='OPSTAT', blank=True,
        null=True, help_text='Hareket durumu')
    provlnaccref = models.IntegerField(db_column='PROVLNACCREF', blank=True,
        null=True)
    provlncostref = models.IntegerField(db_column='PROVLNCOSTREF', blank=True,
        null=True)
    affectcollatrl = models.SmallIntegerField(db_column='AFFECTCOLLATRL',
        blank=True, null=True)
    affectrisk = models.SmallIntegerField(db_column='AFFECTRISK',
        blank=True, null=True)
    orglogoid = models.CharField(db_column='ORGLOGOID', max_length=25,
        blank=True, null=True)
    usegirorate = models.SmallIntegerField(db_column='USEGIRORATE',
        blank=True, null=True)
    frombank = models.SmallIntegerField(db_column='FROMBANK',
        blank=True, null=True)
    useraisedval = models.SmallIntegerField(db_column='USERAISEDVAL',
        blank=True, null=True)
    claccref = models.IntegerField(db_column='CLACCREF',
        blank=True, null=True)
    clcostref = models.IntegerField(db_column='CLCOSTREF',
        blank=True, null=True)
    bncreref = models.IntegerField(db_column='BNCREREF', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_CSTRANS'
        target_db = 'erp'