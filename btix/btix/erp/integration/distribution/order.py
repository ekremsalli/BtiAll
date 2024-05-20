"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class DistOrderCampaignInfos(base.BaseSerialiazer):
	CAMPCODE1 = base.CharField(label="Kod1", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE2 = base.CharField(label="Kod2", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE3 = base.CharField(label="Kod3", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE4 = base.CharField(label="Kod4", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE5 = base.CharField(label="Kod5", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	PCAMPCODE = base.CharField(label="Kod6", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMP_LN_NO = base.IntegerField(label="Satır Numarası", table="LG_CMPGNLINE",field="LINENR",required=False)
	PROM_CLAS_ITEM_CODE = base.CharField(label="Malzeme Kart Kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	ROUT_CODE = base.CharField(label="Rota Kodu", table="LG_DISTROUTING",field="CODE",max_length=25,required=False)
	VEHICLECODE = base.CharField(label="Araç Kodu", table="LG_DISTVEHICLE",field="CODE",max_length=25,required=False)
	W_CAPACITY = base.FloatField(label="Ağırlık", table="LG_DISTVEHICLE",field="WEIGHT",required=False)
	V_CAPACITY = base.FloatField(label="Hacim", table="LG_DISTVEHICLE",field="VOLUME_",required=False)
	P_CAPACITY = base.FloatField(label="Score", table="LG_DISTVEHICLE",field="SCORE",required=False)
	SALESMAN_CODE = base.CharField(label="Satış Elemanı Kodu", table="LG_SLSMAN",field="CODE",max_length=25,required=False)

class DistOrderSlDetails(base.BaseSerialiazer):
	SOURCE_MT_SITEID = base.IntegerField(label="Item Transaction Logical Reference", table="LG_STLINE",field="LOGICALREF",required=False)
	SOURCE_MT_REFERENCE = base.IntegerField(label="Item Transaction Logical Reference", table="LG_STLINE",field="LOGICALREF",required=False)
	SOURCE_SLT_SITEID = base.IntegerField(label="Lot / Serial Transaction Logical Reference", table="LG_SLTRANS",field="LOGICALREF",required=False)
	SOURCE_SLT_REFERENCE = base.IntegerField(label="Lot / Serial Transaction Logical Reference", table="LG_SLTRANS",field="LOGICALREF",required=False)
	SOURCE_QUANTITY = base.FloatField(label="Quantity From Input Transaction Unit", table="LG_SLTRANS",field="INSLAMOUNT",required=False)
	SOURCE_WH = base.IntegerField(label="Ambar Numarası", table="LG_SLTRANS",field="INVENNO",required=False)
	SL_TYPE = base.IntegerField(label="Seri / Lot Türü; (1 Lot; 2 Seri)", table="LG_SLTRANS",field="SLTYPE",required=False)
	SL_CODE = base.CharField(label="Lot / Seri Kodu", table="LG_SERILOTN",field="CODE",max_length=25,required=False)
	LOCATION_CODE = base.CharField(label="Yerleşim Kodu", table="LG_LOCATION",field="CODE",max_length=25,required=False)
	DEST_LOCATION_CODE = base.CharField(label="Stok yeri açıklaması", table="LG_LOCATION",field="NAME",max_length=51,required=False)
	MU_QUANTITY = base.FloatField(label="Ana Birim Miktarı", table="LG_SLTRANS",field="MAINAMOUNT",required=False)
	UNIT_CODE = base.CharField(label="Birim Kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	QUANTITY = base.FloatField(label="Quantity In Line Unit", table="LG_SLTRANS",field="AMOUNT",required=False)
	REM_QUANTITY = base.FloatField(label="Remaining Quantity In Main Unit", table="LG_SLTRANS",field="REMAMOUNT",required=False)
	LU_REM_QUANTITY = base.FloatField(label="Remaining Quantity In Line Unit", table="LG_SLTRANS",field="REMLNUNITAMNT",required=False)
	UNIT_CONV1 = base.FloatField(label="Çevrim Katsayısı1", table="LG_SLTRANS",field="UINFO1",required=False)
	UNIT_CONV2 = base.FloatField(label="Çevrim Katsayısı2", table="LG_SLTRANS",field="UINFO2",required=False)
	UNIT_CONV3 = base.FloatField(label="Çevrim Katsayısı3", table="LG_SLTRANS",field="UINFO3",required=False)
	UNIT_CONV4 = base.FloatField(label="Çevrim Katsayısı4", table="LG_SLTRANS",field="UINFO4",required=False)
	UNIT_CONV5 = base.FloatField(label="Çevrim Katsayısı5", table="LG_SLTRANS",field="UINFO5",required=False)
	UNIT_CONV6 = base.FloatField(label="Çevrim Katsayısı6", table="LG_SLTRANS",field="UINFO6",required=False)
	UNIT_CONV7 = base.FloatField(label="Çevrim Katsayısı7", table="LG_SLTRANS",field="UINFO7",required=False)
	UNIT_CONV8 = base.FloatField(label="Çevrim Katsayısı8", table="LG_SLTRANS",field="UINFO8",required=False)
	DATE_EXPIRED = base.IntegerField(label="Son Kullanım Tarihi", table="LG_SLTRANS",field="EXPDATE",required=False)
	RATE_SCORE = base.IntegerField(label="Notu", table="LG_SLTRANS",field="RATESCORE",required=False)
	OUT_COST = base.FloatField(label="Çıkış Fişleri Çıkış Maliyeti", table="LG_SLTRANS",field="OUTCOST",required=False)
	TC_OUT_COST = base.FloatField(label="Output Vouchers Output Cost In F. Currency", table="LG_SLTRANS",field="OUTCOSTCURR",required=False)
	PRCDIF_COST = base.FloatField(label="Fiyat Farkı Maliyeti", table="LG_SLTRANS",field="DIFFPRCOST",required=False)
	TC_PRCDIF_COST = base.FloatField(label="Cost In F. Currency Because Of Price Difference", table="LG_SLTRANS",field="DIFFPRCOSTCURR",required=False)
	SL_QC_OK = base.IntegerField(label="Kalite Kontrol Uygunluğu", table="LG_SLTRANS",field="SERIQCOK",min_value=0, max_value=1,required=False)
	SOURCE_TYPE = base.IntegerField(label="Kaynak Türü (0-Ambar, 1-İş İstasyonu)", table="LG_SLTRANS",field="SOURCETYPE",min_value=0, max_value=1,required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_SLTRANS",field="SITEID",required=False)
	WF_STATUS = base.IntegerField(label="Kullanım Dışı", table="LG_SLTRANS",field="WFSTATUS",required=False)
	SOURCE_DIST_SL_REFERENCE = base.IntegerField(label="Lot / Serial Transaction Reference in Distribution", table="LG_SLTRANS",field="INDORDSLTRNREF",required=False)
	U_INFO1 = base.FloatField(label="Çevrim Katsayısı1", table="LG_DISTORDLINE",field="UINFO1",required=False)
	U_INFO2 = base.FloatField(label="Çevrim Katsayısı2", table="LG_DISTORDLINE",field="UINFO2",required=False)
	U_INFO3 = base.FloatField(label="Çevrim Katsayısı3", table="LG_DISTORDLINE",field="UINFO3",required=False)
	U_INFO4 = base.FloatField(label="Çevrim Katsayısı4", table="LG_DISTORDLINE",field="UINFO4",required=False)
	U_INFO5 = base.FloatField(label="Çevrim Katsayısı5", table="LG_DISTORDLINE",field="UINFO5",required=False)
	U_INFO6 = base.FloatField(label="Çevrim Katsayısı6", table="LG_DISTORDLINE",field="UINFO6",required=False)
	U_INFO7 = base.FloatField(label="Çevrim Katsayısı7", table="LG_DISTORDLINE",field="UINFO7",required=False)
	U_INFO8 = base.FloatField(label="Çevrim Katsayısı8", table="LG_DISTORDLINE",field="UINFO8",required=False)
	CLIENT_NAME = base.CharField(label="Borçlu/Alacaklı cari Hesap Ünvanı", table="LG_CLCARD",field="DEFINITION_",max_length=51,required=False)
	TOWN_NAME = base.CharField(label="İlçe Adı", table="L_TOWN",field="NAME",max_length=13,required=False)
	DISTRICT_NAME = base.CharField(label="Semt Adı", table="L_DISTRICT",field="NAME",max_length=13,required=False)
	UNIT_CODE = base.CharField(label="Birim Kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_DISTORDLINE",field="SITEID",required=False)

class DistOrderLine(base.BaseSerialiazer):
	LINE_TYPE = base.IntegerField(label="Satır Tipi", table="LG_DISTORDLINE",field="LINETYPE",min_value=0, max_value=1,required=False)
	ORD_SITEID = base.IntegerField(label="Sipariş Fişi Referansı", table="LG_DISTORDLINE",field="ORDFICHEREF",required=False)
	ORD_REFERENCE = base.IntegerField(label="Sipariş Fişi Satır Referansı", table="LG_DISTORDLINE",field="ORDLINEREF",required=False)
	DATE = base.IntegerField(label="Tarih", table="LG_DISTORDLINE",field="DATE_",required=False)
	DUE_DATE = base.IntegerField(label="Shipment Date", table="LG_DISTORDLINE",field="DUEDATE",required=False)
	ORDER_AMOUNT = base.FloatField(label="Sipariş satırındaki kalan tutar", table="LG_DISTORDLINE",field="ORDERAMOUNT",required=False)
	SHIP_AMOUNT = base.FloatField(label="Shipment Amount", table="LG_DISTORDLINE",field="SHIPAMOUNT",required=False)
	REM_AMOUNT = base.FloatField(label="Remaining Amount of Distribution", table="LG_DISTORDLINE",field="REMAMOUNT",required=False)
	COUNTRY_CODE = base.CharField(label="Ülke Kodu", table="LG_DISTORDLINE",field="COUNTRYCODE",max_length=13,required=False)
	CITY_CODE = base.CharField(label="Şehir Kodu", table="LG_DISTORDLINE",field="CITYCODE",max_length=13,required=False)
	TOWN_CODE = base.CharField(label="İlçe Kodu", table="LG_DISTORDLINE",field="TOWNCODE",max_length=13,required=False)
	DISTRICT_CODE = base.CharField(label="Semt Kodu", table="LG_DISTORDLINE",field="DISTRICTCODE",max_length=13,required=False)
	BRANCH = base.IntegerField(label="İşyeri", table="LG_DISTORDLINE",field="BRANCH",required=False)
	DEPARTMENT = base.IntegerField(label="Bölüm", table="LG_DISTORDLINE",field="DEPARTMENT",required=False)
	FACTORY = base.IntegerField(label="Fabrika Numarası", table="LG_DISTORDLINE",field="FACTORY",required=False)
	SOURCE_INDEX = base.IntegerField(label="Ambar Numarası", table="LG_DISTORDLINE",field="SOURCEINDEX",required=False)
	RISK_STATUS = base.IntegerField(label="Risk Durumu; (0 Riskli Değil;1 Riskli)", table="LG_DISTORDLINE",field="RISKSTATUS",required=False)
	ITEM_TRACK_TYPE = base.IntegerField(label="Malzeme İzleme Türü", table="LG_DISTORDLINE",field="ITEMTRACKTYPE",min_value=0, max_value=1,required=False)
	LOC_TRACKING = base.IntegerField(label="Stok yeri takibi (1- Evet, 0- Hayır)", table="LG_DISTORDLINE",field="LOCTRACKING",min_value=0, max_value=1,required=False)
	LINE_NO = base.IntegerField(label="Satır numarası", table="LG_DISTORDLINE",field="LINENR",required=False)
	REASON_FOR_NOT_SHIP = base.IntegerField(label="Reason For Not Shipment", table="LG_DISTORDLINE",field="REASONFORNOTSHP",required=False)
	D_ORD_STATUS = base.IntegerField(label="Dağıtım emri durumu", table="LG_DISTORDLINE",field="DORDSTATUS",min_value=0, max_value=1,required=False)
	D_ORD_GO_DATE = base.IntegerField(label="Distribution Order Shipment Date", table="LG_DISTORDLINE",field="DORDGODATE",required=False)
	D_ORD_RETURN_DATE = base.IntegerField(label="Distribution Order Return Date", table="LG_DISTORDLINE",field="DORDRETURNDATE",required=False)
	ITEM_CODE = base.CharField(label="Malzeme Kart Kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	ITEM_NAME = base.CharField(label="Malzeme Kartı Açıklaması", table="LG_ITEMS",field="NAME",max_length=51,required=False)
	ORD_FICHE_NO = base.CharField(label="Fiş Numarası", table="LG_ORFICHE",field="FICHENO",max_length=9,required=False)
	CL_CODE = base.CharField(label="Borçlu / Alacaklı Cari Hesaplar", table="LG_CLCARD",field="CODE",max_length=17,required=False)
	ORD_VOLUME = base.FloatField(label="Boyut Faktörü", table="LG_ORFLINE",field="UINFO7",required=False)
	ORD_WEIGHT = base.FloatField(label="Boyut Faktörü", table="LG_ORFLINE",field="UINFO8",required=False)
	ORD_DIST_RESERVED = base.FloatField(label="Reserved Distribution Amount", table="LG_ORFLINE",field="DISTRESERVED",required=False)
	ORD_UNIT_PRICE = base.FloatField(label="Fiyat", table="LG_ORFLINE",field="PRICE",required=False)
	VAT = base.FloatField(label="KDV", table="LG_ORFLINE",field="VAT",required=False)
	DIST_POINT = base.FloatField(label="Dağıtım Noktası", table="LG_ITEMS",field="DISTPOINT",required=False)

class DistOrder(base.Serializer):
	"""
		Dağıtım emirleri
	"""
	class Meta:
		XML_ROOT = 'DIST_ORDERS'
		XML_SUBROOT = 'DIST_ORDER'
		DATA_OBJECT = 'doDistOrder'
		REST_ENDPOINT = 'distributionOrders'
		RELATED_TABLE = 'LG_DISTORD'

	FICHE_NO = base.CharField(label="Dağıtım Emri Fiş No", table="LG_DISTORD",field="FICHENO",max_length=17,required=True)
	DATE = base.IntegerField(label="Tarih", table="LG_DISTORD",field="DATE_",required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_DISTORD",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_DISTORD",field="CYPHCODE",max_length=11,required=False)
	STATUS = base.IntegerField(label="Durumu; (0 Öneri;1 Sevk Edilebilir;2 Sevk Edildi)", table="LG_DISTORD",field="STATUS",min_value=0, max_value=1,required=False)
	MAX_CLIENT_LIMIT = base.IntegerField(label="Azami Müşteri Limiti", table="LG_DISTORD",field="MAXCLIENTLIMIT",required=False)
	LOAD_RATE = base.FloatField(label="Oran Yükle", table="LG_DISTORD",field="LOADRATE",required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_DISTORD",field="SITEID",required=False)
	GODATE = base.IntegerField(label="Vehicle Distribution Start Date", table="LG_DISTORD",field="GODATE",required=False)
	RETURNDATE = base.IntegerField(label="Vehicle Distribution Return Date", table="LG_DISTORD",field="RETURNDATE",required=False)

	# subs
	DIST_ORDER_LINES = base.serializers.ListSerializer(child=DistOrderLine())
	SL_DETAILS = base.serializers.ListSerializer(child=DistOrderSlDetails())
	CAMPAIGN_INFOS = base.serializers.ListSerializer(child=DistOrderCampaignInfos())
