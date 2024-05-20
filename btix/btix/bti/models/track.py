"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .flow import Flow

class Track(models.Model):
    firm = models.CharField(max_length=60)
    identifier = models.CharField(max_length=128, unique=True)
    flow = models.ForeignKey(Flow, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    is_processing = models.BooleanField(default=False, db_index=True)

    @property
    def fmt_created(self):
        return self.created.strftime('%d.%m.%Y %H:%M:%S')

    @classmethod
    def control(cls, data):
        return cls.objects.filter(
                firm=data.get('firm'),
                identifier=data.get('identifier')
            ).first()

    def __str__(self):
        return slugify(self.__class__.__name__ + '-' + str(self.id))

    def in_track(self, description="Bu öğe daha önce kayıt edilmiş"):
        return {
            'status': False,
            'description': description,
            'flow': self.flow_id,
            'tid': str(self)
        }


    class Meta:
        abstract = True
        unique_together = ('firm', 'identifier',)
