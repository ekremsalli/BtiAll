"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_EARCHIVEDET(
    BaseLogical,
    models.Model
    ):
    invoiceref = models.ForeignKey(
        "LG_INVOICE",
        db_column='INVOICEREF', 
        blank=True, 
        null=True,
        help_text='Fatura ref',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_itemref"
    )
    installmentnumber = models.CharField(
        db_column='INSTALLMENTNUMBER', max_length=51, blank=True, null=True)
    earchivestatus = models.SmallIntegerField(
        db_column='EARCHIVESTATUS', blank=True, null=True)
    sendmod = models.SmallIntegerField(
        db_column='SENDMOD', blank=True, null=True)
    intsalesaddr = models.CharField(
        db_column='INTSALESADDR', max_length=101, blank=True, null=True)
    intpaymentdesc = models.CharField(
        db_column='INTPAYMENTDESC', max_length=51, blank=True, null=True)
    intpaymenttype = models.SmallIntegerField(
        db_column='INTPAYMENTTYPE', blank=True, null=True)
    intpaymentagent = models.CharField(
        db_column='INTPAYMENTAGENT', max_length=51, blank=True, null=True)
    intpaymentdate = models.IntegerField(
        db_column='INTPAYMENTDATE', blank=True, null=True)
    ockserialnumber = models.CharField(
        db_column='OCKSERIALNUMBER', max_length=51, blank=True, null=True)
    ockznumber = models.CharField(
        db_column='OCKZNUMBER', max_length=51, blank=True, null=True)
    ockfichenumber = models.CharField(
        db_column='OCKFICHENUMBER', max_length=51, blank=True, null=True)
    ockfichedate = models.IntegerField(db_column='OCKFICHEDATE', blank=True, null=True)
    stfref = models.IntegerField(
        db_column='STFREF', blank=True, null=True)
    iscomp = models.SmallIntegerField(db_column='ISCOMP', blank=True, null=True)
    taxnr = models.CharField(db_column='TAXNR', max_length=16, blank=True, null=True)
    tckno = models.CharField(db_column='TCKNO', max_length=16, blank=True, null=True)
    name = models.CharField(db_column='NAME', max_length=31, blank=True, null=True)
    surname = models.CharField(db_column='SURNAME', max_length=31, blank=True, null=True)
    definition_field = models.CharField(
        db_column='DEFINITION_', max_length=201, blank=True, null=True)
    addr1 = models.CharField(db_column='ADDR1', max_length=201, blank=True, null=True)
    addr2 = models.CharField(db_column='ADDR2', max_length=201, blank=True, null=True)
    citycode = models.CharField(db_column='CITYCODE', max_length=13, blank=True, null=True)
    city = models.CharField(db_column='CITY', max_length=21, blank=True, null=True)
    countrycode = models.CharField(db_column='COUNTRYCODE', max_length=13, blank=True, null=True)
    country = models.CharField(db_column='COUNTRY', max_length=21, blank=True, null=True)
    postcode = models.CharField(db_column='POSTCODE', max_length=11, blank=True, null=True)
    districtcode = models.CharField(db_column='DISTRICTCODE', max_length=13, blank=True, null=True)
    district = models.CharField(db_column='DISTRICT', max_length=51, blank=True, null=True)
    towncode = models.CharField(db_column='TOWNCODE', max_length=13, blank=True, null=True)
    town = models.CharField(db_column='TOWN', max_length=51, blank=True, null=True)
    emailaddr = models.CharField(db_column='EMAILADDR', max_length=251, blank=True, null=True)
    ispercurr = models.SmallIntegerField(db_column='ISPERCURR', blank=True, null=True)
    insteadofdesp = models.SmallIntegerField(db_column='INSTEADOFDESP', blank=True, null=True)
    taxoffice = models.CharField(db_column='TAXOFFICE', max_length=31, blank=True, null=True)
    telcodes1 = models.CharField(db_column='TELCODES1', max_length=9, blank=True, null=True)
    telcodes2 = models.CharField(db_column='TELCODES2', max_length=9, blank=True, null=True)
    telnrs1 = models.CharField(db_column='TELNRS1', max_length=51, blank=True, null=True)
    telnrs2 = models.CharField(db_column='TELNRS2', max_length=51, blank=True, null=True)
    oldearchivestatus = models.SmallIntegerField(
        db_column='OLDEARCHIVESTATUS', blank=True, null=True)
    drivername1 = models.CharField(db_column='DRIVERNAME1', max_length=31, blank=True, null=True)
    drivername2 = models.CharField(db_column='DRIVERNAME2', max_length=31, blank=True, null=True)
    drivername3 = models.CharField(db_column='DRIVERNAME3', max_length=31, blank=True, null=True)
    driversurname1 = models.CharField(
        db_column='DRIVERSURNAME1', max_length=31, blank=True, null=True)
    driversurname2 = models.CharField(
        db_column='DRIVERSURNAME2', max_length=31, blank=True, null=True)
    driversurname3 = models.CharField(
        db_column='DRIVERSURNAME3', max_length=31, blank=True, null=True)
    drivertckno1 = models.CharField(db_column='DRIVERTCKNO1', max_length=16, blank=True, null=True)
    drivertckno2 = models.CharField(db_column='DRIVERTCKNO2', max_length=16, blank=True, null=True)
    drivertckno3 = models.CharField(db_column='DRIVERTCKNO3', max_length=16, blank=True, null=True)
    platenum1 = models.CharField(db_column='PLATENUM1', max_length=31, blank=True, null=True)
    platenum2 = models.CharField(db_column='PLATENUM2', max_length=31, blank=True, null=True)
    platenum3 = models.CharField(db_column='PLATENUM3', max_length=31, blank=True, null=True)
    chassisnum1 = models.CharField(db_column='CHASSISNUM1', max_length=51, blank=True, null=True)
    chassisnum2 = models.CharField(db_column='CHASSISNUM2', max_length=51, blank=True, null=True)
    chassisnum3 = models.CharField(db_column='CHASSISNUM3', max_length=51, blank=True, null=True)
    responsecode = models.SmallIntegerField(db_column='RESPONSECODE', blank=True, null=True)
    responsestatus = models.SmallIntegerField(db_column='RESPONSESTATUS', blank=True, null=True)
    statusdesc = models.CharField(db_column='STATUSDESC', max_length=256, blank=True, null=True)
    ordfcref = models.IntegerField(db_column='ORDFCREF', blank=True, null=True)
    sellerclientref = models.IntegerField(db_column='SELLERCLIENTREF', blank=True, null=True)
    chaindelivery = models.SmallIntegerField(db_column='CHAINDELIVERY', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_EARCHIVEDET'
        target_db = 'erp'
