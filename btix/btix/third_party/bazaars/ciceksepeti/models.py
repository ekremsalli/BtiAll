"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..base import *

class CiceksepetiProductMatch(BaseProductMatch):
    class Meta:
        db_table = "btix_ciceksepeti_product_match"

class CiceksepetiProductMismatch(BaseProductMismatch):
    class Meta:
        db_table = "btix_ciceksepeti_product_mismatch"

class CiceksepetiLog(BaseLog):
    class Meta:
        db_table = "btix_ciceksepeti_log"

class CiceksepetiLineLog(BaseLineLog):
    log = models.ForeignKey(CiceksepetiLog, on_delete=models.CASCADE)

    class Meta:
        db_table = "btix_ciceksepeti_line_log"

class CiceksepetiCargoMap(BaseCargoMap):
    class Meta:
        db_table = "btix_ciceksepeti_cargo_map"


class CiceksepetiCargoMismatch(BaseCargoMismatch):
    class Meta:
        db_table = "btix_ciceksepeti_cargo_mismatch"



# signals
@receiver(post_save, sender=CiceksepetiProductMatch)
def check_pm_mismatch(sender, instance, created, **kwargs):
    if created:
        CiceksepetiProductMismatch.objects.filter(
            barcode=instance.barcode,
            product_code=instance.product_code
        ).delete()


@receiver(post_save, sender=CiceksepetiCargoMap)
def check_cm_mismatch(sender, instance, created, **kwargs):
    if created:
        CiceksepetiCargoMismatch.objects.filter(
            input_val=instance.input_val,
        ).delete()                