"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class ServiceGlLinks(base.BaseSerialiazer):
	INFO_TYPE = base.IntegerField(label="Bilgi türü", table="LG_CRDACREF",field="TYP",required=False)
	GLACC_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)

class ServiceUnits(base.BaseSerialiazer):
	UNIT_CODE = base.CharField(label="Birim kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	PRIORITY = base.IntegerField(label="Öncelik", table="LG_SRVUNITA",field="PRIORITY",required=False)

class ServiceWhParams(base.BaseSerialiazer):
	WH_NUMBER = base.IntegerField(label="Ambar numarası", table="LG_INVDEF",field="INVENNO",required=False)
	LEAD_TIME = base.IntegerField(label="Teslim/Temin Süresi", table="LG_SUPPASGN",field="LEADTIME",required=False)


class BaseService(base.Serializer):
	CODE = base.CharField(label="Hizmet kodu", table="LG_SRVCARD",field="CODE",max_length=17,required=True)
	DESCRIPTION = base.CharField(label="Hizmet açıklaması", table="1",field="DEFINITION_",max_length=5,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_SRVCARD",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_SRVCARD",field="CYPHCODE",max_length=11,required=False)
	VAT_PERC = base.FloatField(label="KDV oranı", table="LG_SRVCARD",field="VAT",required=False)
	PAYMENT_CODE = base.CharField(label="Ödeme Plan Kodu", table="LG_PAYPLANS",field="CODE",max_length=17,required=False)
	UNITSET_CODE = base.CharField(label="Birim seti kodu", table="LG_UNITSETF",field="CODE",max_length=25,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_SRVCARD",field="SITEID",required=False)

	# subs
	WH_PARAMS = base.serializers.ListSerializer(child=ServiceWhParams())
	UNITS = base.serializers.ListSerializer(child=ServiceUnits())
	GL_LINKS = base.serializers.ListSerializer(child=ServiceGlLinks())

class SalesService(BaseService):
	"""
		Verilen hizmet kartı
	"""
	class Meta:
		XML_ROOT = "SALES_SERVICES"
		XML_SUBROOT = "SALES_SERVICE"
		DATA_OBJECT = "doSalesService"
		REST_ENDPOINT = "soldServices"
		RELATED_TABLE = 'LG_SRVCARD'

class PurchaseService(BaseService):
	"""
		Alınan hizmet kartı
	"""
	class Meta:
		XML_ROOT = "PURCHASE_SERVICES"
		XML_SUBROOT = "PURCHASE_SERVICE"
		DATA_OBJECT = "doPurchService"
		REST_ENDPOINT = "purchasedServices"
		RELATED_TABLE = 'LG_SRVCARD'
