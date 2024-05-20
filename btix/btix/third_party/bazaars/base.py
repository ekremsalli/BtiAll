"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from bti.models.rotate import FileRotate

class BaseCargoMap(models.Model):
    input_val = models.CharField(db_index=True, max_length=150)
    output_val = models.CharField(max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.input_val} -> {self.output_val}"

    @classmethod
    def check_agent(cls, input_val):
        obj = cls.objects.filter(input_val=input_val).last()
        return obj.output_val if obj else None

class BaseCargoMismatch(models.Model):
    order = models.CharField(
        db_index=True,
        unique=True,
        max_length=255
    )    
    input_val = models.CharField(db_index=True, max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    resolved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)    

    class Meta:
        abstract = True        

    def __str__(self):
        return f"{self.order} {self.input_val}"


class BaseProductMatch(models.Model):
    erp_code = models.CharField(db_index=True, max_length=100)
    barcode = models.CharField(db_index=True, max_length=100, null=True, blank=True)
    product_code = models.CharField(db_index=True, max_length=100, null=True, blank=True)
    merchant_sku = models.CharField(db_index=True, max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.erp_code} {self.barcode} {self.product_code} {self.merchant_sku}"

    @classmethod
    def get_erp_item(cls, data, trd_filter=[], check_erp_first=True, erp_filter=[]):
        from bti.helpers import convert_dict_to_orm_filter
        from erp.models.friendly import Items

        # first check erp!
        if check_erp_first:
            for cline in erp_filter:
                if isinstance(cline, dict):
                    queries = []
                    for ckey, cval in cline.items():
                        queries.append(convert_dict_to_orm_filter(data, ckey, cval))
                    if queries:
                        query = queries.pop()
                    for q in queries:
                        query &= q
                    c1 = Items.objects.filter(active=0).filter(query).first()
                    if c1:
                        return c1

        for tline in trd_filter:
            if isinstance(tline, dict):
                queries = []
                for tkey, tval in tline.items():
                    queries.append(convert_dict_to_orm_filter(data, tkey, tval))
                if queries:
                    query = queries.pop()
                for q in queries:
                    query &= q
                match = cls.objects.filter(query).first()
                if match:
                    return Items.objects.filter(
                        active=0,
                        code=match.erp_code).first()
        return None


class BaseProductMismatch(models.Model):
    order = models.CharField(
        db_index=True,
        unique=True,
        max_length=255
    )
    barcode = models.CharField(db_index=True, max_length=100, null=True, blank=True)
    product_code = models.CharField(db_index=True, max_length=100, null=True, blank=True)
    merchant_sku = models.CharField(db_index=True, max_length=100, null=True, blank=True)
    line = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    resolved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.order} {self.barcode} {self.product_code}"

class BaseLog(FileRotate):
    order_number = models.CharField(
        db_index=True,
        unique=True,
        max_length=255
    )
    order_id = models.CharField(db_index=True, null=True, max_length=255)
    raw = models.TextField()
    internal_ref = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_number} {self.internal_ref} {self.created}"

    class Meta:
        abstract = True

class BaseLineLog(FileRotate):
    line = models.CharField(db_index=True, max_length=255)
    raw = models.TextField()
    internal_ref = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.log.order_number} {self.line} {self.internal_ref} {self.created}"

    class Meta:
        abstract = True