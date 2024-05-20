"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class WorkStatGroupWS(base.BaseSerialiazer):
	CODE = base.CharField(label="Değer kodu", table="LG_WORKSTAT",field="CODE",max_length=25,required=True)
	DEFINITION = base.CharField(label="Değer açıklaması", table="LG_WORKSTAT",field="NAME",max_length=51,required=False)


class WorkStatGroup(base.Serializer):
	"""
		İş istasyonu grupları
	"""
	class Meta:
		XML_ROOT = 'WSTGROUPS'
		XML_SUBROOT = 'WSTGROUP'
		DATA_OBJECT = 'doWstGroup'
		REST_ENDPOINT = 'workstationGroups'

	CODE = base.CharField(label="İş İstasyonu grup kodu", table="LG_WSGRPF",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="İş İstasyonu grup açıklaması", table="LG_WSGRPF",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_WSGRPF",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki kodu", table="LG_WSGRPF",field="CYPHCODE",max_length=11,required=False)
	FACTORYNR = base.IntegerField(label="Fabrika numarası", table="LG_WSGRPF",field="FACTORYNR",required=False)
	APPROVED = base.IntegerField(label="Onay bilgisi", table="LG_WSGRPF",field="APPROVED",min_value=0, max_value=1,required=False)
	OPERATION_TIME = base.FloatField(label="Günlük çalışma saati", table="LG_WSGRPF",field="OPERATIONTIME",required=False)
	HOURLY_STD_COST = base.FloatField(label="Saatlik maliyet", table="LG_WSGRPF",field="HOURLYSTDCOST",required=False)
	HOURLY_STDRP_COST = base.FloatField(label="Saatlik maliyet (Raporlama dövizi)", table="LG_WSGRPF",field="HOURLYSTDRPCOST",required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_WSGRPF",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_WSGRPF",field="SITEID",required=False)
	WFSTATUS = base.IntegerField(label="Kullanım dışı", table="LG_WSGRPF",field="NOTINUSE",required=False)

	# subs
	WORSTATIONS = base.serializers.ListSerializer(child=WorkStatGroupWS())