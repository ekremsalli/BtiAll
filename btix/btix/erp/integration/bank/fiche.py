"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class BankFicheTransaction(base.BaseSerialiazer):
	TYPE = base.IntegerField(label="Hareket türü", table="LG_BNFLINE",field="TRCODE",required=True)
	BANKACC_CODE = base.CharField(label="Banka hesap kodu", table="LG_BANKACC",field="CODE",max_length=17,required=True)
	ARP_CODE = base.CharField(label="Cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)
	GL_CODE1 = base.CharField(label="Muhasebe hesap kodu1", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE1 = base.CharField(label="Masraf merkezi kodu1", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE2 = base.CharField(label="Muhasebe hesap kodu2", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE2 = base.CharField(label="Masraf merkezi kodu2", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	AUXIL_CODE = base.CharField(label="Hareket özel kodu", table="LG_BNFLINE",field="SPECODE",max_length=11,required=False)
	DOC_NUMBER = base.CharField(label="Belge numarası", table="LG_BNFLINE",field="DOCODE",max_length=32,required=False)
	DESCRIPTION = base.CharField(label="Açıklama", table="LG_BNFLINE",field="LINEEXP",max_length=51,required=False)
	CURR_TRANS = base.IntegerField(label="İşlem dövizi", table="LG_BNFLINE",field="TRCURR",min_value=0, max_value=1,required=False)
	DEBIT = base.FloatField(label="Borç", table="LG_BNFLINE",field="AMOUNT",required=False)
	CREDIT = base.FloatField(label="Alacak", table="LG_BNFLINE",field="AMOUNT",required=False)
	TC_XRATE = base.FloatField(label="İşlem dövizi kuru", table="LG_BNFLINE",field="TRRATE",required=False)
	TC_AMOUNT = base.FloatField(label="İşlem dövizi tutarı", table="LG_BNFLINE",field="TRNET",required=False)
	RC_XRATE = base.FloatField(label="Raporlama dövizi kuru", table="LG_BNFLINE",field="REPORTRATE",required=False)
	RC_AMOUNT = base.FloatField(label="Raporlama dövizi tutarı", table="LG_BNFLINE",field="REPORTNET",required=False)
	ARP_BNKDIV_NR = base.CharField(label="Cari hesap banka şubesi numarası", table="LG_BNFLINE",field="CLBNBRANCHNO",max_length=17,required=False)
	ARP_BNKACCOUNT_NR = base.CharField(label="Cari hesap banka hesap numarası", table="LG_BNFLINE",field="CLBNACCOUNTNO",max_length=17,required=False)
	BNK_TRACKING_NR = base.CharField(label="Banka izleme numarası", table="LG_BNFLINE",field="BNTRACKINGNO",max_length=21,required=False)
	BANK_PROC_TYPE = base.IntegerField(label="Banka Hareket Türü", table="LG_BNFLINE",field="BANKPROCTYPE",required=False)
	TRN_STATE = base.IntegerField(label="Hareket Durumu", table="LG_BNFLINE",field="TRNSTATE",required=False)
	TRADING_GRP = base.CharField(label="Ticari işlem grubu", table="LG_BNFLINE",field="TRADINGGRP",max_length=17,required=False)
	CURRSEL_TRANS = base.IntegerField(label="Satır döviz türü", table="LG_BNFLINE",field="LINEEXCTYP",required=False)
	DISCOUNTED = base.IntegerField(label="İndirimli ödeme", table="LG_BNFLINE",field="DISCFLAG",min_value=0, max_value=1,required=False)
	DISCOUNT_RATE = base.FloatField(label="İndirim yüzdesi", table="LG_BNFLINE",field="DISCRATE",required=False)
	VAT_RATE = base.FloatField(label="KDV oranı", table="LG_BNFLINE",field="VATRATE",required=False)
	ARP_CLOSE_AMOUNT = base.FloatField(label="Cari hesap kapanan tutar", table="LG_BNFLINE",field="ARCLOSEAMOUNT",required=False)
	GL_CODE3 = base.CharField(label="Muhasebe hesap kodu3", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE3 = base.CharField(label="Masraf merkezi kodu3", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	TRN_TYPE = base.IntegerField(label="Banka Hareket Türü", table="LG_BNFLINE",field="BANKPROCTYPE",required=False)
	DUE_DATE = base.IntegerField(label="Hareket Tarihi", table="LG_BNFLINE",field="TRANSDUEDATE",required=False)
	DATA_SITEID = base.IntegerField(label="Bilgi veri merkezi", table="LG_BNCARD",field="SITEID",required=False)

class BankFiche(base.Serializer):
	"""
		Banka fişi
	"""
	class Meta:
		XML_ROOT = 'BANK_VOUCHERS'
		XML_SUBROOT = 'BANK_VOUCHER'
		DATA_OBJECT = 'doBankVoucher'
		REST_ENDPOINT = 'bankSlips'
		RELATED_TABLE = 'LG_BNFICHE'

	DATE = base.IntegerField(label="Banka fiş tarihi", table="LG_BNFICHE",field="DATE_",required=True)
	NUMBER = base.CharField(label="Banka fiş numarası", table="LG_BNFICHE",field="FICHENO",max_length=9,required=True)
	AUXIL_CODE = base.CharField(label="Banka fişi özel kodu", table="LG_BNFICHE",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Banka fişi yetki kodu", table="LG_BNFICHE",field="CYPHCODE",max_length=11,required=False)
	DIVISION = base.IntegerField(label="İşyeri", table="LG_BNFICHE",field="BRANCH",required=False)
	DEPARTMENT = base.IntegerField(label="Bölüm", table="LG_BNFICHE",field="DEPARMENT",required=False)
	TYPE = base.IntegerField(label="Türü", table="LG_BNFICHE",field="TRCODE",required=True)
	GL_POSTED = base.IntegerField(label="Muhasebeleştirildi", table="LG_BNFICHE",field="ACCOUNTED",min_value=0, max_value=1,required=False)
	CANCELLED = base.IntegerField(label="İptal edildi", table="LG_BNFICHE",field="CANCELLED",min_value=0, max_value=1,required=False)
	SIGN = base.IntegerField(label="Borç / Alacak işareti", table="LG_BNFICHE",field="SIGN",required=False)
	TOTAL_DEBIT = base.FloatField(label="Toplam borç", table="LG_BNFICHE",field="DEBITTOT",required=False)
	TOTAL_CREDIT = base.FloatField(label="Toplam alacak", table="LG_BNFICHE",field="CREDITTOT",required=False)
	NOTES1 = base.CharField(label="Açıklama1", table="LG_BNFICHE",field="GENEXP1",max_length=51,required=False)
	NOTES2 = base.CharField(label="Açıklama2", table="LG_BNFICHE",field="GENEXP2",max_length=51,required=False)
	NOTES3 = base.CharField(label="Açıklama3", table="LG_BNFICHE",field="GENEXP3",max_length=51,required=False)
	NOTES4 = base.CharField(label="Açıklama4", table="LG_BNFICHE",field="GENEXP4",max_length=51,required=False)
	PRINT_COUNTER = base.IntegerField(label="Basım sayısı", table="LG_BNFICHE",field="PRINTCNT",required=False)
	CURRSEL_TOTALS = base.IntegerField(label="Genel döviz türü", table="LG_BNFICHE",field="GENEXCTYP",required=False)
	CURRSEL_DETAILS = base.IntegerField(label="Satır döviz türü", table="LG_BNFICHE",field="LINEEXCTYP",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi numarası", table="LG_BNFICHE",field="SITEID",required=False)
	RC_TOTAL_DEBIT = base.FloatField(label="Dövizli toplam borç", table="LG_BNFICHE",field="REPDEBIT",required=False)
	RC_TOTAL_CREDIT = base.FloatField(label="Dövizli toplam alacak", table="LG_BNFICHE",field="REPCREDIT",required=False)

	# subs
	TRANSACTIONS = base.serializers.ListSerializer(child=BankFicheTransaction())
