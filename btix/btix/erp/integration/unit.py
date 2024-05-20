"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class UnitsetUnits(base.BaseSerialiazer):
	CODE = base.CharField(label="Kod", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	NAME = base.CharField(label="Birim seti adı", table="LG_UNITSETL",field="NAME",max_length=51,required=False)
	UNIT_ORDER = base.IntegerField(label="Satır Numarası", table="LG_UNITSETL",field="LINENR",required=False)
	MAIN_UNIT = base.IntegerField(label="Ana birim", table="LG_UNITSETL",field="MAINUNIT",required=False)
	CONV_FACT1 = base.FloatField(label="Çevrim Katsayısı", table="LG_UNITSETL",field="CONVFACT1",required=False)
	CONV_FACT2 = base.FloatField(label="Çevrim Katsayısı", table="LG_UNITSETL",field="CONVFACT2",required=False)
	WIDTH = base.FloatField(label="En", table="LG_UNITSETL",field="WIDTH",required=False)
	LENGTH = base.FloatField(label="Boy", table="LG_UNITSETL",field="LENGTH",required=False)
	HEIGHT = base.FloatField(label="Yükseklik", table="LG_UNITSETL",field="HEIGHT",required=False)
	AREA = base.FloatField(label="Alan", table="LG_UNITSETL",field="AREA",required=False)
	VOLUME = base.FloatField(label="Hacim", table="LG_UNITSETL",field="VOLUME",required=False)
	WEIGHT = base.FloatField(label="Ağırlık", table="LG_UNITSETL",field="WEIGHT",required=False)
	DIVISIBLE = base.IntegerField(label="Bölünebilir", table="LG_UNITSETL",field="DIVUNIT",min_value=0, max_value=1,required=False)


class Unitset(base.Serializer):
	"""
		Birim setleri aktarımı
	"""
	class Meta:
		XML_ROOT = 'UNIT_SETS'
		XML_SUBROOT = 'UNITSET'
		DATA_OBJECT = 'doUnitSet'
		REST_ENDPOINT = 'unitSets'
		RELATED_TABLE = 'LG_UNITSETF'

	CODE = base.CharField(label="Birim Seti Kodu", table="LG_UNITSETF",field="CODE",max_length=25,required=False)
	DESCRIPTION = base.CharField(label="Birim Seti Açıklaması", table="LG_UNITSETF",field="NAME",max_length=51,required=False)
	TYPE = base.IntegerField(label="Tür", table="LG_UNITSETF",field="CARDTYPE",required=False)
	ITEM_SPESIFIC = base.IntegerField(label="Yalnız malzeme / hizmet için", table="LG_UNITSETF",field="SPECITEM",min_value=0, max_value=1,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_UNITSETF",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_UNITSETF",field="CYPHCODE",max_length=11,required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_UNITSETF",field="SITEID",required=False)

	# subs
	UNITS = base.serializers.ListSerializer(child=UnitsetUnits())
