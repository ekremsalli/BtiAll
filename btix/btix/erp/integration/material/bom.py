"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class Bom(base.Serializer):
	"""
		Ürün reçeteleri
	"""
	class Meta:
		XML_ROOT = 'BOMS'
		XML_SUBROOT = 'BOM'
		DATA_OBJECT = 'doBOM'
		REST_ENDPOINT = 'Boms'
		RELATED_TABLE = 'LG_BOMASTER'

	CODE = base.CharField(label="Reçete Kodu", table="LG_BOMASTER",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Reçete açıklaması", table="LG_BOMASTER",field="NAME",max_length=51,required=False)
	APPROVED = base.IntegerField(label="Onay bilgisi", table="LG_BOMASTER",field="APPROVED",min_value=0, max_value=1,required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_BOMASTER",field="ACTIVE",required=False)
	DEMONTAJ = base.IntegerField(label="Demontaj", table="LG_BOMASTER",field="DEMONTAJ",required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_BOMASTER",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki kodu", table="LG_BOMASTER",field="CYPHCODE",max_length=11,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_BOMASTER",field="SITEID",required=False)
	WF_STATUS = base.IntegerField(label="Kullanım Dışı", table="LG_BOMASTER",field="WFSTATUS",required=False)
	REV_CODE = base.CharField(label="Reçete revizyon kodu", table="LG_BOMREVSN",field="CODE",max_length=25,required=False)
	REV_NAME = base.CharField(label="Reçete revizyon açıklaması", table="LG_BOMREVSN",field="NAME",max_length=51,required=False)
	REV_RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_BOMREVSN",field="ACTIVE",required=False)
	REV_DATE = base.IntegerField(label="Geçerlilik tarihi", table="LG_BOMREVSN",field="REVDATE",required=False)
	REV_DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_BOMREVSN",field="SITEID",required=False)
	REV_DATA_REFERENCE = base.IntegerField(label="Veri referansı", table="LG_BOMREVSN",field="ORGLOGICREF",required=False)
	REV_WF_STATUS = base.IntegerField(label="Kullanım dışı", table="LG_BOMREVSN",field="WFSTATUS",required=False)
	QTY_DEPT_TIME = base.IntegerField(label="Miktar bağımlı süre (Saat)", table="LG_BOMREVSN",field="QTYDEPTTIME",required=False)
	QTY_UNDEPT_TIME = base.IntegerField(label="Miktar bağımsız süre (Saat)", table="LG_BOMREVSN",field="QTYUNDEPTTIME",required=False)
	STD_OVHD_FORMULA = base.CharField(label="Standart Overhead Cost Formula", table="LG_BOMREVSN",field="STDOVHDFORMULA",max_length=121,required=False)
	STD_OVHD_RP_FORMULA = base.CharField(label="Standart Overhead Cost Formula (Reporting Currency)", table="1",field="LG_BOMREVSN",max_length=12,required=False)
	QTY_DEP_DURATION = base.FloatField(label="Durma süresi", table="LG_BOMASTER",field="QTYDEPDURATION",required=False)
