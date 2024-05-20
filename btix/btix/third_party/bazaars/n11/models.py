"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..base import *

class N11ProductMatch(BaseProductMatch):
    class Meta:
        db_table = "btix_n11_product_match"

class N11ProductMismatch(BaseProductMismatch):
    class Meta:
        db_table = "btix_n11_product_mismatch"

class N11Log(BaseLog):
    class Meta:
        db_table = "btix_n11_log"


class N11LineLog(BaseLineLog):
    log = models.ForeignKey(N11Log, on_delete=models.CASCADE)

    class Meta:
        db_table = "btix_n11_line_log"

class N11CargoMap(BaseCargoMap):
    class Meta:
        db_table = "btix_n11_cargo_map"

class N11CargoMismatch(BaseCargoMismatch):
    class Meta:
        db_table = "btix_n11_cargo_mismatch"


# signals
@receiver(post_save, sender=N11ProductMatch)
def check_pm_mismatch(sender, instance, created, **kwargs):
    if created:
        N11ProductMismatch.objects.filter(
            barcode=instance.barcode,
            product_code=instance.product_code
        ).delete()

@receiver(post_save, sender=N11CargoMap)
def check_cm_mismatch(sender, instance, created, **kwargs):
    if created:
        N11CargoMismatch.objects.filter(
            input_val=instance.input_val,
        ).delete()        
