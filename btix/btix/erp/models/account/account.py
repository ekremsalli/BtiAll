"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_EMUHACC(
    BaseLogical,
    BaseCenter,
    BaseWF,
    BaseActive,
    BaseInfo,
    BaseCode,
    BaseSiteRec,
    models.Model):
    """
        Muhasebe hesapları
    """
    code = models.CharField(
        db_column='CODE',
        unique=True,
        max_length=101,
        blank=True,
        null=True,
        help_text='Muhasebe kodu'
    )
    definition_field = models.CharField(
        db_column='DEFINITION_',
        max_length=101,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    extname = models.CharField(
        db_column='EXTNAME',
        max_length=101,
        blank=True,
        null=True,
        help_text='İkinci açıklama')
    units = models.CharField(
        db_column='UNITS',
        max_length=5,
        blank=True,
        null=True,
        help_text='Birim'
    )
    addinfoptr = models.IntegerField(
        db_column='ADDINFOPTR',
        blank=True,
        null=True,
        help_text='Ek bilgi ref.'
    )
    currdifref = models.IntegerField(
        db_column='CURRDIFREF',
        blank=True,
        null=True,
        help_text='Kuru farkı hesabı ref.'
    )
    subaccounts = models.IntegerField(
        db_column='SUBACCOUNTS',
        blank=True,
        null=True,
        help_text='Alt hesap sayısı'
    )
    level_field = models.SmallIntegerField(
        db_column='LEVEL_',
        blank=True,
        null=True,
        help_text='Seviye')
    groupcode = models.SmallIntegerField(
        db_column='GROUPCODE',
        blank=True,
        null=True,
        help_text='Grup kodu'
    )
    acctype = models.SmallIntegerField(
        db_column='ACCTYPE',
        blank=True,
        null=True,
        choices=[
            (0, 'Borç'),
            (1, 'Alacak'),
            (2, 'Borç+Alacak')
        ],
        help_text='Hesap tipi'
    )
    quanctrl = models.SmallIntegerField(
        db_column='QUANCTRL',
        blank=True,
        null=True,
        help_text='Seviye kontrolü'
    )
    centerctrl = models.SmallIntegerField(
        db_column='CENTERCTRL',
        blank=True,
        null=True,
        help_text='Masraf merkezi kontrolü'
    )
    extenref = models.IntegerField(
        db_column='EXTENREF',
        blank=True,
        null=True,
        help_text='Ekstra dosya ref.'
    )
    orglogicalref = models.IntegerField(
        db_column='ORGLOGICALREF',
        blank=True,
        null=True,
        help_text='Orjinal kayıt ref.'
    )
    postingonly = models.SmallIntegerField(db_column='POSTINGONLY', blank=True,
        null=True)
    category = models.IntegerField(db_column='CATEGORY', blank=True, null=True)
    ftflags = models.CharField(db_column='FTFLAGS', max_length=51, blank=True,
        null=True)
    monetary = models.SmallIntegerField(db_column='MONETARY', blank=True,
        null=True)
    projectctrl = models.SmallIntegerField(db_column='PROJECTCTRL', blank=True,
        null=True)
    notinflated = models.SmallIntegerField(db_column='NOTINFLATED', blank=True,
        null=True)
    currdiffdebtref = models.IntegerField(db_column='CURRDIFFDEBTREF',
        blank=True, null=True)
    infdiffaccref = models.IntegerField(db_column='INFDIFFACCREF', blank=True,
        null=True)
    isanbdgtline = models.SmallIntegerField(db_column='ISANBDGTLINE',
        blank=True, null=True)
    bdgtaccref = models.IntegerField(db_column='BDGTACCREF',
        blank=True, null=True)
    bdreflaccref = models.IntegerField(db_column='BDREFLACCREF', blank=True,
        null=True)
    bdgtpayaref = models.IntegerField(db_column='BDGTPAYAREF', blank=True,
        null=True)
    bdpayreflaref = models.IntegerField(db_column='BDPAYREFLAREF', blank=True,
        null=True)
    crbdgtaccln = models.SmallIntegerField(db_column='CRBDGTACCLN', blank=True,
        null=True)
    crbdgtpayaln = models.SmallIntegerField(db_column='CRBDGTPAYALN',
        blank=True, null=True)
    corpcode1 = models.CharField(db_column='CORPCODE1', max_length=3,
        blank=True, null=True)
    corpcode2 = models.CharField(db_column='CORPCODE2', max_length=3,
        blank=True, null=True)
    corpcode3 = models.CharField(db_column='CORPCODE3', max_length=3,
        blank=True, null=True)
    corpcode4 = models.CharField(db_column='CORPCODE4', max_length=3,
        blank=True, null=True)
    funccode1 = models.CharField(db_column='FUNCCODE1', max_length=3,
        blank=True, null=True)
    funccode2 = models.CharField(db_column='FUNCCODE2', max_length=3,
        blank=True, null=True)
    funccode3 = models.CharField(db_column='FUNCCODE3', max_length=3,
        blank=True, null=True)
    funccode4 = models.CharField(db_column='FUNCCODE4', max_length=3,
        blank=True, null=True)
    fincode = models.CharField(db_column='FINCODE', max_length=3,
        blank=True, null=True)
    ecocode1 = models.CharField(db_column='ECOCODE1', max_length=3,
        blank=True, null=True)
    ecocode2 = models.CharField(db_column='ECOCODE2', max_length=3,
        blank=True, null=True)
    ecocode3 = models.CharField(db_column='ECOCODE3', max_length=3,
        blank=True, null=True)
    ecocode4 = models.CharField(db_column='ECOCODE4', max_length=3,
        blank=True, null=True)
    vatreflaref = models.IntegerField(db_column='VATREFLAREF',
        blank=True, null=True)
    vatreflotharef = models.IntegerField(db_column='VATREFLOTHAREF',
        blank=True, null=True)
    ccurrency = models.SmallIntegerField(db_column='CCURRENCY', blank=True,
        null=True)
    curratetype = models.SmallIntegerField(db_column='CURRATETYPE', blank=True,
        null=True)
    fixedcurrtype = models.SmallIntegerField(db_column='FIXEDCURRTYPE',
        blank=True, null=True)
    cldef = models.CharField(db_column='CLDEF', max_length=201, blank=True,
        null=True)
    taxnr = models.CharField(db_column='TAXNR', max_length=12, blank=True,
        null=True)
    fortaxdecl = models.SmallIntegerField(db_column='FORTAXDECL', blank=True,
        null=True)
    vatacc = models.SmallIntegerField(db_column='VATACC', blank=True, null=True)
    grptransaccref = models.IntegerField(db_column='GRPTRANSACCREF',
        blank=True, null=True)
    specode2 = models.CharField(db_column='SPECODE2', max_length=11,
        blank=True, null=True)
    specode3 = models.CharField(db_column='SPECODE3', max_length=11,
        blank=True, null=True)
    specode4 = models.CharField(db_column='SPECODE4', max_length=11,
        blank=True, null=True)
    specode5 = models.CharField(db_column='SPECODE5', max_length=11,
        blank=True, null=True)
    tckno = models.CharField(db_column='TCKNO', max_length=16, blank=True,
        null=True)
    isperscomp = models.SmallIntegerField(db_column='ISPERSCOMP', blank=True,
        null=True)
    iscash = models.SmallIntegerField(db_column='ISCASH', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_EMUHACC'
        unique_together = (('active', 'code'),)
        target_db = 'erp'

    def __str__(self):
        return f"{self.code} {self.definition_field}"

