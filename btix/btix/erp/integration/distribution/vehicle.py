"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class DistributionVehicle(base.Serializer):
	"""
		Dağıtım araçları
	"""
	class Meta:
		XML_ROOT = "VECHILES"
		XML_SUBROOT = "VECHILE"
		DATA_OBJECT = "doDistVehicle"
		REST_ENDPOINT = "vehicles"
		RELATED_TABLE = 'LG_DISTVEHICLE'

	CODE = base.CharField(label="Dağıtım Aracı Kodu", table="LG_DISTVEHICLE",field="CODE",max_length=25,required=True)
	DEFINITION = base.CharField(label="Dağıtım Aracı Açıklaması", table="LG_DISTVEHICLE",field="DEFINITION",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_DISTVEHICLE",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_DISTVEHICLE",field="CYPHCODE",max_length=11,required=False)
	PLAQUE = base.CharField(label="Plate", table="LG_DISTVEHICLE",field="PLAQUE",max_length=13,required=False)
	WIDTH = base.FloatField(label="En", table="LG_DISTVEHICLE",field="WIDTH",required=False)
	LENGTH = base.FloatField(label="Boy", table="LG_DISTVEHICLE",field="LENGTH",required=False)
	HEIGHT = base.FloatField(label="Yükseklik", table="LG_DISTVEHICLE",field="HEIGHT",required=False)
	AREA = base.FloatField(label="Alan", table="LG_DISTVEHICLE",field="AREA",required=False)
	VOLUME = base.FloatField(label="Hacim", table="LG_DISTVEHICLE",field="VOLUME_",required=False)
	WEIGHT = base.FloatField(label="Ağırlık", table="LG_DISTVEHICLE",field="WEIGHT",required=False)
	SCORE = base.FloatField(label="Score", table="LG_DISTVEHICLE",field="SCORE",required=False)
	USER1 = base.CharField(label="Kullanıcı1", table="LG_DISTVEHICLE",field="USER1",max_length=51,required=False)
	USER2 = base.CharField(label="Kullanıcı2", table="LG_DISTVEHICLE",field="USER2",max_length=51,required=False)
	ACTIVE = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_DISTVEHICLE",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_DISTVEHICLE",field="SITEID",required=False)
	WIDTHCODE = base.CharField(label="Genişlik Kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	LENGTHCODE = base.CharField(label="Uzunluk Kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	HEIGHTCODE = base.CharField(label="Yükseklik Kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	AREACODE = base.CharField(label="Alan Kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	VOLUMECODE = base.CharField(label="Hacim Kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	WEIGHTCODE = base.CharField(label="Ağırlık Kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
