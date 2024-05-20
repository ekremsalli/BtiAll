"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_TRANSAC(
    BaseLogical,
    models.Model):
    """
        Firma dönem bilgileri
    """
    apprdates1 = models.DateTimeField(
        db_column='APPRDATES1',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates2 = models.DateTimeField(
        db_column='APPRDATES2',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates3 = models.DateTimeField(
        db_column='APPRDATES3',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates4 = models.DateTimeField(
        db_column='APPRDATES4',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates5 = models.DateTimeField(
        db_column='APPRDATES5',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates6 = models.DateTimeField(
        db_column='APPRDATES6',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates7 = models.DateTimeField(
        db_column='APPRDATES7',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates8 = models.DateTimeField(
        db_column='APPRDATES8',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates9 = models.DateTimeField(
        db_column='APPRDATES9',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates10 = models.DateTimeField(
        db_column='APPRDATES10',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates11 = models.DateTimeField(
        db_column='APPRDATES11',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates12 = models.DateTimeField(
        db_column='APPRDATES12',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates13 = models.DateTimeField(
        db_column='APPRDATES13',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates14 = models.DateTimeField(
        db_column='APPRDATES14',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates15 = models.DateTimeField(
        db_column='APPRDATES15',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates16 = models.DateTimeField(
        db_column='APPRDATES16',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates17 = models.DateTimeField(
        db_column='APPRDATES17',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates18 = models.DateTimeField(
        db_column='APPRDATES18',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates19 = models.DateTimeField(
        db_column='APPRDATES19',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    apprdates20 = models.DateTimeField(
        db_column='APPRDATES20',
        blank=True,
        null=True,
        help_text='Onaylama tarihi'
    )
    lastjndate = models.DateTimeField(
        db_column='LASTJNDATE',
        blank=True,
        null=True,
    )
    lastjnumber = models.IntegerField(
        db_column='LASTJNUMBER',
        blank=True,
        null=True,
    )
    periodnr = models.SmallIntegerField(
        db_column='PERIODNR',
        blank=True,
        null=True,
        help_text='Dönem no'
    )
    periodbegdate = models.DateTimeField(
        db_column='PERIODBEGDATE',
        blank=True,
        null=True,
        help_text='Dönem başı tarihi'

    )
    periodenddate = models.DateTimeField(
        db_column='PERIODENDDATE',
        blank=True,
        null=True,
        help_text='Dönem sonu tarihi'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_TRANSAC'
        target_db = 'erp'