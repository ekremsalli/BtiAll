"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class ClPaymentList(base.BaseSerialiazer):
	DATE = base.CharField(label="Tarih", table="LG_PAYPLANS",field="DATE",required=False)
	TOTAL = base.FloatField(label="Toplam", table="LG_PAYPLANS",field="TOTAL",required=False)
	EARLY_INTRATE = base.FloatField(label="Erken ödeme faizi", table="LG_PAYPLANS",field="EARLYINTEREST",required=False)
	LATELY_INTRATE = base.FloatField(label="Geç ödeme faizi", table="LG_PAYPLANS",field="LATEINTEREST",required=False)
	MODIFIED = base.IntegerField(label="Değiştirilmiş", table="LG_PAYTRANS",field="MODIFIED",min_value=0, max_value=1,required=False)
	REMIND_LEVEL = base.IntegerField(label="İhtar seviyesi", table="LG_PAYTRANS",field="REMINDLEV",required=False)
	REMIND_SENT = base.IntegerField(label="İhtar gönderisi", table="LG_PAYTRANS",field="REMINDSENT",min_value=0, max_value=1,required=False)
	DISCOUNTED = base.IntegerField(label="İndirimli ödemeler", table="LG_PAYTRANS",field="DISCFLAG",min_value=0, max_value=1,required=False)
	DISCOUNT_DUEDATE = base.IntegerField(label="Kullanım dışı", table="LG_PAYTRANS",field="DISCDUEDATE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri referansı", table="LG_PAYTRANS",field="ORGLOGICREF",required=False)


