from django.db import models
from django.db.models import F
from django.conf import settings

DEF_MAP = settings.GECO_MAPPING['DEF_MAP']

from .base import BaseModel, ActiveManager, DeletedManager

import logging
logger = logging.getLogger("app")
class GecoGroups(BaseModel):
    DEFAULT_GTYPE = 11
    GROUP_TYPES = [
        (1, 'Firma'),
        (2, 'Bölüm'),
        (3, 'Ünvan'),
        (4, 'Çalışan tipi'),
        (5, 'Diğer grup'),
        (6, 'Diğer grup'),
        (7, 'Diğer grup'),
        (8, 'Diğer grup'),
        (9, 'Diğer grup'),
        (10, 'Diğer grup'),
        (11, 'Hesaplama grubu')
    ]
    gtype = models.SmallIntegerField(
        choices=GROUP_TYPES,
        help_text='Grup tipi',
        null=True,
        blank=True,
        db_index=True,
        default=DEFAULT_GTYPE
    )
    geco_id = models.SmallIntegerField(
        help_text='Tanım numarası',
        db_index=True
    )
    code = models.CharField(
        max_length=64,
        help_text='Grup kodu',
        db_index=True
    )
    description = models.TextField(null=True, blank=True)

    active_objects = ActiveManager()
    deleted_objects = DeletedManager()
    objects = models.Manager()

    class Meta:
        ordering = ["code"]

    @classmethod
    def sync(cls, db):
        from datetime import datetime
        from geco.models import Tgrptab
        logger.info("Model/Gecogroups/Sync Fonksiyonu Başladı ")
        GECO_MAPPING = settings.GECO_MAPPING
        bulk_size = 100
        bulk_op = lambda n: [n[i:i + bulk_size] for i in range(0, len(n), bulk_size)]

        DEFAULT_GTYPE = GECO_MAPPING[db.code]['GECO_GROUPS_DEFAULT_GTYPE']
        MAPP = GECO_MAPPING[db.code]['M_GECOGROUPS']

        exists = set(cls.objects.filter(
            source_db=db).values_list(
            'geco_id', flat=True))
        newbies, updates, found = [], [], set([])
        for group in Tgrptab.objects.using(db.code).exclude():
            record = {
                'source_db': db,
                'description': getattr(group, MAPP['description']),
                'geco_id': getattr(group, MAPP['geco_id']),
                'status': 0
            }
            if getattr(group, MAPP['is_person']) == 1:
                record.update({
                    'code': getattr(group, MAPP['people_code']),
                    'gtype': DEFAULT_GTYPE
                })
            else:
                record.update({
                    'code': getattr(group, MAPP['group_code']),
                    'gtype': getattr(group, MAPP['gtype']) + 1
                })
            if group.idnr in exists:
                record.update({'modified_on': datetime.now()})
                updates.append(record)
            else:
                newbies.append(cls(**record))
            found.add(group.idnr)

        diffs = list(exists.difference(found))

        for group in bulk_op(diffs):
            cls.objects.filter(
                source_db=db,
                geco_id__in=group
            ).update(status=-1)
        ids = {rec['geco_id']: rec for rec in updates}
        ikeys = list(ids.keys())
        records = []
        for group in bulk_op(ikeys):
            records.extend(cls.objects.filter(
                source_db=db,
                geco_id__in=group
            ))
        for item in records:
            for kx, vx in ids[item.geco_id].items():
                setattr(item, kx, vx)

        cls.objects.bulk_create(newbies)

        fields = [
            'description', 'code', 'gtype',
            'status', 'modified_on'
        ]

        for field in fields:
            tmp = [rec for rec in records if getattr(rec, field) is not None]
            cls.objects.bulk_update(tmp, [field])
        logger.info("Model/Gecogroups/Sync Fonksiyonu Bitti ")

class TimeTypeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related(
            'source_db').filter(status=0, def_type=DEF_MAP['TIME_TYPES'])


class ExcuseTypeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related(
            'source_db').filter(status=0, def_type=DEF_MAP['EXCUSE_TYPES'])


class DayModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related(
            'source_db').filter(status=0, def_type=DEF_MAP['DAY_MODELS'])


class PayTypeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related(
            'source_db').filter(status=0, def_type=DEF_MAP['PAY_TYPES'])


class PayModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related(
            'source_db').filter(status=0, def_type=DEF_MAP['PAY_MODELS'])


class ShiftModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related(
            'source_db').filter(status=0, def_type=DEF_MAP['SHIFT_MODELS'])


class FlexShiftModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related(
            'source_db').filter(
            status=0,
            def_type=DEF_MAP['FLEX_SHIFT_MODELS']
        )


class GecoDefs(BaseModel):
    DEF_TYPES = [
        (21, 'Zaman tipi'),
        (22, 'Mazeret tipi'),
        (23, 'Gün modeli'),
        (24, 'Puantaj modeli'),
        (25, 'Puantaj tipi'),
        (26, 'Vardiya modeli'),
        (27, 'Değişken vardiya modeli')
    ]
    def_type = models.SmallIntegerField(
        choices=DEF_TYPES,
        help_text='Tanım tipi',
        db_index=True
    )
    code = models.CharField(
        max_length=6,
        db_index=True,
        help_text='Tanım kodu'
    )
    short_code = models.CharField(max_length=2,
                                  help_text='Tanım kısa kodu')
    name = models.CharField(max_length=80, help_text='Tanım adı')
    link_code = models.CharField(max_length=6,
                                 help_text='Tanım bağlantı kodu')
    geco_id = models.SmallIntegerField(
        help_text='Tanım numarası',
        db_index=True
    )

    active_objects = ActiveManager()
    deleted_objects = DeletedManager()
    time_types = TimeTypeManager()
    excuse_types = ExcuseTypeManager()
    day_models = DayModelManager()
    pay_types = PayTypeManager()
    pay_models = PayModelManager()
    shift_models = ShiftModelManager()
    flex_shift_models = FlexShiftModelManager()

    objects = models.Manager()

    class Meta:
        ordering = ["name", "code", "short_code"]

    @staticmethod
    def get_definitons(db):
        return settings.GECO_MAPPING[db]['DEFINITIONS']

    @classmethod
    def base_sync(cls, db, def_type, items):
        from datetime import datetime

        bulk_size = 100
        bulk_op = lambda n: [n[i:i + bulk_size] for i in range(0, len(n), bulk_size)]

        exists = set(cls.objects.filter(
            source_db=db,
            def_type=def_type
        ).values_list('code', flat=True))
        newbies, updates, found = [], [], set([])
        for item in items:
            item['source_db'] = db
            item['status'] = 0
            if item['code'] in exists:
                item.update({'modified_on': datetime.now()})
                updates.append(item)
            else:
                newbies.append(cls(**item))
            found.add(item['code'])

        diffs = list(exists.difference(found))

        for group in bulk_op(diffs):
            cls.objects.filter(
                source_db=db,
                def_type=def_type,
                code__in=group
            ).update(status=-1)

        codes = {rec['code']: rec for rec in updates}
        ckeys = list(codes.keys())
        records = []
        for group in bulk_op(ckeys):
            records.extend(cls.objects.filter(
                source_db=db,
                def_type=def_type,
                code__in=group
            ))
        for item in records:
            for kx, vx in codes[item.code].items():
                setattr(item, kx, vx)

        cls.objects.bulk_create(newbies)
        fields = [
            'geco_id', 'short_code',
            'name', 'link_code',
            'modified_on'
        ]
        for field in fields:
            tmp = [rec for rec in records if getattr(rec, field) is not None]
            cls.objects.bulk_update(tmp, [field])

    @classmethod
    def sync_time_types(cls, db, key='TIME_TYPES'):
        from geco.models import Tzeiart
        MAPP = settings.GECO_MAPPING[db.code]['M_GECODEFS'][key]

        defaults = cls.get_definitons(db.code).get(key).copy()
        data = Tzeiart.objects.using(db.code).values(
            code=F(MAPP['code']),
            name=F(MAPP['name']),
        )
        cls.base_sync(
            db,
            defaults.get('def_type'),
            [dict(item, **defaults) for item in data]
        )

    @classmethod
    def sync_excuse_types(cls, db, key='EXCUSE_TYPES'):
        from geco.models import Tabwart
        MAPP = settings.GECO_MAPPING[db.code]['M_GECODEFS'][key]

        defaults = cls.get_definitons(db.code).get(key).copy()
        data = Tabwart.objects.using(db.code).values(
            code=F(MAPP['code']),
            name=F(MAPP['name']),
            short_code=F(MAPP['short_code']),
            link_code=F(MAPP['link_code'])
        )
        for item in data:
            if item['link_code'] is None:
                item['link_code'] = ""

        cls.base_sync(
            db,
            defaults.get('def_type'),
            [dict(item, **defaults) for item in data]
        )

    @classmethod
    def sync_day_models(cls, db, key='DAY_MODELS'):
        from geco.models import Ttagmod
        MAPP = settings.GECO_MAPPING[db.code]['M_GECODEFS'][key]

        defaults = cls.get_definitons(db.code).get(key).copy()
        data = Ttagmod.objects.using(db.code).values(
            code=F(MAPP['code']),
            name=F(MAPP['name']),
            short_code=F(MAPP['short_code'])
        )
        cls.base_sync(
            db,
            defaults.get('def_type'),
            [dict(item, **defaults) for item in data]
        )

    @classmethod
    def sync_pay_models(cls, db, key='PAY_MODELS'):
        from geco.models import Tlohmod
        MAPP = settings.GECO_MAPPING[db.code]['M_GECODEFS'][key]

        defaults = cls.get_definitons(db.code).get(key).copy()
        data = Tlohmod.objects.using(db.code).values(
            geco_id=F(MAPP['geco_id']),
            code=F(MAPP['code']),
            name=F(MAPP['name'])
        )
        cls.base_sync(
            db,
            defaults.get('def_type'),
            [dict(item, **defaults) for item in data]
        )

    @classmethod
    def sync_pay_types(cls, db, key='PAY_TYPES'):
        from geco.models import Tlohart
        MAPP = settings.GECO_MAPPING[db.code]['M_GECODEFS'][key]

        defaults = cls.get_definitons(db.code).get(key).copy()
        data = Tlohart.objects.using(db.code).values(
            code=F(MAPP['code']),
            name=F(MAPP['name'])
        )
        cls.base_sync(
            db,
            defaults.get('def_type'),
            [dict(item, **defaults) for item in data]
        )

    @classmethod
    def sync_shift_models(cls, db, key='SHIFT_MODELS'):
        from geco.models import Tschmod
        MAPP = settings.GECO_MAPPING[db.code]['M_GECODEFS'][key]

        defaults = cls.get_definitons(db.code).get(key).copy()
        data = Tschmod.objects.using(db.code).values(
            geco_id=F(MAPP['geco_id']),
            code=F(MAPP['code']),
            name=F(MAPP['name'])
        )
        cls.base_sync(
            db,
            defaults.get('def_type'),
            [dict(item, **defaults) for item in data]
        )

    @classmethod
    def sync_flex_shift_models(cls, db, key='FLEX_SHIFT_MODELS'):
        from geco.models import Tsprmod
        MAPP = settings.GECO_MAPPING[db.code]['M_GECODEFS'][key]

        defaults = cls.get_definitons(db.code).get(key).copy()
        data = Tsprmod.objects.using(db.code).values(
            geco_id=F(MAPP['geco_id']),
            code=F(MAPP['code']),
            name=F(MAPP['name'])
        )
        cls.base_sync(
            db,
            defaults.get('def_type'),
            [dict(item, **defaults) for item in data]
        )

    @classmethod
    def sync(cls, db):
        logger.info("Model/Gecodefs/Sync Fonksiyonu Başladı ")
        cls.sync_time_types(db)
        cls.sync_excuse_types(db)
        cls.sync_day_models(db)
        cls.sync_pay_models(db)
        cls.sync_pay_types(db)
        cls.sync_shift_models(db)
        cls.sync_flex_shift_models(db)
        logger.info("Model/Gecodefs/Sync Fonksiyonu Bitti ")