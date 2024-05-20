"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base


class AccountCard(base.Serializer):
	"""
		Muhasebe hesap kartları
	"""
	class Meta:
		XML_ROOT = 'GL_ACCOUNTS'
		XML_SUBROOT = 'GL_ACCOUNT'
		DATA_OBJECT = 'doGLAccount'
		REST_ENDPOINT = 'GLAccounts'
		RELATED_TABLE = "LG_EMUHACC"

	RECORD_STATUS = base.IntegerField(label="Kayıt statüsü", table="LG_EMUHACC",field="ACTIVE",required=False)
	CODE = base.CharField(label="Hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	DESCRIPTION = base.CharField(label="Hesap açıklaması1", table="LG_EMUHACC",field="DEFINITION_",max_length=100,required=False)
	DESCRIPTION2 = base.CharField(label="Hesap açıklaması2", table="LG_EMUHACC",field="EXTNAME",max_length=100,required=False)
	AUXIL_CODE = base.CharField(label="Hesap özel kodu", table="LG_EMUHACC",field="SPECODE",max_length=11,required=False)
	AUTHOR_CODE = base.CharField(label="Hesap yetki kodu", table="LG_EMUHACC",field="CYPHCODE",max_length=11,required=False)
	UNIT = base.CharField(label="Birim", table="LG_EMUHACC",field="UNITS",max_length=5,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	XRATEDIFF_CODE = base.CharField(label="Kur farkı hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	GROUP_CODE = base.IntegerField(label="Grup kodu", table="LG_EMUHACC GROUP",field="CODE",min_value=0, max_value=1,required=False)
	ACCOUNT_TYPE = base.IntegerField(label="Hesap tipi", table="LG_EMUHACC",field="ACCTYPE",min_value=0, max_value=1,required=False)
	MNDTRY_QUAN = base.IntegerField(label="Miktar girişleri", table="LG_EMUHACC",field="QUANCTRL",min_value=0, max_value=1,required=False)
	MNDTRY_OHP = base.IntegerField(label="Masraf merkezi girişleri", table="LG_EMUHACC",field="CENTERCTRL",min_value=0, max_value=1,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_EMUHACC",field="SITEID",required=False)
