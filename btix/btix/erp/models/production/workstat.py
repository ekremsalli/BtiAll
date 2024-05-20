"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_WORKSTAT(
    BaseLogical,
    BaseCode,
    BaseAccount,
    BaseCenter,
    BaseApproved,
    BaseActive,
    BaseInfo,
    BaseSiteRec,
    BaseTextINC,
    BaseWF,
    BaseProject,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        İş istasyonları
    """
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    factorydivnr = models.SmallIntegerField(
        db_column='FACTORYDIVNR',
        blank=True,
        null=True,
        help_text='Fabrika bölüm no'
    )
    factorynr = models.SmallIntegerField(
        db_column='FACTORYNR',
        blank=True,
        null=True,
        help_text='Fabrika no'
    )
    calendarref = models.IntegerField(
        db_column='CALENDARREF',
        blank=True,
        null=True,
        help_text='Takvim ref.'
    )
    operationtime = models.FloatField(
        db_column='OPERATIONTIME',
        blank=True,
        null=True,
        help_text='Günlük çalışma saati'
    )
    hourlystdcost = models.FloatField(
        db_column='HOURLYSTDCOST',
        blank=True,
        null=True,
        help_text='Saatlik maliyet'
    )
    hourlystdrpcost = models.FloatField(
        db_column='HOURLYSTDRPCOST',
        blank=True,
        null=True,
        help_text='Saatlik maliyet'
    )
    imageinc = models.SmallIntegerField(
        db_column='IMAGEINC',
        blank=True,
        null=True
    )
    ininvennr = models.SmallIntegerField(
        db_column='ININVENNR',
        blank=True,
        null=True
    )
    outinvennr = models.SmallIntegerField(
        db_column='OUTINVENNR',
        blank=True,
        null=True
    )
    shftgrpref = models.IntegerField(
        db_column='SHFTGRPREF',
        blank=True,
        null=True
    )
    hourdiffaccref = models.IntegerField(
        db_column='HOURDIFFACCREF',
        blank=True,
        null=True
    )
    hourdiffcenter = models.IntegerField(
        db_column='HOURDIFFCENTER',
        blank=True,
        null=True
    )
    paydiffaccref = models.IntegerField(
        db_column='PAYDIFFACCREF',
        blank=True,
        null=True
    )
    paydiffcenter = models.IntegerField(
        db_column='PAYDIFFCENTER',
        blank=True,
        null=True
    )
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_WORKSTAT'
        unique_together = (
            ('cardtype', 'code'),
            ('active', 'cardtype', 'code'),
        )
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"

class LG_WSATTASG(
    BaseLogical,
    models.Model):
    """
        İş ist. özellik ataması
    """
    wsref = models.ForeignKey(
        "LG_WORKSTAT",
        db_column='WSREF',
        blank=True,
        null=True,
        help_text='İş istasyonu ref -> WORKSTAT',
        on_delete=models.DO_NOTHING
    )
    wsattribref = models.IntegerField(
        db_column='WSATTRIBREF',
        blank=True,
        null=True,
        help_text='Özellik ref.'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_WSATTASG'
        target_db = 'erp'

class LG_WSATTVAS(
    BaseLogical,
    models.Model):
    """
        İş istasyonu özellik değer ataması
    """
    wsattribasgnref = models.ForeignKey(
        "LG_WORKSTAT",
        db_column='WSATTRIBASGNREF',
        blank=True,
        null=True,
        help_text='İş istasyonu ref. -> WORKSTAT',
        on_delete=models.DO_NOTHING
    )
    wsattribvalref = models.IntegerField(
        db_column='WSATTRIBVALREF',
        blank=True,
        null=True,
        help_text='İş istasyonu özellik ref.'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_WSATTVAS'
        target_db = 'erp'

class LG_WSCHCODE(
    BaseLogical,
    BaseApproved,
    BaseCode,
    BaseActive,
    BaseTextINC,
    BaseInfo,
    BaseSiteRec,
    BaseWF,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        İş istasyonu özellikleri
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=25,
        blank=True,
        null=True,
        help_text='Kod'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    name2 = models.CharField(
        db_column='NAME2',
        max_length=51,
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_WSCHCODE'
        unique_together = (('active', 'code'),)
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.name}"

class LG_WSCHVAL(
    BaseLogical,
    models.Model):
    """
        İş istasyonu özellik değerleri
    """
    charcoderef = models.ForeignKey(
        "LG_CHARCODE",
        db_column='CHARCODEREF',
        blank=True,
        null=True,
        help_text='Özellik kod ref -> CHARCODE',
        on_delete=models.DO_NOTHING
    )
    valno = models.IntegerField(
        db_column='VALNO',
        blank=True,
        null=True,
        help_text='Değer no'
    )
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Kod'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    name2 = models.CharField(
        db_column='NAME2',
        max_length=51,
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_WSCHVAL'
        unique_together = (('charcoderef', 'code'),)
        target_db = 'erp'
