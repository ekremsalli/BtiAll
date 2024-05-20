"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class ClCardNotes(base.BaseSerialiazer):
	LINE = base.CharField(label="Satır", table="LG_CLINTEL",field="INTELLINE",max_length=51,required=False)
	CREDIT_TYPE = base.IntegerField(label="Risk kontrol tipi", table="LG_CLRNUMS",field="RISKTYPE",min_value=0, max_value=1,required=False)
	CREDIT_LIMIT = base.FloatField(label="Risk limiti", table="LG_CLRNUMS",field="RISKLIMIT",required=False)
	CREDIT_BALANCED = base.FloatField(label="Kapanan risk", table="LG_CLRNUMS",field="RISKBALANCED",required=False)
	RISKFACT_CHQ = base.FloatField(label="Çek risk çarpanı", table="LG_CLRNUMS",field="CEKRISKFACTOR",required=False)
	RISKFACT_PROMNT = base.FloatField(label="Senet risk çarpanı", table="LG_CLRNUMS",field="SENETRISKFACTOR",required=False)
	ACTION_CREDHOLD_ORD = base.IntegerField(label="Risk limiti aşıldığında-siparişte", table="LG_CLRNUMS",field="ORDRISKOVER",min_value=0, max_value=1,required=False)
	ACTION_CREDHOLD_SHP = base.IntegerField(label="Risk limiti aşıldığında-irsaliyede", table="LG_CLRNUMS",field="DESPRISKOVER",min_value=0, max_value=1,required=False)
	ACTION_CREDHOLD_OTH = base.IntegerField(label="Risk limiti aşıldığında-diğer işlemlerde", table="LG_CLRNUMS",field="RISKOVER",min_value=0, max_value=1,required=False)
	GL_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	PP_GROUP_CODE = base.CharField(label="Ödeme Planı Grup Kodu", table="LG_CLCARD",field="PPGROUPCODE",max_length=11,required=False)
	USE_REP_RISK = base.IntegerField(label="Will be used On Credit Tracking", table="LG_CLRNUMS",field="USEREPRISK",min_value=0, max_value=1,required=False)
	RISK_LIMIT = base.FloatField(label="Raporlama Dövizi Kredi Limiti", table="LG_CLRNUMS",field="REPRISKLIMIT",required=False)
	RISK_BALANCED = base.FloatField(label="Reporting Currency Delivered Credit", table="LG_CLRNUMS",field="REPRISKBALANCED",required=False)
	ORD_SEND_METHOD = base.IntegerField(label="Sipariş Formu Gönderme metodu", table="LG_CLCARD",field="ORDSENDMETHOD",required=False)
	ORD_SEND_EMAIL = base.CharField(label="Sipariş formunun E-mail adresine gönderilmesi", table="LG_CLCARD",field="ORDSENDEMAILADDR",max_length=31,required=False)
	ORD_SEND_FAX = base.CharField(label="Sipariş formunun faks numarasına gönderilmesi", table="LG_CLCARD",field="ORDSENDFAXNR",max_length=16,required=False)
	DSP_SEND_METHOD = base.IntegerField(label="Makbuz/İrsaliye gönderme metodu", table="LG_CLCARD",field="DSPSENDMETHOD",required=False)
	DSP_SEND_EMAIL = base.CharField(label="Makbuz/İrsaliyenin mail adresine gönderilmesi", table="LG_CLCARD",field="DSPSENDEMAILADDR",max_length=31,required=False)
	DSP_SEND_FAX = base.CharField(label="Makbuz/İrsaliyenin faks numarasına gönderilmesi", table="LG_CLCARD",field="DSPSENDFAXNR",max_length=16,required=False)
	INV_SEND_METHOD = base.IntegerField(label="Fatura Formunu gönderme metodu", table="LG_CLCARD",field="INVSENDMETHOD",required=False)
	INV_SEND_EMAIL = base.CharField(label="Faturanın mail adresine gönderilmesi", table="LG_CLCARD",field="INVSENDEMAILADDR",max_length=31,required=False)
	INV_SEND_FAX = base.CharField(label="Faturanın Faks numarasına gönderilmesi", table="LG_CLCARD",field="INVSENDFAXNR",max_length=16,required=False)
	ORD_RISK_TOTAL = base.FloatField(label="Sipariş kredi limiti", table="LG_CLRNUMS",field="ORDRISKTOTAL",required=False)
	ORD_RISK_TOTAL_SUGG = base.FloatField(label="Sipariş kredi limiti (Öneri)", table="LG_CLRNUMS",field="ORDRISKTOTALSUGG",required=False)
	REP_ORD_RISK_TOTAL = base.FloatField(label="Sipariş kredi limiti (Raporlama Dövizi)", table="LG_CLRNUMS",field="REPORDRISKTOTAL",required=False)
	ORD_RISK_TOTAL_SUGG = base.FloatField(label="Sipariş kredi limiti (Raporlama Dövizi) (Öneri)", table="LG_CLRNUMS",field="REPORDRISKTOTALSUGG",required=False)


