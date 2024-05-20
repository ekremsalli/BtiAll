"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class ClShipment(base.Serializer):
	"""
		Cari sevkiyat adresleri
	"""
	class Meta:
		XML_ROOT = 'ARP_SHIPMENT_LOCATIONS'
		XML_SUBROOT = 'SHIPMENT_LOC'
		DATA_OBJECT = 'doArpShipLic'
		REST_ENDPOINT = 'ArpShipmentLocations'
		RELATED_TABLE = 'LG_SHIPINFO'

	ARP_CODE = base.CharField(label="Cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=True)
	CODE = base.CharField(label="Kod", table="LG_SHIPINFO",field="CODE",max_length=25,required=True)
	TITLE = base.CharField(label="Unvan", table="LG_SHIPINFO",field="TITLE",max_length=200,required=False)
	DESCRIPTION = base.CharField(label="Açıklama", table="LG_SHIPINFO",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_SHIPINFO",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki kodu", table="LG_SHIPINFO",field="CYPHCODE",max_length=11,required=False)
	ADDRESS1 = base.CharField(label="Adres1", table="LG_SHIPINFO",field="ADDR1",max_length=255,required=False)
	ADDRESS2 = base.CharField(label="Adres2", table="LG_SHIPINFO",field="ADDR2",max_length=255,required=False)
	DISTRICT_CODE = base.CharField(label="Semt Kodu", table="LG_CLCARD",field="DISTRICTCODE",max_length=13,required=False)
	DISTRICT = base.CharField(label="Semt Açıklaması", table="LG_CLCARD",field="DISTRICT",max_length=51,required=False)
	TOWN_CODE = base.CharField(label="İlçe Kodu", table="LG_CLCARD",field="TOWNCODE",max_length=13,required=False)
	TOWN = base.CharField(label="İlçe", table="LG_CLCARD",field="TOWN",max_length=51,required=False)
	CITY_CODE = base.CharField(label="Şehir Kodu", table="LG_CLCARD",field="CITY",max_length=21,required=False)
	CITY = base.CharField(label="Şehir", table="LG_SHIPINFO",field="CITY",max_length=21,required=False)
	COUNTRY_CODE = base.CharField(label="Ülke Kodu", table="LG_CLCARD",field="COUNTRYCODE",max_length=13,required=False)
	COUNTRY = base.CharField(label="Ülke", table="LG_SHIPINFO",field="COUNTRY",max_length=21,required=False)
	POSTAL_CODE = base.CharField(label="Posta kodu", table="LG_SHIPINFO",field="POSTCODE",max_length=11,required=False)
	TELEPHONE1 = base.CharField(label="Telefon1", table="LG_SHIPINFO",field="TELNRS1",max_length=16,required=False)
	TELEPHONE2 = base.CharField(label="Telefon2", table="LG_SHIPINFO",field="TELNRS2",max_length=16,required=False)
	FAX = base.CharField(label="Faks", table="LG_SHIPINFO",field="FAXNR",max_length=16,required=False)
	TAX_NR = base.CharField(label="Vergi No", table="LG_SHIPINFO",field="TAXNR",max_length=16,required=False)
	TAX_OFFICE = base.CharField(label="Vergi Dairesi", table="LG_SHIPINFO",field="TAXOFFICE",max_length=16,required=False)
	TRADING_GRP = base.CharField(label="Ticari İşlem Grubu", table="LG_SHIPINFO",field="TRADINGGRP",max_length=17,required=False)
	VAT_NR = base.CharField(label="KDV No", table="LG_SHIPINFO",field="VATNR",max_length=33,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_SHIPINFO",field="SITEID",required=False)
	EMAIL_ADDR = base.CharField(label="E-posta adresi", table='LG_SHIPINFO',field='EMAILADDR',max_length=51,required=False)
	INCHANGE = base.CharField(label="?",table="LG_SHIPINFO",field="INCHARGE",max_length=21,required=False)
