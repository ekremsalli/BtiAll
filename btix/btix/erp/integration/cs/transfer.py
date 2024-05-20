"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class CSTransfer(base.Serializer):
	"""
		Devir çek/senetleri
	"""
	class Meta:
		XML_ROOT = 'CQPN_TRANSFERS'
		XML_SUBROOT = 'CQPN_TRANSFER'
		DATA_OBJECT = 'doTransCqPn'
		REST_ENDPOINT = 'chequeAndPnotes'
		RELATED_TABLE = 'LG_CSCARD'

	TYPE = base.IntegerField(label="Fiş tarihi", table="LG_CSCARD",field="DOC",required=True)
	CURRENT_STATUS = base.IntegerField(label="Statüsü", table="LG_CSCARD",field="CURRSTAT",min_value=0, max_value=1,required=False)
	BANK_CODE = base.CharField(label="Banka kodu", table="LG_BNCARD",field="CODE",max_length=7,required=False)
	NUMBER = base.CharField(label="Portföy numarası", table="LG_CSCARD",field="PORTFOYNO",max_length=9,required=True)
	SERIAL_NUMBER = base.CharField(label="Seri numarası", table="LG_CSCARD",field="SERINO",max_length=25,required=False)
	BANK_TITLE = base.CharField(label="Banka Adı", table="LG_CSCARD",field="BANKNAME",max_length=21,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_CSCARD",field="SPECODE",max_length=11,required=False)
	AUTHOR_CODE = base.CharField(label="Yetki kodu", table="LG_CSCARD",field="CYPHCODE",max_length=11,required=False)
	CITY = base.CharField(label="Şehir", table="LG_CSCARD",field="CITY",max_length=16,required=False)
	OWING = base.CharField(label="Sahibi", table="LG_CSCARD",field="OWING",max_length=31,required=False)
	GUARANTOR = base.CharField(label="Kefil", table="LG_CSCARD",field="KEFIL",max_length=31,required=False)
	INFORMANT = base.CharField(label="Muhabir şube", table="LG_CSCARD",field="MUHABIR",max_length=11,required=False)
	DIVISION_NO = base.CharField(label="Banka Şube Numaarası", table="LG_CSCARD",field="BNBRANCHNO",max_length=17,required=False)
	DIVISION = base.IntegerField(label="Şube", table="LG_CSCARD",field="BRANCH",required=False)
	ACCOUNT_NO = base.CharField(label="Banka Hesap Numarası", table="LG_CSCARD",field="BNACCOUNTNO",max_length=17,required=False)
	DUE_DATE = base.IntegerField(label="Vade tarihi", table="LG_CSCARD",field="DUEDATE",required=False)
	DATE = base.IntegerField(label="Tarih", table="LG_CSCARD",field="SETDATE",required=False)
	STAMP_FEE = base.FloatField(label="Pul", table="LG_CSCARD",field="STAMP",required=False)
	AMONUT = base.FloatField(label="Tutar", table="LG_CSCARD",field="AMOUNT",required=False)
	CURR_TRANS = base.IntegerField(label="İşlem dövizi türü", table="LG_CSCARD",field="TRCURR",min_value=0, max_value=1,required=False)
	TC_XRATE = base.FloatField(label="İşlem dövizi kuru", table="LG_CSCARD",field="TRRATE",required=False)
	TC_AMOUNT = base.FloatField(label="İşlem dövizi tutarı", table="LG_CSCARD",field="TRNET",required=False)
	RC_XRATE = base.FloatField(label="Raporlama dövizi kuru", table="LG_CSCARD",field="REPORTRATE",required=False)
	RC_AMOUNT = base.FloatField(label="Raporlama dövizi tutarı", table="LG_CSCARD",field="REPORTNET",required=False)
	CREDIT_FLAG = base.IntegerField(label="Risk bilgisi güncellenecek", table="LG_CSCARD",field="RISKUPDATE",min_value=0, max_value=1,required=False)
	TRANSFERRED = base.IntegerField(label="Devir", table="LG_CSCARD",field="DEVIR",min_value=0, max_value=1,required=False)
	RC_XRATE_COLL = base.FloatField(label="Tahsil edildiğinde raporlama dövizi kuru", table="LG_CSCARD",field="COLLREPRATE",required=False)
	TC_XRATE_COLL = base.FloatField(label="Tahsil edildiğinde işlem dövizi kuru", table="LG_CSCARD",field="COLLTRRATE",required=False)
	CANCELLED = base.IntegerField(label="İptal edildi", table="LG_CSCARD",field="CANCELLED",min_value=0, max_value=1,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi numarası", table="LG_CSCARD",field="SITEID",required=False)
	STAMP_FEE_REQD = base.FloatField(label="Gerekli pul miktarı", table="LG_CSCARD",field="STAMP",required=False)
	OWNACC_CODE = base.CharField(label="İlgili cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)
	ARP_CODE = base.CharField(label="Borçlu cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)

