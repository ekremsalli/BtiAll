"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class SalesRouteLines(base.BaseSerialiazer):
	LINE_NO = base.IntegerField(label="Satır Numarası", table="LG_ROUTETRS",field="LINENO_",required=False)
	CL_CODE = base.CharField(label="Cari Hesap Kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)
	CL_DEFINITION = base.CharField(label="Cari Hesap Ünvanı", table="LG_CLCARD",field="DEFINITION_",max_length=51,required=False)
	SALESMAN_CODE = base.CharField(label="Satış Elemanı Kodu", table="LG_SLSMAN",field="CODE",max_length=25,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_ROUTE",field="SITEID",required=False)


class SalesRoute(base.Serializer):
	"""
		Satış rotaları
	"""
	class Meta:
		XML_ROOT = "CST_SALES_ROUTES"
		XML_SUBROOT = "CST_SALES_ROUTE"
		DATA_OBJECT = "doSlsRoute"
		REST_ENDPOINT = "salesmanRoutes"
		RELATED_TABLE = 'LG_ROUTE'

	CODE = base.CharField(label="Rota Kodu", table="LG_ROUTE",field="CODE",max_length=25,required=False)
	DEFINITION = base.CharField(label="Rota Açıklaması", table="LG_ROUTE",field="DEFINITION_",max_length=51,required=False)
	SPECODE = base.CharField(label="Özel Kod", table="LG_ROUTE",field="SPECODE",max_length=11,required=False)
	CYPHCODE = base.CharField(label="Yetki Kodu", table="LG_ROUTE",field="CYPHCODE",max_length=11,required=False)
	STATUS = base.IntegerField(label="Statü", table="LG_ROUTE",field="STATUS",min_value=0, max_value=1,required=False)
	PERIOD = base.CharField(label="Dönem", table="LG_ROUTE",field="PERIOD",max_length=16,required=False)

	# subs
	ROUTE_LINES = base.serializers.ListSerializer(child=SalesRouteLines())
