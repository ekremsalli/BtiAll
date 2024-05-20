"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *


class L_TRADGRP(
    BaseLogical,
    models.Model):
    """
        Ticari işlem grupları
    """
    gcode = models.CharField(db_column='GCODE', unique=True,
        max_length=17, blank=True, null=True,
        help_text='Ticari işlem grubu kodu'
    )
    gdef = models.CharField(db_column='GDEF', max_length=51,
        blank=True, null=True, help_text='Ticari işlem grubu açıklaması')
    gattrib = models.IntegerField(db_column='GATTRIB', blank=True, null=True)
    trdgrptype = models.SmallIntegerField(db_column='TRDGRPTYPE', blank=True, null=True)
    active = models.SmallIntegerField(db_column='ACTIVE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_TRADGRP'
        target_db = 'system'

    def __str__(self):
        return f'{self.gcode} {self.gdef}'