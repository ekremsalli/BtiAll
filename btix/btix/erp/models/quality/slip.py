"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_QCSLINE(
    BaseLogical,
    models.Model):
    """
        Kalite kontrol satırları
    """
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='K.K. satır kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    setref = models.ForeignKey(
        "LG_QCSET",
        db_column='SETREF',
        blank=True,
        null=True,
        help_text='Ref -> QCSET',
        on_delete=models.DO_NOTHING
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
    qunit = models.CharField(
        db_column='QUNIT',
        max_length=11,
        blank=True,
        null=True,
        help_text='Birimi'
    )
    toolcode = models.CharField(
        db_column='TOOLCODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Kontrol ekipmanı'
    )
    controller = models.SmallIntegerField(
        db_column='CONTROLLER',
        blank=True,
        null=True,
        help_text='Kontrol sorumlusu'
    )
    insppoint = models.SmallIntegerField(
        db_column='INSPPOINT',
        blank=True,
        null=True,
        help_text='Kontrol'
    )
    inspfiches1 = models.SmallIntegerField(
        db_column='INSPFICHES1',
        blank=True,
        null=True,
        help_text='Malz. yönetim fişleri'
    )
    inspfiches2 = models.SmallIntegerField(
        db_column='INSPFICHES2',
        blank=True,
        null=True,
        help_text='Satınalma iraliyeleri'
    )
    inspfiches3 = models.SmallIntegerField(
        db_column='INSPFICHES3',
        blank=True,
        null=True,
        help_text='Satış ve dağ. irsaliye'
    )
    importance = models.CharField(
        db_column='IMPORTANCE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Önem derecesi'
    )
    frequency = models.FloatField(
        db_column='FREQUENCY',
        blank=True,
        null=True,
        help_text='Kontrol sıklığı'
    )
    counter = models.FloatField(
        db_column='COUNTER',
        blank=True,
        null=True,
        help_text='Kontrol sayısı'
    )
    samplesize = models.FloatField(
        db_column='SAMPLESIZE',
        blank=True,
        null=True,
        help_text='Numune miktarı'
    )
    nomval = models.FloatField(
        db_column='NOMVAL',
        blank=True,
        null=True,
        help_text='Nominal değer'
    )
    minval = models.FloatField(
        db_column='MINVAL',
        blank=True,
        null=True,
        help_text='Asgari değer'
    )
    maxval = models.FloatField(
        db_column='MAXVAL',
        blank=True,
        null=True,
        help_text='Azami değer'
    )
    mintol = models.FloatField(
        db_column='MINTOL',
        blank=True,
        null=True,
        help_text='Tolerans (-)'
    )
    maxtol = models.FloatField(
        db_column='MAXTOL',
        blank=True,
        null=True,
        help_text='Tolerans (+)'
    )
    expline = models.CharField(
        db_column='EXPLINE',
        max_length=81,
        blank=True,
        null=True,
        help_text='Açıklama satırı'
    )
    conformrate = models.SmallIntegerField(
        db_column='CONFORMRATE',
        blank=True,
        null=True,
        help_text='Kabul oranı'
    )
    lineno_field = models.SmallIntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    toolref = models.ForeignKey(
        "LG_ITEMS",
        db_column='TOOLREF',
        blank=True,
        null=True,
        help_text='Araç ref. -> ITEMS',
        on_delete=models.DO_NOTHING
    )
    importanceval = models.FloatField(
        db_column='IMPORTANCEVAL',
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_QCSLINE'
        unique_together = (('setref', 'code'),)
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"
