"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base


class MaterialGroupCode(base.Serializer):
	"""
		Malzeme grup kodları
	"""
	class Meta:
		XML_ROOT = 'GRP_CODES'
		XML_SUBROOT = 'CODES'
		DATA_OBJECT = 'doGrpCodes'
		REST_ENDPOINT = 'groupCodes'
		RELATED_TABLE = 'LG_SPECODES'

	CODE_TYPE = base.IntegerField(label="Kod türü", table="LG_SPECODES",field="CODETYPE",required=True)
	SPE_CODE_TYPE = base.IntegerField(label="Özel kod türü", table="LG_SPECODES",field="SPECODETYPE",required=True)
	CODE = base.CharField(label="Özel kod", table="LG_SPECODES",field="SPECODE",max_length=17,required=True)
	DEFINITION = base.CharField(label="Açıklama", table="LG_SPECODES",field="DEFINITION_",max_length=41,required=False)
	COLOR = base.IntegerField(label="Renk", table="LG_SPECODES",field="COLOR",min_value=0, max_value=1,required=False)
	WINCOLOR = base.IntegerField(label="Pencere rengi", table="LG_SPECODES",field="WINCOLOR",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_SPECODES",field="SITEID",required=False)
