"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class BomParams(base.Serializer):
	"""
		Reçete sabitleri
	"""
	class Meta:
		XML_ROOT = 'PRODPARAMS'
		XML_SUBROOT = 'PRODPARAM'
		DATA_OBJECT = 'doPrdParams'
		REST_ENDPOINT = 'productionParameters'
		RELATED_TABLE = 'LG_FRMPRDPARAM'

	FIRM_NO = base.IntegerField(label="Firma Numarası", table="LG_FRMPRDPARAM",field="FIRMNR",required=True)
	CODE = base.CharField(label="Parametre kodu", table="LG_FRMPRDPARAM",field="PARAMCODE",max_length=11,required=True)
	NAME = base.CharField(label="Parametre Açıklaması", table="LG_FRMPRDPARAM",field="PARAMNAME",max_length=51,required=False)
	PARAM_DEFAULT = base.FloatField(label="Parametre öndeğerlemesi", table="LG_FRMPRDPARAM",field="PARAMDEFAULT",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_FRMPRDPARAM",field="SITEID",required=False)
	WF_STATUS = base.IntegerField(label="Kullanım dışı", table="LG_FRMPRDPARAM",field="WFSTATUS",required=False)
