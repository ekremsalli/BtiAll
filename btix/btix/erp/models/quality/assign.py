"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_QASGN(
    BaseLogical,
    models.Model):
    """
        Kalite kontrol hareketi - Kalite kontrol ataması
    """
    setref = models.ForeignKey(
        "LG_QCSET",
        db_column='SETREF',
        blank=True,
        null=True,
        help_text='Kalite kontrol seti ref. -> QCSET',
        on_delete=models.DO_NOTHING
    )
    lineref = models.IntegerField(
        db_column='LINEREF',
        blank=True,
        null=True,
        help_text='Kalite kontrol satırı ref. -> QCLINE'
    )
    importance = models.CharField(
        db_column='IMPORTANCE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Önem'
    )
    frequency = models.FloatField(
        db_column='FREQUENCY',
        blank=True,
        null=True,
        help_text='Sıklık'
    )
    counter = models.FloatField(
        db_column='COUNTER',
        blank=True,
        null=True,
        help_text='Sayaç'
    )
    samplesize = models.FloatField(
        db_column='SAMPLESIZE',
        blank=True,
        null=True,
        help_text='Örnek büyüklük'
    )
    nomval = models.FloatField(
        db_column='NOMVAL',
        blank=True,
        null=True,
        help_text='Nominal değeri'
    )
    minval = models.FloatField(
        db_column='MINVAL',
        blank=True,
        null=True,
        help_text='Minimum değer'
    )
    mintol = models.FloatField(
        db_column='MINTOL',
        blank=True,
        null=True,
        help_text='Minimum tolerans'
    )
    maxval = models.FloatField(
        db_column='MAXVAL',
        blank=True,
        null=True,
        help_text='Maksimum değeri'
    )
    plustol = models.FloatField(
        db_column='PLUSTOL',
        blank=True,
        null=True,
        help_text='Artı tolerans'
    )
    insppoint = models.SmallIntegerField(
        db_column='INSPPOINT',
        blank=True,
        null=True,
        help_text='Kontrol noktası'
    )
    inspfiches1 = models.SmallIntegerField(
        db_column='INSPFICHES1',
        blank=True,
        null=True,
        help_text='Kontrol fişi 1'
    )
    inspfiches2 = models.SmallIntegerField(
        db_column='INSPFICHES2',
        blank=True,
        null=True,
        help_text='Kontrol fişi 2'
    )
    inspfiches3 = models.SmallIntegerField(
        db_column='INSPFICHES3',
        blank=True,
        null=True,
        help_text='Kontrol fişi 3'
    )
    asgnref = models.IntegerField(
        db_column='ASGNREF',
        blank=True,
        null=True,
        help_text='Atama ref.'
    )
    opitemref = models.ForeignKey(
        "LG_ITEMS",
        db_column='OPITEMREF',
        blank=True,
        null=True,
        help_text='Ek malzeme ref. -> ITEMS',
        on_delete=models.DO_NOTHING
    )
    asgntype = models.SmallIntegerField(
        db_column='ASGNTYPE',
        blank=True,
        null=True,
        help_text='Atama tipi'
    )
    valref = models.ForeignKey(
        "LG_QCLVAL",
        db_column='VALREF',
        blank=True,
        null=True,
        help_text='Kalite kontrol değerleri ref. -> QCVAL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_valref"
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    revisionno = models.IntegerField(
        db_column='REVISIONNO',
        blank=True,
        null=True,
        help_text='Revizyon no'
    )
    conformrate = models.SmallIntegerField(
        db_column='CONFORMRATE',
        blank=True,
        null=True,
        help_text='Uygunluk oranı'
    )
    toolcode = models.CharField(
        db_column='TOOLCODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Araç kodu'
    )
    controller = models.SmallIntegerField(
        db_column='CONTROLLER',
        blank=True,
        null=True,
        help_text='Kontrol eden'
    )
    toolref = models.IntegerField(
        db_column='TOOLREF',
        blank=True,
        null=True,
        help_text='Araç kartı -> ITEMS'
    )
    orgrevno = models.IntegerField(
        db_column='ORGREVNO',
        blank=True,
        null=True,
        help_text='Orjinal kayıt ref.'
    )
    revsiteid = models.SmallIntegerField(
        db_column='REVSITEID',
        blank=True,
        null=True
    )
    importanceval = models.FloatField(
        db_column='IMPORTANCEVAL',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_QASGN'
        target_db = 'erp'

