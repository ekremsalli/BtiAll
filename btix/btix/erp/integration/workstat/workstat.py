"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class WorkStatChare(base.BaseSerialiazer):
	CODE = base.CharField(label="İş İstasyonu özellik kodu", table="LG_WSCHCODE",field="CODE",max_length=25,required=True)

class WorkStatCharv(base.BaseSerialiazer):
	CODE = base.CharField(label="Değer kodu", table="LG_WSCHVAL",field="CODE",max_length=25,required=True)

class WorkStat(base.Serializer):
	"""
		İş istasyonları
	"""
	class Meta:
		XML_ROOT = 'WORKSTATS'
		XML_SUBROOT = 'WORKSTAT'
		DATA_OBJECT = 'doWorkStat'
		REST_ENDPOINT = 'workstations'

	CODE = base.CharField(label="İş İstasyonu Kodu", table="LG_WORKSTAT",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="İş İstasyonu Açıklaması", table="LG_WORKSTAT",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_WORKSTAT",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_WORKSTAT",field="CYPHCODE",max_length=11,required=False)
	FACTORYDIVNR = base.IntegerField(label="Fabrika işyeri numarası", table="LG_WORKSTAT",field="FACTORYDIVNR",required=False)
	FACTORYNR = base.IntegerField(label="Fabrika numarası", table="LG_WORKSTAT",field="FACTORYNR",required=False)
	APPROVED = base.IntegerField(label="Onay Bilgisi", table="LG_WORKSTAT",field="APPROVED",min_value=0, max_value=1,required=False)
	OPERATION_TIME = base.FloatField(label="Günlük çalışma saati", table="LG_WORKSTAT",field="OPERATIONTIME",required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_WORKSTAT",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_WORKSTAT",field="SITEID",required=False)
	WFSTATUS = base.IntegerField(label="Kullanım dışı", table="LG_WORKSTAT NOT IN",field="USE",required=False)
	IN_INVENNR = base.IntegerField(label="Mamul/Yarı Mamul Ambar no", table="LG_WORKSTAT",field="ININVENNR",required=False)
	OUT_INVENNR = base.IntegerField(label="Hammadde ambar numarası", table="LG_WORKSTAT",field="OUTINVENNR",required=False)
	GL_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)

	# subs
	CHARACTERISTICS = base.serializers.ListSerializer(child=WorkStatChare())
	VALUE = base.serializers.ListSerializer(child=WorkStatCharv())


class WorkStatCharValues(base.BaseSerialiazer):
	CODE = base.CharField(label="Değer kodu", table="LG_WSCHVAL",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Değer açıklaması", table="LG_WSCHVAL",field="NAME",max_length=51,required=False)


class WorkStatChar(base.Serializer):
	"""
		İş istasyonu özellikleri
	"""
	class Meta:
		XML_ROOT = 'WSTCHARS'
		XML_SUBROOT = 'WSTCHAR'
		DATA_OBJECT = 'doWstChars'
		REST_ENDPOINT = 'characteristics'

	CODE = base.CharField(label="İş İstasyonu özellik kodu", table="LG_WSCHCODE",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="İş İstasyonu özellik açıklaması", table="LG_WSCHCODE",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_WSCHCODE",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki kodu", table="LG_WSCHCODE",field="CYPHCODE",max_length=11,required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_WSCHCODE",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_WSCHCODE",field="SITEID",required=False)

	# subs
	VALUES = base.serializers.ListSerializer(child=WorkStatCharValues())