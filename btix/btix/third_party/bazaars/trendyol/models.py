"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..base import *

class TrendyolProductMatch(BaseProductMatch):
    class Meta:
        db_table = "btix_trendyol_product_match"

class TrendyolProductMismatch(BaseProductMismatch):
    class Meta:
        db_table = "btix_trendyol_product_mismatch"

class TrendyolLog(BaseLog):
    class Meta:
        db_table = "btix_trendyol_log"

class TrendyolLineLog(BaseLineLog):
    log = models.ForeignKey(TrendyolLog, on_delete=models.CASCADE)

    class Meta:
        db_table = "btix_trendyol_line_log"

class TrendyolCargoMap(BaseCargoMap):
    class Meta:
        db_table = "btix_trendyol_cargo_map"

class TrendyolCargoMismatch(BaseCargoMismatch):
    class Meta:
        db_table = "btix_trendyol_cargo_mismatch"



# signals
@receiver(post_save, sender=TrendyolProductMatch)
def check_pm_mismatch(sender, instance, created, **kwargs):
    if created:
        TrendyolProductMismatch.objects.filter(
            barcode=instance.barcode,
            product_code=instance.product_code
        ).delete()

@receiver(post_save, sender=TrendyolCargoMap)
def check_cm_mismatch(sender, instance, created, **kwargs):
    if created:
        TrendyolCargoMismatch.objects.filter(
            input_val=instance.input_val,
        ).delete()       
