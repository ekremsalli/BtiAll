"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class WsChars(base.BaseSerialiazer):
	CCODE = base.CharField(label="İş İstasyonu Özelliği Kodu", table="LG_WSCHCODE",field="CODE",max_length=25,required=True)
	CNAME = base.CharField(label="İş İstasyonu Özelliği Açıklaması", table="LG_WSCHCODE",field="NAME",max_length=51,required=False)
	VCODE = base.CharField(label="İş İstasyonu Özellik Değeri Kodu", table="LG_WSCHVAL",field="CODE",max_length=25,required=False)

class LaborReq(base.BaseSerialiazer):
	LINE_NO = base.IntegerField(label="Satır numarası", table="LG_LABORREQ",field="LINENO_",required=False)
	GROUP = base.IntegerField(label="Çalışan grubu", table="LG_LABORREQ",field="GROUP_",required=False)
	AMOUNT = base.FloatField(label="Çalışan sayısı", table="LG_LABORREQ",field="AMOUNT",required=False)
	EMP_CODE = base.CharField(label="Çalışan Kodu", table="LG_EMPLOYEE",field="CODE",max_length=25,required=True)
	EMP_NAME = base.CharField(label="Çalışan Açıklaması", table="LG_EMPLOYEE",field="NAME",max_length=51,required=False)

class ToolReq(base.BaseSerialiazer):
	LINE_NO = base.IntegerField(label="Çalışan grubu açıklaması", table="LG_EMPGROUP",field="NAME",required=False)
	AMOUNT = base.FloatField(label="Miktar", table="LG_TOOLREQ",field="QUANTITY",required=False)
	ITEM_CODE = base.CharField(label="Satır numarası", table="LG_TOOLREQ",field="LINENO_",max_length=4,required=False)
	ITEM_NAME = base.CharField(label="Miktar", table="LG_TOOLREQ",field="AMOUNT",max_length=8,required=False)
	UNIT_SET_CODE = base.CharField(label="Malzeme kartı kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	UNIT_CODE = base.CharField(label="Malzeme kartı açıklaması", table="LG_ITEMS",field="NAME",max_length=51,required=True)


class OpertionReqs(base.BaseSerialiazer):
	LINE_NO = base.IntegerField(label="Satır numarası", table="LG_OPRTREQ",field="LINENO_",required=False)
	GROUP = base.IntegerField(label="İş İstasyonu Grup Kodu", table="LG_OPRTREQ",field="GROUP_",required=True)
	BEGDATE = base.IntegerField(label="Başlangıç Tarihi", table="LG_OPRTREQ",field="BEGDATE",required=False)
	FIXED_SETUP_TIME = base.IntegerField(label="Sabit Hazırlık Süresi", table="LG_OPRTREQ",field="FIXEDSETUPTIME",required=False)
	BATCH_QUANTITY = base.FloatField(label="İşlem partisi", table="LG_OPRTREQ",field="BATCHQUANTITY",required=False)
	RUN_TIME = base.IntegerField(label="İşlem Süresi", table="LG_OPRTREQ",field="RUNTIME",required=False)
	TRANS_BATCH_QTY = base.FloatField(label="Taşıma Partisi", table="LG_OPRTREQ",field="TRANSBATCHQTY",required=False)
	TRANS_BATCH_QTY_ = base.IntegerField(label="Taşıma Süresi", table="LG_OPRTREQ",field="TRANSBATCHTIME",required=False)
	INSP_TIME = base.IntegerField(label="Kontrol zamanı", table="LG_OPRTREQ",field="INSPTIME",required=False)
	QUE_TIME = base.IntegerField(label="Kuyruk süresi", table="LG_OPRTREQ",field="QUETIME",required=False)
	HEAD_TIME = base.IntegerField(label="Operasyon Öncesi Bekleme Süresi", table="LG_OPRTREQ",field="HEADTIME",required=False)
	TAIL_TIME = base.IntegerField(label="Operasyon Sonrası Bekleme Süresi", table="LG_OPRTREQ",field="TAILTIME",required=False)
	USAGE_PER = base.FloatField(label="Personnel In Use", table="LG_OPRTREQ",field="USAGEPER",required=False)
	EFFICIENCY = base.FloatField(label="Verim", table="LG_OPRTREQ",field="EFFICIENCY",required=False)
	PRIORITY = base.IntegerField(label="Öncelik", table="LG_OPRTREQ",field="PRIORITY",required=False)
	MIN_AMOUNT = base.FloatField(label="Asgari miktar", table="LG_OPRTREQ",field="MINAMOUNT",required=False)
	MAX_AMOUNT = base.FloatField(label="Azami miktar", table="LG_OPRTREQ",field="MAXAMOUNT",required=False)
	WS_CODE = base.CharField(label="İş İstasyonu kodu", table="LG_WORKSTAT",field="CODE",max_length=25,required=False)
	WS_NAME = base.CharField(label="İş İstasyonu açıklaması", table="LG_WORKSTAT",field="NAME",max_length=51,required=False)
	PLANT_NO = base.IntegerField(label="Fabrika numarası", table="LG_WORKSTAT",field="FACTORYNR",required=False)


class Opertion(base.Serializer):
	"""
		Operasyonlar
	"""
	class Meta:
		XML_ROOT = 'OPERATIONS'
		XML_SUBROOT = 'OPERATION'
		DATA_OBJECT = 'doOperation'
		REST_ENDPOINT = 'operations'
		RELATED_TABLE = 'LG_OPERTION'

	CODE = base.CharField(label="Operasyon Kodu", table="LG_OPERTION",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Operasyon Açıklaması", table="LG_OPERTION",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_OPERTION",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_OPERTION",field="CYPHCODE",max_length=11,required=False)
	APPROVED = base.IntegerField(label="Onay bilgisi", table="LG_OPERTION",field="APPROVED",min_value=0, max_value=1,required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_OPERTION",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_OPERTION",field="SITEID",required=False)

	# subs
	REQUIREMENTS = base.serializers.ListSerializer(child=OpertionReqs())
