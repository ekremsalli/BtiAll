"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class BaseServicePrice(base.Serializer):
	OWNER_CODE = base.CharField(label="Kullanıcı Kodu", table="LG_SRVCARD",field="CODE",max_length=17,required=True)
	ARP_CODE = base.CharField(label="Cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)
	ARP_AUXCODE = base.CharField(label="Cari hesap özel kodu", table="LG_CLCARD",field="SPECODE",max_length=11,required=False)
	PAYMENT_CODE = base.CharField(label="Ödeme plan kodu", table="LG_PAYPLANS",field="CODE",max_length=17,required=False)
	PRICE = base.FloatField(label="Birim fiyat", table="LG_PRCLIST",field="PRICE",required=False)
	UNIT_CODE = base.CharField(label="Birim seti kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	VAT_INCL = base.IntegerField(label="KDV dahil/hariç", table="LG_PRCLIST",field="INCVAT",min_value=0, max_value=1,required=False)
	CURRENCY = base.IntegerField(label="Döviz türü", table="LG_PRCLIST",field="CURRENCY",min_value=0, max_value=1,required=False)
	PRIORITY = base.IntegerField(label="Öncelik", table="LG_PRCLIST",field="PRIORITY",min_value=0, max_value=1,required=False)
	MTRL_TYPE = base.IntegerField(label="Malzeme türü", table="LG_PRCLIST",field="MTRLTYPE",required=False)
	LEAD_TIME = base.IntegerField(label="Temin tarihi", table="LG_PRCLIST",field="LEADTIME",required=False)
	DATE_STARTED = base.IntegerField(label="Başlangıç tarihi", table="LG_PRCLIST",field="BEGDATE",required=False)
	DATE_ENDED = base.IntegerField(label="Bitiş tarihi", table="LG_PRCLIST",field="ENDDATE",required=False)
	CONDITION = base.CharField(label="Koşul", table="LG_PRCLIST",field="CONDITION",max_length=81,required=False)
	SHIPMENT_TYPE = base.CharField(label="Teslimat türü", table="LG_PRCLIST",field="SHIPTYPE",max_length=5,required=False)
	SPECIALIZED = base.IntegerField(label="Özellikler", table="LG_PRCLIST",field="SPECIALIZED",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_PRCLIST",field="SITEID",required=False)


class ServiceSalesPrice(BaseServicePrice):
	"""
		Hizmet satış fiyatı
	"""
	class Meta:
		XML_ROOT = "SERVICE_SALES_PRICE"
		XML_SUBROOT = "SERVICE_SALES_PRICE"
		DATA_OBJECT = "doSalesPriceService"
		REST_ENDPOINT = "salesServicePrices"
		RELATED_TABLE = "LG_PRCLIST"


class ServicePurchasePrice(BaseServicePrice):
	"""
		Hizmet alım fiyatı
	"""
	class Meta:
		XML_ROOT = "SERVICE_PURCHASE_PRICE"
		XML_SUBROOT = "SERVICE_PURCHASE_PRICE"
		DATA_OBJECT = "doPurchPriceService"
		REST_ENDPOINT = "purchasedServicePrices"
		RELATED_TABLE = "LG_PRCLIST"
