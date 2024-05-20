"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class PromotionBundles(base.BaseSerialiazer):
	ITEM_CODE = base.CharField(label="Malzeme kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	FORMULA = base.CharField(label="Formül", table="LG_PRCARDS",field="PROMLINES_FORMULA",max_length=81,required=False)
	PRICE = base.FloatField(label="Birim fiyat", table="LG_PRCARDS",field="PROMLINES_PRICE",required=False)
	ROUND_BASE = base.FloatField(label="Yuvarlama tabanı", table="LG_PRCARDS",field="PROMLINES_RNDVAL",required=False)
	UNIT_CODE = base.CharField(label="Birim kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	GL_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)


class BasePromotion(base.Serializer):
	CODE = base.CharField(label="Hizmet kodu", table="LG_PRCARDS",field="CODE",max_length=17,required=True)
	DESCRIPTION = base.CharField(label="Hizmet açıklaması", table="LG_PRCARDS",field="DEFINITION_",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_PRCARDS",field="SPECODE",max_length=11,required=False)
	AUTHOR_CODE = base.CharField(label="Yetki Kodu", table="LG_PRCARDS",field="CYPHCODE",max_length=11,required=False)
	ITEM_CODE = base.CharField(label="Malzeme kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	STOCKREF = base.IntegerField(label="Stok referansı", table="LG_PRCARDS",field="STOCKREF",required=False)
	MATITEM_TYPE = base.IntegerField(label="Malzeme türü", table="LG_PRCARDS",field="MTRLTYPE",required=False)
	DATE_STARTED = base.IntegerField(label="Başlama tarihi", table="LG_PRCARDS",field="BEGDATE",required=False)
	DATE_ENDED = base.IntegerField(label="Bitiş tarihi", table="LG_PRCARDS",field="ENDDATE",required=False)
	PRICE = base.FloatField(label="Birim fiyat", table="LG_PRCARDS",field="PRICE",required=False)
	MODUL_ID = base.IntegerField(label="Modül numarası", table="LG_PRCARDS",field="FICHEMODUL",required=False)
	MATRL_TRANS = base.IntegerField(label="Malzeme hareketleri", table="LG_PRCARDS",field="FICHETYPES1",required=False)
	PURCH_TRANS = base.CharField(label="Satınalma hareketleri", table="LG_PRCARDS",field="FICHETYPES2",max_length=2,required=False)
	SALES_TRANS = base.IntegerField(label="Satış hareketleri", table="LG_PRCARDS",field="FICHETYPES3",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_PRCARDS",field="SITEID",required=False)

	# subs
	BUNDLES = base.serializers.ListSerializer(child=PromotionBundles())

class PurchasePromotion(BasePromotion):
	"""
		Alış promosyon kartları
	"""
	class Meta:
		XML_ROOT = "PURCHASE_PROMOTIONS"
		XML_SUBROOT = "PURCHASE_PROMOTION"
		DATA_OBJECT = "doPurchProm"
		REST_ENDPOINT = "purchasePromotions"
		RELATED_TABLE = 'LG_PRCARDS'

class SalesPromotion(BasePromotion):
	"""
		Satış promosyon kartları
	"""
	class Meta:
		XML_ROOT = "SALES_PROMOTIONS"
		XML_SUBROOT = "SALE_PROMOTIONS"
		DATA_OBJECT = "doSalesProm"
		REST_ENDPOINT = "salesPromotions"
		RELATED_TABLE = 'LG_PRCARDS'
