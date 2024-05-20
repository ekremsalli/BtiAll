"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import json
from uuid import uuid4
from django.apps import apps
from django.db import models
from .rotate import FileRotate

class Flow(FileRotate):
    company = models.CharField(max_length=50, default='default')
    period = models.CharField(max_length=10, default='')
    user = models.CharField(max_length=32, default="AKTARIM")
    handler = models.CharField(max_length=6, db_index=True)
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=24)
    data = models.TextField(null=True, blank=True)
    related_object = models.CharField(max_length=50, null=True, blank=True)
    internal_ref = models.IntegerField(null=True, blank=True)
    request = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    exception = models.TextField(null=True, blank=True)
    success = models.BooleanField(default=False, db_index=True)
    next_flow = models.ForeignKey('self', null=True, blank=True,
        on_delete=models.DO_NOTHING, related_name="nextflow")
    prev_flow = models.ForeignKey('self', null=True, blank=True,
        on_delete=models.DO_NOTHING, related_name="prevflow")
    error_code = models.SmallIntegerField(
        default=0,
        db_index=True,
        choices=[
            (1, 'Internal exception'),
            (2, 'Endpoint not responds'),
            (3, 'Malformed request')
        ]
    )
    pid = models.CharField(max_length=32, db_index=True)
    took = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    keyword1 = models.CharField(max_length=255, db_index=True, null=True)
    keyword2 = models.CharField(max_length=255, db_index=True, null=True)
    keyword3 = models.CharField(max_length=255, db_index=True, null=True)

    def as_xml(self, target):
        data = json.loads(self.request)
        obj = target(data=data)
        return obj.prepare_xml()


    def get_related_obj(self):
        if self.success and self.related_object and self.internal_ref:
            model = apps.get_model(
                app_label='erp',
                model_name=self.related_object
            )
            return model.objects.get(pk=self.internal_ref)
        return None


    def is_success(self):
        if self.success is not None:
            if self.success:
                if self.internal_ref:
                    return True
        return False


    @classmethod
    def generate_pid(cls):
        return uuid4().hex

    def __str__(self):
        return f"{self.pk} - {self.company} {self.endpoint} {self.method}"

    class Meta:
        db_table = "btix_flow"
        ordering = ["-id"]
