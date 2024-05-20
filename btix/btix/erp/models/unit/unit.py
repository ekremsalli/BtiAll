"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_UNITSETF(
    BaseLogical,
    BaseCode,
    BaseInfo,
    BaseSiteRec,
    BaseWF,
    BaseGUID,
    BaseRef,
    models.Model):
    """
        Birimler
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=25,
        blank=True,
        null=True,
        help_text='Birim seti kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Birim seti açıklaması'
    )
    cardtype = models.SmallIntegerField(
        db_column='CARDTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Uzunluk ölçüleri'),
            (2, 'Alan ölçüleri'),
            (3, 'Hacim ölçüleri'),
            (4, 'Ağırlık ölçüleri'),
            (5, 'Kullanıcı tanımlı ölçüler')
        ],
        help_text='Kayıt türü'
    )
    specitem = models.SmallIntegerField(
        db_column='SPECITEM',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text='Malzeme / Hizmet kartına özel'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_UNITSETF'
        unique_together = (('cardtype', 'code'),)
        target_db='erp'

    def __str__(self):
        return f"{self.code} {self.name}"

class LG_UNITSETL(
    BaseLogical,
    models.Model):
    code = models.CharField(
        db_column='CODE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Birim kodu'
    )
    name = models.CharField(
        db_column='NAME',
        max_length=51,
        blank=True,
        null=True,
        help_text='Birim açıklaması'
    )
    unitsetref = models.ForeignKey(
        "LG_UNITSETF",
        db_column='UNITSETREF',
        blank=True,
        null=True,
        help_text='Birim set kaydı ref. -> UNITSETF',
        on_delete=models.DO_NOTHING
    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Saır no'
    )
    mainunit = models.SmallIntegerField(
        db_column='MAINUNIT',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text='Ana birim'
    )
    convfact1 = models.FloatField(
        db_column='CONVFACT1',
        blank=True,
        null=True,
        help_text='Çevrim katsayısı'
    )
    convfact2 = models.FloatField(
        db_column='CONVFACT2',
        blank=True,
        null=True,
        help_text='Çevrim katsayısı'
    )
    width = models.FloatField(
        db_column='WIDTH',
        blank=True,
        null=True,
        help_text='Genişlik'
    )
    length = models.FloatField(
        db_column='LENGTH',
        blank=True,
        null=True,
        help_text='Uzunluk'
    )
    height = models.FloatField(
        db_column='HEIGHT',
        blank=True,
        null=True,
        help_text='Yükseklik'
    )
    area = models.FloatField(
        db_column='AREA',
        blank=True,
        null=True,
        help_text='Alan'
    )
    volume_field = models.FloatField(
        db_column='VOLUME_',
        blank=True,
        null=True,
        help_text='Hacim'
    )
    weight = models.FloatField(
        db_column='WEIGHT',
        blank=True,
        null=True,
        help_text='Ağırlık'
    )
    widthref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='WIDTHREF',
        blank=True,
        null=True,
        help_text='Genişlik ölçü birimi ref. -> UNITSETL',
        related_name="%(app_label)s_%(class)s_widthref",
        on_delete=models.DO_NOTHING
    )
    lengthref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='LENGTHREF',
        blank=True,
        null=True,
        help_text='Uzunluk ölçü birimi ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_lengthref"
    )
    heightref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='HEIGHTREF',
        blank=True,
        null=True,
        help_text='Yükseklik ölçü birimi ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_heightref"
    )
    arearef = models.ForeignKey(
        "LG_UNITSETL",
        db_column='AREAREF',
        blank=True,
        null=True,
        help_text='Alan ölçü birimi ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_arearef"
    )
    volumeref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='VOLUMEREF',
        blank=True,
        null=True,
        help_text='Hacim ölçü birimi ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_volumeref"
    )
    weightref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='WEIGHTREF',
        blank=True,
        null=True,
        help_text='Ağırlık ölçü birimi ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_weightref"
    )
    divunit = models.SmallIntegerField(
        db_column='DIVUNIT',
        blank=True,
        null=True,
        choices=[
            (1, 'Evet'),
            (0, 'Hayır')
        ],
        help_text='Bölünebilir'
    )
    measurecode = models.CharField(
        db_column='MEASURECODE',
        max_length=51,
        blank=True,
        null=True,
    )
    globalcode = models.CharField(
        db_column='GLOBALCODE',
        max_length=11,
        blank=True,
        null=True,
        help_text=''
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_UNITSETL'
        target_db = 'erp'

class LG_SRVUNITA(
    BaseLogical,
    BasePriority,
    models.Model):
    """
        Hizmet kaydı - Birim ataması
    """
    srvref = models.ForeignKey(
        "LG_SRVCARD",
        db_column='SRVREF',
        blank=True,
        null=True,
        help_text='Hizmet kartı ref. -> SRVCARD',
        on_delete=models.DO_NOTHING
    )
    linenr = models.SmallIntegerField(
        db_column='LINENR',
        blank=True,
        null=True,
        help_text='Satır numarası'
    )
    unitlineref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UNITLINEREF',
        blank=True,
        null=True,
        help_text='Birim ref. -> UNITSETL',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_SRVUNITA'
        unique_together = (('srvref', 'unitlineref'),)
        target_db = 'erp'

class LG_UNITSETC(
    BaseLogical,
    models.Model):
    """
        Birim setleri arası çevrim katsayıları
    """
    parentusref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='PARENTUSREF',
        blank=True,
        null=True,
        help_text='Ana birim ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_parentusref"
    )
    childusref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='CHILDUSREF',
        blank=True,
        null=True,
        help_text='Alt birim ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_childusref"

    )
    convfact1 = models.FloatField(
        db_column='CONVFACT1',
        blank=True,
        null=True,
        help_text='Çevrim katsayısı'
    )
    convfact2 = models.FloatField(
        db_column='CONVFACT2',
        blank=True,
        null=True,
        help_text='Çevrim katsayısı'
    )

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_UNITSETC'
        unique_together = (('parentusref', 'childusref'),)
        target_db = 'erp'
