"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_ACTPEPL(
    BaseLogical,
    BaseInfo,
    BaseSiteRec,
    BaseRef,
    models.Model):
    """
        Satış faaliyetine bağlı kişiler
    """
    name = models.CharField(
        db_column='NAME',
        max_length=21,
        blank=True,
        null=True,
        help_text='Adı'
    )
    midinit = models.CharField(
        db_column='MIDINIT',
        max_length=11,
        blank=True,
        null=True,
        help_text='İkinci adı'
    )
    famname = models.CharField(
        db_column='FAMNAME',
        max_length=21,
        blank=True,
        null=True,
        help_text='Soyadı'
    )
    actref = models.IntegerField(
        db_column='ACTREF',
        blank=True,
        null=True,
        help_text='Aktivite ref.'
    )
    emailaddr = models.CharField(
        db_column='EMAILADDR',
        max_length=51,
        blank=True,
        null=True,
        help_text='E-posta adresi'
    )

    class Meta:
        managed = False
        db_table = 'LG_ACTPEPL'
        target_db = 'erp'

    #rels -> L_SLSACTIV