"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class CashCard(base.Serializer):
	"""
		Kasa kartları
	"""
	class Meta:
		XML_ROOT = 'SAFE_DEPOSITS'
		XML_SUBROOT = 'SAFE_DEPOSIT'
		DATA_OBJECT = 'doSafeDeposit'
		REST_ENDPOINT = 'safeDeposits'
		RELATED_TABLE = 'LG_KSCARD'

	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_KSCARD",field="ACTIVE",required=False)
	CODE = base.CharField(label="Banka hesap kodu", table="LG_KSCARD",field="CODE",max_length=17,required=True)
	DESCRIPTION = base.CharField(label="Banka hesap açıklaması", table="LG_KSCARD",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_KSCARD",field="SPECODE",max_length=11,required=False)
	AUTHOR_CODE = base.CharField(label="Yetki Kodu", table="LG_KSCARD",field="CYPHCODE",max_length=11,required=False)
	USAGE_NOTE = base.CharField(label="Açıklama", table="LG_KSCARD",field="EXPLAIN",max_length=51,required=False)
	ADDRESS1 = base.CharField(label="Adres1", table="LG_KSCARD",field="ADDR1",max_length=51,required=False)
	ADDRESS2 = base.CharField(label="Adres2", table="LG_KSCARD",field="ADDR2",max_length=51,required=False)
	DATA_SITEID = base.IntegerField(label="Bilgi veri merkezi", table="LG_KSCARD",field="SITEID",required=False)
	GL_CODE1 = base.CharField(label="Muhasebe hesap kodu 1", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE1 = base.CharField(label="Masraf merkezi kodu 1", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE2 = base.CharField(label="Muhasebe hesap kodu 2", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE2 = base.CharField(label="Masraf merkezi kodu 2", table="LG_EMCENTER",field="CODE",max_length=17,required=False)

