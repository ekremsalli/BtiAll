"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base


class StockCodes(base.Serializer):
	"""
		Stok yeri kodları
	"""
	class Meta:
		XML_ROOT = 'LOC_CODES'
		XML_SUBROOT = 'CODES'
		DATA_OBJECT = 'doLocCodes'
		REST_ENDPOINT = 'locationCodes'
		RELATED_TABLE = 'LG_LOCATION'

	INVENNR = base.IntegerField(label="Ambar Numarası", table="LG_LOCATION",field="INVENNR",required=True)
	CODE = base.CharField(label="Stok Yeri Kodu", table="LG_LOCATION",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Stok Yeri Açıklaması", table="LG_LOCATION",field="NAME",max_length=51,required=False)
	WIDTH = base.FloatField(label="Raf Eni", table="LG_LOCATION",field="WIDTH",required=False)
	LENGTH = base.FloatField(label="Raf Uzunluğu", table="LG_LOCATION",field="LENGTH",required=False)
	HEIGHT = base.FloatField(label="Raf Yüksekliği", table="LG_LOCATION",field="HEIGHT",required=False)
	MIN_LEVEL = base.FloatField(label="Raf asgari stok seviyesi", table="LG_LOCATION",field="MINLEVEL",required=False)
	MAX_LEVEL = base.FloatField(label="Raf azami stok seviyesi", table="LG_LOCATION",field="MAXLEVEL",required=False)
	SHELF_TYPE = base.IntegerField(label="Raf türü sınıfları", table="LG_LOCATION",field="SHELF_TYPE",required=False)
	CONTENT_TYPE = base.IntegerField(label="Type of Shelf Contents", table="LG_LOCATION",field="CONTENTTYPE",required=False)
	PRIORITY = base.IntegerField(label="Priority for the Same Type of Items", table="LG_LOCATION",field="PRIORITY",required=False)
	IS_EURO_PALETTE = base.IntegerField(label="Is Shelf Content EUROPALETTE (1- Yes, 0- No)", table="LG_LOCATION",field="ISEUROPALETTE",min_value=0, max_value=1,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_LOCATION",field="SITEID",required=False)
	WF_STATUS = base.IntegerField(label="Kullanım Dışı", table="LG_LOCATION",field="WFSTATUS",required=False)
	WIDTH_CODE = base.CharField(label="Genişlik Kodu", table="LG_UNITSETL",field="WIDTH_CODE",max_length=8,required=False)
	LENGTH_CODE = base.CharField(label="Uzunluk kodu", table="LG_UNITSETL",field="LENGTH_CODE",max_length=8,required=False)
	HEIGHT_CODE = base.CharField(label="Yükseklik kodu", table="LG_UNITSETL",field="HEIGHT_CODE",max_length=8,required=False)
