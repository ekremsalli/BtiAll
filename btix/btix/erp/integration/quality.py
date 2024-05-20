"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class QsetLineList(base.BaseSerialiazer):
	CODE = base.CharField(label="Kalite kontrol satır kodu", table="LG_QCSLINE",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Kalite kontrol satır açıklaması", table="LG_QCSLINE",field="NAME",max_length=51,required=False)
	QTYPE = base.IntegerField(label="Kalite kontrol türü (0- Nicel, 1- Nitel)", table="LG_QCSLINE",field="QTYPE",required=False)
	QUNIT = base.CharField(label="Kalite kontrol birimi", table="LG_QCSLINE",field="QUNIT",max_length=11,required=False)
	TOOLCODE = base.CharField(label="Kontrol ekipmanı", table="LG_QCSLINE",field="TOOLCODE",max_length=25,required=False)
	CONTROLLER = base.IntegerField(label="Kontrol Sorumlusu", table="LG_QCSLINE",field="CONTROLLER",required=False)
	INSPPOINT = base.IntegerField(label="Kontrol noktası", table="LG_QCSLINE",field="INSPPOINT",required=False)
	INSPFICHES1 = base.IntegerField(label="Malzeme Yönetimi Fişleri", table="LG_QCSLINE",field="INSPFICHES1",required=False)
	INSPFICHES2 = base.IntegerField(label="Alım İrsaliyeleri", table="LG_QCSLINE",field="INSPFICHES2",required=False)
	INSPFICHES3 = base.IntegerField(label="Satış ve Dağıtım İrsaliyeleri", table="LG_QCSLINE",field="INSPFICHES3",required=False)
	IMPORTANCE = base.CharField(label="Öncelik derecesi", table="LG_QCSLINE",field="IMPORTANCE",max_length=11,required=False)
	FREQUENCY = base.FloatField(label="Kontrol Sıklığı", table="LG_QCSLINE",field="FREQUENCY",required=False)
	COUNTER = base.FloatField(label="Kontrol Sayısı", table="LG_QCSLINE",field="COUNTER",required=False)
	SAMPLESIZE = base.FloatField(label="Numune Miktarı", table="LG_QCSLINE",field="SAMPLESIZE",required=False)
	NOMVAL = base.FloatField(label="Nominal değer", table="LG_QCSLINE",field="NOMVAL",required=False)
	MINVAL = base.FloatField(label="Asgari değer", table="LG_QCSLINE",field="MINVAL",required=False)
	MAXVAL = base.FloatField(label="Azami değer", table="LG_QCSLINE",field="MAXVAL",required=False)
	MINTOL = base.FloatField(label="(-) Tolerans", table="LG_QCSLINE",field="MINTOL",required=False)
	MAXTOL = base.FloatField(label="(+) Tolerans", table="LG_QCSLINE",field="MAXTOL",required=False)
	EXPLINE = base.CharField(label="Açıklama Satırı", table="LG_QCSLINE",field="EXPLINE",max_length=81,required=False)
	CONFORMRATE = base.IntegerField(label="Kabul oranı", table="LG_QCSLINE",field="CONFORMRATE",required=False)
	LINENO = base.IntegerField(label="Satır numarası", table="LG_QCSLINE",field="LINENO_",required=False)


class QsetValList(base.BaseSerialiazer):
	CODE = base.CharField(label="KKK Değer Kodu", table="LG_QCLVAL",field="CODE",max_length=25,required=False)
	NAME = base.CharField(label="KKK Değer Açıklaması", table="LG_QCLVAL",field="NAME",max_length=51,required=False)
	TARGETFLAG = base.IntegerField(label="Target Flag", table="LG_QCLVAL",field="TARGETFLAG",required=False)
	LINENO = base.IntegerField(label="Satır numarası", table="LG_QCLVAL LINENO_",field="LINENO_",required=False)


class QsetTargetList(base.BaseSerialiazer):
	CODE = base.CharField(label="KKK Değeri Kodu", table="LG_QCLVAL",field="CODE",max_length=25,required=False)
	NAME = base.CharField(label="KKK Değeri Açıklaması", table="LG_QCLVAL",field="NAME",max_length=51,required=False)
	TARGETFLAG = base.IntegerField(label="Target Flag", table="LG_QCLVAL",field="TARGETFLAG",required=False)
	LINENO = base.IntegerField(label="Satır Numarası", table="LG_QCLVAL",field="LINENO_",required=False)


class Qset(base.Serializer):
	"""
		Kalite kontrol kriter setleri
	"""
	class Meta:
		XML_ROOT = 'QCCSETS'
		XML_SUBROOT = 'QCCSET'
		DATA_OBJECT = 'doQCCSet'
		REST_ENDPOINT = 'QCCriteriaSets'
		RELATED_TABLE = 'LG_QCSET'

	CODE = base.CharField(label="Kontrol kodu", table="LG_QCSET",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Kontrol açıklaması", table="LG_QCSET",field="NAME",max_length=51,required=False)
	ITYPE = base.IntegerField(label="Kontrol türü", table="LG_QCSET",field="ITYPE",required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_QCSET",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki kodu", table="LG_QCSET",field="CYPHCODE",max_length=11,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_QCSET",field="SITEID",required=False)
	WFSTATUS = base.IntegerField(label="Kullanım dışı", table="LG_QCSET",field="WFSTATUS",required=False)

	# subs
	LINELIST = base.serializers.ListSerializer(child=QsetLineList())
	VAL_LIST = base.serializers.ListSerializer(child=QsetValList())
	TARGET_LIST = base.serializers.ListSerializer(child=QsetTargetList())