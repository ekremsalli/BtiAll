"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base


class MaterialCharacteristicValues(base.BaseSerialiazer):
	VALNO = base.IntegerField(label="Değer numarası", table="LG_CHARVAL",field="VALNO",required=False)
	CODE = base.CharField(label="Değer kodu", table="LG_CHARVAL",field="CODE",max_length=25,required=False)
	NAME = base.CharField(label="Değer açıklaması", table="LG_CHARVAL",field="NAME",max_length=51,required=False)


class MaterialCharacteristics(base.Serializer):
	"""
		Malzeme özellikleri
	"""
	class Meta:
		XML_ROOT = 'ITEM_CHARACTERISTICS'
		XML_SUBROOT = 'ITEM_CHARACTERISTIC'
		DATA_OBJECT = 'doItChCodes'
		REST_ENDPOINT = 'itemCharacteristics'
		RELATED_TABLE = 'LG_CHARCODE'

	CODE = base.CharField(label="Özellik kodu", table="LG_CHARCODE",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Özellik açıklaması", table="LG_CHARCODE",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_CHARCODE",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki kodu", table="LG_CHARCODE",field="CYPHCODE",max_length=11,required=False)
	APPROVED = base.IntegerField(label="Onay bilgisi", table="LG_CHARCODE",field="APPROVED",min_value=0, max_value=1,required=False)
	CARD_TYPE = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_CHARCODE",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_CHARCODE",field="SITEID",required=False)

	# subs
	VALUES = base.serializers.ListSerializer(child=MaterialCharacteristicValues())
