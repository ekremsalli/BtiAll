"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class MaterialAlternates(base.Serializer):
	"""
		Malzeme kartı
	"""
	class Meta:
		XML_ROOT = 'ITEM_ALTERNATES'
		XML_SUBROOT = 'ITEM'
		DATA_OBJECT = 'doItemAlters'
		REST_ENDPOINT = 'itemAlternatives'
		RELATED_TABLE = 'LG_ITEMSUBS'

	LINE_NO = base.IntegerField(label="Satır Sayısı", table="LG_ITEMSUBS",field="LINENO_",required=False)
	PRIORITY = base.IntegerField(label="Öncelik", table="LG_ITEMSUBS",field="PRIORITY",required=False)
	CONV_FACT1 = base.FloatField(label="Çevrim Katsayısı", table="LG_ITEMSUBS",field="CONVFACT1",required=False)
	CONV_FACT2 = base.FloatField(label="Çevrim Katsayısı", table="LG_ITEMSUBS",field="CONVFACT2",required=False)
	MAX_QUANTITY = base.FloatField(label="Azami miktar", table="LG_ITEMSUBS",field="MAXQUANTITY",required=False)
	MIN_QUANTITY = base.FloatField(label="Asgari miktar", table="LG_ITEMSUBS",field="MINQUANTITY",required=False)
	BEG_DATE = base.IntegerField(label="Başlangıç tarihi", table="LG_ITEMSUBS",field="BEGDATE",required=False)
	END_DATE = base.IntegerField(label="Bitiş tarihi", table="LG_ITEMSUBS",field="ENDDATE",required=False)
	SUBS_CODE = base.CharField(label="Malzeme kart kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	MAIN_CODE = base.CharField(label="Malzeme kart kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_ITEMS",field="SITEID",required=False)
