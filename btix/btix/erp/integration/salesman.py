"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class SalesmanCustList(base.BaseSerialiazer):
	CODE = base.CharField(label="Borçlu / Alacaklı Hesap Kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)
	NAME = base.CharField(label="Borçlu / Alacaklı Hesap Açıklaması", table="LG_CLCARD",field="DEFINITION_",max_length=51,required=False)
	BEG_DATE = base.IntegerField(label="Ziyaret Başlangıç tarihi", table="LG_SLSCLREL",field="BEGDATE",required=False)
	VISIT_DAY = base.IntegerField(label="Ziyaret günü", table="LG_SLSCLREL",field="VISITDAY",min_value=0, max_value=1,required=False)
	VISIT_PERIOD = base.CharField(label="Ziyaret periyodu", table="LG_SLSCLREL",field="VISITPERIOD",max_length=51,required=False)

class Salesman(base.Serializer):
	"""
		Satıcı-Cari Bağlatısı
	"""
	class Meta:
		XML_ROOT = "CLSALESMANS"
		XML_SUBROOT = "CLSALESMAN"
		DATA_OBJECT = "doSalesmanCl"
		REST_ENDPOINT = "salesmen"
		RELATED_TABLE = 'LG_SLSMAN'

	CODE = base.CharField(label="Satış elemanı kodu", table="LG_SLSMAN",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Satış elemanı açıklaması", table="LG_SLSMAN",field="DEFINITION_",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_SLSMAN",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki kodu", table="LG_SLSMAN",field="CYPHCODE",max_length=11,required=False)
	POSITION = base.CharField(label="Satış elemanı pozisyonu", table="LG_SLSMAN",field="POSITION_",max_length=11,required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_SLSMAN",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_SLSMAN",field="SITEID",required=False)
	USER_ID = base.IntegerField(label="Kullanıcı Kodu", table="LG_SLSMAN",field="USERID",required=False)
	DEPT_ID = base.IntegerField(label="Bölüm Kodu", table="LG_SLSMAN",field="DEPTID",required=False)
	DIVIS_ID = base.IntegerField(label="İşyeri Kodu", table="LG_SLSMAN",field="DIVISID",required=False)
	FIRM_NO = base.IntegerField(label="Firma Numarası", table="LG_SLSMAN",field="FIRMNR",required=False)

	# subs
	CUST_LIST = base.serializers.ListSerializer(child=SalesmanCustList())

