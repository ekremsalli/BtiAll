"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_FAYEAR(models.Model):
    """
        Sabit kıymet yıllık kaydı
    """
    lref = models.AutoField(
        db_column='LREF',
        primary_key=True,
        help_text='Fiziksel adres'
    )
    tablety = models.SmallIntegerField(
        db_column='TABLETY',
        blank=True,
        null=True,
        choices=[
            (0, 'Yerel'),
            (1, 'Dövizli')
        ],
        help_text='Tablo türü'
    )
    fregref = models.ForeignKey(
        "LG_FAREGIST",
        db_column='FREGREF',
        blank=True,
        null=True,
        help_text='S.K. kayot ref. -> FAREGIST',
        on_delete=models.DO_NOTHING
    )
    year_field = models.SmallIntegerField(
        db_column='YEAR_',
        blank=True,
        null=True,
        help_text='Yıl'
    )
    drate = models.FloatField(
        db_column='DRATE',
        blank=True,
        null=True,
        help_text='Amortisman oranı'
    )
    revrate = models.FloatField(
        db_column='REVRATE',
        blank=True,
        null=True,
        help_text='Yeniden değerleme oranı'
    )
    dtype = models.SmallIntegerField(
        db_column='DTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Normal'),
            (2, 'Azalan bakiyeler')
        ],
        help_text='Amortisman türü'
    )
    quanout = models.FloatField(
        db_column='QUANOUT',
        blank=True,
        null=True,
        help_text='Düşülen miktar'
    )
    locfigs_costop = models.FloatField(
        db_column='LOCFIGS_COSTOP',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden başlangıç rakamları'
    )
    locfigs_expusual = models.FloatField(
        db_column='LOCFIGS_EXPUSUAL',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden değerlemeye tabi giderler rakamları'
    )
    locfigs_expoutrev = models.FloatField(
        db_column='LOCFIGS_EXPOUTREV',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden değerleme harici giderler rakamları'
    )
    locfigs_cumexpor = models.FloatField(
        db_column='LOCFIGS_CUMEXPOR',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden birikmiş değerleme dışı giderler'
    )
    locfigs_amountout = models.FloatField(
        db_column='LOCFIGS_AMOUNTOUT',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden düşülen değerler rakamı'
    )
    locfigs_amountoutr = models.FloatField(
        db_column='LOCFIGS_AMOUNTOUTR',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden düşülen değerleme dışı tutar rakamları'
    )
    locfigs_bookvalop = models.FloatField(
        db_column='LOCFIGS_BOOKVALOP',
        blank=True,
        null=True,
        help_text='Yerel ara üzerinden değerleme öncesi S.K. değeri'
    )
    locfigs_accdeprop = models.FloatField(
        db_column='LOCFIGS_ACCDEPROP',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden değerleme öncesi birikmiş amortisman rakamları'
    )
    locfigs_accdpout = models.FloatField(
        db_column='LOCFIGS_ACCDPOUT',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden amortismandan düşülecek tutar'
    )
    locfigs_bookvalrv = models.FloatField(
        db_column='LOCFIGS_BOOKVALRV',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden değerlendirme sonrası S.K. değeri'
    )
    locfigs_accdeprrv = models.FloatField(
        db_column='LOCFIGS_ACCDEPRRV',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden değerlendirme sonrası birikmiş para'
    )
    locfigs_deprann = models.FloatField(
        db_column='LOCFIGS_DEPRANN',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden yıllık amortisman tutarı'
    )
    locfigs_accdepreoy = models.FloatField(
        db_column='LOCFIGS_ACCDEPREOY',
        blank=True,
        null=True,
        help_text='Yerel para üzerinden yıl sonu birikmiş amortisman'
    )
    locfigs_accdeprcst = models.FloatField(
        db_column='LOCFIGS_ACCDEPRCST',
        blank=True,
        null=True,
        help_text='Yerel para maliyet üzerinden birikmiş amortisman'
    )
    locfigs_revamounin = models.FloatField(
        db_column='LOCFIGS_REVAMOUNIN', blank=True, null=True)
    locfigs_revamounout = models.FloatField(
        db_column='LOCFIGS_REVAMOUNOUT', blank=True, null=True)
    curfigs_costop = models.FloatField(
        db_column='CURFIGS_COSTOP',
        blank=True,
        null=True,
        help_text='Raporlama dövizi üzerinden başlangıç'
    )
    curfigs_expusual = models.FloatField(
        db_column='CURFIGS_EXPUSUAL',
        blank=True,
        null=True,
        help_text='Raporlama dövizi üzrinden değerlemeye tabi giderler'
    )
    curfigs_expoutrev = models.FloatField(
        db_column='CURFIGS_EXPOUTREV',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_cumexpor = models.FloatField(
        db_column='CURFIGS_CUMEXPOR',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_amountout = models.FloatField(
        db_column='CURFIGS_AMOUNTOUT',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_amountoutr = models.FloatField(
        db_column='CURFIGS_AMOUNTOUTR',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_bookvalop = models.FloatField(
        db_column='CURFIGS_BOOKVALOP',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_accdeprop = models.FloatField(
        db_column='CURFIGS_ACCDEPROP',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_accdpout = models.FloatField(
        db_column='CURFIGS_ACCDPOUT',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_bookvalrv = models.FloatField(
        db_column='CURFIGS_BOOKVALRV',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_accdeprrv = models.FloatField(
        db_column='CURFIGS_ACCDEPRRV',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_deprann = models.FloatField(
        db_column='CURFIGS_DEPRANN',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_accdepreoy = models.FloatField(
        db_column='CURFIGS_ACCDEPREOY',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_accdeprcst = models.FloatField(
        db_column='CURFIGS_ACCDEPRCST',
        blank=True,
        null=True,
        help_text=''
    )
    curfigs_revamounin = models.FloatField(
        db_column='CURFIGS_REVAMOUNIN', blank=True, null=True)
    curfigs_revamounout = models.FloatField(
        db_column='CURFIGS_REVAMOUNOUT', blank=True, null=True)
    vatposted = models.FloatField(
        db_column='VATPOSTED',
        blank=True,
        null=True,
        help_text='Muhasebeleşen KDV'
    )
    daccflag = models.SmallIntegerField(
        db_column='DACCFLAG',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Amortisman muhasebeleşmiş'
    )
    raccflag = models.SmallIntegerField(
        db_column='RACCFLAG',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Yeniden değ. muhasebeleşmiş'
    )
    vaccflag = models.SmallIntegerField(
        db_column='VACCFLAG',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='KDV muhasebeleşmiş'
    )
    calcmon = models.SmallIntegerField(
        db_column='CALCMON',
        blank=True,
        null=True,
        help_text='Hesaplanan dönem sonu'
    )
    accficheref = models.IntegerField(
        db_column='ACCFICHEREF', blank=True, null=True)
    locfigs2_perdreval = models.FloatField(
        db_column='LOCFIGS2_PERDREVAL', blank=True, null=True)
    locfigs2_perdaccdeprrv = models.FloatField(
        db_column='LOCFIGS2_PERDACCDEPRRV', blank=True, null=True)
    locfigs2_perddepr = models.FloatField(
        db_column='LOCFIGS2_PERDDEPR', blank=True, null=True)
    curfigs2_perdreval = models.FloatField(
        db_column='CURFIGS2_PERDREVAL', blank=True, null=True)
    curfigs2_perdaccdeprrv = models.FloatField(
        db_column='CURFIGS2_PERDACCDEPRRV', blank=True, null=True)
    curfigs2_perddepr = models.FloatField(
        db_column='CURFIGS2_PERDDEPR', blank=True, null=True)
    infidx = models.FloatField(
        db_column='INFIDX', blank=True, null=True)
    closed = models.SmallIntegerField(
        db_column='CLOSED', blank=True, null=True)
    faexpitemref = models.IntegerField(
        db_column='FAEXPITEMREF', blank=True, null=True)
    faexptype = models.SmallIntegerField(
        db_column='FAEXPTYPE', blank=True, null=True)
    prodamount = models.FloatField(
        db_column='PRODAMOUNT', blank=True, null=True)
    cutdepramnt = models.FloatField(
        db_column='CUTDEPRAMNT', blank=True, null=True)
    stopped = models.SmallIntegerField(
        db_column='STOPPED', blank=True, null=True)
    branch = models.SmallIntegerField(
        db_column='BRANCH', blank=True, null=True)
    allocateall = models.SmallIntegerField(
        db_column='ALLOCATEALL', blank=True, null=True)
    skipdepr = models.SmallIntegerField(
        db_column='SKIPDEPR', blank=True, null=True)
    curfigs2_perddeprkkeg = models.FloatField(
        db_column='CURFIGS2_PERDDEPRKKEG', blank=True, null=True)
    locfigs2_perddeprkkeg = models.FloatField(
        db_column='LOCFIGS2_PERDDEPRKKEG', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_FAYEAR'
        target_db = 'erp'
