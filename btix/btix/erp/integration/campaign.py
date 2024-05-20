"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class CampaignLines(base.BaseSerialiazer):
	LINE_NR = base.IntegerField(label="Satır Numarası", table="LG_CMPGNLINE",field="LINENR",required=False)
	LINE_TYPE = base.IntegerField(label="Satır Türü (1:İndirim; 2:Masraf; 3:Promosyon; 4:Puan)", table="LG_CMPGNLINE",field="LINETYPE",required=False)
	APPLY_TYPE = base.IntegerField(label="Uygulama Türü ; (0: Satıra; 1: Genele)", table="LG_CMPGNLINE",field="APPLYTYPE",required=False)
	COND_ITEM_CODE = base.CharField(label="Koşul Malzeme Kodu", table="LG_CMPGNLINE",field="CONDITEMCODE",max_length=25,required=False)
	CONDITION = base.CharField(label="Koşul", table="LG_CMPGNLINE",field="CONDITION",max_length=251,required=False)
	FORMULA = base.CharField(label="Formül", table="LG_CMPGNLINE",field="FORMULA",max_length=251,required=False)
	PROMIS_CLASS = base.IntegerField(label="Is Material Class (1- Yes, 0- No)", table="LG_CMPGNLINE",field="PROMISCLASS",min_value=0, max_value=1,required=False)
	ITEM_CODE = base.CharField(label="Malzeme Kartı Kodu", table="LG_ITEMS",field="CODE",max_length=25,required=False)
	UOM_CODE = base.CharField(label="Birim Kodu", table="LG_UNITSETL",field="CODE",max_length=11,required=False)

class BaseCampaign(base.Serializer):
	CODE = base.CharField(label="Alış Kampanya Kart Kodu", table="LG_CAMPAIGN",field="CODE",max_length=25,required=True)
	NAME = base.CharField(label="Alış Kampanya Kart Açıklaması", table="LG_CAMPAIGN",field="NAME",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_CAMPAIGN",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_CAMPAIGN",field="CYPHCODE",max_length=11,required=False)
	BEG_DATE = base.IntegerField(label="Başlangıç Tarihi", table="LG_CAMPAIGN",field="BEGDATE",required=False)
	END_DATE = base.IntegerField(label="Bitiş Tarihi", table="LG_CAMPAIGN",field="ENDDATE",required=False)
	PRIORITY_GRP = base.CharField(label="Öncelik Grubu", table="LG_CAMPAIGN",field="PRIORITYGRP",max_length=11,required=False)
	PRIORITY = base.IntegerField(label="Öncelik", table="LG_CAMPAIGN",field="PRIORITY",required=False)
	DONT_FIX_LINES = base.IntegerField(label="Material Lines That Realize Campaign Conditions Can Be Distributed (1- Yes, 0- No)", table="LG_CAMPAIGN",field="DONTFIXLINES",min_value=0, max_value=1,required=False)
	CLIENT_CODE = base.CharField(label="Cari Hesap Kodu", table="LG_CAMPAIGN",field="CLIENTCODE",max_length=17,required=False)
	CL_AUXIL_CODE = base.CharField(label="Cari Hesap Özel Kodu", table="LG_CAMPAIGN",field="CLSPECODE",max_length=11,required=False)
	TRADING_GRP = base.CharField(label="Ticari İşlem Grubu", table="LG_CAMPAIGN",field="TRADINGGRP",max_length=17,required=False)
	PAY_PLAN_CODE = base.CharField(label="Ödeme Plan Kodu", table="LG_CAMPAIGN",field="PAYPLANCODE",max_length=17,required=False)
	PP_GROUP_CODE = base.CharField(label="Ödeme Plan Grup Kodu", table="LG_CAMPAIGN",field="PPGROUPCODE",max_length=11,required=False)
	TOWN_CODE = base.CharField(label="İlçe Kodu", table="LG_CAMPAIGN",field="TOWNCODE",max_length=13,required=False)
	DISTRICT_CODE = base.CharField(label="Semt Kodu", table="LG_CAMPAIGN",field="DISTRICTCODE",max_length=13,required=False)
	CITY_CODE = base.CharField(label="Şehir Kodu", table="LG_CAMPAIGN",field="CITYCODE",max_length=13,required=False)
	COUNTRY_CODE = base.CharField(label="Ülke Kodu", table="LG_CAMPAIGN",field="COUNTRYCODE",max_length=13,required=False)
	VARIABLE_DEFS1 = base.CharField(label="Variable Definition 1", table="LG_CAMPAIGN",field="VARIABLEDEFS11",max_length=251,required=False)
	VARIABLE_DEFS2 = base.CharField(label="Variable Definition 2", table="LG_CAMPAIGN",field="VARIABLEDEFS2",max_length=251,required=False)
	VARIABLE_DEFS3 = base.CharField(label="Variable Definition 3", table="LG_CAMPAIGN",field="VARIABLEDEFS3",max_length=251,required=False)
	VARIABLE_DEFS4 = base.CharField(label="Variable Definition 4", table="LG_CAMPAIGN",field="VARIABLEDEFS4",max_length=251,required=False)
	VARIABLE_DEFS5 = base.CharField(label="Variable Definition 5", table="LG_CAMPAIGN",field="VARIABLEDEFS5",max_length=251,required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_CAMPAIGN",field="SITEID",required=False)

	# subs
	CAMPAIGN_LINES = base.serializers.ListSerializer(child=CampaignLines())

class SalesCampaign(BaseCampaign):
	"""
		Satış kampanyası
	"""
	class Meta:
		XML_ROOT = "SALES_CAMPAIGNS"
		XML_SUBROOT = "CAMPAIGN"
		DATA_OBJECT = "doSlCampaign"
		REST_ENDPOINT = "salesCampaigns"
		RELATED_TABLE = 'LG_CAMPAIGN'

class PurchaseCampaign(BaseCampaign):
	"""
		Alım kampanyası
	"""
	class Meta:
		XML_ROOT = "PURCHASE_CAMPAIGNS"
		XML_SUBROOT = "CAMPAIGN"
		DATA_OBJECT = "doPrCampaign"
		REST_ENDPOINT = "purchaseCampaigns"
		RELATED_TABLE = 'LG_CAMPAIGN'
