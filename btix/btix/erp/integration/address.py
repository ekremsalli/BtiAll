"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base


class Country(base.Serializer):
	"""
		Ülkeler
	"""
	class Meta:
		XML_ROOT = 'COUNTRIES'
		XML_SUBROOT = 'COUNTRY'
		DATA_OBJECT = 'doCountry'
		REST_ENDPOINT = 'countries'
		RELATED_TABLE = 'L_COUNTRY'

	CODE = base.CharField(label="Ülke Kodu", table="L_COUNTRY",field="CODE",max_length=13,required=True)
	NAME = base.CharField(label="Ülke Ad", table="L_COUNTRY",field="NAME",max_length=41,required=True)

class City(base.Serializer):
	"""
		İller
	"""
	class Meta:
		XML_ROOT = 'CITIES'
		XML_SUBROOT = 'CITY'
		DATA_OBJECT = 'doCity'
		REST_ENDPOINT = 'cities'
		RELATED_TABLE = 'L_CITY'

	CODE = base.CharField(label="İl Kodu", table="L_CITY",field="CODE",max_length=13,required=True)
	NAME = base.CharField(label="İl Adı", table="L_CITY",field="NAME",max_length=41,required=True)
	COUNTRYCODE = base.CharField(label="Ülke Kodu", table="L_COUNTRY",field="CODE",max_length=13,required=True)

class District(base.Serializer):
	"""
		Semt
	"""
	class Meta:
		XML_ROOT = 'DISTRICTS'
		XML_SUBROOT = 'DISTRICT'
		DATA_OBJECT = 'doDistrict'
		REST_ENDPOINT = 'districts'
		RELATED_TABLE = 'L_DISTRICT'

	CODE = base.CharField(label="Semt Kodu", table="L_DISTRICT",field="CODE",max_length=13,required=True)
	NAME = base.CharField(label="Semt Ad", table="L_DISTRICT",field="NAME",max_length=51,required=True)
	COUNTRYCODE = base.CharField(label="Ülke Kodu", table="L_COUNTRY",field="CODE",max_length=13,required=False)
	CITYCODE = base.CharField(label="İl Kodu", table="L_CITY",field="CODE",max_length=13,required=False)
	TOWNCODE = base.CharField(label="İlçe Kodu", table="L_TOWN",field="CODE",max_length=13,required=False)

class Town(base.Serializer):
	"""
		İlçe
	"""
	class Meta:
		XML_ROOT = 'TOWNS'
		XML_SUBROOT = 'TOWN'
		DATA_OBJECT = 'doTown'
		REST_ENDPOINT = 'towns'
		RELATED_TABLE = 'L_TOWN'

	CODE = base.CharField(label="İlçe Kodu", table="L_TOWN",field="CODE",max_length=13,required=False)
	NAME = base.CharField(label="İlçe Ad", table="L_TOWN",field="NAME",max_length=51,required=True)
	COUNTRYCODE = base.CharField(label="Ülke Kodu", table="L_COUNTRY",field="CODE",max_length=13,required=True)
	CITYCODE = base.CharField(label="İl Kodu", table="L_CITY",field="CODE",max_length=13,required=True)

class Postcode(base.Serializer):
	"""
		Posta kodları
	"""
	class Meta:
		XML_ROOT = 'POST_CODES'
		XML_SUBROOT = 'POSTCODE'
		DATA_OBJECT = 'doPostCode'
		REST_ENDPOINT = 'postCodes'
		RELATED_TABLE = 'L_POSTCODE'

	CODE = base.CharField(label="Posta Kodu", table="L_POSTCODE",field="POSTCODE",max_length=21,required=True)
	COUNTRYCODE = base.CharField(label="Ülke Kodu", table="L_COUNTRY",field="CODE",max_length=33,required=True)
	CITYCODE = base.CharField(label="İl Kodu", table="L_CITY",field="CODE",max_length=33,required=True)
