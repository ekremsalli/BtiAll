"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.models.base import *

class L_CAPIUSER(models.Model):
    logicalref = models.AutoField(db_column='LOGICALREF', primary_key=True)
    nr = models.SmallIntegerField(db_column='NR', unique=True, blank=True, null=True)
    name = models.CharField(db_column='NAME', unique=True, max_length=21, blank=True, null=True)
    key_field = models.CharField(db_column='KEY_', max_length=32, blank=True, null=True)
    groups1 = models.SmallIntegerField(db_column='GROUPS1', blank=True, null=True)
    groups2 = models.SmallIntegerField(db_column='GROUPS2', blank=True, null=True)
    groups3 = models.SmallIntegerField(db_column='GROUPS3', blank=True, null=True)
    firm = models.ForeignKey("L_CAPIFIRM", db_column='FIRMNR', blank=True, null=True,
        to_field='nr', on_delete=models.DO_NOTHING
    )
    # @check
    lang = models.SmallIntegerField(db_column='LANG', blank=True, null=True)
    options = models.SmallIntegerField(db_column='OPTIONS', blank=True, null=True)
    blocked = models.SmallIntegerField(db_column='BLOCKED', blank=True, null=True)
    logflag = models.SmallIntegerField(db_column='LOGFLAG', blank=True, null=True)
    intfres = models.CharField(db_column='INTFRES', max_length=13, blank=True, null=True)
    emaila = models.CharField(db_column='EMAILA', max_length=51, blank=True, null=True)
    defrole = models.SmallIntegerField(db_column='DEFROLE', blank=True, null=True)
    roles1 = models.SmallIntegerField(db_column='ROLES1', blank=True, null=True)
    roles2 = models.SmallIntegerField(db_column='ROLES2', blank=True, null=True)
    roles3 = models.SmallIntegerField(db_column='ROLES3', blank=True, null=True)
    roles4 = models.SmallIntegerField(db_column='ROLES4', blank=True, null=True)
    roles5 = models.SmallIntegerField(db_column='ROLES5', blank=True, null=True)
    userext = models.IntegerField(db_column='USEREXT', blank=True, null=True)
    uniflog = models.SmallIntegerField(db_column='UNIFLOG', blank=True, null=True)
    dmconn = models.SmallIntegerField(db_column='DMCONN', blank=True, null=True)
    webconn = models.SmallIntegerField(db_column='WEBCONN', blank=True, null=True)
    extroles1 = models.SmallIntegerField(db_column='EXTROLES1', blank=True, null=True)
    extroles2 = models.SmallIntegerField(db_column='EXTROLES2', blank=True, null=True)
    extroles3 = models.SmallIntegerField(db_column='EXTROLES3', blank=True, null=True)
    extroles4 = models.SmallIntegerField(db_column='EXTROLES4', blank=True, null=True)
    extroles5 = models.SmallIntegerField(db_column='EXTROLES5', blank=True, null=True)
    seller = models.SmallIntegerField(db_column='SELLER', blank=True, null=True)
    specode = models.CharField(db_column='SPECODE', max_length=11, blank=True, null=True)
    cyphcode = models.CharField(db_column='CYPHCODE', max_length=11, blank=True, null=True)
    divnr = models.SmallIntegerField(db_column='DIVNR', blank=True, null=True)
    deptnr = models.SmallIntegerField(db_column='DEPTNR', blank=True, null=True)
    whnr = models.SmallIntegerField(db_column='WHNR', blank=True, null=True)
    keycdate = models.DateTimeField(db_column='KEYCDATE', blank=True, null=True)
    disabled = models.SmallIntegerField(db_column='DISABLED', blank=True, null=True)
    prclimitgrp = models.SmallIntegerField(db_column='PRCLIMITGRP', blank=True, null=True)
    budgetadmin = models.SmallIntegerField(db_column='BUDGETADMIN', blank=True, null=True)
    prevkey1 = models.CharField(db_column='PREVKEY1', max_length=32, blank=True, null=True)
    prevkey2 = models.CharField(db_column='PREVKEY2', max_length=32, blank=True, null=True)
    focusadmin = models.SmallIntegerField(db_column='FOCUSADMIN', blank=True, null=True)
    blockedtheme = models.SmallIntegerField(db_column='BLOCKEDTHEME', blank=True, null=True)
    factnr = models.SmallIntegerField(db_column='FACTNR', blank=True, null=True)
    activedirectoryuser = models.SmallIntegerField(db_column='ACTIVEDIRECTORYUSER', blank=True, null=True)
    adusercannotmodify = models.SmallIntegerField(db_column='ADUSERCANNOTMODIFY', blank=True, null=True)
    singlesignon = models.SmallIntegerField(db_column='SINGLESIGNON', blank=True, null=True)
    workspace = models.SmallIntegerField(db_column='WORKSPACE', blank=True, null=True)
    localcaldr = models.SmallIntegerField(db_column='LOCALCALDR', blank=True, null=True)
    forcerelogin = models.SmallIntegerField(db_column='FORCERELOGIN', blank=True, null=True)
    failedlogins = models.SmallIntegerField(db_column='FAILEDLOGINS', blank=True, null=True)
    phoneno = models.CharField(db_column='PHONENO', max_length=25, blank=True, null=True)
    loginblckcnt = models.SmallIntegerField(db_column='LOGINBLCKCNT', blank=True, null=True)
    username = models.CharField(db_column='USERNAME', max_length=25, blank=True, null=True)
    usersurname = models.CharField(db_column='USERSURNAME', max_length=25, blank=True, null=True)
    mobilsecuritycode = models.CharField(db_column='MOBILSECURITYCODE', max_length=33, blank=True, null=True)
    forcereloginmsg = models.CharField(db_column='FORCERELOGINMSG', max_length=255, blank=True, null=True)
    dontshowlogobipage = models.SmallIntegerField(db_column='DONTSHOWLOGOBIPAGE', blank=True, null=True)
    onlyobject = models.SmallIntegerField(db_column='ONLYOBJECT', blank=True, null=True)
    objectfullright = models.SmallIntegerField(db_column='OBJECTFULLRIGHT', blank=True, null=True)
    faxusername = models.CharField(db_column='FAXUSERNAME', max_length=21, blank=True, null=True)
    faxuserkey = models.CharField(db_column='FAXUSERKEY', max_length=32, blank=True, null=True)
    faxuseremail = models.CharField(db_column='FAXUSEREMAIL', max_length=51, blank=True, null=True)
    key_md5 = models.CharField(db_column='KEY_MD5', max_length=51, blank=True, null=True)
    accesstype = models.SmallIntegerField(db_column='ACCESSTYPE', blank=True, null=True)
    usertype = models.SmallIntegerField(db_column='USERTYPE', blank=True, null=True)
    kvkkuser = models.SmallIntegerField(db_column='KVKKUSER', blank=True, null=True)
    usrprojectcode = models.CharField(db_column='USRPROJECTCODE', max_length=101, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_CAPIUSER'
        target_db = 'system'

    def __str__(self):
        return f'{self.nr} {self.name}'

class L_GOUSERS(models.Model):
    logicalref = models.AutoField(
        db_column='LOGICALREF',
        primary_key=True,
        help_text='Fiziksel adres'
    )
    usrnr = models.SmallIntegerField(
        db_column='USRNR',
        blank=True,
        null=True,
        help_text='Kullanıcı no'
    )
    termnr = models.SmallIntegerField(
        db_column='TERMNR',
        blank=True,
        null=True,
        help_text='Terminal no'
    )
    llogindate = models.IntegerField(
        db_column='LLOGINDATE',
        blank=True,
        null=True,
        help_text='Programa giriş tarihi'
    )
    llogintime = models.IntegerField(
        db_column='LLOGINTIME',
        blank=True,
        null=True,
        help_text='Programa giriş saati'
    )
    llogoutdate = models.IntegerField(
        db_column='LLOGOUTDATE',
        blank=True,
        null=True,
        help_text='Programdan çıkış tarihi'
    )
    llogouttime = models.IntegerField(
        db_column='LLOGOUTTIME',
        blank=True,
        null=True,
        help_text='Programdan çıkış saati'
    )
    abnterms = models.IntegerField(db_column='ABNTERMS', blank=True, null=True)
    tdeferrors = models.IntegerField(db_column='TDEFERRORS', blank=True, null=True)
    appname = models.CharField(db_column='APPNAME', max_length=129, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'L_GOUSERS'
        target_db = 'system'

    def __str__(self):
        return f'{self.usrnr}'

