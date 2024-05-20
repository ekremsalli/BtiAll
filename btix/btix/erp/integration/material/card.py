"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class MaterialCardFactoryParams(base.BaseSerialiazer):
	FACTORYNR = base.IntegerField(label="Fabrika numarası", table="LG_ITMFACTP",field="FACTORYNR",required=False)
	SPECIALIZED = base.IntegerField(label="Kullanım dışı", table="LG_ITMFACTP",field="SPECIALIZED",required=False)
	PROCURECLASS = base.IntegerField(label="Temin şekli (0- Satınalma, 1- Üretim)", table="LG_ITMFACTP",field="PROCURECLASS",required=False)
	LOWLEVELCODE = base.IntegerField(label="Low Level Code", table="LG_ITMFACTP",field="LOWLEVELCODE",required=False)
	DIVLOTSIZE = base.IntegerField(label="Lot Büyüklüğü Bölünebilir", table="LG_ITMFACTP",field="DIVLOTSIZE",min_value=0, max_value=1,required=False)
	MRPCNTRL = base.IntegerField(label="Kullanım dışı", table="LG_ITMFACTP",field="MRPCNTRL",min_value=0, max_value=1,required=False)
	PLANPOLICY = base.IntegerField(label="Planlama Metodu", table="LG_ITMFACTP",field="PLANPOLICY",required=False)
	LOTSIZINGMTD = base.IntegerField(label="Lot Belirleme Yöntemi", table="LG_ITMFACTP",field="LOTSIZINGMTD",required=False)
	FIXEDLOTSIZE = base.FloatField(label="Sabit", table="LG_ITMFACTP",field="FIXEDLOTSIZE",required=False)
	YIELD = base.FloatField(label="Verim", table="LG_ITMFACTP",field="YIELD",required=False)
	MINORDERQTY = base.FloatField(label="Asgari sipariş miktarı", table="LG_ITMFACTP",field="MINORDERQTY",required=False)
	MAXORDERQTY = base.FloatField(label="Azami sipariş miktarı", table="LG_ITMFACTP",field="MAXORDERQTY",required=False)
	MULTORDERQTY = base.FloatField(label="Kullanım dışı", table="LG_ITMFACTP",field="MULTORDERQTY",required=False)
	MINORDERDAY = base.FloatField(label="Minimum Order Day", table="LG_ITMFACTP",field="MINORDERDAY",required=False)
	MAXORDERDAY = base.FloatField(label="Maximum Order Day", table="LG_ITMFACTP",field="MAXORDERDAY",required=False)
	REORDERPOINT = base.FloatField(label="Reorder Point", table="LG_ITMFACTP",field="REORDERPOINT",required=False)
	AUTOMTRISSUE = base.IntegerField(label="Otomatik Malzeme Çekişi", table="LG_ITMFACTP",field="AUTOMTRISSUE",min_value=0, max_value=1,required=False)
	DEFSERILOTNO = base.CharField(label="Lot / Serial Number First Value", table="LG_ITMFACTP",field="DEFSERILOTNO",max_length=25,required=False)
	AUTOLOTOUTMTD = base.IntegerField(label="Sarf ve Firelerde Lot Belirleme Yöntemi (0- FIFO, 1-LIFO)", table="LG_ITMFACTP",field="AUTOLOTOUTMTD",required=False)
	LOTPARTY = base.IntegerField(label="Lot Size Of Inputs From Production", table="LG_ITMFACTP",field="LOTPARTY",required=False)
	OUTLOTSIZE = base.FloatField(label="Lot Size Of Outputs", table="LG_ITMFACTP",field="OUTLOTSIZE",required=False)
	COUNTFORMPS = base.IntegerField(label="Enter to MPS", table="LG_ITMFACTP COUNTFORMPS 25 LG_ITEMS",field="CODE",required=False)
	DOMINANTCODE = base.CharField(label="Malzeme kart kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)

class MaterialCardWHParams(base.BaseSerialiazer):
	WH_NUMBER = base.IntegerField(label="Ambar numarası", table="LG_INVDEF",field="INVENNO",required=False)
	MIN_LEVEL = base.FloatField(label="Asgari seviye", table="LG_INVDEF",field="MINLEVEL",required=False)
	MAX_LEVEL = base.FloatField(label="Azami seviye", table="LG_INVDEF",field="MAXLEVEL",required=False)
	SAFETY_LEVEL = base.FloatField(label="Güvenli seviye", table="LG_INVDEF",field="SAFELEVEL",required=False)
	LOCATION_CODE = base.CharField(label="Stok yeri kodu", table="LG_LOCATION",field="CODE",max_length=25,required=False)
	PERIOD_CLOSE_DATE = base.IntegerField(label="Dönem kapatma tarihi", table="LG_INVDEF",field="PERCLOSEDATE",required=False)
	ABC_CODE = base.IntegerField(label="ABC kodu", table="LG_INVDEF",field="ABCCODE",required=False)
	MIN_LEVEL_FLAG = base.IntegerField(label="Asgari seviye kontrolü", table="LG_INVDEF",field="MINLEVELCTRL",min_value=0, max_value=1,required=False)
	MAX_LVEL_FLAG = base.IntegerField(label="Azami seviye kontrolü", table="LG_INVDEF",field="MAXLEVELCTRL",min_value=0, max_value=1,required=False)
	SAFETY_LEVEL_FLAG = base.IntegerField(label="Güvenli seviye kontolü", table="LG_INVDEF",field="SAFELEVELCTRL",min_value=0, max_value=1,required=False)
	BACKORDER_FLAG = base.IntegerField(label="Negatif Stok Seviyesi Kontrolü", table="LG_INVDEF",field="NEGLEVELCTRL",min_value=0, max_value=1,required=False)

class MaterialCardCharacteristics(base.BaseSerialiazer):
	LINENR = base.IntegerField(label="Satır numarası", table="LG_CHARASGN",field="LINENR",required=False)
	MATRIXLOC = base.IntegerField(label="Matrix Location Info; (0 Line;1 Column)", table="LG_CHARASGN",field="MATRIXLOC",required=False)
	PRIORITY = base.IntegerField(label="Öncelik", table="LG_CHARASGN",field="PRIORITY",required=False)
	CCODE = base.CharField(label="Özellik kodu", table="LG_CHARCODE",field="CODE",max_length=25,required=True)
	VCODE = base.CharField(label="Değer kodu", table="LG_CHARVAL",field="CODE",max_length=25,required=True)

class MaterialCardDominantClasses(base.BaseSerialiazer):
	DOM_TYPE = base.IntegerField(label="Sınıf türü", table="LG_ITEMS",field="CLASSTYPE",required=False)
	CLASS_CODE = base.CharField(label="Sınıf kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)

class MaterialCardUnitBarcode(base.BaseSerialiazer):
	BARCODE = base.CharField(label="Barkod", table="LG_ITMUNITA",field="BARCODE",required=False,max_length=100)

class MaterialCardUnitBarcodeHolder(base.BaseSerialiazer):
	items = base.serializers.ListSerializer(child=MaterialCardUnitBarcode())


class MaterialCardUnits(base.BaseSerialiazer):
	UNIT_CODE = base.CharField(label="Birim kodu", table="LG_UNITSETL",field="CODE",max_length=4,required=False)
	BARCODE_LIST = MaterialCardUnitBarcodeHolder()
	USEF_MRTLCLASS = base.IntegerField(label="Kullanım Yeri-Malzeme sınıfı", table="LG_ITMUNITA",field="MTRLCLAS",required=False)
	USEF_PURCHASECLASS = base.IntegerField(label="Kullanım Yeri-Satınalma", table="LG_ITMUNITA",field="PURCHCLAS",required=False)
	USEF_SALESCLASS = base.IntegerField(label="Kulanım Yeri-Satış ve Dağıtım", table="LG_ITMUNITA",field="SALESCLAS",required=False)
	MTRL_PRIORITY = base.IntegerField(label="Malzeme Yönetimi öncelik derecesi", table="LG_ITMUNITA",field="MTRLPRIORITY",required=False)
	PURCH_PRIORITY = base.IntegerField(label="Satınalma öncelik derecesi", table="LG_ITMUNITA",field="PURCHPRIORTY",required=False)
	SALES_PRIORITY = base.IntegerField(label="Satış ve Dağıtım öncelik derecesi", table="LG_ITMUNITA",field="SALESPRIORITY",required=False)
	WIDTH = base.FloatField(label="En", table="LG_ITMUNITA",field="WIDTH",required=False)
	LENGTH = base.FloatField(label="Boy", table="LG_ITMUNITA",field="LENGTH",required=False)
	HEIGHT = base.FloatField(label="Yükseklik", table="LG_ITMUNITA",field="HEIGHT",required=False)
	AREA = base.FloatField(label="Alan", table="LG_ITMUNITA",field="AREA",required=False)
	VOLUME = base.FloatField(label="Hacim", table="LG_ITMUNITA",field="VOLUME",required=False)
	WEIGHT = base.FloatField(label="Ağırlık", table="LG_ITMUNITA",field="WEIGHT",required=False)
	GROSS_VOLUME = base.FloatField(label="Brüt Hacim", table="LG_ITMUNITA GROSS",field="VOLUME",required=False)
	GROSS_WEIGHT = base.FloatField(label="Brüt Ağırlık", table="LG_ITMUNITA GROSS",field="WEIGHT",required=False)
	CONV_FACT1 = base.FloatField(label="Çevrim Katsayıları1", table="LG_ITMUNITA",field="CONV_FACT1",required=False)
	CONV_FACT2 = base.FloatField(label="Çevrim Katsayıları2", table="LG_ITMUNITA",field="CONV_FACT2",required=False)
	WIDTH_CODE = base.CharField(label="Genişlik Kodu", table="LG_UNITSETL",field="WIDTH_CODE",max_length=8,required=False)
	LENGTH_CODE = base.CharField(label="Uzunluk kodu", table="LG_UNITSETL",field="LENGTH_CODE",max_length=8,required=False)
	HEIGHT_CODE = base.CharField(label="Yükseklik kodu", table="LG_UNITSETL",field="HEIGHT_CODE",max_length=8,required=False)
	AREA_CODE = base.CharField(label="Alan kodu", table="LG_UNITSETL",field="AREA_CODE",max_length=8,required=False)
	VOLUME_CODE = base.CharField(label="Hacim kodu", table="LG_UNITSETL",field="VOLUME_CODE",max_length=8,required=False)
	WEIGHT_CODE = base.CharField(label="Ağırlık kodu", table="LG_UNITSETL",field="WEIGHT_CODE",max_length=8,required=False)

class MaterialCardUnitHolder(base.BaseSerialiazer):
	items = base.serializers.ListSerializer(child=MaterialCardUnits())

class MaterialCardComposites(base.BaseSerialiazer):
	CODE = base.CharField(label="Kod", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	QUANTITY = base.FloatField(label="Miktar", table="LG_STCOMPLN",field="AMNT",required=False)
	PRICE = base.FloatField(label="Fiyat", table="LG_STCOMPLN",field="PRICE",required=False)
	SHARE_PERC = base.CharField(label="Dağılım yüzdesi", table="LG_STCOMPLN",field="PERC",max_length=8,required=False)

class MaterialCardGlLinks(base.BaseSerialiazer):
	INFO_TYPE = base.IntegerField(label="Bilgi türü", table="LG_CRDACREF",field="TYP",required=False)
	GLACC_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)

class MaterialCardSuppliers(base.BaseSerialiazer):
	SUPPLYTYPE = base.IntegerField(label="Tedarikçi / Müşteri türü", table="LG_SUPPASGN",field="SUPPLYTYPE",required=False)
	PRIORITY = base.IntegerField(label="Öncelik", table="LG_SUPPASGN",field="PRIORITY",required=False)
	LINENO = base.IntegerField(label="Satır numarası", table="LG_SUPPASGN",field="LINENR",required=False)
	TRADING_GRP = base.CharField(label="Ticari İşlem Grubu", table="LG_SUPPASGN",field="TRADINGGRP",max_length=17,required=False)
	CL_CARD_TYPE = base.IntegerField(label="Borçlu/Alacaklı Hesap Türü", table="LG_SUPPASGN",field="CLCARDTYPE",required=False)
	LEAD_TIME = base.IntegerField(label="Teslim/Temin Süresi", table="LG_SUPPASGN",field="LEADTIME",required=False)
	MAX_QUANTITY = base.FloatField(label="Azami Miktar", table="LG_SUPPASGN",field="MAXQUANTITY",required=False)
	MIN_QUANTITY = base.FloatField(label="Asgari Miktar", table="LG_SUPPASGN",field="MINQUANTITY",required=False)
	BEG_DATE = base.IntegerField(label="Başlangıç Tarihi", table="LG_SUPPASGN",field="BEGDATE",required=False)
	SPECIALIZED = base.IntegerField(label="Kullanım dışı", table="LG_SUPPASGN",field="SPECIALIZED",required=False)
	ICUST_SUP_CODE = base.CharField(label="Müşteri/Tedarikçi Kodu", table="LG_SUPPASGN",field="ICUSTSUPCODE",max_length=25,required=False)
	ICUST_SUP_NAME = base.CharField(label="Müşteri/Tedarikçi Açıklaması", table="LG_SUPPASGN",field="ICUSTSUPNAME",max_length=51,required=False)
	ARP_CODE = base.CharField(label="Borçlu/Alacaklı Hesap Kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)

class MaterialCard(base.Serializer):
	"""
		Malzeme kartı
	"""
	class Meta:
		XML_ROOT = 'ITEMS'
		XML_SUBROOT = 'ITEM'
		DATA_OBJECT = 'doMaterial'
		REST_ENDPOINT = 'items'
		RELATED_TABLE = 'LG_ITEMS'

	RECORD_STATUS = base.IntegerField(label="Kayıt statüsü", table="LG_ITEMS",field="ACTIVE",required=False)
	CARD_TYPE = base.IntegerField(label="Malzeme kayıt türü", table="LG_ITEMS",field="CARDTYPE",required=True)
	CODE = base.CharField(label="Malzeme kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Malzeme açıklaması", table="LG_ITEMS",field="NAME",max_length=51,required=False)
	GROUP_CODE = base.CharField(label="Malzeme grup kodu", table="LG_ITEMS",field="STGRPCODE",max_length=17,required=False)
	PRODUCER_CODE = base.CharField(label="Üretici Kodu", table="LG_ITEMS",field="PRODUCERCODE",max_length=25,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_ITEMS",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_ITEMS",field="CYPHCODE",max_length=11,required=False)
	CLASS_TYPE = base.IntegerField(label="Malzeme Sınıfı Türü", table="LG_ITEMS",field="CLASSTYPE",required=False)
	USEF_PURCHASING = base.IntegerField(label="Kullanım Yeri-Satınalma", table="LG_ITEMS",field="PURCHBRWS",required=False)
	USEF_SALES = base.IntegerField(label="Kullanım Yeri-Satış ve Dağıtım", table="LG_ITEMS",field="SALESBRWS",required=False)
	USEF_MM = base.IntegerField(label="Kullanım Yeri-Malzeme Yönetimi", table="LG_ITEMS",field="MTRLBRWS",required=False)
	VAT = base.FloatField(label="KDV", table="LG_ITEMS",field="VAT",required=False)
	PAYMENT_CODE = base.IntegerField(label="Ödeme Plan Kodu", table="LG_PAYPLANS",field="CODE",min_value=0, max_value=1,required=False)
	TRACK_TYPE = base.IntegerField(label="İzleme Yöntemi", table="LG_ITEMS",field="TRACKTYPE",min_value=0, max_value=1,required=False)
	LOCATION_TRACKING = base.IntegerField(label="Stok yeri takibi", table="LG_ITEMS",field="LOCTRACKING",min_value=0, max_value=1,required=False)
	TOOL = base.IntegerField(label="Araç", table="LG_ITEMS",field="TOOL",min_value=0, max_value=1,required=False)
	AUTOINCLS = base.IntegerField(label="Seri numarası otomatik artırılacak", table="LG_ITEMS",field="AUTOINCSL",min_value=0, max_value=1,required=False)
	LOTS_DIVISIBLE = base.IntegerField(label="Lot büyüklükleri bölünebilir", table="LG_ITEMS",field="DIVLOTSIZE",min_value=0, max_value=1,required=False)
	SHELF_LIFE = base.FloatField(label="Raf ömrü", table="LG_ITEMS",field="SHELFLIFE",required=False)
	SHELF_DATE = base.IntegerField(label="Son kullanma tarihi", table="LG_ITEMS",field="SHELFDATE",required=False)
	DEPREC_TYPE = base.IntegerField(label="Amortisman türü", table="LG_ITEMS",field="DEPRTYPE",required=False)
	DEPREC_RATE = base.FloatField(label="Amortisman oranı", table="LG_ITEMS",field="DEPRRATE",required=False)
	DEPREC_DURATION = base.IntegerField(label="Amortisman süresi", table="LG_ITEMS",field="DEPRDUR",required=False)
	SALVAGE_VALUE = base.FloatField(label="Hurda değeri", table="LG_ITEMS",field="SALVAGEVAL",required=False)
	REVAL_FLAG = base.IntegerField(label="Yeniden değerleme", table="LG_ITEMS",field="REVALFLAG",min_value=0, max_value=1,required=False)
	REVDEPREC_RFLAG = base.IntegerField(label="Değerleme amortismanı", table="LG_ITEMS",field="REVDEPRFLAG",min_value=0, max_value=1,required=False)
	PARTIAL_DEPREC = base.IntegerField(label="Kıst amortismanı", table="LG_ITEMS",field="PARTDEP",required=False)
	DEPREC_TYPE2 = base.FloatField(label="Amortisman türü2", table="LG_ITEMS",field="DEPRTYPE2",required=False)
	DEPREC_RATE2 = base.IntegerField(label="Amortisman oranı2", table="LG_ITEMS",field="DEPRRATE2",required=False)
	DEPREC_DURATION2 = base.FloatField(label="Amortisman süresi2", table="LG_ITEMS",field="DEPRDUR2",required=False)
	REVAL_FLAG2 = base.IntegerField(label="Yeniden değerleme2", table="LG_ITEMS",field="REVALFLAG2",min_value=0, max_value=1,required=False)
	REVDEPREC_FLAG2 = base.IntegerField(label="Alternatif değerleme amortismanı", table="LG_ITEMS",field="REVDEPRFLAG2",min_value=0, max_value=1,required=False)
	PARTIAL_DEPREC2 = base.IntegerField(label="Kıst amortismanı2", table="LG_ITEMS",field="PARTDEP2",min_value=0, max_value=1,required=False)
	APPROVED = base.IntegerField(label="Onay bilgisi", table="LG_ITEMS",field="APPROVED",min_value=0, max_value=1,required=False)
	UNITSET_CODE = base.CharField(label="Birim seti kodu", table="LG_UNITSETF",field="CODE",max_length=4,required=False)
	QCCSET_CODE = base.CharField(label="Kalite kontrol seti kodu", table="LG_QCSET",field="CODE",max_length=4,required=False)
	DISTRIBUTED_AMOUNT = base.FloatField(label="Dağıtılan toplam", table="LG_ITEMS",field="DISTAMOUNT",required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_ITEMS",field="SITEID",required=False)
	UNIVERSAL_ID = base.CharField(label="Kullanım dışı", table="LG_ITEMS",field="UNIVID",max_length=25,required=False)
	DIST_LOT_UNITS = base.IntegerField(label="Lot büyüklükleri dağıtılabilir", table="LG_ITEMS",field="DISTLOTUNITS",min_value=0, max_value=1,required=False)
	COMB_LOT_UNITS = base.IntegerField(label="Lot büyüklükleri birleştirilebilir", table="LG_ITEMS",field="COMBLOTUNITS",min_value=0, max_value=1,required=False)

	# subs
	#FACTORY_PARAMS = base.serializers.ListSerializer(child=MaterialCardFactoryParams())
	#WH_PARAMS = base.serializers.ListSerializer(child=MaterialCardWHParams())
	#CHARACTERISTICS = base.serializers.ListSerializer(child=MaterialCardCharacteristics())
	#DOMINANTS_CLASSES = base.serializers.ListSerializer(child=MaterialCardDominantClasses())

	UNITS = MaterialCardUnitHolder()
	#COMPOSITES = base.serializers.ListSerializer(child=MaterialCardComposites())
	#GL_LINKS = base.serializers.ListSerializer(child=MaterialCardGlLinks())
	#SUPPLIERS = base.serializers.ListSerializer(child=MaterialCardSuppliers())

	SELVAT = base.FloatField(label="Satış kdv", table="LG_ITEMS",field="SELVAT",required=False)
	RETURNVAT = base.FloatField(label="Satış iade kdv", table="LG_ITEMS",field="RETURNVAT",required=False)
	SELLPRVAT = base.FloatField(label="Perakande satış kdv", table="LG_ITEMS",field="SELPRVAT",required=False)
	RETURNPRVAT = base.FloatField(label="Perakende satış iade kdv", table="LG_ITEMS",field="RETURNPRVAT",required=False)
	MARKCODE = base.CharField(label="Marka kodu", table="LG_ITEMS",field="MARKREF",max_length=25,required=False)
