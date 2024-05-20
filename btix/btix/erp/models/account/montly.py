"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from erp.active import Active
from erp.models.base import *

class LG_EMUHTOT(
    BaseLogical,
    BaseAccount,
    BaseMontly,
    models.Model):
    """
        EMUHTOT tablosunda muhasebe hesap kartlarının ve masraf merkezlerinin
        aylık borç ve alacak hesap toplamları tutulmaktadır. Her hesap kartı
        için 14 adet toplam kaydı bulunmaktadır.
    """
    trancount = models.IntegerField(
        db_column='TRANCOUNT',
        blank=True,
        null=True,
        help_text='Hareket sayacı'
    )
    tottype = models.SmallIntegerField(
        db_column='TOTTYPE',
        blank=True,
        null=True,
        choices=[
            (1, 'Muhasebe TL toplam'),
            (2, 'Muhasebe dövizli toplam'),
            (3, 'Muhasebe birimli toplam'),
            (4, 'Masraf merkezi TL toplam'),
            (5, 'Masraf merkezi dövizli toplam')
        ],
        help_text='Toplam türü'
    )
    month_field = models.SmallIntegerField(
        db_column='MONTH_',
        blank=True,
        null=True,
        help_text='Ay'
    )
    debitrem = models.FloatField(
        db_column='DEBITREM',
        blank=True,
        null=True,
        help_text='Bakiye borç'
    )
    creditrem = models.FloatField(
        db_column='CREDITREM',
        blank=True,
        null=True,
        help_text='Bakiye alacak'
    )
    debitinfl = models.FloatField(
        db_column='DEBITINFL', blank=True, null=True)
    creditinfl = models.FloatField(
        db_column='CREDITINFL', blank=True, null=True)
    year_field = models.SmallIntegerField(
        db_column='YEAR_', blank=True, null=True)
    branch = models.SmallIntegerField(
        db_column='BRANCH', blank=True, null=True)
    department = models.SmallIntegerField(
        db_column='DEPARTMENT', blank=True, null=True)
    debitresrv = models.FloatField(
        db_column='DEBITRESRV', blank=True, null=True)
    creditresrv = models.FloatField(
        db_column='CREDITRESRV', blank=True, null=True)
    currtyp = models.SmallIntegerField(
        db_column='CURRTYP', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_{Active.namespace}_{Active.period}_EMUHTOT'
        unique_together = (
            (
                'accountref', 'tottype', 'year_field', 'month_field', 'branch',
                'department', 'currtyp'), ('accountref', 'tottype',
                'department', 'branch', 'currtyp', 'year_field',
                'month_field'
            ),
        )
        target_db = 'erp'