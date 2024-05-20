"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base


class BaseExpense(base.Serializer):
	CODE = base.CharField(label="Masraf kodu", table="LG_DECARDS",field="CODE",max_length=17,required=True)
	DESCRIPTION = base.CharField(label="Masraf açıklaması", table="LG_DECARDS",field="DEFINITION_",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_DECARDS",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_DECARDS",field="CYPHCODE",max_length=11,required=False)
	FORMULA = base.CharField(label="Formül", table="LG_DECARDS",field="FORMULA",max_length=251,required=False)
	ROUND_BASE = base.FloatField(label="Yuvarlama tabanı", table="LG_DECARDS",field="RNDVAL",required=False)
	VAT_PERC = base.FloatField(label="KDV oranı", table="LG_DECARDS",field="VAT",required=False)
	UNIT = base.CharField(label="Birim", table="LG_DECARDS",field="UNITSTR",max_length=5,required=False)
	PROD_STATUS = base.IntegerField(label="Üretim durumu", table="LG_DECARDS",field="LPRODSTAT",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_DECARDS",field="SITEID",required=False)
	GL_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)

class SalesExpense(BaseExpense):
	"""
		Satış masraf kartı
	"""
	class Meta:
		XML_ROOT = "SALES_EXPENSES"
		XML_SUBROOT = "EXPENSE"
		DATA_OBJECT = "doSalesExpn"
		REST_ENDPOINT = "salesExpenses"
		RELATED_TABLE = 'LG_DECARDS'

class PurchaseExpense(BaseExpense):
	"""
		Alış masraf kartı
	"""
	class Meta:
		XML_ROOT = "PURCHASE_EXPENSES"
		XML_SUBROOT = "EXPENSE"
		DATA_OBJECT = "doPurchExpn"
		REST_ENDPOINT = "purchaseExpenses"
		RELATED_TABLE = 'LG_DECARDS'
