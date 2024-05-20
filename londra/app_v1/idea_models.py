from django.db import models


class Storemap(models.Model):
    firmnr = models.CharField(
        db_column='FIRMNR',
        max_length=50,
        db_collation='SQL_Latin1_General_CP1_CI_AS'
    )
    store_nr = models.CharField(
        db_column='STORE_NR',
        max_length=50,
        db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True,
        null=True
    )
    wh_nr = models.CharField(
        db_column='WH_NR',
        max_length=50,
        db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True,
        null=True
    )
    store_name = models.CharField(
        db_column='STORE_NAME',
        max_length=150,
        db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True,
        null=True
    )
    wh_name = models.CharField(
        db_column='WH_NAME',
        max_length=150,
        db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True,
        null=True
    )
    status = models.CharField(
        db_column='STATUS',
        max_length=50,
        db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True,
        null=True
    )
    wh_demand_status = models.CharField(
        db_column='WH_DEMAND_STATUS',
        max_length=50,
        db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True,
        null=True
    )
    depoxnum = models.CharField(
        db_column='DEPOXNUM',
        max_length=10,
        db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True,
        null=True
    )
    transfer_status = models.IntegerField(db_column='TRANSFER_STATUS', blank=True, null=True)
    arpcode = models.CharField(
        db_column='ARPCODE',
        max_length=50,
        db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'BTI_PRT_STOREMAP'
        target_db = 'idea'
