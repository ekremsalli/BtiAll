"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class Employee(base.Serializer):
	"""
		Çalışanlar
	"""
	class Meta:
		XML_ROOT = 'EMPLOYEES'
		XML_SUBROOT = 'EMPLOYEE'
		DATA_OBJECT = 'doEmployee'
		REST_ENDPOINT = 'employees'
		RELATED_TABLE = 'LG_EMPLOYEE'

	CODE = base.CharField(label="Çalışan Kodu", table="LG_EMPLOYEE",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Çalışan açıklaması", table="LG_EMPLOYEE",field="NAME",max_length=51,required=False)
	FACTORYDIVNR = base.IntegerField(label="Fabrika işyeri", table="LG_EMPLOYEE",field="FACTORYDIVNR",required=False)
	FACTORYNR = base.IntegerField(label="Fabrika numarası", table="LG_EMPLOYEE",field="FACTORYNR",required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_EMPLOYEE",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki kodu", table="LG_EMPLOYEE",field="CYPHCODE",max_length=11,required=False)
	APPROVED = base.IntegerField(label="Onay bilgisi", table="LG_EMPLOYEE",field="APPROVED",min_value=0, max_value=1,required=False)
	OPERATION_TIME = base.FloatField(label="Günlük çalışma saati", table="LG_EMPLOYEE",field="OPERATIONTIME",required=False)
	HOURLY_STD_COST = base.FloatField(label="Saatlik maliyet", table="LG_EMPLOYEE",field="HOURLYSTDCOST",required=False)
	HOURLY_STDRP_COST = base.FloatField(label="Saatlik maliyet (Raporlama dövizi)", table="LG_EMPLOYEE",field="HOURLYSTDRPCOST",required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_EMPLOYEE",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_EMPLOYEE",field="SITEID",required=False)
	WFSTATUS = base.IntegerField(label="Kullanım dışı", table="LG_EMPLOYEE NOT IN",field="USE",required=False)
	SHIFT_CODE = base.CharField(label="Çalışan Grup Kodu", table="LG_EMPGROUP",field="CODE",max_length=25,required=False)
	GL_CODE1 = base.CharField(label="Muhasebe hesap kodu 1", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE1 = base.CharField(label="Masraf merkezi kodu 1", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE2 = base.CharField(label="Muhasebe hesap kodu 2", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE2 = base.CharField(label="Masraf merkezi kodu 2", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE3 = base.CharField(label="Muhasebe hesap kodu 3", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE3 = base.CharField(label="Masraf merkezi kodu 3", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE4 = base.CharField(label="Muhasebe hesap kodu 4", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE4 = base.CharField(label="Masraf merkezi kodu 4", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE5 = base.CharField(label="Muhasebe hesap kodu 5", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE5 = base.CharField(label="Masraf merkezi kodu 5", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE6 = base.CharField(label="Muhasebe hesap kodu 6", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE6 = base.CharField(label="Masraf merkezi kodu 6", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