class ClCard(base.Serializer):
	"""
		Cari hesap kartları
	"""
	class Meta:
		XML_ROOT = 'AR_APS'
		XML_SUBROOT = 'AR_AP'
		DATA_OBJECT = 'doAccountsRP'
		REST_ENDPOINT = 'Arps'
		RELATED_TABLE = 'LG_CLCARD'

	RECORD_STATUS = base.IntegerField(label="Kayıt statüsü", table="LG_CLCARD",field="ACTIVE",required=False)
	ACCOUNT_TYPE = base.IntegerField(label="Kayıt tipi", table="LG_CLCARD",field="CARDTYPE",required=True)
	CODE = base.CharField(label="Cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=True)
	TITLE = base.CharField(label="Cari hesap ünvanı", table="LG_CLCARD",field="DEFINITION_",max_length=180,required=False, allow_blank=True)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_CLCARD",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_CLCARD",field="CYPHCODE",max_length=11,required=False)
	ADDRESS1 = base.CharField(label="Adres 1", table="LG_CLCARD",field="ADDR1",max_length=255,required=False)
	ADDRESS2 = base.CharField(label="Adres 2", table="LG_CLCARD",field="ADDR2",max_length=255,required=False)
	DISTRICT_CODE = base.CharField(label="Semt Kodu", table="LG_CLCARD",field="DISTRICTCODE",max_length=13,required=False)
	DISTRICT = base.CharField(label="Semt Açıklaması", table="LG_CLCARD",field="DISTRICT",max_length=51,required=False)
	TOWN_CODE = base.CharField(label="İlçe Kodu", table="LG_CLCARD",field="TOWNCODE",max_length=13,required=False)
	TOWN = base.CharField(label="İlçe", table="LG_CLCARD",field="TOWN",max_length=51,required=False)
	CITY_CODE = base.CharField(label="Şehir Kodu", table="LG_CLCARD",field="CITYCODE",max_length=13,required=False)
	CITY = base.CharField(label="Şehir", table="LG_CLCARD",field="CITY",max_length=51,required=False)
	COUNTRY_CODE = base.CharField(label="Ülke Kodu", table="LG_CLCARD",field="COUNTRYCODE",max_length=13,required=False)
	COUNTRY = base.CharField(label="Ülke", table="LG_CLCARD",field="COUNTRY",max_length=21,required=False)
	POSTAL_CODE = base.CharField(label="Posta kodu", table="LG_CLCARD",field="POSTCODE",max_length=11,required=False)
	TELEPHONE1 = base.CharField(label="Telefon 1", table="LG_CLCARD",field="TELNRS1",max_length=16,required=False)
	TELEPHONE2 = base.CharField(label="Telefon 2", table="LG_CLCARD",field="TELNRS2",max_length=16,required=False)
	FAX = base.CharField(label="Faks", table="LG_CLCARD",field="FAXNR",max_length=16,required=False)
	TAX_ID = base.CharField(label="Vergi numarası", table="LG_CLCARD",field="TAXNR",max_length=16,required=False)
	TAX_OFFICE = base.CharField(label="Vergi dairesi", table="LG_CLCARD",field="TAXOFFICE",max_length=30,required=False)
	TAX_OFFICE_CODE = base.CharField(label="Vergi Dairesi Kodu", table="LG_CLCARD",field="TAXOFFCODE",max_length=17,required=False)
	CONTACT = base.CharField(label="İlgili", table="LG_CLCARD",field="INCHARGE",max_length=21,required=False)
	DISCOUNT_RATE = base.CharField(label="İndirim oranı", table="LG_CLCARD",field="DISCRATE",max_length=8,required=False)
	PAYMENT_CODE = base.CharField(label="Ödeme Plan Kodu", table="LG_PAYPLANS",field="CODE",max_length=17,required=False)
	E_MAIL = base.CharField(label="E-mail", table="LG_CLCARD",field="EMAILADDR",max_length=251,required=False)
	WEB_URL = base.CharField(label="Web", table="LG_CLCARD",field="WEBADDR",max_length=101,required=False)
	REMINDER_TYPE = base.IntegerField(label="İhtar türü", table="LG_CLCARD",field="WARNMETHOD",required=False)
	REMINDER_EMAIL = base.CharField(label="İhtar adresi -E_mail", table="LG_CLCARD",field="WARNEMAILADDR",max_length=31,required=False)
	REMINDER_FAX = base.CharField(label="İhtar şekli - Faks", table="LG_CLCARD",field="WARNFAXNR",max_length=16,required=False)
	CORRESP_LANG = base.IntegerField(label="Yazışma dili", table="LG_CLCARD",field="CLANGUAGE",required=False)
	VAT_ID = base.CharField(label="KDV no", table="LG_CLCARD",field="VATNR",max_length=33,required=False)
	BLOCKED = base.CharField(label="Durduruldu", table="LG_CLCARD",field="BLOCKED",max_length=2,required=False)
	BANK_ID1 = base.CharField(label="Banka numarası 1", table="LG_CLCARD",field="BANKBRANCHS1",max_length=17,required=False)
	BANK_ID2 = base.CharField(label="Banka numarası 2", table="LG_CLCARD",field="BANKBRANCHS2",max_length=17,required=False)
	BANK_ID3 = base.CharField(label="Banka numarası 3", table="LG_CLCARD",field="BANKBRANCHS3",max_length=17,required=False)
	BANK_ID4 = base.CharField(label="Banka numarası 4", table="LG_CLCARD",field="BANKBRANCHS4",max_length=17,required=False)
	BANK_ID5 = base.CharField(label="Banka numarası 5", table="LG_CLCARD",field="BANKBRANCHS5",max_length=17,required=False)
	BANK_ID6 = base.CharField(label="Banka numarası 6", table="LG_CLCARD",field="BANKBRANCHS6",max_length=17,required=False)
	BANK_ID7 = base.CharField(label="Banka numarası 7", table="LG_CLCARD",field="BANKBRANCHS7",max_length=17,required=False)
	BANK_ACCOUNT1 = base.CharField(label="Banka hesap numarası 1", table="LG_CLCARD",field="BANKACCOUNTS1",max_length=17,required=False)
	BANK_ACCOUNT2 = base.CharField(label="Banka hesap numarası 2", table="LG_CLCARD",field="BANKACCOUNTS2",max_length=17,required=False)
	BANK_ACCOUNT3 = base.CharField(label="Banka hesap numarası 3", table="LG_CLCARD",field="BANKACCOUNTS3",max_length=17,required=False)
	BANK_ACCOUNT4 = base.CharField(label="Banka hesap numarası 4", table="LG_CLCARD",field="BANKACCOUNTS4",max_length=17,required=False)
	BANK_ACCOUNT5 = base.CharField(label="Banka hesap numarası 5", table="LG_CLCARD",field="BANKACCOUNTS5",max_length=17,required=False)
	BANK_ACCOUNT6 = base.CharField(label="Banka hesap numarası 6", table="LG_CLCARD",field="BANKACCOUNTS6",max_length=17,required=False)
	BANK_ACCOUNT7 = base.CharField(label="Banka hesap numarası 7", table="LG_CLCARD",field="BANKACCOUNTS7",max_length=17,required=False)
	DELIVERY_METHOD = base.CharField(label="Teslim şekli", table="LG_CLCARD",field="DELIVERYMETHOD",max_length=13,required=False)
	SHIPMENT_AGENT = base.CharField(label="Taşıyıcı firma", table="LG_CLCARD",field="DELIVERYFIRM",max_length=13,required=False)
	CURRENCY = base.IntegerField(label="Döviz", table="LG_CLCARD",field="CCURRENCY",required=False)
	E_COMM_ID = base.CharField(label="Veri aktarım ID", table="LG_CLCARD",field="EDINO",max_length=25,required=False)
	TRADING_GRP = base.CharField(label="Ticari işlem grubu", table="LG_CLCARD",field="TRADINGGRP",max_length=17,required=False)
	DEBT_TRCK_TYPE = base.IntegerField(label="Ödeme izleme türü", table="LG_CLCARD",field="PAYMENTPROC",required=False)
	XRTDIF_TYPE = base.IntegerField(label="Kur farkı hesabı", table="LG_CLCARD",field="CRATEDIFFPROC",required=False)

	CL_ORD_FREQ = base.IntegerField(label="?", required=False)
	ORD_DAY = base.IntegerField(label="?", required=False)
	PURCHBRWS = base.IntegerField(label="?", required=False)
	SALESBRWS = base.IntegerField(label="?", required=False)
	IMPBRWS = base.IntegerField(label="?", required=False)
	EXPBRWS = base.IntegerField(label="?", required=False)
	FINBRWS = base.IntegerField(label="?", required=False)
	COLLATRLRISK_TYPE = base.IntegerField(label="?", required=False)
	RISK_TYPE1 = base.IntegerField(label="?", required=False)
	RISK_TYPE2 = base.IntegerField(label="?", required=False)
	RISK_TYPE3 = base.IntegerField(label="?", required=False)
	TCKNO = base.CharField(label="T.C. kimlik numarası", table="LG_CLCARD", field="TCKNO", max_length=16, required=False)
	NAME = base.CharField(label="Ad", table="LG_CLCARD", field="NAME", max_length=31, required=False)
	SURNAME = base.CharField(label="Soyad", table="LG_CLCARD", field="SURNAME", max_length=31, required=False)
	PERSCOMPANY = base.IntegerField(label="Şahıs şirketi", table="LG_CLCARD", field="ISPERSCOMP", required=False)
	ACCEPT_EINV = base.IntegerField(label="e-Fatura", required=False)
	EARCHIVE_IS_RETAIL_AR_AP = base.IntegerField(label="?", required=False)
	FBS_SEND_EMAILADDR = base.CharField(label="?", required=False)
	FBA_SEND_EMAILADDR = base.CharField(label="?", required=False)

	POST_LABEL = base.CharField(label="?", required=False)
	SENDER_LABEL = base.CharField(label="?", required=False)
	ACCEPT_DESP = base.CharField(label="?", required=False)
	POST_LABEL_CODE_DESP = base.CharField(label="?", required=False)
	SENDER_LABEL_CODE_DESP = base.CharField(label="?", required=False)
	GL_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)


	# subs
	NOTES = ClCardNotes(required=False)
