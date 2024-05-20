"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class EmployeeGroupEmps(base.BaseSerialiazer):
	CODE = base.CharField(label="Çalışan Kodu", table="LG_EMPLOYEE",field="CODE",max_length=25,required=True)
	DEFINITION = base.CharField(label="Çalışan açıklaması", table="LG_EMPLOYEE",field="NAME",max_length=51,required=False)


class EmployeeGroup(base.Serializer):
	"""
		Çalışan grupları
	"""
	class Meta:
		XML_ROOT = 'EMPGROUPS'
		XML_SUBROOT = 'GROUP'
		DATA_OBJECT = 'doEmpGroup'
		REST_ENDPOINT = 'employeeGroups'
		RELATED_TABLE = 'LG_EMGROUP'

	CODE = base.CharField(label="Çalışan grubu kodu", table="LG_EMPGROUP",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Çalışan grubu açıklaması", table="LG_EMPGROUP",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_EMPGROUP",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki kodu", table="LG_EMPGROUP",field="CYPHCODE",max_length=11,required=False)
	FACTORYNR = base.IntegerField(label="Fabrika numarası", table="LG_EMPGROUP",field="FACTORYNR",required=False)
	APPROVED = base.IntegerField(label="Onay bilgisi", table="LG_EMPGROUP",field="APPROVED",min_value=0, max_value=1,required=False)
	OPERATION_TIME = base.FloatField(label="Günlük çalışma saati", table="LG_EMPGROUP",field="OPERATIONTIME",required=False)
	HOURLY_STD_COST = base.FloatField(label="Saatlik maliyet", table="LG_EMPGROUP",field="HOURLYSTDCOST",required=False)
	HOURLY_STDRP_COST = base.FloatField(label="Saatlik maliyet (Raporlama dövizi)", table="LG_EMPGROUP",field="HOURLYSTDRPCOST",required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_EMPGROUP",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_EMPGROUP",field="SITEID",required=False)
	WFSTATUS = base.IntegerField(label="Kullanım dışı", table="LG_EMPGROUP NOT IN",field="USE",required=False)
	GL_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)

	# subs
	EMPLOYEES = base.serializers.ListSerializer(child=EmployeeGroupEmps())
