"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_PRODUCER(
    BaseLogical,
    models.Model):
    """
        Müstahsil portu
        Üreticilerden yaptığımız alış işlemlerinde kullandığımız Müstahsil
        faturalarındaki müstahsil ek bilgilerinin tutulduğu tablodur.
    """
    invref = models.OneToOneField(
        "LG_INVOICE",
        db_column='INVREF',
        unique=True,
        blank=True,
        null=True,
        help_text='Ambar ref.',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_invref"
    )
    stopajper = models.FloatField(
        db_column='STOPAJPER',
        blank=True,
        null=True,
        help_text='Stopaj (%)'
    )
    ssdfper = models.FloatField(
        db_column='SSDFPER',
        blank=True,
        null=True,
        help_text='SSDF (%)'
    )
    borsaper = models.FloatField(
        db_column='BORSAPER',
        blank=True,
        null=True,
        help_text='Borsa (%)'
    )
    komisyonper = models.FloatField(
        db_column='KOMISYONPER',
        blank=True,
        null=True,
        help_text='Komisyon (%)'
    )
    komkdvper = models.FloatField(
        db_column='KOMKDVPER',
        blank=True,
        null=True,
        help_text='Komisyon KDV\' si (%)'
    )
    bagkurper = models.FloatField(
        db_column='BAGKURPER',
        blank=True,
        null=True,
        help_text='Bağkur (%)'
    )
    stopaj = models.FloatField(
        db_column='STOPAJ',
        blank=True,
        null=True,
        help_text='Stopaj'
    )
    ssdf = models.FloatField(
        db_column='SSDF',
        blank=True,
        null=True,
        help_text='SSDF'
    )
    borsa = models.FloatField(
        db_column='BORSA',
        blank=True,
        null=True,
        help_text='Borsa'
    )
    komisyon = models.FloatField(
        db_column='KOMISYON',
        blank=True,
        null=True,
        help_text='Komisyon'
    )
    komkdv = models.FloatField(
        db_column='KOMKDV',
        blank=True,
        null=True,
        help_text='Komisyon KDV\'si'
    )
    bagkur = models.FloatField(
        db_column='BAGKUR',
        blank=True,
        null=True,
        help_text='Bağkur'
    )
    stopajaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='STOPAJACCREF',
        blank=True,
        null=True,
        help_text='Stopaj muhasebe ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_stopajaccref"
    )
    ssdfaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='SSDFACCREF',
        blank=True,
        null=True,
        help_text='SSDF muhasebe ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_ssdfaccref"
    )
    borsaaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='BORSAACCREF',
        blank=True,
        null=True,
        help_text='Borsa muhasebe ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_borsaaccref"
    )
    komisyonaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='KOMISYONACCREF',
        blank=True,
        null=True,
        help_text='Komi̇syon muhasebe ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_komisyonaccref"
    )
    komkdvaccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='KOMKDVACCREF',
        blank=True,
        null=True,
        help_text='Komisyon KDV\'si muhasebe ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_komkdvaccref"
    )
    bagkuraccref = models.ForeignKey(
        "LG_EMUHACC",
        db_column='BAGKURACCREF',
        blank=True,
        null=True,
        help_text='Bağkur muhasebe ref. -> EMUHACC',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_bagkuraccref"
    )
    stopajcref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='STOPAJCREF',
        blank=True,
        null=True,
        help_text='Stopaj masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_stopajcref"
    )
    ssdfcref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='SSDFCREF',
        blank=True,
        null=True,
        help_text='SSDF masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_ssdfcref"
    )
    borsacref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='BORSACREF',
        blank=True,
        null=True,
        help_text='Borsa masraf merezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_borsacref"
    )
    komisyoncref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='KOMISYONCREF',
        blank=True,
        null=True,
        help_text='Komisyon masraf merezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_komisyoncref"
    )
    komkdvcref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='KOMKDVCREF',
        blank=True,
        null=True,
        help_text='Komisyon KDVsi masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_komkdvcref"
    )
    bagkurcref = models.ForeignKey(
        "LG_EMCENTER",
        db_column='BAGKURCREF',
        blank=True,
        null=True,
        help_text='Bağkur masraf merkezi ref. -> EMCENTER',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_bagkurcref"
    )
    komentry = models.SmallIntegerField(
        db_column='KOMENTRY',
        blank=True,
        null=True,
        help_text='Komisyon girişi'
    )
    ek1per = models.FloatField(db_column='EK1PER', blank=True, null=True)
    ek2per = models.FloatField(db_column='EK2PER', blank=True, null=True)
    ek1 = models.FloatField(db_column='EK1', blank=True, null=True)
    ek2 = models.FloatField(db_column='EK2', blank=True, null=True)
    ek1accref = models.IntegerField(
        db_column='EK1ACCREF', blank=True, null=True)
    ek2accref = models.IntegerField(
        db_column='EK2ACCREF', blank=True, null=True)
    ek1cref = models.IntegerField(db_column='EK1CREF', blank=True, null=True)
    ek2cref = models.IntegerField(db_column='EK2CREF', blank=True, null=True)
    ek3 = models.FloatField(db_column='EK3', blank=True, null=True)
    ek4 = models.FloatField(db_column='EK4', blank=True, null=True)
    ek5 = models.FloatField(db_column='EK5', blank=True, null=True)
    ek3per = models.FloatField(db_column='EK3PER', blank=True, null=True)
    ek4per = models.FloatField(db_column='EK4PER', blank=True, null=True)
    ek5per = models.FloatField(db_column='EK5PER', blank=True, null=True)
    ek3accref = models.IntegerField(
        db_column='EK3ACCREF', blank=True, null=True)
    ek4accref = models.IntegerField(
        db_column='EK4ACCREF', blank=True, null=True)
    ek5accref = models.IntegerField(
        db_column='EK5ACCREF', blank=True, null=True)
    ek3cref = models.IntegerField(db_column='EK3CREF', blank=True, null=True)
    ek4cref = models.IntegerField(db_column='EK4CREF', blank=True, null=True)
    ek5cref = models.IntegerField(db_column='EK5CREF', blank=True, null=True)
    bagkurcalctype = models.SmallIntegerField(
        db_column='BAGKURCALCTYPE', blank=True, null=True)
    stopajcalctype = models.SmallIntegerField(
        db_column='STOPAJCALCTYPE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_PRODUCER'
        target_db = 'erp'

