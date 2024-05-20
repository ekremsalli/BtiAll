"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import json
import os
import logging
from datetime import datetime
from django.db import models

logger = logging.getLogger("app")


class RotateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_rotated=False)

class FileRotate(models.Model):
    is_rotated = models.BooleanField(
        verbose_name='Dosyaya yönlendirildi', default=False, db_index=True)
    rotated_to = models.TextField(
        verbose_name='Yönlendirilen dosya',
        null=True, blank=True)
    rotated_at = models.DateTimeField(
        verbose_name='Yönlendirilme zamanı',
        null=True, blank=True
    )
    rotated_fields = models.CharField(null=True, blank=True, max_length=255)

    objects = models.Manager()
    rotate_objects = RotateManager()

    class Meta:
        abstract = True

    def read_rotated_data(self):
        if self.is_rotated:
            with open(self.rotated_to, 'r') as fp:
                return json.loads(fp.read())
        return None

    def rotate(self, path, prefix='', suffix='json', pointer='data'):

        if isinstance(pointer, list) is False:
            pointer = [pointer]

        data = {}
        for point in pointer:        
            data.update({point: getattr(self, point)})
        
        name = f'{prefix}{self.pk}.{suffix}'

        try:
            os.makedirs(path, exist_ok=True)
            with open(f'{path}{name}', 'w+') as fp:
                fp.write(json.dumps(data))
        except Exception as e:            
            logger.exception(e)
        else:
            self.is_rotated = True
            self.rotated_at = datetime.now()
            self.rotated_to = f'{path}{name}'
            self.rotated_fields = json.dumps(list(data.keys()))
            for point in pointer:
                setattr(self, point, '')
            
            self.save()
