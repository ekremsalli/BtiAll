"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

from .flow import Flow
from .rotate import FileRotate


class QueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_processing=False,
            is_processed=False,
            is_cancelled=False            
        ).order_by('-priority', 'created')    

class Que(FileRotate):
    firm = models.CharField(max_length=60)
    identifier = models.CharField(max_length=128, unique=True)
    data = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_processing = models.BooleanField(default=False, db_index=True)
    is_processed = models.BooleanField(default=False, db_index=True)
    is_cancelled = models.BooleanField(db_index=True, default=False)
    cancellation_reason = models.TextField(null=True, blank=True)
    processed = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(default=0)

    objects = models.Manager()    
    waiting = QueManager()

    class Meta:
        abstract = True
        unique_together = ('firm', 'identifier',)

    @property
    def fmt_created(self):
        return self.created.strftime('%d.%m.%Y %H:%M:%S')

    @property
    def fmt_processed(self):
        if self.processed:
            return self.processed.strftime('%d.%m.%Y %H:%M:%S')
        return ''

    def __str__(self):
        return slugify(self.__class__.__name__ + '-' + str(self.id))

    def get_data(self):
        import json
        if self.data:
            return json.loads(self.data)
        return None

    @classmethod
    def control(cls, data):
        return cls.objects.filter(
                firm=data.get('firm'),
                identifier=data.get('identifier')
            ).first()

    def in_que(self, description='Bu öğe daha önce eklenmiş'):
        return {
            'status': False,
            'description': description,
            'qid': str(self),
            'processed': self.is_processed,
            'processed_at': self.fmt_processed
        }

    def success(self, description="Öğe başarıyla kuyruğa eklendi"):
        return {
            'status': True,
            'description': description,
            'qid': str(self)
        }


class QueLog(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    flow = models.ForeignKey(Flow, null=True, on_delete=models.SET_NULL)
    exception = models.TextField(null=True, blank=True)
    is_success = models.BooleanField(db_index=True, default=False)
    class Meta:
        abstract = True

    def get_related_object(self):
        model_class = self.content_type.model_class()
        return model_class.objects.get(id=self.object_id)

    def get_model_class(self):
        return self.content_type.model_class()
