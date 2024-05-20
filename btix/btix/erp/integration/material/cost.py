"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class MaterialCost(base.Serializer):
	"""
		Standart malzeme maliyeti
	"""
	class Meta:
		XML_ROOT = 'STD_ITM_COSTS'
		XML_SUBROOT = 'STD_ITM_COST'
		DATA_OBJECT = 'doItmStdCosts'
		REST_ENDPOINT = 'itemStandardCosts'
		RELATED_TABLE = 'LG_STDUNITCOST'

	CARDTYPE = base.IntegerField(label="Kart türü", table="LG_STDUNITCOST",field="CARDTYPE",min_value=0, max_value=1,required=True)
	FACTORYNR = base.IntegerField(label="Fabrika No", table="LG_STDUNITCOST",field="FACTORYNR",required=False)
	UNITCOST = base.FloatField(label="Birim Maliyet", table="LG_STDUNITCOST",field="UNITCOST",required=False)
	REPUNITCOST = base.FloatField(label="Raporlama dövizi birim maliyeti", table="LG_STDUNITCOST",field="REPUNITCOST",required=False)
	TRUNITCOST = base.FloatField(label="İşlem dövizi birim maliyeti", table="LG_STDUNITCOST",field="TRUNITCOST",required=False)
	TRCURR = base.IntegerField(label="İşlem dövizi türü", table="LG_STDUNITCOST",field="TRCURR",min_value=0, max_value=1,required=False)
	TRRATE = base.FloatField(label="İşlem döviz kuru", table="LG_STDUNITCOST",field="TRRATE",required=False)
	REPORTRATE = base.FloatField(label="Raporlama döviz kuru", table="LG_STDUNITCOST",field="REPORTRATE",required=False)
	LINENO = base.IntegerField(label="Satır numarası", table="LG_STDUNITCOST",field="LINENO_",required=False)
	PERIODCODE = base.CharField(label="Kod", table="LG_STDCOSTPERIOD",field="CODE",max_length=25,required=True)
	PERIODNAME = base.CharField(label="Açıklama", table="LG_STDCOSTPERIOD",field="NAME",max_length=51,required=False)
	CARD_CODE = base.CharField(label="Malzeme Kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_ITEMS",field="SITEID",required=False)