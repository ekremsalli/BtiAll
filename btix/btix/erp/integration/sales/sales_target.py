"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class SalesTarget(base.Serializer):
	"""
		Satış hedefleri
	"""
	class Meta:
		XML_ROOT = "CST_SALES_TARGET"
		XML_SUBROOT = "CST_SALES_TARGET"
		DATA_OBJECT = "doSlsTarget"
		REST_ENDPOINT = "salesmanDestinations"
		RELATED_TABLE = 'LG_TARGETS'

	CODE = base.CharField(label="Hedef Kodu", table="LG_TARGETS",field="CODE",max_length=17,required=False)
	DEFINITION = base.CharField(label="Hedef Açıklaması", table="LG_TARGETS",field="DEFINITION_",max_length=51,required=False)
	TYP = base.IntegerField(label="Hedef Türü", table="LG_TARGETS",field="TYP",min_value=0, max_value=1,required=False)
	BEG_DATE = base.IntegerField(label="Başlangıç Tarihi", table="LG_TARGETS",field="BEGDATE",required=False)
	END_DATE = base.IntegerField(label="Bitiş Tarihi", table="LG_TARGETS",field="ENDDATE",required=False)
	ST_CODE = base.CharField(label="Malzeme Kodu", table="LG_TARGETS",field="STCODE",max_length=25,required=False)
	ST_GROUP_CODE = base.CharField(label="Malzeme Grup Kodu", table="LG_TARGETS",field="STGROUPCODE",max_length=17,required=False)
	TARGET_SALE_AMOUNT = base.FloatField(label="Hedef Satış Miktarı", table="LG_TARGETS",field="TARGETSALEAMOUNT",required=False)
	SALE_AMOUNT_LIMIT = base.FloatField(label="Satış miktarı limiti", table="LG_TARGETS",field="SALEAMOUNTLIMIT",required=False)
	NET_SALE_AMOUNT = base.FloatField(label="Net Satış Miktarı", table="LG_TARGETS",field="NETSALEAMOUNT",required=False)
	SALE_DISCOUNT_LIMIT = base.FloatField(label="Satış indirimleri sınırı", table="LG_TARGETS",field="SALEDISCOUNTLIMIT",required=False)
	SALE_EXPENSE_LIMIT = base.FloatField(label="Satış masrafları sınırı", table="LG_TARGETS",field="SALEEXPENSELIMIT",required=False)
	SALESMAN_CODE = base.CharField(label="Satış Elemanı Kodu", table="LG_SLSMAN",field="CODE",max_length=25,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_TARGETS",field="SITEID",required=False)
