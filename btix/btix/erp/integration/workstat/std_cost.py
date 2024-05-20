"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class WorkStatStdCost(base.Serializer):
	"""
		İş istasyonu standart maliyetleri
	"""
	class Meta:
		XML_ROOT = 'STD_WST_COSTS'
		XML_SUBROOT = 'COST'
		DATA_OBJECT = 'doWStdCosts'
		REST_ENDPOINT = 'workstationStandardCosts'

	CARDTYPE = base.IntegerField(label="Kart Türü", table="LG_STDUNITCOST",field="CARDTYPE",min_value=0, max_value=1,required=True)
	FACTORYNR = base.IntegerField(label="Fabrika No", table="LG_STDUNITCOST",field="FACTORYNR",required=False)
	UNITCOST = base.FloatField(label="Birim Maliyeti", table="LG_STDUNITCOST",field="UNITCOST",required=False)
	REPUNITCOST = base.FloatField(label="Raporlama Dövizi Birim Maliyeti", table="LG_STDUNITCOST",field="REPUNITCOST",required=False)
	TRUNITCOST = base.FloatField(label="İşlem Dövizi Birim Maliyeti", table="LG_STDUNITCOST",field="TRUNITCOST",required=False)
	TRCURR = base.IntegerField(label="İşlem Dövizi Türü", table="LG_STDUNITCOST",field="TRCURR",min_value=0, max_value=1,required=False)
	TRRATE = base.FloatField(label="İşlem Dövizi Kuru", table="LG_STDUNITCOST",field="TRRATE",required=False)
	REPORTRATE = base.FloatField(label="Raporlama Dövizi Kuru", table="LG_STDUNITCOST",field="REPORTRATE",required=False)
	LINENO = base.IntegerField(label="Satır numarası", table="LG_STDUNITCOST",field="LINENO",required=False)
	PERIODCODE = base.CharField(label="Kod", table="LG_STDCOSTPERIOD",field="CODE",max_length=25,required=True)
	CARD_CODE = base.CharField(label="Kod", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_STDUNITCOST",field="SITEID",required=False)


