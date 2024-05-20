"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class DRDistRtLines(base.BaseSerialiazer):
	LINENR = base.IntegerField(label="Satır Numarası", table="LG_DISTROUTLINE",field="LINENR",required=False)
	BCOUNTRYCODE = base.CharField(label="Başlangıç Ülke Kodu", table="LG_DISTROUTLINE",field="BCOUNTRYCODE",max_length=13,required=False)
	BCITYCODE = base.CharField(label="Başlangıç Şehir Kodu", table="LG_DISTROUTLINE",field="BCITYCODE",max_length=13,required=False)
	BTOWNCODE = base.CharField(label="Başlangıç İlçe Kodu", table="LG_DISTROUTLINE",field="BTOWNCODE",max_length=13,required=False)
	BDISTRICTCODE = base.CharField(label="Başlangıç Semt Kodu", table="LG_DISTROUTLINE",field="BDISTRICTCODE",max_length=13,required=False)
	ECOUNTRYCODE = base.CharField(label="Bitiş Ülke Kodu", table="LG_DISTROUTLINE",field="ECOUNTRYCODE",max_length=13,required=False)
	ECITYCODE = base.CharField(label="Bitiş Şehir Kodu", table="LG_DISTROUTLINE",field="ECITYCODE",max_length=13,required=False)
	ETOWNCODE = base.CharField(label="Bitiş İlçe Kodu", table="LG_DISTROUTLINE",field="ETOWNCODE",max_length=13,required=False)
	EDISTRICTCODE = base.CharField(label="Bitiş Semt Kodu", table="LG_DISTROUTLINE",field="EDISTRICTCODE",max_length=13,required=False)

class DistributionRouting(base.Serializer):
	"""
		Dağıtım Rotası
	"""
	class Meta:
		XML_ROOT = "DIST_ROUTINGS"
		XML_SUBROOT = "ROUTING"
		DATA_OBJECT = "doDistRouting"
		REST_ENDPOINT = "distributionRoutes"
		RELATED_TABLE = 'LG_DISTROUTING'

	CODE = base.CharField(label="Dağıtım Rota Kodu", table="LG_DISTROUTING",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Dağıtım Rota Açıklaması", table="LG_DISTROUTING",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_DISTROUTING",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_DISTROUTING",field="CYPHCODE",max_length=11,required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_DISTROUTING",field="ACTIVE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_DISTROUTING",field="SITEID",required=False)

	# subs
	DIST_RT_LINES = base.serializers.ListSerializer(child=DRDistRtLines())
