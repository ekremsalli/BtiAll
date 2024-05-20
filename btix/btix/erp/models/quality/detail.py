"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_SLQCASGN(
    BaseLogical,
    BaseItem,
    BaseAmount,
    BaseCancelled,
    models.Model):
    """
        Kalite kontrol hareketleri
    """
    asgntype = models.SmallIntegerField(
        db_column='ASGNTYPE',
        blank=True,
        null=True,
        help_text='Atama türü'
    )
    ficheref = models.ForeignKey(
        "LG_STFICHE",
        db_column='FICHEREF',
        blank=True,
        null=True,
        help_text='Fiş ref. -> STFICHE',
        on_delete=models.DO_NOTHING
    )
    sttransref = models.ForeignKey(
        "LG_STLINE",
        db_column='STTRANSREF',
        blank=True,
        null=True,
        help_text='Malzeme hareketi ref. -> STLINE',
        on_delete=models.DO_NOTHING
    )
    sltransref = models.ForeignKey(
        "LG_SLTRANS",
        db_column='SLTRANSREF',
        blank=True,
        null=True,
        help_text='Seri̇/Lot/Yerleşim hareketi ref. -> SLTRANS',
        on_delete=models.DO_NOTHING
    )
    qcsetref = models.ForeignKey(
        "LG_QCSET",
        db_column='QCSETREF',
        blank=True,
        null=True,
        help_text='Kalite kontrol seti ref. -> QCSET',
        on_delete=models.DO_NOTHING
    )
    qccoderef = models.IntegerField(
        db_column='QCCODEREF',
        blank=True,
        null=True,
        help_text='Kalite kontrol kodu'
    )
    qcvalref = models.ForeignKey(
        "LG_QCLVAL",
        db_column='QCVALREF',
        blank=True,
        null=True,
        help_text='Kalite kontrol değerleri ref. -> QCLVAL',
        on_delete=models.DO_NOTHING
    )
    qcasgnlogicref = models.IntegerField(
        db_column='QCASGNLOGICREF',
        blank=True,
        null=True,
        help_text='Kalite kontrol ataması ref. -> QASGN'
    )
    qcrevno = models.IntegerField(
        db_column='QCREVNO',
        blank=True,
        null=True,
        help_text='Kalite kontrol ataması revizyon numarası'
    )
    qtype = models.SmallIntegerField(
        db_column='QTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Nicel'),
            (1, 'Nitel')
        ],
        help_text='Türü'
    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    qvalue = models.FloatField(
        db_column='QVALUE',
        blank=True,
        null=True,
        help_text='Kalite kontrol değeri'
    )
    confirmed = models.SmallIntegerField(
        db_column='CONFIRMED',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Kalite kontrol değeri uygun'
    )
    qdate = models.DateTimeField(
        db_column='QDATE',
        blank=True,
        null=True,
        help_text='Kalite kontrol değerinin girildiği tarih'
    )
    lineexp = models.CharField(
        db_column='LINEEXP',
        max_length=201,
        blank=True,
        null=True,
    )
    condconamount = models.FloatField(
        db_column='CONDCONAMOUNT',
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_SLQCASGN'
        target_db = 'erp'