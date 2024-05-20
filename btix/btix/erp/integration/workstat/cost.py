"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class WorkStatCost(base.Serializer):
	"""
		İş istasyonu maliyetleri
	"""
	class Meta:
		XML_ROOT = 'WRSTCOSTS'
		XML_SUBROOT = 'WRSTCOST'
		DATA_OBJECT = 'doWrStCost'
		REST_ENDPOINT = 'workstationCosts'

	RESTYPE = base.IntegerField(label="Kaynak türü 1.Çalışan 2.İş İstasyonu", table="LG_STDCOST",field="RESTYPE",required=False)
	BEGDATE = base.IntegerField(label="Başlangıç tarihi", table="LG_STDCOST",field="BEGDATE",required=False)
	HOURLY_STD_COST = base.FloatField(label="Saatlik standart maliyet", table="LG_STDCOST",field="HOURLYSTDCOST",required=False)
	HOURLY_STDRP_COST = base.FloatField(label="Saatlik standart maliyet (Raporlama dövizi)", table="LG_STDCOST",field="HOURLYSTDRPCOST",required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_STDCOST",field="ACTIVE",required=False)
	WS_CODE = base.CharField(label="İş İstasyonu kodu", table="LG_WORKSTAT",field="CODE",max_length=25,required=True)
	WS_NAME = base.CharField(label="İş İstasyonu açıklaması", table="LG_WORKSTAT",field="NAME",max_length=51,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_WORKSTAT",field="SITEID",required=False)
