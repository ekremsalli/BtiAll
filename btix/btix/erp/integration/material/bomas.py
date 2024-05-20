"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class Bomas(base.Serializer):
	"""
		Malzeme - ürün reçetesi ilişkisi
	"""
	class Meta:
		XML_ROOT = 'ITEM_BOM_ASGN'
		XML_SUBROOT = 'ITEM_BOM_ASGN'
		DATA_OBJECT = 'doItemBOM'
		REST_ENDPOINT = 'itemBoms'
		RELATED_TABLE = 'LG_ITMBOMAS'

	REL_TYPE = base.IntegerField(label="Ürün reçetesi malzeme ilişkisi türü", table="LG_ITMBOMAS",field="RELTYPE",required=False)
	FACTORY_NR = base.IntegerField(label="Fabrika numarası", table="LG_ITMBOMAS",field="FACTORYNR",required=False)
	PRIORITY = base.IntegerField(label="Öncelik", table="LG_ITMBOMAS",field="PRIORITY",required=False)
	LINE_NR = base.IntegerField(label="Satır numarası", table="LG_ITMBOMAS",field="LINENR",required=False)
	MAX_QUANTITY = base.FloatField(label="Azami miktar", table="LG_ITMBOMAS",field="MAXQUANTITY",required=False)
	MIN_QUANTITY = base.FloatField(label="Asgari miktar", table="LG_ITMBOMAS",field="MINQUANTITY",required=False)
	BEG_DATE = base.IntegerField(label="Başlangıç Tarihi", table="LG_ITMBOMAS",field="BEGDATE",required=False)
	STD_COST_FLG = base.IntegerField(label="Bitiş Tarihi", table="LG_ITMBOMAS",field="STDCOSTFLAG",min_value=0, max_value=1,required=False)
	BOM_CODE = base.CharField(label="Ürün Reçetesi Kodu", table="LG_BOMASTER",field="CODE",max_length=25,required=True)
	ITEM_CODE = base.CharField(label="Stok kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	FOR_MRP = base.IntegerField(label="MRP için kullanılacak (1- Evet, 0- Hayır)", table="LG_ITMBOMAS",field="FORMRP",min_value=0, max_value=1,required=False)