"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_TRGPAR(
    BaseLogical,
    models.Model):
    """
        Trigger parametreleri
    """
    risktype = models.SmallIntegerField(
        db_column='RISKTYPE',
        blank=True,
        null=True,
        help_text='Risk toplamı (bakiye/irsaliye)'
    )
    riskover = models.SmallIntegerField(
        db_column='RISKOVER',
        blank=True,
        null=True,
        help_text='Genel müşteri riski aşıldığında'
    )
    ordriskover = models.SmallIntegerField(
        db_column='ORDRISKOVER',
        blank=True,
        null=True,
        help_text='Sipariş müşteri risk aşıldığında'
    )
    despriskover = models.SmallIntegerField(
        db_column='DESPRISKOVER',
        blank=True,
        null=True,
        help_text='İrsaliye müşteri riski aşıldığında'
    )
    usereprisk = models.SmallIntegerField(
        db_column='USEREPRISK',
        blank=True,
        null=True,
    )
    preturneffectorder = models.SmallIntegerField(
        db_column='PRETURNEFFECTORDER',
        blank=True,
        null=True
    )
    sreturneffectorder = models.SmallIntegerField(
        db_column='SRETURNEFFECTORDER',
        blank=True,
        null=True
    )
    firmcalendartype = models.SmallIntegerField(
        db_column='FIRMCALENDARTYPE',
        blank=True,
        null=True
    )
    collrisktype = models.SmallIntegerField(
        db_column='COLLRISKTYPE',
        blank=True,
        null=True
    )
    collriskover = models.SmallIntegerField(
        db_column='COLLRISKOVER',
        blank=True,
        null=True
    )
    ordcollriskover = models.SmallIntegerField(
        db_column='ORDCOLLRISKOVER',
        blank=True,
        null=True
    )
    despcollriskover = models.SmallIntegerField(
        db_column='DESPCOLLRISKOVER',
        blank=True,
        null=True
    )
    userepcollrisk = models.SmallIntegerField(
        db_column='USEREPCOLLRISK',
        blank=True,
        null=True
    )
    firmrepcurr = models.SmallIntegerField(
        db_column='FIRMREPCURR',
        blank=True,
        null=True
    )
    risktypes1 = models.SmallIntegerField(
        db_column='RISKTYPES1',
        blank=True,
        null=True
    )
    risktypes2 = models.SmallIntegerField(
        db_column='RISKTYPES2',
        blank=True,
        null=True
    )
    risktypes3 = models.SmallIntegerField(
        db_column='RISKTYPES3',
        blank=True,
        null=True
    )
    risktypes4 = models.SmallIntegerField(
        db_column='RISKTYPES4',
        blank=True,
        null=True
    )
    risktypes5 = models.SmallIntegerField(
        db_column='RISKTYPES5',
        blank=True,
        null=True
    )
    accriskover = models.SmallIntegerField(
        db_column='ACCRISKOVER',
        blank=True,
        null=True
    )
    mycsriskover = models.SmallIntegerField(
        db_column='MYCSRISKOVER',
        blank=True,
        null=True
    )
    cstcsriskover = models.SmallIntegerField(
        db_column='CSTCSRISKOVER',
        blank=True,
        null=True
    )
    riskgrpctrl = models.SmallIntegerField(
        db_column='RISKGRPCTRL',
        blank=True,
        null=True
    )
    riskctrltype = models.SmallIntegerField(
        db_column='RISKCTRLTYPE',
        blank=True,
        null=True
    )
    ordriskoversugg = models.SmallIntegerField(
        db_column='ORDRISKOVERSUGG',
        blank=True,
        null=True
    )
    cstcsciroriskover = models.SmallIntegerField(
        db_column='CSTCSCIRORISKOVER',
        blank=True,
        null=True
    )
    despriskoversugg = models.SmallIntegerField(
        db_column='DESPRISKOVERSUGG',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_TRGPAR'
        target_db = 'erp'

