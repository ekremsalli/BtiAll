"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_LNGEXCSETS(
    BaseLogical,
    BaseSiteRec,
    BaseRef,
    models.Model):
    """
        Bazı kayıtların diğer dillerdeki açıklamaları
    """
    docid = models.IntegerField(
        db_column='DOCID',
        blank=True,
        null=True,
        choices=[
            (1, 'Malzeme'),
            (2, 'Cari Hesap'),
            (3, 'Banka'),
            (4, 'Muhasebe')
        ],
        help_text='Kayıt tipi'
    )
    docref = models.IntegerField(
        db_column='DOCREF',
        blank=True,
        null=True,
        help_text='Kayıt ref.'
    )
    fieldid = models.IntegerField(
        db_column='FIELDID',
        blank=True,
        null=True,
        choices=[
            (1, 'Malzeme açıklaması'),
            (2, 'Cari hesap ünvanı'),
            (3, 'Banka adı'),
            (4, 'Muhasebe hesabı açıklaması')
        ],
        help_text='Alan tipi'
    )
    langid = models.SmallIntegerField(
        db_column='LANGID',
        blank=True,
        null=True,
        help_text='Seçilen dil'
    )
    fieldcont = models.CharField(
        db_column='FIELDCONT',
        max_length=256,
        blank=True,
        null=True,
        help_text='Açıklama'
    )
    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_LNGEXCSETS'
        unique_together = (('docid', 'docref', 'fieldid', 'langid'),)
        target_db = 'erp'
