"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class OrderDetails(base.BaseSerialiazer):
	TYPE = base.IntegerField(label="Tür", table="LG_ORFLINE",field="LINETYPE",min_value=0, max_value=1,required=False)
	MASTER_CODE = base.CharField(label="Ana ürün kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	DETAIL_LEVEL = base.IntegerField(label="Detay seviyesi", table="LG_ORFLINE",field="DETLINE",min_value=0, max_value=1,required=False)
	CALC_TYPE = base.IntegerField(label="Hesaplama türü", table="LG_ORFLINE",field="CALCTYPE",min_value=0, max_value=1,required=False)
	OHP_CODE1 = base.CharField(label="Masraf merkezi kodu 1", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE1 = base.CharField(label="Muhasebe hesap kodu 1", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	GL_CODE2 = base.CharField(label="Muhasebe hesap kodu 2", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE2 = base.CharField(label="Masraf merkezi kodu 2", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_ORFLINE",field="SPECODE",max_length=17,required=False)
	DELVRY_CODE = base.CharField(label="Teslimat kodu", table="LG_ORFLINE",field="DELVRYCODE",max_length=5,required=False)
	QUANTITY = base.FloatField(label="Miktar", table="LG_ORFLINE",field="AMOUNT",required=False)
	PRICE = base.FloatField(label="Birim fiyat", table="LG_ORFLINE",field="PRICE",required=False)
	TOTAL = base.FloatField(label="Toplam", table="LG_ORFLINE",field="TOTAL",required=False)
	QUANTITY_SHIPPED = base.FloatField(label="Teslim edilen miktar", table="LG_ORFLINE",field="SHIPPEDAMOUNT",required=False)
	DISCOUNT_RATE = base.FloatField(label="İskonto oranı", table="LG_ORFLINE",field="DISCPER",required=False)
	COST_DISTR = base.FloatField(label="Dağıtılan maliyet", table="LG_ORFLINE",field="DISTCOST",required=False)
	DISCOUNT_DISTR = base.FloatField(label="Dağıtılan indirim", table="LG_ORFLINE",field="DISTDISC",required=False)
	EXPENSE_DISTR = base.FloatField(label="Dağıtılan masraf", table="LG_ORFLINE",field="DISTEXP",required=False)
	PROMOTION_DISTR = base.FloatField(label="Dağıtılan promosyon", table="LG_ORFLINE",field="DISTPROM",required=False)
	VAT_RATE = base.FloatField(label="KDV oranı", table="LG_ORFLINE",field="VAT",required=False)
	TRANS_DESCRIPTION = base.CharField(label="Hareket açıklaması", table="LG_ORFLINE",field="LINEEXP",max_length=31,required=False)
	UNIT_CODE = base.CharField(label="Birim kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	UNIT_CONV1 = base.FloatField(label="Birim çevrimi1", table="LG_ORFLINE",field="UINFO1",required=False)
	UNIT_CONV2 = base.FloatField(label="Birim çevrimi2", table="LG_ORFLINE",field="UINFO2",required=False)
	UNIT_CONV3 = base.FloatField(label="Birim çevrimi3", table="LG_ORFLINE",field="UINFO3",required=False)
	UNIT_CONV4 = base.FloatField(label="Birim çevrimi4", table="LG_ORFLINE",field="UINFO4",required=False)
	UNIT_CONV5 = base.FloatField(label="Birim çevrimi5", table="LG_ORFLINE",field="UINFO5",required=False)
	UNIT_CONV6 = base.FloatField(label="Birim çevrimi6", table="LG_ORFLINE",field="UINFO6",required=False)
	UNIT_CONV7 = base.FloatField(label="Birim çevrimi7", table="LG_ORFLINE",field="UINFO7",required=False)
	UNIT_CONV8 = base.FloatField(label="Birim çevrimi8", table="LG_ORFLINE",field="UINFO8",required=False)
	VAT_INCLUDED = base.IntegerField(label="KDV dahil / hariç", table="LG_STLINE",field="VATINC",min_value=0, max_value=1,required=False)
	ORDER_CLOSED = base.IntegerField(label="Kapanan siparişler", table="LG_ORFLINE",field="CLOSED",min_value=0, max_value=1,required=False)
	ORDER_RESERVE = base.IntegerField(label="Sipariş rezerve durumu", table="LG_ORFLINE",field="DORESERVE",min_value=0, max_value=1,required=False)
	DUE_DATE = base.IntegerField(label="Vade tarihi", table="LG_ORFLINE",field="DUEDATE",required=False)
	CURR_PRICE = base.IntegerField(label="Dövizli birim fiyat", table="LG_ORFLINE",field="PRCURR",min_value=0, max_value=1,required=False)
	PC_PRICE = base.FloatField(label="Fiyatlandırma dövizi", table="LG_ORFLINE",field="PRPRICE",required=False)
	RC_XRATE = base.FloatField(label="Raporlama dövizi kuru", table="LG_ORFLINE",field="REPORTRATE",required=False)
	PAYMENT_CODE = base.CharField(label="Ödeme planı kodu", table="LG_PAYPLANS",field="CODE",max_length=17,required=False)
	COMPOSITE = base.IntegerField(label="Karma koli", table="LG_ORFLINE",field="CPSTFLAG",min_value=0, max_value=1,required=False)
	SOURCE_WH = base.IntegerField(label="Kaynak ambar", table="LG_ORFLINE",field="SOURCEINDEX",required=False)
	SOURCE_COST_GRP = base.IntegerField(label="Kaynak maliyet grubu", table="LG_ORFLINE",field="SOURCECOSTGRP",required=False)
	DIVISION = base.IntegerField(label="İşyeri", table="LG_ORFLINE",field="BRANCH",required=False)
	DEPARTMENT = base.IntegerField(label="Bölüm", table="LG_ORFLINE",field="DEPARTMENT",required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_ORFLINE",field="SITEID",required=False)
	FACTORY = base.IntegerField(label="Fabrika", table="LG_ORFLINE",field="FACTORYNR",required=False)
	REASON_FOR_NOT_SHP = base.IntegerField(label="Reason For Not Shipment", table="LG_ORFLINE",field="REASONFORNOTSHP",required=False)

class OrderCampaignInfos(base.BaseSerialiazer):
	CAMPCODE1 = base.CharField(label="Kod1", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE2 = base.CharField(label="Kod2", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE3 = base.CharField(label="Kod3", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE4 = base.CharField(label="Kod4", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE5 = base.CharField(label="Kod5", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMP_LN_NO = base.IntegerField(label="Satır Numarası", table="LG_CMPGNLINE",field="LINENR",required=False)
	CAMPAIGN_POINT = base.FloatField(label="Kampanya Noktası", table="LG_ORFLINE",field="CAMPPOINT",required=False)
	PROM_CLAS_ITEM_CODE = base.CharField(label="Malzeme Kart Kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	GROSS_U_INFO1 = base.FloatField(label="Brüt Hacim", table="LG_STLINE",field="GROSSUINFO1",required=False)
	GROSS_U_INFO2 = base.FloatField(label="Brüt Ağırlık", table="LG_STLINE",field="GROSSUINFO2",required=False)
	CUST_ORD_NO = base.CharField(label="Müşteri Sipariş Fiş Numarası", table="LG_ORFICHE",field="CUSTORDNO",max_length=25,required=False)
	DLV_CLIENT = base.IntegerField(label="Sevkiyat Adresi Müşteri Türü", table="LG_ORFICHE",field="DLVCLIENT",min_value=0, max_value=1,required=False)

class OrderTransactions(base.BaseSerialiazer):
	TYPE = base.IntegerField(label="Tür", table="LG_ORFLINE",field="LINETYPE",min_value=0, max_value=20,required=False)
	MASTER_CODE = base.CharField(label="Ana ürün kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	DETAIL_LEVEL = base.IntegerField(label="Detay seviyesi", table="LG_ORFLINE",field="DETLINE",min_value=0, max_value=1,required=False)
	CALC_TYPE = base.IntegerField(label="Hesaplama türü", table="LG_ORFLINE",field="CALCTYPE",min_value=0, max_value=1,required=False)
	OHP_CODE1 = base.CharField(label="Masraf merkezi 1", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE1 = base.CharField(label="Muhasebe hesap kodu 1", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	GL_CODE2 = base.CharField(label="Muhasebe hesap kodu 2", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE2 = base.CharField(label="Masraf merkezi kodu 2", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE3 = base.CharField(label="Muhasebe hesap kodu 3", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE3 = base.CharField(label="Masraf merkezi kodu 3", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE4 = base.CharField(label="Muhasebe hesap kodu 3", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE4 = base.CharField(label="Masraf merkezi kodu 4", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_ORFLINE",field="SPECODE",max_length=17,required=False)
	DELVRY_CODE = base.CharField(label="Teslimat kodu", table="LG_ORFLINE",field="DELVRYCODE",max_length=5,required=False)
	QUANTITY = base.FloatField(label="Miktar", table="LG_ORFLINE",field="AMOUNT",required=False)
	PRICE = base.FloatField(label="Birim fiyat", table="LG_ORFLINE",field="PRICE",required=False)
	TOTAL = base.FloatField(label="Toplam", table="LG_ORFLINE",field="TOTAL",required=False)
	QUANTITY_SHIPPED = base.FloatField(label="Teslim edilen miktar", table="LG_ORFLINE",field="SHIPPEDAMOUNT",required=False)
	DISCOUNT_RATE = base.FloatField(label="Dağılım yüzdesi", table="LG_ORFLINE",field="DISCPER",required=False)
	COST_DISTR = base.FloatField(label="Dağıtılan maliyet", table="LG_ORFLINE",field="DISTCOST",required=False)
	DISCOUNT_DISTR = base.FloatField(label="Dağıtılan indirim", table="LG_ORFLINE",field="DISTDISC",required=False)
	EXPENSE_DISTRB = base.FloatField(label="Masraf dağıtımı", table="LG_STLINE",field="DISTEXP",required=False)
	PROMOTION_DISTR = base.FloatField(label="Dağıtılan promosyon", table="LG_STLINE",field="DISTPROM",required=False)
	VAT_RATE = base.FloatField(label="KDV yüzdesi", table="LG_ORFLINE",field="VAT",required=False)
	TRANS_DESCRIPTION = base.CharField(label="Hareket açıklaması", table="LG_ORFLINE",field="LINEEXP",max_length=31,required=False)
	UNIT_CODE = base.CharField(label="Malzeme kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	UNIT_CONV1 = base.FloatField(label="Birim çevrimi1", table="LG_ORFLINE",field="UINFO1",required=False)
	UNIT_CONV2 = base.FloatField(label="Birim çevrimi2", table="LG_ORFLINE",field="UINFO2",required=False)
	UNIT_CONV3 = base.FloatField(label="Birim çevrimi3", table="LG_ORFLINE",field="UINFO3",required=False)
	UNIT_CONV4 = base.FloatField(label="Birim çevrimi4", table="LG_ORFLINE",field="UINFO4",required=False)
	UNIT_CONV5 = base.FloatField(label="Birim çevrimi5", table="LG_ORFLINE",field="UINFO5",required=False)
	UNIT_CONV6 = base.FloatField(label="Birim çevrimi6", table="LG_ORFLINE",field="UINFO6",required=False)
	UNIT_CONV7 = base.FloatField(label="Birim çevrimi7", table="LG_ORFLINE",field="UINFO7",required=False)
	UNIT_CONV8 = base.FloatField(label="Birim çevrimi8", table="LG_ORFLINE",field="UINFO8",required=False)
	VAT_INCLUDED = base.IntegerField(label="KDV dahil/Hariç", table="LG_ORFLINE",field="VATINC",min_value=0, max_value=1,required=False)
	ORDER_CLOSED = base.IntegerField(label="Kapanan sipariler", table="LG_ORFLINE",field="CLOSED",min_value=0, max_value=1,required=False)
	ORDER_RESERVE = base.IntegerField(label="Sipariş rezerve durumu", table="LG_ORFLINE",field="DORESERVE",min_value=0, max_value=1,required=False)
	DUE_DATE = base.CharField(label="Teslim tarihi", table="LG_ORFLINE",field="DUEDATE",required=False)
	CURR_PRICE = base.IntegerField(label="Dövizli diyat", table="LG_ORFLINE",field="PRCURR",min_value=0, max_value=1,required=False)
	PC_PRICE = base.FloatField(label="Fiyatlandırma dövizi", table="LG_ORFLINE",field="PRPRICE",required=False)
	RC_XRATE = base.FloatField(label="Raporlama dövizi kuru", table="LG_ORFLINE",field="REPORTRATE",required=False)
	PAYMENT_CODE = base.CharField(label="Ödeme plan kodu", table="LG_PAYPLANS",field="CODE",max_length=17,required=False)
	COMPOSITE = base.IntegerField(label="Karma koli", table="LG_ORFLINE",field="CPSTFLAG",min_value=0, max_value=1,required=False)
	SOURCE_WH = base.IntegerField(label="Kaynak ambar", table="LG_ORFLINE",field="SOURCEINDEX",required=False)
	SOURCE_COST_GRP = base.IntegerField(label="Kaynak maliyet grubu", table="LG_ORFLINE",field="SOURCECOSTGRP",required=False)
	DIVISION = base.IntegerField(label="İşyeri", table="LG_ORFLINE",field="BRANCH",required=False)
	DEPARTMENT = base.IntegerField(label="Bölüm", table="LG_ORFLINE",field="DEPARTMENT",required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_ORFLINE",field="SITEID",required=False)
	FACTORY = base.IntegerField(label="Fabrika", table="LG_ORFLINE",field="FACTORYNR",required=False)
	NET_DSC_FLAG = base.IntegerField(label="Nete uygulanan indirim ve tutar işareti", table="LG_STLINE",field="NETDISCFLAG",min_value=0, max_value=1,required=False)
	NET_DSC_RATE = base.FloatField(label="Net indirim oranı (%)", table="LG_STLINE",field="NETDISCPERC",required=False)
	NET_DSC_AMOUNT = base.FloatField(label="Net indirim tutarı (%)", table="LG_STLINE",field="NETDISCAMNT",required=False)

	VATEXCEPT_REASON = base.CharField(label="KDV istisna nedeni",required=False,max_length=200)
	VATEXCEPT_CODE = base.CharField(label="KDV istisna kodu", required=False,max_length=10)

	AUXIL_CODE2 = base.CharField(label="Özel kod 2", table="LG_ORFLINE",field="SPECODE2",max_length=17,required=False)


	# subs
	#DETAILS = base.serializers.ListSerializer(child=OrderDetails())
	#CAMPAIGN_INFOS = base.serializers.ListSerializer(child=OrderCampaignInfos())

class OrderTransactionHolder(base.BaseSerialiazer):
	items = base.serializers.ListSerializer(child=OrderTransactions())


class BaseOrder(base.Serializer):
	NUMBER = base.CharField(label="Fiş numarası", table="LG_ORFICHE",field="FICHENO",max_length=16,required=False)
	DOC_TRACK_NR = base.CharField(label="Doküman izleme numarası", table="LG_INVOICE",field="DOCTRACKINGNR",max_length=21,required=False)
	DATE = base.CharField(label="Fiş tarihi", table="LG_ORFICHE",field="DATE_",required=True)
	TIME = base.IntegerField(label="Fiş kayıt zamanı", table="LG_ORFICHE",field="TIME_",required=False)
	DOC_NUMBER = base.CharField(label="Fiş belge numarası", table="LG_ORFICHE",field="DOCODE",max_length=32,required=False)
	AUXIL_CODE = base.CharField(label="Fiş özel kodu", table="LG_ORFICHE",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Fiş yetki kodu", table="LG_ORFICHE",field="CYPHCODE",max_length=11,required=False)
	ARP_CODE = base.CharField(label="Cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)
	ARP_CODE_SHPM = base.CharField(label="Sevk edilen cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)
	SHIPLOC_CODE = base.CharField(label="Kod", table="LG_SHIPINFO",field="CODE",max_length=25,required=False)
	GL_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	SOURCE_WH = base.IntegerField(label="Kaynak ambar kodu", table="LG_ORFICHE",field="SOURCEINDEX",required=False)
	SOURCE_COST_GRP = base.IntegerField(label="Kaynak maliyet grubu", table="LG_ORFICHE",field="SOURCECOSTGRP",required=False)
	ADD_DISCOUNTS = base.FloatField(label="Fiş feneline ait ek indirimler", table="LG_ORFICHE",field="ADDDISCOUNTS",required=False)
	TOTAL_DISCOUNTS = base.FloatField(label="Toplam indirimler", table="LG_ORFICHE",field="TOTALDISCOUNTS",required=False)
	ADD_EXPENSES = base.FloatField(label="Fiş geneline ait ek masraflar", table="LG_ORFICHE",field="ADDEXPENSES",required=False)
	TOTAL_EXPENSES = base.FloatField(label="Toplam masraflar", table="LG_ORFICHE",field="TOTALEXPENSES",required=False)
	TOTAL_PROMOTIONS = base.FloatField(label="Toplam promosyonlar", table="LG_ORFICHE",field="TOTALPROMOTIONS",required=False)
	RC_RATE = base.FloatField(label="Raporlama dövizi kuru", table="LG_ORFICHE",field="REPORTRATE",required=False)
	NOTES1 = base.CharField(label="Açıklama1", table="LG_ORFICHE",field="GENEXP1",max_length=50,required=False)
	NOTES2 = base.CharField(label="Açıklama2", table="LG_ORFICHE",field="GENEXP2",max_length=50,required=False)
	NOTES3 = base.CharField(label="Açıklama3", table="LG_ORFICHE",field="GENEXP3",max_length=50,required=False)
	NOTES4 = base.CharField(label="Açıklama4", table="LG_ORFICHE",field="GENEXP4",max_length=50,required=False)
	NOTES5 = base.CharField(label="Açıklama5", table="LG_ORFICHE",field="GENEXP5",max_length=50,required=False)
	NOTES6 = base.CharField(label="Açıklama6", table="LG_ORFICHE",field="GENEXP6",max_length=50,required=False)
	PAYMENT_CODE = base.CharField(label="Ödeme planı kodu", table="LG_PAYPLANS",field="CODE",max_length=17,required=False)
	PAYDEFREF = base.IntegerField(label="Ödeme tanımı referansı", table="LG_ORFICHE",field="PAYDEFREF",required=False)
	PRINT_COUNTER = base.IntegerField(label="Basım sayısı", table="LG_ORFICHE",field="PRINTCNT",required=False)
	DIVISION = base.IntegerField(label="İşyeri", table="LG_ORFICHE",field="BRANCH",required=False)
	DEPARTMENT = base.IntegerField(label="Bölüm", table="LG_ORFICHE",field="DEPARTMENT",required=False)
	ORDER_STATUS = base.IntegerField(label="Sipariş statüsü", table="LG_ORFICHE",field="STATUS",required=False)
	SALESMAN_CODE = base.CharField(label="Satış elemanı kodu", table="LG_SLSMAN",field="CODE",max_length=25,required=False)
	SHIPMENT_TYPE = base.CharField(label="Sevkiyat türü", table="LG_ORFICHE",field="SHPTYPCOD",max_length=13,required=False)
	SHIPPING_AGENT = base.CharField(label="Taşıyıcı kodu", table="LG_ORFICHE",field="SHPAGNCOD",max_length=13,required=False)
	CURRSEL_TOTALS = base.IntegerField(label="Genel Döviz Türü", table="LG_ORFICHE",field="GENEXCTYP",required=False)
	CURRSEL_DETAILS = base.IntegerField(label="Satır Döviz Türü", table="LG_ORFICHE",field="LINEEXCTYP",required=False)
	TRADING_GROUP = base.CharField(label="Ticari işlem grubu", table="LG_ORFICHE",field="TRADINGGRP",max_length=17,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_ORFICHE",field="SITEID",required=False)
	FACTORY = base.IntegerField(label="Fabrika", table="LG_ORFICHE",field="FACTORYNR",required=False)
	PROJECT_CODE = base.CharField(label="Proje kodu",table="LG_PROJECT",field="CODE",max_length=100,required=False)
	CANCELLED = base.IntegerField(label="İptal edildi", table="LG_ORFICHE",field="CANCELLED",min_value=0, max_value=1,required=False)
	VATEXCEPT_REASON = base.CharField(label="KDV istisna nedeni",required=False,max_length=200)
	VATEXCEPT_CODE = base.CharField(label="KDV istisna kodu", required=False,max_length=10)

	EINVOICE = base.IntegerField(label='E-tip', required=False)
	EARCHIVEDETR_INTSALESADDR = base.CharField(label="", required=False, max_length=60)
	EARCHIVEDETR_EARCHIVESTATUS = base.IntegerField(label="", required=False)
	EARCHIVEDETR_SENDMOD = base.IntegerField(label="", required=False)
	PROFILE_ID = base.IntegerField(label="", required=False)
	EINVOICE_TYPE = base.IntegerField(label='E-tip', table="LG_INVOICE",field="?",required=False)

	EARCHIVEDETR_INTPAYMENTDATE	= base.CharField(label="", required=False)
	EARCHIVEDETR_INTPAYMENTTYPE = base.IntegerField(label="", required=False)
	EARCHIVEDETR_INTPAYMENTAGENT = base.CharField(label='Paying Agent', required=False)
	EARCHIVEDETR_INSTALLMENTNUMBER = base.CharField(
		label='Installation Number / Tesisat numarası', 
		required=False
	)

	ORIGINAL_DATE = base.CharField(label='Orjinal fiş tarihi', table='LG_ORFICHE', field='ORGDATE', required=False)



class BaseOrderForJSON(BaseOrder):
	TRANSACTIONS = OrderTransactionHolder(required=False)

class BaseOrderForXML(BaseOrder):
	TRANSACTIONS = base.serializers.ListSerializer(child=OrderTransactions())

class PurchaseOrder(BaseOrderForJSON):
	"""
		Alış sipariş
	"""
	class Meta:
		XML_ROOT = "PURCHASE_ORDERS"
		XML_SUBROOT = "ORDER_SLIP"
		DATA_OBJECT = "doPurchOrderSlip"
		REST_ENDPOINT = "purchaseOrders"
		RELATED_TABLE = 'LG_ORFICHE'

class SalesOrder(BaseOrderForJSON):
	"""
		Satış sipariş
	"""
	class Meta:
		XML_ROOT = "SALES_ORDERS"
		XML_SUBROOT = "ORDER_SLIP"
		DATA_OBJECT = "doSalesOrderSlip"
		REST_ENDPOINT = "salesOrders"
		RELATED_TABLE = 'LG_ORFICHE'



class PurchaseOrderXML(BaseOrderForXML):
	"""
		Alış sipariş
	"""
	class Meta:
		XML_ROOT = "PURCHASE_ORDERS"
		XML_SUBROOT = "ORDER_SLIP"
		DATA_OBJECT = "doPurchOrderSlip"
		REST_ENDPOINT = "purchaseOrders"
		RELATED_TABLE = 'LG_ORFICHE'

class SalesOrderXML(BaseOrderForXML):
	"""
		Satış sipariş
	"""
	class Meta:
		XML_ROOT = "SALES_ORDERS"
		XML_SUBROOT = "ORDER_SLIP"
		DATA_OBJECT = "doSalesOrderSlip"
		REST_ENDPOINT = "salesOrders"
		RELATED_TABLE = 'LG_ORFICHE'