class BaseTransaction(base.Serializer):
	ARP_CODE = base.CharField(label="Cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=True)
	GL_CODE1 = base.CharField(label="Muhasebe hesap kodu1", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE1 = base.CharField(label="Masraf merkezi kodu1", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE2 = base.CharField(label="Muhasebe hesap kodu2", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE2 = base.CharField(label="Masraf merkezi kodu2", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	AUXIL_CODE = base.CharField(label="Hareket özel kodu", table="LG_CLFLINE",field="SPECODE",max_length=11,required=False)
	DOC_NUMBER = base.CharField(label="Belge numarası", table="LG_CLFLINE",field="CYPHCODE",max_length=50,required=False)
	DESCRIPTION = base.CharField(label="Açıklama", table="LG_CLFLINE",field="LINEEXP",max_length=51,required=False)
	DEBIT = base.FloatField(label="Borç", table="LG_CLFLINE",field="AMOUNT",required=False)
	CREDIT = base.FloatField(label="Alacak", table="LG_CLFLINE",field="AMOUNT",required=False)
	CURR_TRANS = base.IntegerField(label="İşlem dövizi", table="LG_CLFLINE",field="TRCURR",min_value=0, max_value=1,required=False)
	TC_XRATE = base.FloatField(label="İşlem dövizi kuru", table="LG_CLFLINE",field="TRRATE",required=False)
	TC_AMOUNT = base.FloatField(label="İşlem dövizi tutarı", table="LG_CLFLINE",field="TRNET",required=False)
	RC_XRATE = base.FloatField(label="Raporlama dövizi kuru", table="LG_CLFLINE",field="REPORTRATE",required=False)
	RC_AMOUNT = base.FloatField(label="Raporlama dövizi tutarı", table="LG_CLFLINE",field="REPORTNET",required=False)
	PAYMENT_CODE = base.CharField(label="Ödeme plan kodu", table="LG_PAYPLANS",field="CODE",max_length=17,required=False)
	TRADING_GRP = base.CharField(label="Ticari işlem grubu", table="LG_CLFLINE",field="TRADINGGRP",max_length=17,required=False)
	CURRSEL_TRANS = base.IntegerField(label="Satır Döviz Türü", table="LG_CLFLINE",field="LINEEXCTYP",required=False)
	SINGLE_PAYMENT = base.IntegerField(label="Tek satırlı ödeme", table="LG_CLFLINE",field="ONLYONEPAYLINE",min_value=0, max_value=1,required=False)
	DISCOUNTED = base.IntegerField(label="İndirimler", table="LG_CLFLINE",field="DISCFLAG",min_value=0, max_value=1,required=False)
	DISCOUNT_RATE = base.FloatField(label="İndirim yüzdesi", table="LG_CLFLINE",field="DISCRATE",required=False)
	VAT_RATE = base.FloatField(label="KDV oranı", table="LG_CLFLINE",field="VATRATE",required=False)
	DISCOUNTED_AMOUNT = base.CharField(label="İndirim toplamı", table="LG_CLFLINE",field="CASHAMOUNT",max_length=8,required=False)
	GL_CODE3 = base.CharField(label="Muhasebe hesap kodu3", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE3 = base.CharField(label="Masraf merkezi kodu3", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE4 = base.CharField(label="Muhasebe hesap kodu4", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE4 = base.CharField(label="Masraf merkezi kodu4", table="LG_EMCENTER",field="CODE",max_length=17,required=False)

	BANKACC_CODE = base.CharField(label='Banka hesap kodu', table='LG_CLFICHE',field='?',required=False)
	BANK_GL_CODE = base.CharField(label='?', table='LG_CLFICHE',field='?',required=False)
	BANK_OHP_CODE = base.CharField(label='?', table='LG_CLFICHE',field='?',required=False)
	AFFECT_RISK = base.IntegerField(label='?',table='LG_CLFICHE',field='?',required=False)

	BNLN_TC_AMOUNT = base.FloatField(label="?", table="LG_CLFLINE",required=False)
	BNLN_TC_XRATE = base.FloatField(label="?", table="LG_CLFLINE",required=False)
	BNLN_TC_CURR = base.IntegerField(label="?", table="LG_CLFLINE",required=False)


class CLTransactionPaymentHolder(base.BaseSerialiazer):
	items = base.serializers.ListSerializer(child=ClPaymentList())

class ClTransactionForJSON(BaseTransaction):
	PAYMENT_LIST = CLTransactionPaymentHolder()

class ClTransactionForXML(BaseTransaction):
	PAYMENT_LIST = base.serializers.ListSerializer(child=ClPaymentList())

class BaseCL(base.Serializer):
	NUMBER = base.CharField(label="Cari hesap fiş numarası", table="LG_CLFICHE",field="FICHENO",max_length=9,required=True)
	DATE = base.CharField(label="Fiş tarihi", table="LG_CLFICHE",field="DATE_",required=True)
	TIME = base.IntegerField(label="Fiş kayıt zamanı", table="LG_CLFICHE",field="FTIME",required=False)
	DOC_NUMBER = base.CharField(label="Belge numarası", table="LG_CLFICHE",field="DOCODE",max_length=32,required=False)
	TYPE = base.IntegerField(label="Türü", table="• LG_CLFICHE",field="TRCODE",required=False)
	AUXIL_CODE = base.CharField(label="Fiş özel kodu", table="LG_CLFICHE",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Fiş yetki kodu", table="LG_CLFICHE",field="CYPHCODE",max_length=11,required=False)
	DIVISION = base.IntegerField(label="İşyeri", table="LG_CLFICHE",field="BRANCH",required=False)
	DEPARTMENT = base.IntegerField(label="Bölüm", table="LG_CLFICHE",field="DEPARTMENT",required=False)
	NOTES1 = base.CharField(label="Açıklama1", table="LG_CLFICHE",field="GENEXP1",max_length=51,required=False)
	NOTES2 = base.CharField(label="Açıklama2", table="LG_CLFICHE",field="GENEXP2",max_length=51,required=False)
	NOTES3 = base.CharField(label="Açıklama3", table="LG_CLFICHE",field="GENEXP3",max_length=51,required=False)
	NOTES4 = base.CharField(label="Açıklama4", table="LG_CLFICHE",field="GENEXP4",max_length=51,required=False)
	TOTAL_DEBIT = base.FloatField(label="Toplam borç", table="LG_CLFICHE",field="DEBIT",required=False)
	TOTAL_CREDIT = base.FloatField(label="Toplam alacak", table="LG_CLFICHE",field="CREDIT",required=False)
	RC_TOTAL_DEBIT = base.FloatField(label="Dövizli toplam borç", table="LG_CLFICHE",field="REPDEBIT",required=False)
	RC_TOTAL_CREDIT = base.FloatField(label="Dövizli toplam alacak", table="LG_CLFICHE",field="REPCREDIT",required=False)
	GL_POSTED = base.IntegerField(label="Muhasebeleştir", table="LG_CLFICHE",field="ACCOUNTED",min_value=0, max_value=1,required=False)
	GL_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	PRINT_COUNTER = base.IntegerField(label="Basım sayısı", table="LG_CLFICHE",field="PRINTCNT",required=False)
	CANCELLED = base.IntegerField(label="İptal edildi", table="LG_CLFICHE",field="CANCELLED",min_value=0, max_value=1,required=False)
	CURRSEL_TOTALS = base.IntegerField(label="Genel döviz türü", table="LG_CLFICHE",field="GENEXCTYP",required=False)
	CURRSEL_DETAILS = base.IntegerField(label="Satır döviz türü", table="LG_CLFICHE",field="LINEEXCTYP",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi numarası", table="LG_CLFICHE",field="SITEID",required=False)
	ARP_CODE = base.CharField(label="Cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=True)

	BANKACC_CODE = base.CharField(label='Banka hesap kodu', table='LG_CLFICHE',field='?',required=False)
	BNOHP_CODE = base.CharField(label='', table='LG_CLFICHE',field='?',required=False)
	# subs
	#TRANSACTIONS = base.serializers.ListSerializer(child=ClTransaction())
	#PAYMENT_LIST = base.serializers.ListSerializer(child=ClPaymentList())


class CLTransactionHolder(base.BaseSerialiazer):
	items = base.serializers.ListSerializer(child=ClTransactionForJSON())

class BaseCLForJSON(BaseCL):
	TRANSACTIONS = CLTransactionHolder()

class BaseCLForXML(BaseCL):
	TRANSACTIONS = base.serializers.ListSerializer(child=ClTransactionForXML())


class ClFiche(BaseCLForJSON):
	"""
		Cari hesap fişleri
	"""
	class Meta:
		XML_ROOT = 'ARP_VOUCHERS'
		XML_SUBROOT = 'ARP_VOUCHER'
		DATA_OBJECT = 'doARAPVoucher'
		REST_ENDPOINT = 'ArpSlips'
		RELATED_TABLE = 'LG_CLFICHE'

class ClFicheXML(BaseCLForXML):
	"""
		Cari hesap fişleri
	"""
	class Meta:
		XML_ROOT = 'ARP_VOUCHERS'
		XML_SUBROOT = 'ARP_VOUCHER'
		DATA_OBJECT = 'doARAPVoucher'
		REST_ENDPOINT = 'ArpSlips'
		RELATED_TABLE = 'LG_CLFICHE'
