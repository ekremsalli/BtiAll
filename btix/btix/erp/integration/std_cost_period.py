"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class StdCostPeriod(base.Serializer):
	"""
		Standart Maliyet Periyotları
	"""
	class Meta:
		XML_ROOT = 'STD_COST_PERIODS'
		XML_SUBROOT = 'STD_COST_PERIOD'
		DATA_OBJECT = 'doStdCostPrd'
		REST_ENDPOINT = 'standardCostPeriods'
		RELATED_TABLE = 'LG_STDCOSTPERIOD'

	CODE = base.CharField(label="Kod", table="LG_STDCOSTPERIOD",field="CODE",max_length=25,required=False)
	NAME = base.CharField(label="Açıklama", table="LG_STDCOSTPERIOD",field="NAME",max_length=51,required=False)
	BEG_DATE = base.IntegerField(label="Başlangıç tarihi", table="LG_STDCOSTPERIOD",field="BEGDATE",required=False)
	END_DATE = base.IntegerField(label="Bitiş tarihi", table="LG_STDCOSTPERIOD",field="ENDDATE",required=False)
	APPROVED = base.IntegerField(label="Onay Bilgisi", table="LG_STDCOSTPERIOD",field="APPROVED",min_value=0, max_value=1,required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_STDCOSTPERIOD",field="SITEID",required=False)
