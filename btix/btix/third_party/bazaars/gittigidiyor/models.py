"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..base import *

class GittiGidiyorProductMatch(BaseProductMatch):
    class Meta:
        db_table = "btix_gittigidiyor_product_match"

class GittiGidiyorProductMismatch(BaseProductMismatch):
    order = models.CharField(db_index=True, max_length=128)
    class Meta:
        db_table = "btix_gittigidiyor_product_mismatch"

class GittiGidiyorLog(BaseLog):
    class Meta:
        db_table = "btix_gittigidiyor_log"


class GittiGidiyorLineLog(BaseLineLog):
    log = models.ForeignKey(GittiGidiyorLog, on_delete=models.CASCADE)

    class Meta:
        db_table = "btix_gittigidiyor_line_log"

class GittiGidiyorCargoMap(BaseCargoMap):
    class Meta:
        db_table = "btix_gittigidiyor_cargo_map"

class GittiGidiyorCargoMismatch(BaseCargoMismatch):
    order = models.CharField(db_index=True, max_length=128)
    class Meta:
        db_table = "btix_gittigidiyor_cargo_mismatch"



# signals
@receiver(post_save, sender=GittiGidiyorProductMatch)
def check_pm_mismatch(sender, instance, created, **kwargs):
    if created:
        GittiGidiyorProductMismatch.objects.filter(
            barcode=instance.barcode,
            product_code=instance.product_code
        ).delete()

@receiver(post_save, sender=GittiGidiyorCargoMap)
def check_cm_mismatch(sender, instance, created, **kwargs):
    if created:
        GittiGidiyorCargoMismatch.objects.filter(
            input_val=instance.input_val,
        ).delete()        
