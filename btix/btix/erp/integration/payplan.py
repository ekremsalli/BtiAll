"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.integration import base

class PayplanTerms(base.BaseSerialiazer):
	AFTER_DAYS = base.IntegerField(label="Gün sonra", table="LG_PAYLINES",field="AFTERDAYS",required=False)
	FORMULA = base.CharField(label="Formül", table="LG_PAYLINES",field="FORMULA",max_length=31,required=False)
	CONDITION = base.CharField(label="Koşul", table="LG_PAYLINES",field="CONDITION",max_length=51,required=False)
	DAY = base.CharField(label="Gün", table="LG_PAYLINES",field="DAY_",max_length=8,required=False)
	MONTH = base.CharField(label="Ay", table="LG_PAYLINES",field="MOUNTH",max_length=6,required=False)
	YEAR = base.CharField(label="Yıl", table="LG_PAYLINES",field="YEAR_",max_length=6,required=False)
	ROUND_BASE = base.IntegerField(label="Yuvarlama tabanı", table="LG_PAYLINES",field="RNDVALUE",required=False)
	ABSOLUTE_DATE = base.IntegerField(label="Kesin Tarih", table="LG_PAYLINES",field="ABSDATE",required=False)
	DATE_SELECTOR = base.IntegerField(label="Tarih", table="LG_PAYLINES",field="DATETYPE",min_value=0, max_value=1,required=False)
	DISC_RATE = base.FloatField(label="İndirim oranı", table="LG_PAYLINES",field="DISCRATE",required=False)
	PP_GROUP_CODE = base.CharField(label="Ödeme Planı Grup Kodu", table="LG_PAYPLANS",field="PPGROUPCODE",max_length=11,required=False)


class Payplan(base.Serializer):
	"""
		Ödeme Planı
	"""
	class Meta:
		XML_ROOT = 'PAYMENT_PLANS'
		XML_SUBROOT = 'PAYMENT_PLAN'
		DATA_OBJECT = 'doPayPlan'
		REST_ENDPOINT = 'paymentPlans'
		RELATED_TABLE = 'LG_PAYPLANS'

	RECORD_STATUS = base.IntegerField(label="Kayıt statüsü", table="LG_PAYPLANS",field="ACTIVE",required=False)
	CODE = base.CharField(label="Ödeme planıkodu", table="LG_PAYPLANS",field="CODE",max_length=17,required=True)
	DESCRIPTION = base.CharField(label="Ödeme planı açıklaması", table="LG_PAYPLANS",field="DEFINITION_",max_length=51,required=False)
	AUXIL_CODE = base.CharField(label="Özel Kod", table="LG_PAYPLANS",field="SPECODE",max_length=11,required=False)
	AUTHOR_CODE = base.CharField(label="Yetki Kodu", table="LG_PAYPLANS",field="CYPHCODE",max_length=11,required=False)
	EARLY_INTRATE = base.FloatField(label="Erken ödeme faizi", table="LG_PAYPLANS",field="EARLYINTEREST",required=False)
	LATE_INTRATE = base.FloatField(label="Geç ödeme faizi", table="LG_PAYPLANS",field="LATEINTEREST",required=False)
	COUNTER = base.IntegerField(label="Sayaç", table="LG_PAYPLANS",field="COUNTER",required=False)
	WORK_DAYS = base.IntegerField(label="Çalışma günleri", table="LG_PAYPLANS",field="WRKDAYS",min_value=0, max_value=1,required=False)
	DATA_SITEID = base.IntegerField(label="Bilgi veri merkezi", table="LG_PAYPLANS",field="SITEID",required=False)

	# subs
	PAYMENT_TERMS = base.serializers.ListSerializer(child=PayplanTerms())
