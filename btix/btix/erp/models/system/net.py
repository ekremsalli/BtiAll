"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class L_NET(
    BaseLogical,
    models.Model):
    lockstr = models.CharField(
        db_column='LOCKSTR',
        unique=True,
        max_length=41,
        blank=True,
        null=True,
        help_text='Lock açıklaması'
    )
    counter = models.IntegerField(
        db_column='COUNTER',
        blank=True,
        null=True,
        help_text='Sayaç'
    )
    sessioncode = models.CharField(
        db_column='SESSIONCODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Oturum'
    )
    programname = models.CharField(
        db_column='PROGRAMNAME',
        max_length=129,
        blank=True,
        null=True,
        help_text='Program'
    )

    class Meta:
        managed = False
        db_table = 'L_NET'
        target_db = 'system'
