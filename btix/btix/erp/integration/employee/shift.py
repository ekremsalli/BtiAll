"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class EmployeeShiftLine(base.BaseSerialiazer):
	BEG_TIME = base.IntegerField(label="Başlangıç tarihi", table="LG_SHFTTIME",field="BEGTIME",required=False)
	END_TIME = base.IntegerField(label="Bitiş tarihi", table="LG_SHFTTIME",field="ENDTIME",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_SHFTTIME",field="SITEID",required=False)


class EmployeeShift(base.Serializer):
	"""
		Vardiyalar
	"""
	class Meta:
		XML_ROOT = 'SHIFTS'
		XML_SUBROOT = 'SHIFT'
		DATA_OBJECT = 'doShifts'
		REST_ENDPOINT = 'shifts'
		RELATED_TABLE = 'LG_SHIFT'

	CODE = base.CharField(label="Vardiya Kodu", table="LG_SHIFT",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Vardiya Açıklaması", table="LG_SHIFT",field="NAME",max_length=51,required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_SHIFT",field="ACTIVE",required=False)
	SPECODE = base.CharField(label="Özel Kod", table="LG_SHIFT",field="SPECODE",max_length=11,required=False)
	CYPHCODE = base.CharField(label="Yetki Kodu", table="LG_SHIFT",field="CYPHCODE",max_length=11,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_SHIFT",field="SITEID",required=False)

	# subs
	SHIFT_LINES = base.serializers.ListSerializer(child=EmployeeShiftLine())

class EmployeeShiftAssign(base.Serializer):
	"""
		Vardiya atamaları
	"""
	class Meta:
		XML_ROOT = 'SHIFTASG'
		XML_SUBROOT = 'SHIFTASG'
		DATA_OBJECT = 'doShiftAsg'
		REST_ENDPOINT = 'shiftAssignments'
		RELATED_TABLE = 'LG_SHFTASGN'

	"""
		Source_Type 0 ise Source_Code -> Çalışan kodu LG_EMPLOYEE.CODE
		Source_Type 1 ise Source_Code -> Çalışan grup kodu LG_EMPGROUP.CODE
		Source_Type 2 ise Source_Code -> İş istasyonu kodu LG_WORKSTAT.CODE
		Source_Type 3 ise Source_Code -> İş istasyonu grup kodu LG_WSGRPF.CODE
	"""

	SOURCE_TYPE = base.IntegerField(label="Kaynak Türü", table="LG_SHFTASGN",field="SOURCETYPE",required=True)
	SOURCE_CODE = base.CharField(label="(Kaynak türüne göre tablo değişir) Grup Kodu", table="LG_WSGRPF",field="CODE",max_length=25,required=True)
	SHIFT_CODE = base.CharField(label="Kod", table="LG_SHIFT",field="CODE",max_length=25,required=True)
	BEGDATE = base.IntegerField(label="Başlangıç Tarihi", table="LG_SHFTASGN",field="BEGDATE",required=False)
	LINENR = base.IntegerField(label="Bitiş Tarihi", table="LG_SHFTASGN",field="LINENR",required=False)
