"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class BomCost(base.Serializer):
	"""
		Standart reçete maliyetleri
	"""
	class Meta:
		XML_ROOT = 'STD_BOM_COSTS'
		XML_SUBROOT = 'STD_BOM_COST'
		DATA_OBJECT = 'doStdBOMCosts'
		REST_ENDPOINT = 'BomStandardCosts'
		RELATED_TABLE = 'LG_STDBOMCOST'

	FACTORYNR = base.IntegerField(label="Fabrika Numarası", table="LG_STDBOMCOST",field="FACTORYNR",required=False)
	REPROTRATE = base.FloatField(label="Raporlama döviz kuru", table="LG_STDBOMCOST",field="REPORTRATE",required=False)
	CRTYPE = base.IntegerField(label="Kullanım dışı", table="LG_STDBOMCOST",field="CRTYPE",min_value=0, max_value=1,required=False)
	TRCURRDATE = base.FloatField(label="Kullanım dışı", table="LG_STDBOMCOST",field="TRCURRDATE",required=False)
	STDMTRCOSTLOCAL = base.FloatField(label="Standart Malzeme Maliyeti (Yerel Para Birimi)", table="LG_STDBOMCOST",field="STDMTRCOSTLOCAL",required=False)
	STDMTRCOSTTRCURR = base.FloatField(label="Standart Malzeme Maliyeti (İşlem Dövizi)", table="LG_STDBOMCOST",field="STDMTRCOSTTRCURR",required=False)
	STDMTRCOSTREPCURR = base.FloatField(label="Standart Malzeme Maliyeti (Raporlama Dövizi)", table="LG_STDBOMCOST",field="STDMTRCOSTREPCURR",required=False)
	STDLBRCOSTLOCAL = base.FloatField(label="Standart Çalışan Maliyeti (Yerel Para Birimi)", table="LG_STDBOMCOST",field="STDLBRCOSTLOCAL",required=False)
	STDLBRCOSTTRCURR = base.FloatField(label="Standart Çalışan Maliyeti (İşlem Dövizi)", table="LG_STDBOMCOST",field="STDLBRCOSTTRCURR",required=False)
	STDLBRCOSTREPCURR = base.FloatField(label="Standart Çalışan Maliyeti (Raporlama Dövizi)", table="LG_STDBOMCOST",field="STDLBRCOSTREPCURR",required=False)
	STDWSCOSTLOCAL = base.FloatField(label="Standart İş İstasyonu Maliyeti (Yerel Para Birimi)", table="LG_STDBOMCOST",field="STDWSCOSTLOCAL",required=False)
	STDWSCOSTTRCURR = base.FloatField(label="Standart İş İstasyonu Maliyeti (İşlem Dövizi)", table="LG_STDBOMCOST",field="STDWSCOSTTRCURR",required=False)
	STDWSCOSTREPCURR = base.FloatField(label="Standart İş İstasyonu Maliyeti (Raporlama Dövizi)", table="LG_STDBOMCOST",field="STDWSCOSTREPCURR",required=False)
	STDOVHDCOSTLOCAL = base.FloatField(label="Standart Genel Gider Maliyeti (Yerel Para Birimi)", table="LG_STDBOMCOST",field="STDOVHDCOSTLOCAL",required=False)
	STDOVHDCOSTTRCURR = base.FloatField(label="Standart Genel Gider Maliyeti (İşlem Dövizi)", table="LG_STDBOMCOST",field="STDOVHDCOSTTRCURR",required=False)
	STDOVHDCOSTREPCURR = base.FloatField(label="Standart Genel Gider Maliyeti (Raporlama Dövizi)", table="LG_STDBOMCOST",field="STDOVHDCOSTREPCURR",required=False)
	OVHDCOSTFORMULA = base.CharField(label="Genel Gider Maliyet Formülü", table="LG_STDBOMCOST",field="OVHDCOSTFORMULA",max_length=121,required=False)
	OVHDCOSTREPFORMULA = base.CharField(label="Genel Gider Maliyet Formülü (Yerel Para Birimi)", table="LG_STDBOMCOST",field="OVHDCOSTREPFORMULA",max_length=121,required=False)
	STDUNITCOSTLOCAL = base.FloatField(label="Standart Birim Maliyeti (Yerel Para Birimi)", table="LG_STDBOMCOST",field="STDUNITCOSTLOCAL",required=False)
	STDUNITCOSTTRCURR = base.FloatField(label="Standart Birim Maliyeti (İşlem Dövizi)", table="LG_STDBOMCOST",field="STDUNITCOSTTRCURR",required=False)
	STDUNITCOSTREPCURR = base.FloatField(label="Standart Birim Maliyeti (Raporlama Dövizi)", table="LG_STDBOMCOST",field="STDUNITCOSTREPCURR",required=False)
	PERIODCODE = base.CharField(label="Periyod Kodu", table="LG_STDCOSTPERIOD",field="CODE",max_length=25,required=True)
	PERIODNAME = base.CharField(label="Periyod Açıklaması", table="LG_STDCOSTPERIOD",field="NAME",max_length=51,required=False)
	ITEMCODE = base.CharField(label="Malzeme Kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	ITEMNAME = base.CharField(label="Malzeme Açıklaması", table="LG_ITEMS",field="NAME",max_length=51,required=False)
	BOMCODE = base.CharField(label="Reçete Kodu", table="LG_BOMASTER",field="CODE",max_length=25,required=True)
	BOMNAME = base.CharField(label="Reçete Açıklaması", table="LG_BOMASTER",field="NAME",max_length=51,required=False)
	REVCODE = base.CharField(label="Ürün Reçete Revizyon Kodu", table="LG_BOMREVSN",field="CODE",max_length=25,required=True)
	REVNAME = base.CharField(label="Ürün Reçete Revizyon Açıklaması", table="LG_BOMREVSN",field="NAME",max_length=51,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_STDBOMCOST",field="SITEID",required=False)