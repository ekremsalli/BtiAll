"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class Emcenter(base.Serializer):
	"""
		Masraf merkezi
	"""
	class Meta:
		XML_ROOT = 'OHP_ACCOUNTS'
		XML_SUBROOT = 'OHP_ACCOUNT'
		DATA_OBJECT = 'doOverheadPoolAcc'
		REST_ENDPOINT = 'overheadAccounts'
		RELATED_TABLE = "LG_EMCENTER"

	CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	DESCRIPTION = base.CharField(label="Masraf merkezi açıklaması", table="LG_EMCENTER",field="DEFINITION",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Masraf merkezi özel kodu", table="LG_EMCENTER",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Masraf merkezi yetki kodu", table="LG_EMCENTER",field="CYPHCODE",max_length=11,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_EMCENTER",field="SITEID",required=False)