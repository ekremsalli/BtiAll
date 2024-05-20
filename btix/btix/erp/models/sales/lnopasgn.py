"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *


class LG_LNOPASGN(
    BaseLogical,
    BaseItem,
    BaseAmount,
    BaseSiteRec,
    BaseWF,
    BaseRef,
    models.Model):
    """
        Operasyon-malzeme ilişkisi
    """
    bomrevref = models.ForeignKey(
        "LG_BOMASTER",
        db_column='BOMREVREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi -> BOMASTER',
        on_delete=models.DO_NOTHING
    )
    bomlineref = models.ForeignKey(
        "LG_BOMLINE",
        db_column='BOMLINEREF',
        blank=True,
        null=True,
        help_text='Ürün reçetesi satırı -> BOMLINE',
        on_delete=models.DO_NOTHING
    )
    routingref = models.ForeignKey(
        "LG_ROUTING",
        db_column='ROUTINGREF',
        blank=True,
        null=True,
        help_text='Üretim rotaları kartı -> ROUTING',
        on_delete=models.DO_NOTHING
    )
    routlineref = models.ForeignKey(
        "LG_RTNGLINE",
        db_column='ROUTLINEREF',
        blank=True,
        null=True,
        help_text='Üretim rotaaları satırları kartı -> RTNGLINE',
        on_delete=models.DO_NOTHING
    )
    uomref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UOMREF',
        blank=True,
        null=True,
        help_text='Birim ref. -> UNITSETL',
        on_delete=models.DO_NOTHING
    )
    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_LNOPASGN'
        unique_together = (('routlineref', 'bomlineref'),)
        target_db = 'erp'