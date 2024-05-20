"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class MaterialTree(base.Serializer):
	"""
		Malzeme sınıfı ağacı
	"""
	class Meta:
		XML_ROOT = 'M_M_Class_Tree'
		XML_SUBROOT = 'M_M_Class_Tree'
		DATA_OBJECT = 'doItemClsAsgn'
		REST_ENDPOINT = 'itemClassAssignments'
		RELATED_TABLE = 'LG_ITEMS'

	CLASS_CODE = base.CharField(label="Malzeme Sınıfı Ağacı Kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	CLASS_NAME = base.CharField(label="Malzeme Sınıfı Ağacı Açıklaması", table="LG_ITEMS",field="NAME",max_length=51,required=False)
	ITEM_CODE = base.CharField(label="Malzeme Kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	ITEM_NAME = base.CharField(label="Malzeme Açıklaması", table="LG_ITEMS",field="NAME",max_length=51,required=False)
