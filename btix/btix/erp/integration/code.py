"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class CypCode(base.Serializer):
	"""
		Yetki kodları
	"""
	class Meta:
		XML_ROOT = 'CYP_CODES'
		XML_SUBROOT = 'CODE'
		DATA_OBJECT = 'doCypCodes'
		REST_ENDPOINT = 'authorizationCodes'
		RELATED_TABLE = 'LG_SPECODES'

	CODE_TYPE = base.IntegerField(label="Kart türü", table="LG_SPECODES",field="CODETYPE",required=True)
	SPE_CODE_TYPE = base.IntegerField(label="Özel kod türü", table="LG_SPECODES",field="SPECODETYPE",required=True)
	CODE = base.CharField(label="Özel kod", table="LG_SPECODES",field="SPECODE",max_length=17,required=True)
	DEFINITION = base.CharField(label="Açıklama", table="LG_SPECODES",field="DEFINITION_",max_length=41,required=False)
	COLOR = base.IntegerField(label="Renk", table="LG_SPECODES",field="COLOR",min_value=0, max_value=1,required=False)
	WINCOLOR = base.IntegerField(label="Pencere rengi", table="LG_SPECODES",field="WINCOLOR",required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_ITEMS",field="SITEID",required=False)


class SpeCode(base.Serializer):
	"""
		Özel kodlar
	"""
	class Meta:
		XML_ROOT = 'SPE_CODES'
		XML_SUBROOT = 'CODE'
		DATA_OBJECT = 'doSpeCodes'
		REST_ENDPOINT = 'specialCodes'
		RELATED_TABLE = 'LG_SPECODES'

	CODE_TYPE = base.IntegerField(label="Kart türü", table="LG_SPECODES",field="CODETYPE",required=True)
	SPE_CODE_TYPE = base.IntegerField(label="Özel kod türü", table="LG_SPECODES",field="SPECODETYPE",required=True)
	CODE = base.CharField(label="Özel kod", table="LG_SPECODES",field="SPECODE",max_length=17,required=True)
	DEFINITION = base.CharField(label="Açıklama", table="LG_SPECODES",field="DEFINITION_",max_length=41,required=False)
	COLOR = base.IntegerField(label="Renk", table="LG_SPECODES",field="COLOR",min_value=0, max_value=1,required=False)
	WINCOLOR = base.IntegerField(label="Pencere rengi", table="LG_SPECODES",field="WINCOLOR",required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_ITEMS",field="SITEID",required=False)


class PrgCode(base.Serializer):
	"""
		Ödeme Planı Grup Kodu
	"""
	class Meta:
		XML_ROOT = 'PPG_CODES'
		XML_SUBROOT = 'PPG_CODE'
		DATA_OBJECT = 'doPPGCodes'
		REST_ENDPOINT = 'paymentPlanGroupCodes'
		RELATED_TABLE = 'LG_SPECODES'

	CODE_TYPE = base.IntegerField(label="Kart türü", table="LG_SPECODES",field="CODETYPE",required=True)
	SPE_CODE_TYPE = base.IntegerField(label="Özel kod türü", table="LG_SPECODES",field="SPECODETYPE",required=True)
	CODE = base.CharField(label="Özel kod", table="LG_SPECODES",field="SPECODE",max_length=17,required=True)
	DEFINITION = base.CharField(label="Açıklama", table="LG_SPECODES",field="DEFINITION_",max_length=41,required=False)
	COLOR = base.IntegerField(label="Renk", table="LG_SPECODES",field="COLOR",min_value=0, max_value=1,required=False)
	WINCOLOR = base.IntegerField(label="Pencere rengi", table="LG_SPECODES",field="WINCOLOR",required=False)
	DATA_SITEID = base.IntegerField(label="Bilgi veri merkezi", table="LG_BNCARD",field="SITEID",required=False)

