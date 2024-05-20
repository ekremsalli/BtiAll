"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base


class EmficheTransaction(base.BaseSerialiazer):
	SIGN = base.IntegerField(label="SIGN", table="?",field="?",min_value=0, max_value=1,required=False)
	GL_CODE = base.CharField(label="GL_CODE",table="?",field="?",max_length=255,required=False)
	PARENT_GLCODE = base.CharField(label="PARENT_GLCODE",table="?",field="?",max_length=255,required=False)
	DEBIT = base.FloatField(label="DEBIT",table="?",field="?",required=False)
	CREDIT = base.FloatField(label="CREDIT",table="?",field="?",required=False)
	DESCRIPTION = base.CharField(label="DESCRIPTION",table="?",field="?",required=False,max_length=255)
	DOC_DATE = base.CharField(label="DOC_DATE",table="?",field="?",required=False,max_length=20)

class EmTransactionHolder(base.BaseSerialiazer):
	items = base.serializers.ListSerializer(child=EmficheTransaction())


class BaseEmfiche(base.Serializer):
	TYPE = base.IntegerField(label="Fiş türü", table="LG_EMFICHE",field="TRCODE",required=True)
	NUMBER = base.CharField(label="Fiş numarası", table="LG_EMFICHE",field="FICHENO",max_length=9,required=True)
	DATE = base.CharField(label="Fiş Tarihi", table="LG_EMFICHE",field="DATE_",required=True)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_EMFICHE",field="SPECODE",max_length=11,required=False)
	AUTH_CODE = base.CharField(label="Yetki Kodu", table="LG_EMFICHE",field="CYPHCODE",max_length=11,required=False)
	DOC_NUMBER = base.CharField(label="Belge numarası", table="LG_EMFICHE",field="DOCODE",max_length=32,required=False)
	DIVISION = base.IntegerField(label="İşyeri", table="LG_EMFICHE",field="BRANCH",required=False)
	DEPARTMENT = base.IntegerField(label="Bölüm", table="LG_EMFICHE",field="DEPARTMENT",required=False)
	NOTES1 = base.CharField(label="Notlar1", table="LG_EMFICHE",field="GENEXP1",max_length=51,required=False)
	NOTES2 = base.CharField(label="Notlar2", table="LG_EMFICHE",field="GENEXP2",max_length=51,required=False)
	NOTES3 = base.CharField(label="Notlar3", table="LG_EMFICHE",field="GENEXP3",max_length=51,required=False)
	NOTES4 = base.CharField(label="Notlar4", table="LG_EMFICHE",field="GENEXP4",max_length=51,required=False)
	JOURNAL_NR = base.IntegerField(label="Yevmiye numarası", table="LG_EMFICHE",field="JOURNALNO",required=False)
	TOTAL_DEBIT = base.FloatField(label="Toplam borç", table="LG_EMFICHE",field="TOTALACTIVE",required=False)
	TOTAL_CREDIT = base.FloatField(label="Toplam alacak", table="LG_EMFICHE",field="TOTALPASSIVE",required=False)
	CANCELLED = base.IntegerField(label="İptal edilenler", table="LG_EMFICHE",field="CANCELLED",min_value=0, max_value=1,required=False)
	PRINT_COUNTER = base.IntegerField(label="Toplam basım sayısı", table="LG_EMFICHE",field="PRINTCNT",required=False)
	SOURCE_MODULE = base.IntegerField(label="Kaynak Modül", table="LG_EMFICHE",field="MODULENR",required=False)
	EURO_TOTAL_DEBIT = base.FloatField(label="Euro Toplam Borç", table="LG_EMFICHE",field="EMUTOTACTIVE",required=False)
	EURO_TOTAL_CREDIT = base.FloatField(label="Euro Toplam Alacak", table="LG_EMFICHE",field="EMUTOTPASSIVE",required=False)
	CURRSEL_TOTALS = base.IntegerField(label="Genel Döviz Türü", table="LG_EMFICHE",field="GENEXCTYP",required=False)
	CURRSEL_DETAILS = base.IntegerField(label="Satır Döviz Türü", table="LG_EMFICHE",field="LINEEXCTYP",required=False)
	DATA_SITEID = base.IntegerField(label="Veri Merkezi", table="LG_EMFICHE",field="SITEID",required=False)
	RC_TOTAL_DEBIT = base.FloatField(label="Dövizli toplam borç", table="LG_EMFICHE",field="REPTOTACTIVE",required=False)
	# ext
	EBOOK_DOCDATE = base.CharField(label="E-defter Tarih",table="LG_EMFICHE",field="EBOOK_DOCDATE",required=False)
	EBOOK_DOCNR = base.CharField(label="E-defter dokuman numarası",table="LG_EMFICHE",field="EBOOK_DOCNR",required=False)
	EBOOK_DOCTYPE = base.IntegerField(label="E-defter dokuman tipi", required=False)
	EBOOK_EXPLAIN = base.CharField(label="Açıklama", required=False)
	EBOOK_NOPAY = base.IntegerField(label='', required=False)
	DOC_DATE = base.CharField(label="Tarih", table="LG_EMFICHE",field="DOC_DATE",required=False)


class BaseEmficheForJSON(BaseEmfiche):
	TRANSACTIONS = EmTransactionHolder()

class BaseEmficheForXML(BaseEmfiche):
	TRANSACTIONS = base.serializers.ListSerializer(child=EmficheTransaction(),required=False)


class Emfiche(BaseEmficheForJSON):
	"""
		Muhasebe fişleri
	"""
	class Meta:
		XML_ROOT = 'GL_VOUCHERS'
		XML_SUBROOT = 'GL_VOUCHER'
		DATA_OBJECT = 'doGLVoucher'
		REST_ENDPOINT = 'GLSlips'
		RELATED_TABLE = 'LG_EMFICHE'

class EmficheXML(BaseEmficheForXML):
	"""
		Muhasebe fişleri
	"""
	class Meta:
		XML_ROOT = 'GL_VOUCHERS'
		XML_SUBROOT = 'GL_VOUCHER'
		DATA_OBJECT = 'doGLVoucher'
		REST_ENDPOINT = 'GLSlips'
		RELATED_TABLE = 'LG_EMFICHE'

