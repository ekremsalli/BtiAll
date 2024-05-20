"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class ProductionRoutingLinesPrevOprList(base.BaseSerialiazer):
	OVERLAPPER = base.FloatField(label="Örtüşme yüzdesi", table="LG_PRVOPASG",field="OVERLAPPER",required=False)
	OPR_CODE = base.CharField(label="Operasyon kodu", table="LG_OPERTION",field="CODE",max_length=25,required=False)

class ProductionRoutingLines(base.BaseSerialiazer):
	LINE_NO = base.IntegerField(label="Satır numarası", table="LG_RTNGLINE",field="LINENO_",required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_RTNGLINE",field="SPECODE",max_length=11,required=False)
	COST_RELATED = base.IntegerField(label="Cost Related", table="LG_RTNGLINE",field="COSTRELATED",min_value=0, max_value=1,required=False)
	PLAN_RELATED = base.IntegerField(label="Planning Related", table="LG_RTNGLINE",field="PLANRELATED",min_value=0, max_value=1,required=False)
	LINE_EXP = base.CharField(label="Satır açıklaması", table="LG_RTNGLINE",field="LINEEXP",max_length=51,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_RTNGLINE",field="SITEID",required=False)
	WF_STATUS = base.IntegerField(label="Kullanım Dışı", table="LG_RTNGLINE",field="WFSTATUS",required=False)
	OPR_CODE = base.CharField(label="Operasyon kodu", table="LG_OPERTION",field="CODE",max_length=25,required=False)
	OPR_NAME = base.CharField(label="Operasyon açıklaması", table="LG_OPERTION",field="NAME",max_length=51,required=False)
	# subs
	PREV_OPR_LIST = base.serializers.ListSerializer(child=ProductionRoutingLinesPrevOprList())


class ProductionRouting(base.Serializer):
	"""
		Rotalar
	"""
	class Meta:
		XML_ROOT = 'ROUTINGS'
		XML_SUBROOT = 'ROUTING'
		DATA_OBJECT = 'doRouting'
		REST_ENDPOINT = 'productionRoutes'
		RELATED_TABLE = 'LG_ROUTING'

	CODE = base.CharField(label="Üretim rota kodu", table="LG_ROUTING",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Üretim rota açıklaması", table="LG_ROUTING",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_ROUTING",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki kodu", table="LG_ROUTING",field="CYPHCODE",max_length=11,required=False)
	APPROVED = base.IntegerField(label="Onay bilgisi", table="LG_ROUTING",field="APPROVED",min_value=0, max_value=1,required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_ROUTING",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_ROUTING",field="SITEID",required=False)
	WF_STATUS = base.IntegerField(label="Kullanım dışı", table="LG_ROUTING",field="WFSTATUS",required=False)

	# subs
	LINES = base.serializers.ListSerializer(child=ProductionRoutingLines())

