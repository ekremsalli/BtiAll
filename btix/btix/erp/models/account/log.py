"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_LOGREP(
    BaseLogical,
    models.Model):
    """
        Muhasebeştir işlemi sonunda çıkan log ekranı
    """
    logtype = models.SmallIntegerField(
        db_column='LOGTYPE',
        blank=True,
        null=True,
        help_text='Tutulan log tipi'
    )
    linenr = models.IntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    linetype = models.SmallIntegerField(
        db_column='LINETYPE',
        blank=True,
        null=True,
        help_text='Log satırı tipi'
    )
    lineexp = models.CharField(
        db_column='LINEEXP',
        max_length=201,
        blank=True,
        null=True,
        help_text='Log satırı açıklaması'
    )
    msgnum1 = models.IntegerField(
        db_column='MSGNUM1',
        blank=True,
        null=True,
        help_text='Genel amaçlı longint1'
    )
    msgnum2 = models.IntegerField(
        db_column='MSGNUM2',
        blank=True,
        null=True,
        help_text='Genel amaçlı longint2'

    )
    sessioncode = models.CharField(
        db_column='SESSIONCODE', max_length=61, blank=True, null=True)
    lineexplain2 = models.CharField(
        db_column='LINEEXPLAIN2', max_length=201, blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_LOGREP'
        target_db = 'erp'

