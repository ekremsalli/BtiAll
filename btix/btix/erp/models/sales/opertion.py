"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_OPERTION(
    BaseLogical,
    BaseApproved,
    BaseWF,
    BaseSiteRec,
    BaseInfo,
    BaseTextINC,
    BaseGUID,
    BasePrint,
    BaseCode,
    BaseActive,
    BaseRef,
    models.Model):
    """
        Operasyonlar
    """
    code = models.CharField(
        db_column='CODE',
        max_length=25,
        blank=True,
        null=True,
        help_text='Operasyon kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Operasyon adı'
    )
    qccsetref = models.ForeignKey(
        "LG_QCSET",
        db_column='QCCSETREF',
        blank=True,
        null=True,
        help_text='KKK seti ref. -> QCSET',
        on_delete=models.DO_NOTHING
    )
    disttype = models.SmallIntegerField(
        db_column='DISTTYPE',
        blank=True,
        null=True
    )
    docounting = models.SmallIntegerField(
        db_column='DOCOUNTING',
        blank=True,
        null=True
    )
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True
    )
    printdate = models.DateTimeField(
        db_column='PRINTDATE',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_OPERTION'
        unique_together = (
            ('cardtype', 'code'),
            ('active', 'cardtype', 'code'),
        )
        target_db = 'erp'

class LG_OPRTREQ(
    BaseLogical,
    BasePriority,
    models.Model):
    """
        Operasyon - ihtiyaçları
    """
    operationref = models.IntegerField(
        db_column='OPERATIONREF',
        blank=True,
        null=True,
        help_text='Operasyon kartı ref -> ITEMS'
    )
    lineno_field = models.IntegerField(
        db_column='LINENO_',
        blank=True,
        null=True,
        help_text='Satır no'
    )
    group_field = models.SmallIntegerField(
        db_column='GROUP_',
        blank=True,
        null=True,
        help_text='İş istasyonu grup kodu'
    )
    wsref = models.ForeignKey(
        "LG_WORKSTAT",
        db_column='WSREF',
        blank=True,
        null=True,
        help_text='İş istasyonu ref. -> WORKSTAT',
        on_delete=models.DO_NOTHING
    )
    begdate = models.DateTimeField(
        db_column='BEGDATE',
        blank=True,
        null=True,
        help_text='Başlangıç tarihi'
    )
    fixedsetuptime = models.IntegerField(
        db_column='FIXEDSETUPTIME',
        blank=True,
        null=True,
        help_text='Sabit hazırlık süresi'
    )
    batchquantity = models.FloatField(
        db_column='BATCHQUANTITY',
        blank=True,
        null=True,
        help_text='İşlem partisi'
    )
    runtime = models.IntegerField(
        db_column='RUNTIME',
        blank=True,
        null=True,
        help_text='İşlem süresi'
    )
    transbatchqty = models.FloatField(
        db_column='TRANSBATCHQTY',
        blank=True,
        null=True,
        help_text='Taşıma partisi'
    )
    transbatchtime = models.IntegerField(
        db_column='TRANSBATCHTIME',
        blank=True,
        null=True,
        help_text='Taşıma süresi'
    )
    insptime = models.IntegerField(
        db_column='INSPTIME',
        blank=True,
        null=True,
        help_text='Kontrol süresi'
    )
    quetime = models.IntegerField(
        db_column='QUETIME',
        blank=True,
        null=True,
        help_text='Kuyruk süresi'
    )
    headtime = models.IntegerField(
        db_column='HEADTIME',
        blank=True,
        null=True,
        help_text='Operasyon öncesi bekleme süresi'
    )
    tailtime = models.IntegerField(
        db_column='TAILTIME',
        blank=True,
        null=True,
        help_text='Operasyon sonrası bekleme süresi'
    )
    usageper = models.FloatField(
        db_column='USAGEPER',
        blank=True,
        null=True,
        help_text='Kullanılan personel'
    )
    efficiency = models.FloatField(
        db_column='EFFICIENCY',
        blank=True,
        null=True,
        help_text='Verimlilik'
    )
    minamount = models.FloatField(
        db_column='MINAMOUNT',
        blank=True,
        null=True,
        help_text='Asgari miktar'
    )
    maxamount = models.FloatField(
        db_column='MAXAMOUNT',
        blank=True,
        null=True,
        help_text='Azami miktar'
    )
    condition = models.CharField(
        db_column='CONDITION',
        max_length=251,
        blank=True,
        null=True
    )
    lineupdelay = models.FloatField(
        db_column='LINEUPDELAY',
        blank=True,
        null=True
    )
    delayunit = models.SmallIntegerField(
        db_column='DELAYUNIT',
        blank=True,
        null=True
    )
    occsliceusage = models.SmallIntegerField(
        db_column='OCCSLICEUSAGE',
        blank=True,
        null=True
    )
    occslicetime = models.IntegerField(
        db_column='OCCSLICETIME',
        blank=True,
        null=True
    )
    waitbatchqty = models.FloatField(
        db_column='WAITBATCHQTY',
        blank=True,
        null=True
    )
    waitbatchtime = models.IntegerField(
        db_column='WAITBATCHTIME',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_OPRTREQ'
        unique_together = (
            ('operationref', 'group_field', 'wsref', 'logicalref'),
        )
        target_db = 'erp'

class LG_OPATTASG(
    BaseLogical,
    models.Model):
    """
        Operasyon - özellik ataması
    """
    wsattasgref = models.ForeignKey(
        "LG_WSATTASG",
        db_column='WSATTASGREF',
        blank=True,
        null=True,
        help_text='İş istasyonu özellik değeri ataması -> WSATTASG',
        on_delete=models.DO_NOTHING
    )
    wsattvalref = models.ForeignKey(
        "LG_WSATTVAS",
        db_column='WSATTVALREF',
        blank=True,
        null=True,
        help_text='İş istasyonu - özellik değeri ataması -> WSATTVAS',
        on_delete=models.DO_NOTHING
    )
    opreqref = models.ForeignKey(
        "LG_OPRTREQ",
        db_column='OPREQREF',
        blank=True,
        null=True,
        help_text='Operasyon ihtiyaçları kartı -> OPRTREQ',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_OPATTASG'
        unique_together = (('wsattasgref', 'wsattvalref', 'opreqref'),)
        target_db = 'erp'
