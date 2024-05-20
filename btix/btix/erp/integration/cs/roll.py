"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class CSRoll(base.Serializer):
	"""
		Çek/senet bordrosu
	"""
	class Meta:
		XML_ROOT = 'CQPN_ROLLS'
		XML_SUBROOT = 'CQPN_ROLL'
		DATA_OBJECT = 'doCQPnRoll'
		REST_ENDPOINT = 'chequeAndPnoteRolls'
		RELATED_TABLE = 'LG_CSROLL'

	TYPE = base.IntegerField(label="Fiş türü", table="LG_CSROLL",field="TRCODE",required=True)
	NUMBER = base.CharField(label="Çek / senet bordro numarası", table="LG_CSROLL",field="ROLLNO",max_length=9,required=True)
	MASTER_MODULE = base.IntegerField(label="Kart modül numarası", table="LG_CSROLL",field="CARDMD",min_value=0, max_value=1,required=False)
	MASTER_CODE = base.CharField(label="Cari Hesap Kodu", table="LG_CLCARD",field="CODE",max_length=25,required=True)
	OHP_CODE = base.CharField(label="Masraf merkezi kodu", table="LG_EMCENTER",field="CODE",max_length=17,required=False)
	AUXIL_CODE = base.CharField(label="Bordro özel kodu", table="LG_CSROLL",field="SPECODE",max_length=11,required=False)
	AUTHOR_CODE = base.CharField(label="Bordro yetki kodu", table="LG_CSROLL",field="CYPHCODE",max_length=11,required=False)
	DATE = base.IntegerField(label="Bordro tarihi", table="LG_CSROLL",field="DATE_",required=True)
	DIVISION = base.IntegerField(label="İşyeri", table="LG_CSROLL",field="BRANCH",required=False)
	DEPARTMENT = base.IntegerField(label="Bölüm", table="LG_CSROLL",field="DEPARTMENT",required=False)
	DEST_DIVISION = base.IntegerField(label="Hedef işyeri", table="LG_CSROLL",field="DESTBRANCH",required=False)
	DEST_DEPARTMENT = base.IntegerField(label="Hedef bölüm", table="LG_CSROLL",field="DESTDEPARTMENT",required=False)
	PROC_TYPE = base.IntegerField(label="Türü", table="LG_CSROLL",field="PROCTYPE",min_value=0, max_value=1,required=False)
	SINGLE_PAYMENT = base.IntegerField(label="Tek satırlı ödeme", table="LG_CSROLL",field="ONEPAYLINE",min_value=0, max_value=1,required=False)
	GL_POSTED = base.IntegerField(label="Muhasebeleştir", table="LG_CSROLL",field="ACCOUNTED",min_value=0, max_value=1,required=False)
	AVERAGE_AGE = base.IntegerField(label="Ortalama yaş", table="LG_CSROLL",field="AVERAGEAGE",required=False)
	DOCUMENT_COUNT = base.IntegerField(label="Kayıt sayısı", table="LG_CSROLL",field="DOCCNT",required=False)
	PRINT_COUNTER = base.IntegerField(label="Basım sayısı", table="LG_CSROLL",field="PRINTCNT",required=False)
	TOTAL = base.FloatField(label="Toplam", table="LG_CSROLL",field="TOTAL",required=False)
	CURR_TRANS = base.IntegerField(label="İşlem döviz türü", table="LG_CSROLL",field="TRCURR",min_value=0, max_value=1,required=False)
	TC_XRATE = base.FloatField(label="İşlem dövizi kuru", table="LG_CSROLL",field="TRRATE",required=False)
	TC_AMOUNT = base.FloatField(label="İşlem dövizi tutarı", table="LG_CSROLL",field="TRNET",required=False)
	RC_XRATE = base.FloatField(label="Raporlama dövizi kuru", table="LG_CSROLL",field="REPORTRATE",required=False)
	RC_AMOUNT = base.FloatField(label="Raporlama dövizi tutarı", table="LG_CSROLL",field="REPORTNET",required=False)
	NOTES1 = base.CharField(label="Açıklama1", table="LG_CSROLL",field="GENEXP1",max_length=51,required=False)
	NOTES2 = base.CharField(label="Açıklama2", table="LG_CSROLL",field="GENEXP2",max_length=51,required=False)
	NOTES3 = base.CharField(label="Açıklama3", table="LG_CSROLL",field="GENEXP3",max_length=51,required=False)
	NOTES4 = base.CharField(label="Açıklama4", table="LG_CSROLL",field="GENEXP4",max_length=51,required=False)
	GL_CODE = base.CharField(label="Muhasebe hesap kodu", table="LG_EMUHACC",field="CODE",max_length=25,required=False)
	CANCELLED = base.IntegerField(label="İptal edilenler", table="LG_CSROLL",field="CANCELLED",min_value=0, max_value=1,required=False)
	TRADING_GRP = base.CharField(label="Ticari işlem grubu", table="LG_CSROLL",field="TRADINGGRP",max_length=17,required=False)
	CURRSEL_TOTALS = base.IntegerField(label="Genel döviz türü", table="LG_CSROLL",field="GENEXCTYP",required=False)
	CURRSEL_DETAILS = base.IntegerField(label="Satır döviz türü", table="LG_CSROLL",field="LINEEXCTYP",required=False)
	DATA_SITEID = base.IntegerField(label="Veri merkezi numarası", table="LG_CSROLL",field="SITEID",required=False)
