"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class BankAccount(base.Serializer):
	"""
		Banka hesap kartları
	"""
	class Meta:
		XML_ROOT = 'BANK_ACCOUNTS'
		XML_SUBROOT = 'BANK_ACCOUNT'
		DATA_OBJECT = 'doBankAccount'
		REST_ENDPOINT = 'bankAccounts'
		RELATED_TABLE = 'LG_BANKACC'

	ACCOUNT_TYPE = base.IntegerField(label="Hesap tipi", table="LG_BANKACC",field="CARDTYPE",required=False)
	RECORD_STATUS = base.IntegerField(label="Kullanım Durumu (0- Kullanımda, 1- Kullanım Dışı)", table="LG_BANKACC",field="ACTIVE",required=False)
	CODE = base.CharField(label="Banka hesap kodu", table="LG_BANKACC",field="CODE",max_length=17,required=True)
	DESCRIPTION = base.CharField(label="Banka hesap açıklaması", table="LG_BANKACC",field="DEFINITION_",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_BANKACC",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_BANKACC",field="CYPHCODE",max_length=11,required=False)
	BANK_CODE = base.CharField(label="Banka kodu", table="LG_BNCARD",field="CODE",max_length=7,required=False)
	CHEQUE_MARGIN = base.FloatField(label="Kredi marjı %çek", table="LG_BANKACC",field="CHECKMARGIN",required=False)
	PN_MARGIN = base.FloatField(label="Kredi marjı %senet", table="LG_BANKACC",field="NOTEMARGIN",required=False)
	INTRATE_GEN = base.FloatField(label="Cari hesap faiz oranı", table="LG_BANKACC",field="CUSTINTEREST",required=False)
	INTRATE_CHQCRD = base.FloatField(label="Çek karşılığı kredi faizi (Aylık)", table="LG_BANKACC",field="CKINTEREST",required=False)
	INTRATE_PNCRD = base.FloatField(label="Senet karşılığı kredi (Aylık)", table="LG_BANKACC",field="SKINTEREST",required=False)
	DEDTAX_RATE = base.FloatField(label="Stopaj oranı", table="LG_BANKACC",field="STOPAJPER",required=False)
	OFCFUND_RATE = base.FloatField(label="Fon oranı", table="LG_BANKACC",field="FONPER",required=False)
	CURRENCY = base.IntegerField(label="Döviz türü", table="LG_BANKACC",field="CURRENCY",min_value=0, max_value=1,required=False)
	ACCOUNT_NR = base.CharField(label="Hesap numarası", table="LG_BANKACC",field="ACCOUNTNO",max_length=17,required=False)
	GL_CODE1 = base.CharField(label="Muhasebe hesap kodu 1", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE1 = base.CharField(label="Masraf merkezi kodu 1", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE2 = base.CharField(label="Muhasebe hesap kodu 2", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE2 = base.CharField(label="Masraf merkezi kodu 2", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE3 = base.CharField(label="Muhasebe hesap kodu 3", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE3 = base.CharField(label="Masraf merkezi kodu 3", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE4 = base.CharField(label="Muhasebe hesap kodu 4", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE4 = base.CharField(label="Masraf merkezi kodu 4", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	DATA_SITEID = base.IntegerField(label="Bilgi veri merkezi", table="LG_BNCARD",field="SITEID",required=False)
