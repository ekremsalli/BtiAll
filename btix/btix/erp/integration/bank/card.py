"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class BankCard(base.Serializer):
	"""
		Banka kartları
	"""
	class Meta:
		XML_ROOT = 'BANKS'
		XML_SUBROOT = 'BANK'
		DATA_OBJECT = 'doBank'
		REST_ENDPOINT = 'banks'
		RELATED_TABLE = 'LG_BNCARD'

	RECORD_STATUS = base.IntegerField(label="Kayıt statüsü", table="LG_BNCARD",field="ACTIVE",required=False)
	CODE = base.CharField(label="Kod", table="LG_BNCARD",field="CODE",max_length=7,required=True)
	TITLE = base.CharField(label="Açıklama", table="LG_BNCARD",field="DEFINITION_",max_length=51,required=False)
	DIVISION = base.CharField(label="Şube", table="LG_BNCARD",field="BRANCH",max_length=21,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_BNCARD",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_BNCARD",field="CYPHCODE",max_length=11,required=False)
	DIVISION_ID = base.CharField(label="Şube no", table="LG_BNCARD",field="BRANCHNO",max_length=17,required=False)
	ADDRESS1 = base.CharField(label="Adres 1", table="LG_BNCARD",field="ADDR1",max_length=51,required=False)
	ADDRESS2 = base.CharField(label="Adres 2", table="LG_BNCARD",field="ADDR2",max_length=51,required=False)
	DISTRICT = base.CharField(label="Semt", table="LG_CLCARD",field="DISTRICT",max_length=51,required=False)
	TOWN = base.CharField(label="İlçe", table="LG_CLCARD",field="TOWN",max_length=51,required=False)
	CITY = base.CharField(label="Şehir", table="LG_BNCARD",field="CITY",max_length=21,required=False)
	COUNTRY_CODE = base.CharField(label="Ülke Kodu", table="LG_DISTORDLINE",field="COUNTRYCODE",max_length=13,required=False)
	COUNTRY = base.CharField(label="Ülke", table="LG_BNCARD",field="COUNTRY",max_length=21,required=False)
	POSTAL_CODE = base.CharField(label="Posta kodu", table="LG_BNCARD",field="POSTCODE",max_length=11,required=False)
	TELEPHONE1 = base.CharField(label="Telefon 1", table="LG_BNCARD",field="TELNRS1",max_length=16,required=False)
	TELEPHONE2 = base.CharField(label="Telefon 2", table="LG_BNCARD",field="TELNRS2",max_length=16,required=False)
	FAX = base.CharField(label="Faks", table="LG_BNCARD",field="FAXNR",max_length=16,required=False)
	CONTACT = base.CharField(label="İlgili", table="LG_BNCARD",field="INCHARGE",max_length=21,required=False)
	E_MAIL = base.CharField(label="E-mail", table="LG_BNCARD",field="EMAILADDR",max_length=31,required=False)
	WEB_URL = base.CharField(label="Web", table="LG_BNCARD",field="WEBADDR",max_length=41,required=False)
	DATA_SITEID = base.IntegerField(label="Bilgi veri merkezi", table="LG_BNCARD",field="SITEID",required=False)