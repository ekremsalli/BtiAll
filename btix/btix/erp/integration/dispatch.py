"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class DispatchTransactions(base.BaseSerialiazer):
	TYPE = base.IntegerField(label="Tür", table="LG_STLINE",field="LINETYPE",min_value=0, max_value=1,required=False)
	MASTER_CODE = base.CharField(label="Ana ürün kodu", table="LG_ITEMS",field="CODE",max_length=25,required=True)
	DETAIL_LEVEL = base.IntegerField(label="Malzeme sınıfı detay satırı", table="LG_STLINE",field="DETLINE",min_value=0, max_value=1,required=False)
	DISCEXP_CALC = base.IntegerField(label="İndirim/masraf hesaplamaları", table="LG_STLINE",field="CALCTYPE",required=False)
	SOURCECOSTGRP = base.IntegerField(label="Kaynak maliyet grubu", table="LG_STLINE",field="SOURCECOSTGRP",required=False)
	ORDER_REFERENCE = base.IntegerField(label="Sipariş referansı", table="LG_STLINE",field="ORDTRANSREF",required=False)
	ORDER_SITE = base.IntegerField(label="Sipariş merkezi", table="LG_ORFICHE",field="SITEID",required=False)
	OHP_CODE1 = base.CharField(label="Masraf merkezi 1", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE1 = base.CharField(label="Muhasebe hesap kodu 1", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	GL_CODE2 = base.CharField(label="Muhasebe hesap kodu 2", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE2 = base.CharField(label="Masraf merkezi kodu 2", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE3 = base.CharField(label="Muhasebe hesap kodu 3", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE3 = base.CharField(label="Masraf merkezi kodu 3", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE4 = base.CharField(label="Muhasebe hesap kodu 4", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE4 = base.CharField(label="Masraf merkezi kodu 4", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	PROMOTION_CODE = base.CharField(label="Promosyon kodu", table="LG_PRCARDS",field="CODE",max_length=17,required=False)
	PAYMENT_CODE = base.CharField(label="Ödeme planı kodu", table="LG_PAYPLANS",field="CODE",max_length=17,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_STLINE",field="SPECODE",max_length=17,required=False)
	DELVRY_CODE = base.CharField(label="Teslimat kodu", table="LG_STLINE",field="DELVRYCODE",max_length=5,required=False)
	QUANTITY = base.FloatField(label="Miktar", table="LG_STLINE",field="AMOUNT",required=True)
	PRICE = base.FloatField(label="Birim fiyat", table="LG_STLINE",field="PRICE",required=False)
	TOTAL = base.FloatField(label="Toplam", table="LG_STLINE",field="TOTAL",required=False)
	CURR_PRICE = base.IntegerField(label="Dövizli birim fiyat", table="LG_STLINE",field="PRCURR",min_value=0, max_value=1,required=False)
	PC_PRICE = base.FloatField(label="Fiyatlandırma dövizi", table="LG_STLINE",field="PRPRICE",required=False)
	CURR_TRANSACTION = base.IntegerField(label="İşlem dövizi türü", table="LG_STLINE",field="TRCURR",min_value=0, max_value=1,required=False)
	TC_XRATE = base.FloatField(label="İşlem dövizi kuru", table="LG_STLINE",field="TRRATE",required=False)
	RC_XRATE = base.FloatField(label="Raporlama dövizi kuru", table="LG_STLINE",field="REPORTRATE",required=False)
	COST_DISTR = base.FloatField(label="Dağıtılan maliyet", table="LG_STLINE",field="DISTCOST",required=False)
	DISCOUNT_DISTR = base.FloatField(label="Dağıtılan indirim", table="LG_STLINE",field="DISTDISC",required=False)
	EXPENSE_DISTR = base.FloatField(label="Dağıtılan masraf", table="LG_STLINE",field="DISTEXP",required=False)
	PROMOTION_DISTR = base.FloatField(label="Dağıtılan promosyon", table="LG_STLINE",field="DISTPROM",required=False)
	DISCOUNT_RATE = base.FloatField(label="Dağılım yüzdesi", table="LG_STLINE",field="DISCPER",required=False)
	DESCRIPTION = base.CharField(label="Açıklama", table="LG_STLINE",field="LINEEXP",max_length=31,required=False)
	UNIT_CODE = base.CharField(label="Malzeme kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=True)
	UNIT_CONV1 = base.FloatField(label="Birim çevrimi1", table="LG_STLINE",field="UINFO1",required=False)
	UNIT_CONV2 = base.FloatField(label="Birim çevrimi2", table="LG_STLINE",field="UINFO2",required=False)
	UNIT_CONV3 = base.FloatField(label="Boyut katsayısı3", table="LG_STLINE",field="UINFO3",required=False)
	UNIT_CONV4 = base.FloatField(label="Boyut katsayısı4", table="LG_STLINE",field="UINFO4",required=False)
	UNIT_CONV5 = base.FloatField(label="Boyut katsayısı5", table="LG_STLINE",field="UINFO5",required=False)
	UNIT_CONV6 = base.FloatField(label="Boyut katsayısı6", table="LG_STLINE",field="UINFO6",required=False)
	UNIT_CONV7 = base.FloatField(label="Boyut katsayısı7", table="LG_STLINE",field="UINFO7",required=False)
	UNIT_CONV8 = base.FloatField(label="Boyut katsayısı8", table="LG_STLINE",field="UINFO8",required=False)
	UNIT_CONV9 = base.FloatField(label="Planlanan Miktar", table="LG_STLINE",field="PLNAMOUNT",required=False)
	VAT_INCLUDED = base.IntegerField(label="KDV Dahil/Hariç", table="LG_STLINE",field="VATINC",min_value=0, max_value=1,required=False)
	VAT_RATE = base.FloatField(label="KDV yüzdesi", table="LG_STLINE",field="VAT",required=False)
	VAT_ADJUSTMENT = base.FloatField(label="KDV Farkı", table="LG_STLINE",field="VATCALCDIFF",required=False)
	BILLED = base.IntegerField(label="Faturalandı", table="LG_STLINE",field="BILLED",min_value=0, max_value=1,required=False)
	COMPOSITE = base.IntegerField(label="Karma koli", table="LG_STLINE",field="CPSTFLAG",min_value=0, max_value=1,required=False)
	RET_COST_TYPE = base.IntegerField(label="İade maliyeti türü", table="LG_STLINE",field="RETCOSTTYPE",min_value=0, max_value=3,required=False)
	SOURCE_REFERENCE = base.IntegerField(label="Invoice Logical Reference", table="LG_INVOICE",field="LOGICALREF",required=False)
	RET_COST = base.FloatField(label="İade maliyeti", table="LG_STLINE",field="RETCOST",required=False)
	TC_RETCOST = base.FloatField(label="İşlem dövizi iade maliyeti", table="LG_STLINE",field="RETCOSTCURR",required=False)
	OUT_COST = base.FloatField(label="Çıkış maliyeti", table="LG_STLINE",field="OUTCOST",required=False)
	TC_OUTCOST = base.FloatField(label="İşlem dövizi çıkış maliyeti", table="LG_STLINE",field="OUTCOSTCURR",required=False)
	FIXAST_CODE = base.CharField(label="Sabit kıymet kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	FIXAST_STATUS = base.IntegerField(label="Sabit kıymet statüsü", table="LG_STLINE",field="FAATTRIB",min_value=0, max_value=1,required=False)
	CANCELLED = base.IntegerField(label="İptal edildi", table="LG_STLINE",field="CANCELLED",min_value=0, max_value=1,required=False)
	PRICE_UPDATE = base.FloatField(label="Fiyat güncelleme", table="LG_STLINE",field="DIFFPRICE",required=False)
	PRICE_UPDCOST = base.FloatField(label="Maliyet fiyat güncelleme", table="LG_STLINE",field="DIFFPRCOST",required=False)
	PRICE_UPDNEG = base.IntegerField(label="Fiyat farkı", table="LG_STLINE",field="DECPRDIFF",min_value=0, max_value=1,required=False)
	PROD_EXPN_DISTR = base.FloatField(label="Üretim masraf dağılımı", table="LG_STLINE",field="PRDEXPTOTAL",required=False)
	RC_PRICE_UPD = base.FloatField(label="Raporlama dövizi fiyat farkı", table="LG_STLINE",field="DIFFREPPRICE",required=False)
	RC_PRICE_UPDCOST = base.FloatField(label="Fiyat farkı raporlandırma dövizi", table="LG_STLINE",field="DIFFPRCRCOST",required=False)
	OUTPUT_CODE = base.CharField(label="Çıkış kodu", table="LG_STLINE",field="OUTPUTIDCODE",max_length=25,required=False)
	COST_RATE = base.FloatField(label="Maliyet yüzdesi", table="LG_STLINE",field="COSTRATE",required=False)
	QC_OK = base.IntegerField(label="Kalite kontrol", table="LG_STLINE",field="TRANSQCOK",min_value=0, max_value=1,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_STLINE",field="SITEID",required=False)
	NET_DSC_FLAG = base.IntegerField(label="Net indirim satırı ve Tutar işareti (1-Evet 0-Hayır)", table="LG_STLINE",field="NETDISCFLAG",min_value=0, max_value=1,required=False)
	NET_DSC_RATE = base.FloatField(label="Net indirim oranı (%)", table="LG_STLINE",field="NETDISCPERC",required=False)
	NET_DSC_AMOUNT = base.FloatField(label="Net indirim tutarı (%)", table="LG_STLINE",field="NETDISCAMNT",required=False)
	DISPATCH_NUMBER = base.CharField(label="İrsaliye numarası", table="LG_STFICHE",field="FICHENO",max_length=17,required=False)

	#new
	SOURCEINDEX = base.CharField(label="?", required=False)
	EDT_CURR = base.IntegerField(label="?", required=False)

class DispatchFaInfo(base.BaseSerialiazer):
	CODE = base.CharField(label="Alım irsaliye kodu", table="LG_FAREGIST",field="REGCODE",max_length=17,required=False)
	DIVISION = base.IntegerField(label="İşyeri Integer 2 LG_FAREGIST DEPARTMENT Bölüm", table="LG_FAREGIST",field="DEPARTMENT",required=False)
	TRANSFER = base.IntegerField(label="Devir", table="LG_FAREGIST",field="TRANSFER",min_value=0, max_value=1,required=False)
	DATE_ACQUIRED = base.IntegerField(label="Alım tarihi", table="LG_FAREGIST",field="DATEIN",required=False)
	DATE_DEPRSTART = base.IntegerField(label="Amortisman Başlangıcı", table="LG_FAREGIST",field="DATEOFDEPR",required=False)
	QUANTITY = base.FloatField(label="Miktar", table="LG_FAREGIST",field="QUANTITY",required=False)
	QUANTITY_OUT = base.FloatField(label="Düşük miktar", table="LG_FAREGIST",field="TOTOUT",required=False)
	ACQ_VALUE = base.FloatField(label="Giriş maliyeti", table="LG_FAREGIST",field="INVALUE",required=False)
	VATAMOUNT = base.FloatField(label="İndirilecek KDV", table="LG_FAREGIST",field="VAT_AMOUNT",required=False)
	VAT_POST_DUR = base.IntegerField(label="KDV Süresi", table="LG_FAREGIST",field="VATDUR",required=False)
	DEPR_RATE = base.FloatField(label="Amortisman oranı", table="LG_FAREGIST",field="DEPRRATE",required=False)
	DEPR_DUR = base.IntegerField(label="Amortisman süresi", table="LG_FAREGIST",field="DEPRDUR",required=False)
	DEPR_TYPE = base.IntegerField(label="Amortisman türü", table="LG_FAREGIST",field="DEPRTYPE",min_value=0, max_value=1,required=False)
	REVALUATE = base.IntegerField(label="Değerleme işareti (1- Evet, 0- Hayır)", table="LG_FAREGIST",field="REVFLAG",min_value=0, max_value=1,required=False)
	REV_DEPR = base.IntegerField(label="Değerleme amortismanı işareti (1- Evet, 0- Hayır)", table="LG_FAREGIST",field="REVDEPFLAG",min_value=0, max_value=1,required=False)
	PARTIAL_DEPR = base.IntegerField(label="Kıst Amortisman", table="LG_FAREGIST",field="PARTDEP",min_value=0, max_value=1,required=False)
	CANCELLED = base.IntegerField(label="İptal edilmiş (Evet/Hayır)", table="LG_FAREGIST",field="CANCELLED",min_value=0, max_value=1,required=False)
	RC_XRATE = base.IntegerField(label="Raporlama dövizi kuru", table="LG_FAREGIST",field="REPORTRATE",min_value=0, max_value=1,required=False)
	RC_ACQ_VALUE = base.FloatField(label="Giriş maliyeti (Raporlama dövizi)", table="LG_FAREGIST",field="INVALUEX",required=False)
	TOTAL_EXPENSES = base.FloatField(label="Gider toplamı", table="LG_FAREGIST",field="EXPTOTAL",required=False)
	ACCUM_DEPR = base.FloatField(label="Toplu amortisman", table="LG_FAREGIST",field="ACCUMDEPR",required=False)
	ACCUM_REVAL = base.FloatField(label="Toplu değerleme", table="LG_FAREGIST",field="ACCUMREVAL",required=False)
	RC_TOTAL_EXPN = base.FloatField(label="Giderler toplamı (Raporlama dövizi)", table="LG_FAREGIST",field="EXPTOTALX",required=False)
	RC_ACCUM_DEPR = base.FloatField(label="Birikmiş Amortisman (Raporlama dövizi)", table="LG_FAREGIST",field="ACCUMDEPRX",required=False)
	RC_ACCUM_REVAL = base.FloatField(label="Değerleme (Raporlama dövizi)", table="LG_FAREGIST",field="ACCUMREVALX",required=False)
	DEPR_TYPE2 = base.IntegerField(label="Alternatif amortisman türü", table="LG_FAREGIST",field="DEPRTYPE2",required=False)
	DEPR_RATE2 = base.FloatField(label="Alternatif amortisman oranı", table="LG_FAREGIST",field="DEPRRATE2",required=False)
	DEPR_DUR2 = base.IntegerField(label="Alternatif amortisman süresi", table="LG_FAREGIST",field="DEPRDUR2",required=False)
	REVALUATE2 = base.IntegerField(label="Değerleme işareti (Alternatif) (1- Evet, 0- Hayır)", table="LG_FAREGIST",field="REVALFLAG2",min_value=0, max_value=1,required=False)
	REV_DEPR2 = base.IntegerField(label="Değerleme amortismanı işareti (Alternatif) (1- Evet, 0-Hayır)", table="LG_FAREGIST",field="REVDEPRFLAG2",min_value=0, max_value=1,required=False)
	OPEN_REVAL2 = base.FloatField(label="Sabit kıymet yeniden değerleme (Açılış)", table="LG_FAREGIST",field="OPVALS_BEGREVAL",required=False)
	OPEN_DEPR2 = base.FloatField(label="Sabit kıymet amortismanı (Açılış)", table="LG_FAREGIST",field="OPVALS_BEGDEPR",required=False)
	OPEN_REVDEPR2 = base.FloatField(label="Sabit kıymet yeniden değerleme amortismanı (Açılış)", table="LG_FAREGIST",field="OPVALS_BEGREVDEPR",required=False)
	RC_OPENREVDEPR2 = base.FloatField(label="Sabit kıymrt yeniden değerleme amortismanı (Açılış RD)", table="LG_FAREGIST",field="OPVALSX_BEGREVDEPR",required=False)
	DATE_DEPRSTART = base.IntegerField(label="Amortisman Başlangıcı", table="LG_FAREGIST",field="DATEOFDEPR",required=True)
	PART_DEP2 = base.IntegerField(label="Kıst Amortismanı", table="LG_FAREGIST",field="PARTDEP2",min_value=0, max_value=1,required=False)

class DispatchSlDetails(base.BaseSerialiazer):
	SOURCE_MT_REFERENCE = base.IntegerField(label="Giren stok hareket referansı", table="LG_SLTRANS",field="INTRANSREF",required=False)
	SOURCE_SLT_REFERENCE = base.IntegerField(label="Input Lot / Serial / Location Transaction", table="LG_SLTRANS",field="INSLTRANSREF",required=False)
	SOURCE_QUANTITY = base.FloatField(label="Quantity From Input Transaction Unit", table="LG_SLTRANS",field="INSLAMOUNT",required=False)
	SOURCE_WH = base.IntegerField(label="Ambar numarası", table="LG_SLTRANS",field="INVENNO",required=False)
	SLTYPE = base.IntegerField(label="Seri / Lot Türü 1. Lot, 2. Seri", table="LG_SLTRANS",field="SLTYPE",required=False)
	SL_CODE = base.CharField(label="Seri / Lot kodu", table="LG_SERILOTN",field="CODE",max_length=25,required=False)
	LOCATION_CODE = base.CharField(label="Stok yeri kodu", table="LG_LOCATION",field="CODE",max_length=25,required=False)
	DEST_LOCATION_CODE = base.CharField(label="Stok yeri açıklaması", table="LG_LOCATION",field="NAME",max_length=51,required=False)
	MU_QUANTITY = base.FloatField(label="Ana birim miktarı", table="LG_SLTRANS",field="MAINAMOUNT",required=False)
	UNIT_CODE = base.CharField(label="Birim kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	QUANTITY = base.FloatField(label="Satır birim miktarı", table="LG_SLTRANS",field="AMOUNT",required=False)
	REM_QUANTITY = base.FloatField(label="Ana birim kalan miktar", table="LG_SLTRANS",field="REMAMOUNT",required=False)
	LU_REM_QUANTITY = base.FloatField(label="Ana birim satır miktarı", table="LG_SLTRANS",field="REMLNUNITAMNT",required=False)
	UNIT_CONV1 = base.FloatField(label="Çevrim katsayısı1", table="LG_SLTRANS",field="UINFO1",required=False)
	UNIT_CONV2 = base.FloatField(label="Çevrim katsayısı2", table="LG_SLTRANS",field="UINFO2",required=False)
	UNIT_CONV3 = base.FloatField(label="Boyut katsayısı3", table="LG_SLTRANS",field="UINFO3",required=False)
	UNIT_CONV4 = base.FloatField(label="Boyut katsayısı4", table="LG_SLTRANS",field="UINFO4",required=False)
	UNIT_CONV5 = base.FloatField(label="Boyut katsayısı5", table="LG_SLTRANS",field="UINFO5",required=False)
	UNIT_CONV6 = base.FloatField(label="Boyut katsayısı6", table="LG_SLTRANS",field="UINFO6",required=False)
	UNIT_CONV7 = base.FloatField(label="Boyut katsayısı7", table="LG_SLTRANS",field="UINFO7",required=False)
	UNIT_CONV8 = base.FloatField(label="Boyut katsayısı8", table="LG_SLTRANS",field="UINFO8",required=False)
	DATE_EXPIRED = base.IntegerField(label="Son Kullanım Tarihi", table="LG_SLTRANS",field="EXPDATE",required=False)
	RATE_SCORE = base.IntegerField(label="Note", table="LG_SLTRANS",field="RATESCORE",required=False)
	OUT_COST = base.FloatField(label="Çıkış fişleri çıkış maliyeti", table="LG_SLTRANS",field="OUTCOST",required=False)
	TC_OUT_COST = base.FloatField(label="Çıkış fişleri çıkış maliyeti (Döviz)", table="LG_SLTRANS",field="OUTCOSTCURR",required=False)
	PRCDIF_COST = base.FloatField(label="Fiyat farkı maliyeti", table="LG_SLTRANS",field="DIFFPRCOST",required=False)
	TC_PRCDIF_COST = base.FloatField(label="Cost In F. Currency Because Of Price Difference", table="LG_SLTRANS",field="DIFFPRCOSTCURR",required=False)
	SL_QC_OK = base.IntegerField(label="Uygunluk kontrolü", table="LG_SLTRANS",field="SERIQCOK",min_value=0, max_value=1,required=False)
	SOURCE_TYPE = base.IntegerField(label="Kaynak türü (0- Ambar, 1- İş İstasyonu)", table="LG_SLTRANS",field="SOURCETYPE",min_value=0, max_value=1,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_SLTRANS",field="SITEID",required=False)

class DispatchDetails(base.BaseSerialiazer):
	ITEM_CODE = base.CharField(label="Malzeme kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	ITEM_REFERENCE = base.IntegerField(label="Malzeme referansı", table="LG_STLINE",field="STOCKREF",required=False)
	LINE_TYPE = base.IntegerField(label="Satır türü", table="LG_STLINE",field="LINETYPE",min_value=0, max_value=1,required=False)
	DETAIL_LEVEL = base.IntegerField(label="Malzeme sınıfı detay satırı", table="LG_STLINE",field="DETLINE",min_value=0, max_value=1,required=False)
	DISCEXP_CALC = base.IntegerField(label="İndirim/masraf hesaplama", table="LG_STLINE",field="CALCTYPE",min_value=0, max_value=1,required=False)
	LINE_NUMBER = base.IntegerField(label="Satır numarası", table="LG_STLINE",field="STFICHELNNO",required=False)
	GL_CODE1 = base.CharField(label="Muhasebe hesap kodu 1", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE1 = base.CharField(label="Masraf merkezi 1", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE2 = base.CharField(label="Muhasebe hesap kodu 2", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE2 = base.CharField(label="Masraf merkezi kodu 2", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE3 = base.CharField(label="Muhasebe hesap kodu 3", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE3 = base.CharField(label="Masraf merkezi kodu 3", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	GL_CODE4 = base.CharField(label="Muhasebe hesap kodu 4", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE4 = base.CharField(label="Masraf merkezi kodu 4", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	AUXIL_CODE = base.CharField(label="Özel kod", table="LG_STLINE",field="SPECODE",max_length=17,required=False)
	DELVRY_CODE = base.CharField(label="Teslimat kodu", table="LG_STLINE",field="DELVRYCODE",max_length=5,required=False)
	QUANTITY = base.FloatField(label="Miktar", table="LG_STLINE",field="AMOUNT",required=False)
	PRICE = base.FloatField(label="Birim fiyat", table="LG_STLINE",field="PRICE",required=False)
	TOTAL = base.FloatField(label="Toplam", table="LG_STLINE",field="TOTAL",required=False)
	NET_TOTAL = base.FloatField(label="Net toplam", table="LG_STLINE",field="LINENET",required=False)
	CURR_PRICE = base.IntegerField(label="Dövizli birim fiyat", table="LG_STLINE",field="PRCURR",min_value=0, max_value=1,required=False)
	PC_PRICE = base.FloatField(label="Fiyatlandırma dövizi", table="LG_STLINE",field="PRPRICE",required=False)
	CURR_TRANS = base.IntegerField(label="İşlem dövizi türü", table="LG_STLINE",field="TRCURR",min_value=0, max_value=1,required=False)
	TC_XRATE = base.FloatField(label="İşlem dövizi kuru", table="LG_STLINE",field="TRRATE",required=False)
	RC_XRATE = base.FloatField(label="Raporlama dövizi kuru", table="LG_STLINE",field="REPORTRATE",required=False)
	TCOST_DISTR = base.FloatField(label="İşlem maliyet dağılımı", table="LG_STLINE",field="DISTCOST",required=False)
	DISCOUNT_DISTR = base.FloatField(label="Dağıtılan indirim", table="LG_STLINE",field="DISTDISC",required=False)
	EXPENSE_DISTR = base.FloatField(label="Dağıtılan masraf", table="LG_STLINE",field="DISTEXP",required=False)
	PROMOTION_DISTR = base.FloatField(label="Dağıtılan promosyon", table="LG_STLINE",field="DISTPROM",required=False)
	DISCOUNT_PERC = base.FloatField(label="Masraf yüzdesi", table="LG_STLINE",field="DISCPER",required=False)
	DESCRIPTION = base.CharField(label="Açıklama", table="LG_STLINE",field="LINEEXP",max_length=31,required=False)
	UNIT_CODE = base.CharField(label="Birim kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)
	UNIT_CONV1 = base.FloatField(label="Birim çevrimi1", table="LG_STLINE",field="UINFO1",required=False)
	UNIT_CONV2 = base.FloatField(label="Birim çevrimi2", table="LG_STLINE",field="UINFO2",required=False)
	UNIT_CONV3 = base.FloatField(label="Birim çevrimi3", table="LG_STLINE",field="UINFO3",required=False)
	UNIT_CONV4 = base.FloatField(label="Birim çevrimi4", table="LG_STLINE",field="UINFO4",required=False)
	UNIT_CONV5 = base.FloatField(label="Birim çevrimi5", table="LG_STLINE",field="UINFO5",required=False)
	UNIT_CONV6 = base.FloatField(label="Birim çevrimi6", table="LG_STLINE",field="UINFO6",required=False)
	UNIT_CONV7 = base.FloatField(label="Birim çevrimi7", table="LG_STLINE",field="UINFO7",required=False)
	UNIT_CONV8 = base.FloatField(label="Birim çevrimi8", table="LG_STLINE",field="UINFO8",required=False)
	VAT_INCLUDED = base.IntegerField(label="KDV dahil / hariç", table="LG_STLINE",field="VATINC",min_value=0, max_value=1,required=False)
	VAT_PERC = base.FloatField(label="KDV yüzdesi", table="LG_STLINE",field="VAT",required=False)
	VAT_AMNT = base.FloatField(label="KDV tutarı", table="LG_STLINE",field="VATAMNT",required=False)
	COMPOSITE = base.IntegerField(label="Karma koli", table="LG_STLINE",field="CPSTFLAG",min_value=0, max_value=1,required=False)
	RET_COST_TYPE = base.IntegerField(label="İade maliyet türü", table="LG_STLINE",field="RETCOSTTYPE",min_value=0, max_value=3,required=False)
	RET_COST = base.FloatField(label="İade maliyeti", table="LG_STLINE",field="RETCOST",required=False)
	CURR_RET_COST = base.FloatField(label="Dövizli iade maliyeti", table="LG_STLINE",field="RETCOSTCURR",required=False)
	OUT_COST = base.FloatField(label="Çıkış maliyeti", table="LG_STLINE",field="OUTCOST",required=False)
	CURR_OUT_COST = base.FloatField(label="Dövizli çıkış maliyeti", table="LG_STLINE",field="OUTCOSTCURR",required=False)
	RET_QUANTITY = base.FloatField(label="İade miktarı", table="LG_STLINE",field="RETAMOUNT",required=False)
	FAREG_CODE = base.CharField(label="Sabit kıymet kodu", table="LG_FAREGIST",field="REGCODE",max_length=17,required=False)
	FA_STATUS = base.IntegerField(label="Sabit kıymet statüsü", table="LG_STLINE",field="FAATTRIB",min_value=0, max_value=1,required=False)
	CANCELLED = base.IntegerField(label="İptal edilenler", table="LG_STLINE",field="CANCELLED",min_value=0, max_value=1,required=False)
	PRICE_ADJUSTMENT = base.FloatField(label="Fiyat farkı toplamı", table="LG_STLINE",field="DIFFPRICE",required=False)
	COST_ADJUSTMENT_PR = base.FloatField(label="Fiyat farkı maliyeti", table="LG_STLINE",field="DIFFPRCOST",required=False)
	NEGPRC_ADJUSTMENT = base.IntegerField(label="Fiyat farkı", table="LG_STLINE",field="DECPRDIFF",min_value=0, max_value=1,required=False)
	RC_PRJADJUST = base.FloatField(label="Toplu fiyat farkı (Raporlama dövizi)", table="LG_STLINE",field="DIFFREPPRICE",required=False)
	RC_COSTADJUST = base.FloatField(label="Fiyat Farkı Maliyeti (Raporlama Dövizi)", table="LG_STLINE",field="DIFFPRCRCOST",required=False)
	OUTPUT_IDCODE = base.CharField(label="Çıkış izleme kodu", table="LG_STLINE",field="OUTPUTIDCODE",max_length=25,required=False)
	COST_RATE = base.FloatField(label="Maliyet yüzdesi", table="LG_STLINE",field="COSTRATE",required=False)
	QC_STATUS = base.FloatField(label="Kalite kontrol durumu", table="LG_STLINE",field="TRANSQCOK",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_INVOICE",field="SITEID",required=True)

class DispatchCampaignInfos(base.BaseSerialiazer):
	CAMPCODE1 = base.CharField(label="Kod1", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE2 = base.CharField(label="Kod2", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE3 = base.CharField(label="Kod3", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE4 = base.CharField(label="Kod4", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMPCODE5 = base.CharField(label="Kod5", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	PCAMPCODE = base.CharField(label="Kod6", table="LG_CAMPAIGN",field="CODE",max_length=25,required=False)
	CAMP_LN_NO = base.IntegerField(label="Satır Numarası", table="LG_CMPGNLINE",field="LINENR",required=False)
	CAMPAIGN_POINT = base.FloatField(label="Kampanya Noktası", table="LG_ORFLINE",field="CAMPPOINT",required=False)
	PROM_CLAS_ITEM_CODE = base.CharField(label="Malzeme Kart Kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	ADD_TAX_RATE = base.FloatField(label="ÖTV oranı", table="LG_STLINE",field="ADDTAXRATE",required=False)
	ADD_TAX_CONV_FACT = base.FloatField(label="ÖTV Çevrim Katsayısı", table="LG_STLINE",field="ADDTAXCONVFACT",required=False)
	ADD_TAX_AMOUNT = base.FloatField(label="ÖTV Tutarı", table="LG_STLINE",field="ADDTAXAMOUNT",required=False)
	ADD_TAX_PRCOST = base.FloatField(label="ÖTV Maliyeti", table="LG_STLINE",field="ADDTAXPRCOST",required=False)
	ADD_TAX_RETCOST = base.FloatField(label="ÖTV İade Maliyeti", table="LG_STLINE",field="ADDTAXRETCOST",required=False)
	ADD_TAX_RETCOSTCURR = base.FloatField(label="ÖTV İade Maliyeti (Raporlama Dövizi)", table="LG_STLINE",field="ADDTAXRETCOSTCURR",required=False)
	GROSS_U_INFO1 = base.FloatField(label="Brüt Hacim", table="LG_STLINE",field="GROSSUINFO1",required=False)
	GROSS_U_INFO2 = base.FloatField(label="Brüt Ağırlık", table="LG_STLINE",field="GROSSUINFO2",required=False)
	ADD_TAX_PRCOSTCURR = base.FloatField(label="ÖTV Maliyeti (Raporlama Dövizi)", table="LG_STLINE",field="ADDTAXPROCOSTCURR",required=False)
	GL_CODE5 = base.CharField(label="Muhasebe hesap kodu 5", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE5 = base.CharField(label="Masraf merkezi kodu 5", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	ADD_TAX_AMNT_IS_UPD = base.IntegerField(label="Additional Tax is Edited (1- Evet, 0- Hayır)", table="LG_STLINE",field="ADDTAXAMNTISUPD",min_value=0, max_value=1,required=False)
	DLV_CLIENT = base.IntegerField(label="Sevkiyat Adresi Müşteri Türü", table="LG_ORFICHE",field="DLVCLIENT",min_value=0, max_value=1,required=False)
	ADD_TAX_CALC = base.IntegerField(label="Hesaplanan Ek Vergi", table="LG_STFICHE",field="ADDTAXCALC",min_value=0, max_value=1,required=False)
	TOTAL_ADD_TAX = base.FloatField(label="Ek Vergi Toplamı", table="LG_STFICHE",field="TOTALADDTAX",required=False)

class DispatchTransactionHolder(base.BaseSerialiazer):
	items = base.serializers.ListSerializer(child=DispatchTransactions())

class BaseDispatch(base.Serializer):
	TYPE = base.IntegerField(label="İrsaliye türü", table="LG_STFICHE",field="TRCODE",required=True)
	NUMBER = base.CharField(label="İrsaliye numarası", table="LG_STFICHE",field="FICHENO",max_length=17,required=True)
	DOC_TRACK_NR = base.CharField(label="Doküman izleme numarası", table="LG_INVOICE",field="DOCTRACKINGNR",max_length=21,required=False)
	DATE = base.CharField(label="İrsaliye tarihi", table="LG_STFICHE",field="DATE",required=True)
	TIME = base.IntegerField(label="Fiş kayıt zamanı", table="LG_STFICHE",field="FTIME",required=False)
	DOC_NUMBER = base.CharField(label="Fiş belge numarası", table="LG_STFICHE",field="DOCODE",max_length=32,required=False)
	INVOICE_NUMBER = base.CharField(label="Fatura Numarası", table="LG_STFICHE",field="INVNO",max_length=17,required=False)
	AUXIL_CODE = base.CharField(label="Fiş özel kodu", table="LG_STFICHE",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Fiş yetki kodu", table="LG_STFICHE",field="CYPHCODE",max_length=11,required=False)
	ARP_CODE = base.CharField(label="Cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)
	ARP_CODE_SHPM = base.CharField(label="Sevk edilen cari hesap kodu", table="LG_CLCARD",field="CODE",max_length=17,required=False)
	SHIPLOC_CODE = base.CharField(label="Kod", table="LG_SHIPINFO",field="CODE",max_length=25,required=False)
	GL_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	PORDER_NUMBER = base.CharField(label="Üretim emri numarası", table="LG_PRODORD",field="FICHENO",max_length=17,required=False)
	SOURCE_TYPE = base.IntegerField(label="Kaynak türü", table="LG_STFICHE",field="SOURCETYPE",min_value=0, max_value=1,required=False)
	SOURCE_WH = base.CharField(label="Kaynak ambar kodu", table="LG_STFICHE",field="SOURCEINDEX",required=False)
	SOURCE_WSCODE = base.CharField(label="Kaynak iş istasyonu kodu", table="LG_WORKSTAT",field="CODE",max_length=25,required=False)
	SOURCE_COST_GRP = base.IntegerField(label="Kaynak maliyet grubu", table="LG_STFICHE",field="SOURCECOSTGRP",required=False)
	DEST_TYPE = base.IntegerField(label="Hedef türü", table="LG_STFICHE",field="DESTTYPE",min_value=0, max_value=1,required=False)
	DEST_WH = base.IntegerField(label="Hedef ambarı", table="LG_STFICHE",field="DESTINDEX",required=False)
	DESTWSCODE = base.CharField(label="Hedef iş istasyonu kodu", table="LG_WORKSTAT",field="CODE",max_length=25,required=False)
	DEST_COST_GRP = base.IntegerField(label="Hedef maliyet grubu", table="LG_STFICHE",field="DESTCOSTGRP",required=False)
	FACTORY = base.IntegerField(label="Fabrika", table="LG_STFICHE",field="FACTORYNR",required=False)
	DIVISION = base.CharField(label="İşyeri", table="LG_STFICHE",field="BRANCH",required=False)
	DEPARTMENT = base.IntegerField(label="Bölüm", table="LG_STFICHE",field="DEPARTMENT",required=False)
	DEST_DIVISION = base.IntegerField(label="Hedef işyeri", table="LG_STFICHE",field="COMPBRANCH",required=False)
	DEST_DEPARTMENT = base.IntegerField(label="Hedef bölüm", table="LG_STFICHE",field="COMPDEPARTMENT",required=False)
	DEST_FACTORY = base.IntegerField(label="Hedef fabrika", table="LG_STFICHE",field="COMPFACTORY",required=False)
	PROD_STATUS = base.IntegerField(label="Üretim statüsü", table="LG_STFICHE",field="PRODSTAT",required=False)
	CANCELLED = base.IntegerField(label="İptal edildi", table="LG_STFICHE",field="CANCELLED",min_value=0, max_value=1,required=False)
	INVOICED = base.IntegerField(label="Faturalandı", table="LG_STFICHE",field="BILLED",min_value=0, max_value=1,required=False)
	GL_POSTED = base.IntegerField(label="Muhasebeleştirildi", table="LG_STFICHE",field="ACCOUNTED",min_value=0, max_value=1,required=False)
	INVOICE_TYPE = base.IntegerField(label="Fatura türü", table="LG_STFICHE",field="INVKIND",min_value=0, max_value=1,required=False)
	ADD_DISCOUNTS = base.FloatField(label="Fiş geneline ait ek indirimler", table="LG_STFICHE",field="ADDDISCOUNTS",required=False)
	TOTAL_DISCOUNTS = base.FloatField(label="Toplam indirimler", table="LG_STFICHE",field="TOTALDISCOUNTS",required=False)
	ADD_EXPENSES = base.FloatField(label="Fiş geneline ait ek masraflar", table="LG_STFICHE",field="ADDEXPENSES",required=False)
	TOTAL_EXPENSES = base.FloatField(label="Toplam masraflar", table="LG_STFICHE",field="TOTALEXPENSES",required=False)
	TOTAL_DEPOSITED = base.FloatField(label="Toplam depozitolar", table="LG_STFICHE",field="TOTALDEPOZITO",required=False)
	TOTAL_PROMOTIONS = base.FloatField(label="Toplam promosyonlar", table="LG_STFICHE",field="TOTALPROMOTIONS",required=False)
	NOTES1 = base.CharField(label="Açıklama1", table="LG_STFICHE",field="GENEXP1",max_length=51,required=False)
	NOTES2 = base.CharField(label="Açıklama2", table="LG_STFICHE",field="GENEXP2",max_length=51,required=False)
	NOTES3 = base.CharField(label="Açıklama3", table="LG_STFICHE",field="GENEXP3",max_length=51,required=False)
	NOTES4 = base.CharField(label="Açıklama4", table="LG_STFICHE",field="GENEXP4",max_length=51,required=False)
	NOTES5 = base.CharField(label="Açıklama5", table="LG_STFICHE",field="GENEXP5",max_length=51,required=False)
	NOTES6 = base.CharField(label="Açıklama6", table="LG_STFICHE",field="GENEXP6",max_length=51,required=False)
	RC_RATE = base.FloatField(label="Raporlama dövizi kuru", table="LG_STFICHE",field="REPORTRATE",required=False)
	PAYMENT_CODE = base.CharField(label="Ödeme planı kodu", table="LG_PAYPLANS",field="CODE",max_length=17,required=False)
	PRINT_COUNTER = base.IntegerField(label="Basım sayısı", table="LG_STFICHE",field="PRINTCNT",required=False)
	SALESMANCODE = base.CharField(label="Satış elemanı kodu", table="LG_SLSMAN",field="CODE",max_length=25,required=False)
	GL_POST_CANCL = base.IntegerField(label="Muhasebeleştirme iptali", table="LG_STFICHE",field="CANCELLEDACC",min_value=0, max_value=1,required=False)
	SHIPMENT_TYPE = base.CharField(label="Sevkiyat türü", table="LG_STFICHE",field="SHPTYPCOD",max_length=13,required=False)
	SHIPPING_AGENT = base.CharField(label="Taşıyıcı kodu", table="LG_STFICHE",field="SHPAGNCOD",max_length=13,required=False)
	TRACK_NR = base.CharField(label="İzleme numarası", table="LG_STFICHE",field="TRACKNR",max_length=17,required=False)
	CURRSEL_TOTALS = base.IntegerField(label="Genel Döviz Türü", table="LG_STFICHE",field="GENEXCTYP",required=False)
	CURRSEL_DETAILS = base.IntegerField(label="Satır Döviz Türü", table="LG_STFICHE",field="LINEEXCTYP",required=False)
	TRADING_GROUP = base.CharField(label="Ticari işlem grubu", table="LG_STFICHE",field="TRADINGGRP",max_length=17,required=False)
	TEXTINC = base.IntegerField(label="Detay açıklama", table="LG_STFICHE",field="TEXTINC",min_value=0, max_value=1,required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi", table="LG_STFICHE",field="SITEID",required=False)
	ORIG_NUMBER = base.CharField(label="Sevkiyat cari hesabı ünvanı", table="LG_CLCARD",field="DEFINITION_",max_length=51,required=False)

	# subs
	#FA_INFO = base.serializers.ListSerializer(child=DispatchFaInfo())
	#SL_DETAILS = base.serializers.ListSerializer(child=DispatchSlDetails())
	#DETAILS = base.serializers.ListSerializer(child=DispatchDetails())
	#CAMPAIGN_INFOS = base.serializers.ListSerializer(child=DispatchCampaignInfos())

	# extras
	SHIP_DATE = base.CharField(label='Sevkiyat tarihi', required=False)
	SHIP_TIME = base.IntegerField(label='Sevkiyat zamanı', required=False)
	DOC_DATE = base.CharField(label='Belge tarihi', required=False)
	DOC_TIME = base.IntegerField(label='Belge zamanı', required=False)
	EDESPATCH = base.IntegerField(label='?', required=False)
	EDESPATCH_PROFILEID = base.IntegerField(label="?", required=False)
	EINVOICE = base.IntegerField(label="?", required=False)
	EINVOICE_PROFILEID = base.IntegerField(label="?", required=False)
	EINVOICE_DRIVERNAME1 = base.CharField(label="?", required=False)
	EINVOICE_DRIVERSURNAME1 = base.CharField(label="?", required=False)
	EINVOICE_PLATENUM1 = base.CharField(label="?", required=False)
	DEDUCTIONPART1 = base.IntegerField(label="?", required=False)
	DEDUCTIONPART2 = base.IntegerField(label="?", required=False)
	AFFECT_RISK = base.IntegerField(label="?", required=False)
	DISP_STATUS = base.IntegerField(label="?", required=False)


class BaseDispatchForJSON(BaseDispatch):
	TRANSACTIONS = DispatchTransactionHolder()

class BaseDispatchForXML(BaseDispatch):
	TRANSACTIONS = base.serializers.ListSerializer(child=DispatchTransactions())


class SalesDispatch(BaseDispatchForJSON):
	"""
		Satış irsaliyeleri
	"""
	class Meta:
		XML_ROOT = "SALES_DISPATCHES"
		XML_SUBROOT = "DISPATCH"
		DATA_OBJECT = "doSalesDispatch"
		REST_ENDPOINT = "salesDispatches"
		RELATED_TABLE = 'LG_STFICHE'

class PurchaseDispatch(BaseDispatchForJSON):
	"""
		Alış irsaliyeleri
	"""
	class Meta:
		XML_ROOT = "PURCHASE_DISPATCHES"
		XML_SUBROOT = "DISPATCH"
		DATA_OBJECT = "doPurchDispatch"
		REST_ENDPOINT = "purchaseDispatches"
		RELATED_TABLE = 'LG_STFICHE'

class SalesDispatchXML(BaseDispatchForXML):
	"""
		Satış irsaliyeleri
	"""
	class Meta:
		XML_ROOT = "SALES_DISPATCHES"
		XML_SUBROOT = "DISPATCH"
		DATA_OBJECT = "doSalesDispatch"
		REST_ENDPOINT = "salesDispatches"
		RELATED_TABLE = 'LG_STFICHE'

class PurchaseDispatchXML(BaseDispatchForXML):
	"""
		Alış irsaliyeleri
	"""
	class Meta:
		XML_ROOT = "PURCHASE_DISPATCHES"
		XML_SUBROOT = "DISPATCH"
		DATA_OBJECT = "doPurchDispatch"
		REST_ENDPOINT = "purchaseDispatches"
		RELATED_TABLE = 'LG_STFICHE'
