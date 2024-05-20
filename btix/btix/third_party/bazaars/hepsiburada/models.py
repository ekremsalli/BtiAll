"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..base import *

class HepsiburadaProductMatch(BaseProductMatch):
    class Meta:
        db_table = "btix_hepsiburada_product_match"

class HepsiburadaProductMismatch(BaseProductMismatch):
    class Meta:
        db_table = "btix_hepsiburada_product_mismatch"

class HepsiburadaLog(BaseLog):
    class Meta:
        db_table = "btix_hepsiburada_log"

class HepsiburadaLineLog(BaseLineLog):
    log = models.ForeignKey(HepsiburadaLog, on_delete=models.CASCADE)

    class Meta:
        db_table = "btix_hepsiburada_line_log"

class HepsiburadaCargoMap(BaseCargoMap):
    class Meta:
        db_table = "btix_hepsiburada_cargo_map"


class HepsiburadaCargoMismatch(BaseCargoMismatch):
    class Meta:
        db_table = "btix_hepsiburada_cargo_mismatch"



# signals
@receiver(post_save, sender=HepsiburadaProductMatch)
def check_pm_mismatch(sender, instance, created, **kwargs):
    if created:
        HepsiburadaProductMismatch.objects.filter(
            barcode=instance.barcode,
            product_code=instance.product_code
        ).delete()


@receiver(post_save, sender=HepsiburadaCargoMap)
def check_cm_mismatch(sender, instance, created, **kwargs):
    if created:
        HepsiburadaCargoMismatch.objects.filter(
            input_val=instance.input_val,
        ).delete()                