"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class L_LDOCNUM(
    BaseLogical,
    models.Model):
    dociden = models.IntegerField(
        db_column='DOCIDEN',
        blank=True,
        null=True,
        help_text='Döküman no'
    )
    appmodule = models.IntegerField(
        db_column='APPMODULE',
        blank=True,
        null=True,
        help_text='Modül no'
    )
    firmid = models.IntegerField(
        db_column='FIRMID',
        blank=True,
        null=True,
        help_text='Firma no'
    )
    divisid = models.IntegerField(
        db_column='DIVISID',
        blank=True,
        null=True,
        help_text='Bölüm no'
    )
    whid = models.IntegerField(
        db_column='WHID',
        blank=True,
        null=True,
        help_text='Ambar no'
    )
    factid = models.IntegerField(
        db_column='FACTID',
        blank=True,
        null=True,
        help_text='Fabrika no'
    )
    groupid = models.IntegerField(
        db_column='GROUPID',
        blank=True,
        null=True,
        help_text='Şablonu kullanabilecek gruplar'
    )
    roleid = models.IntegerField(
        db_column='ROLEID',
        blank=True,
        null=True,
        help_text='Şablonu kullanabilecek roller'
    )
    userid = models.IntegerField(
        db_column='USERID',
        blank=True,
        null=True,
        help_text='Şablonu kullanabilecek kullanıcılar'
    )
    firstnum = models.CharField(
        db_column='FIRSTNUM',
        max_length=65,
        blank=True,
        null=True,
        help_text='Başlangıç numarası'
    )
    lastnum = models.CharField(
        db_column='LASTNUM',
        max_length=65,
        blank=True,
        null=True,
        help_text='Bitiş numarası'
    )
    effsdate = models.DateTimeField(
        db_column='EFFSDATE',
        blank=True,
        null=True,
        help_text='Atama başlangıç tarihi'
    )
    effedate = models.DateTimeField(
        db_column='EFFEDATE',
        blank=True,
        null=True,
        help_text='Atama bitiş tarihi'
    )
    numform = models.SmallIntegerField(
        db_column='NUMFORM',
        blank=True,
        null=True,
        help_text='Numara formatı sayı/metin'
    )
    lastasgnd = models.CharField(
        db_column='LASTASGND',
        max_length=65,
        blank=True,
        null=True,
        help_text='Son atama tarihi'
    )
    owncode = models.CharField(
        db_column='OWNCODE',
        max_length=65,
        blank=True,
        null=True,
    )
    segments1_segstart = models.CharField(
        db_column='SEGMENTS1_SEGSTART',
        max_length=33,
        blank=True,
        null=True,
        help_text='Aralık başlangıçı'

    )
    segments1_segend = models.CharField(
        db_column='SEGMENTS1_SEGEND',
        max_length=33,
        blank=True,
        null=True,
        help_text='Aralık bitişi'
    )
    segments1_seglen = models.SmallIntegerField(
        db_column='SEGMENTS1_SEGLEN',
        blank=True,
        null=True,
        help_text='Karakter sayısı'
    )
    segments1_segattrb = models.SmallIntegerField(
        db_column='SEGMENTS1_SEGATTRB',
        blank=True,
        null=True,
        help_text='Özellik'
    )
    segments1_fillch = models.SmallIntegerField(
        db_column='SEGMENTS1_FILLCH',
        blank=True,
        null=True,
        help_text='Boşluk karakteri'
    )
    segments1_segform = models.SmallIntegerField(
        db_column='SEGMENTS1_SEGFORM',
        blank=True,
        null=True,
        help_text='Sıralama'
    )
    segments1_increm = models.SmallIntegerField(
        db_column='SEGMENTS1_INCREM',
        blank=True,
        null=True,
        help_text='Artırımlı'
    )
    segments1_txtlang = models.SmallIntegerField(
        db_column='SEGMENTS1_TXTLANG',
        blank=True,
        null=True,
        help_text='Dili'
    )
    segments1_resvd1 = models.IntegerField(
        db_column='SEGMENTS1_RESVD1',
        blank=True,
        null=True,
        help_text='Rezerve alan 1'
    )
    segments1_resvd2 = models.IntegerField(
        db_column='SEGMENTS1_RESVD2',
        blank=True,
        null=True,
        help_text='Rezerve alan 2'
    )

    segments2_segstart = models.CharField(
        db_column='SEGMENTS2_SEGSTART',
        max_length=33,
        blank=True,
        null=True,
        help_text='Aralık başlangıçı'

    )
    segments2_segend = models.CharField(
        db_column='SEGMENTS2_SEGEND',
        max_length=33,
        blank=True,
        null=True,
        help_text='Aralık bitişi'
    )
    segments2_seglen = models.SmallIntegerField(
        db_column='SEGMENTS2_SEGLEN',
        blank=True,
        null=True,
        help_text='Karakter sayısı'
    )
    segments2_segattrb = models.SmallIntegerField(
        db_column='SEGMENTS2_SEGATTRB',
        blank=True,
        null=True,
        help_text='Özellik'
    )
    segments2_fillch = models.SmallIntegerField(
        db_column='SEGMENTS2_FILLCH',
        blank=True,
        null=True,
        help_text='Boşluk karakteri'
    )
    segments2_segform = models.SmallIntegerField(
        db_column='SEGMENTS2_SEGFORM',
        blank=True,
        null=True,
        help_text='Sıralama'
    )
    segments2_increm = models.SmallIntegerField(
        db_column='SEGMENTS2_INCREM',
        blank=True,
        null=True,
        help_text='Artırımlı'
    )
    segments2_txtlang = models.SmallIntegerField(
        db_column='SEGMENTS2_TXTLANG',
        blank=True,
        null=True,
        help_text='Dili'
    )
    segments2_resvd1 = models.IntegerField(
        db_column='SEGMENTS2_RESVD1',
        blank=True,
        null=True,
        help_text='Rezerve alan 1'
    )
    segments2_resvd2 = models.IntegerField(
        db_column='SEGMENTS2_RESVD2',
        blank=True,
        null=True,
        help_text='Rezerve alan 2'
    )
    workid = models.IntegerField(
        db_column='WORKID', blank=True, null=True)
    placeref = models.IntegerField(
        db_column='PLACEREF', blank=True, null=True)
    specode = models.CharField(
        db_column='SPECODE', max_length=11, blank=True, null=True)
    placecode = models.CharField(
        db_column='PLACECODE', max_length=33, blank=True, null=True)
    workarea = models.SmallIntegerField(
        db_column='WORKAREA', blank=True, null=True)
    termid = models.IntegerField(
        db_column='TERMID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_LDOCNUM'
        target_db = 'system'
