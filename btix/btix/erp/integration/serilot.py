"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class Serilot(base.Serializer):
	"""
		Seri Lot Tablosu
	"""
	class Meta:
		XML_ROOT = 'SERIAL_LOT_RECORDS'
		XML_SUBROOT = 'SERIAL_LOT_RECORD'
		DATA_OBJECT = 'doSerialLot'
		REST_ENDPOINT = 'serialAndLotNumbers'
		RELATED_TABLE = 'LG_SERILOTN'

	ITEM_CODE = base.CharField(label="Malzeme Kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	TYPE = base.IntegerField(label="Türü", table="LG_SERILOTN",field="SLTYPE",required=False)
	CODE = base.CharField(label="Kodu", table="LG_SERILOTN",field="CODE",max_length=25,required=False)
	DESCRIPTION = base.CharField(label="Açıklaması", table="LG_SERILOTN",field="NAME",max_length=51,required=False)
	STATE = base.IntegerField(label="Durumu", table="LG_SERILOTN",field="STATE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_SERILOTN",field="SITEID",required=False)