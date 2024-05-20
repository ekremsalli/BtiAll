from datetime import datetime
from django.db import models
from django.conf import settings


from .base import BaseModel, ActiveManager, DeletedManager
import logging

logger = logging.getLogger("app")
class Employees(BaseModel):
    EMPLOYEE_STATUS = [
        (0, 'Aktif personel'),
        (1, 'Eski personel'),
        (-1, 'Silinmiş')
    ]

    WORKER_TYPE = [
        (1, 'Beyaz yaka'),
        (2, 'Mavi yaka')
    ]

    status = models.SmallIntegerField(choices=EMPLOYEE_STATUS, 
        db_index=True, help_text='Kayıt durumu')
    nr = models.BigIntegerField(db_index=True, 
        help_text='Sicil numarası')
    name = models.CharField(max_length=40, 
        help_text='Personel adı')
    surname = models.CharField(max_length=40, 
        help_text='Personel soyadı')
    firm = models.CharField(max_length=50, 
        help_text='Firma adı')
    department = models.CharField(max_length=50, 
        help_text='Departman adı')
    title = models.CharField(max_length=50, help_text='Ünvanı')
    worker_type = models.SmallIntegerField(choices=WORKER_TYPE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    psoft_id = models.CharField(max_length=50, null=True, 
        blank=True, help_text='People Soft ID')
    work_id = models.CharField(max_length=50, 
        null=True, blank=True, help_text='Çalışma ID')
    account = models.CharField(max_length=20, 
        null=True, blank=True, help_text='Hesaplama grup kodu')
    cost_center = models.CharField(max_length=20, 
        null=True, blank=True, 
        help_text='Güncel masraf yeri kodu'
    )

    active_objects = ActiveManager()
    deleted_objects = DeletedManager()    
    objects = models.Manager()

    class Meta:
        unique_together = ('source_db', 'nr')

    def __str__(self):
        return f'({self.nr}) {self.name} {self.surname} [{self.source_db.code} / { self.firm }]'


    @classmethod
    def sync(cls, db):
        logger.info("Model/Employee/Sync Fonksiyonu Başladı ")
        from geco.models import Tpertab, Tperind
        EMP_MAPPING = settings.GECO_MAPPING[db.code]['EMPLOYEE']
        WT = EMP_MAPPING['WORKER_TYPES']
        MAPP = settings.GECO_MAPPING[db.code].get('M_EMPLOYEE')

        bulk_size = 100
        bulk_op = lambda n: [ n[i:i+bulk_size] for i in range(0, len(n), bulk_size) ]

        exists = set(cls.objects.filter(
            source_db=db
        ).values_list('nr', flat=True))        
        newbies, updates, found = [], [], set([])
        additionals = { 
            getattr(n, MAPP['per_nr']) : n 
            for n in Tperind.objects.using(db.code).all() 
        }
        for personel in Tpertab.objects.using(db.code).all():
            """
                Giriş tarihi belirtilmişse
                Çıkış tarihi belirtilmişse
                ve Giriş tarihi, Çıkış tarihinden küçükse.
                * Yeniden işe girebilir.
            """
            tstart = getattr(personel, MAPP['start'])
            tend = getattr(personel, MAPP['end'])
            oldie = 1 if (tstart and tend and tstart < tend) else 0

            worker_type = getattr(personel, MAPP['worker_type'])
            name = getattr(personel, MAPP['name'])
            surname = getattr(personel, MAPP['surname'])
            firm = getattr(personel, MAPP['firm'])
            department = getattr(personel, MAPP['department'])
            title = getattr(personel, MAPP['title'])
            psoft_id = getattr(personel, MAPP['psoft_id'])
            account = getattr(personel, MAPP['account'])
            cost_center = getattr(personel, MAPP['cost_center'])
            record = {
                'source_db': db,                
                'status': oldie,
                'nr': getattr(personel, MAPP['nr']),
                'name': name if name else '',
                'surname': surname if surname else '',
                'firm': firm if firm else '',
                'department': department if department else '',
                'title': title if title else '',
                'worker_type': WT.get(worker_type, None),
                'psoft_id': psoft_id,
                'account': account,
                'cost_center': cost_center 
            }
            if getattr(personel, MAPP['nr']) in additionals:
                item = additionals[getattr(personel, MAPP['nr'])]
                record.update({
                    'work_id': getattr(item, MAPP['work_id'])
                })
            if personel.per_persnr in exists:
                record.update({'modified_on': datetime.now()})
                updates.append(record)
            else:
                newbies.append(cls(**record))
                        
        diffs = list(exists.difference(found))

        for group in bulk_op(diffs):
            cls.objects.filter(
                source_db=db,
                nr__in=group
                ).update(status=-1)
        
        nrs = { rec['nr']: rec for rec in updates }
        nkeys = list(nrs.keys())
        records = []
        for group in bulk_op(nkeys):
            records.extend(cls.objects.filter(
                source_db=db,
                nr__in=group
            ))
        for item in records:
            for kx, vx in nrs[item.nr].items():
                setattr(item, kx, vx)
        cls.objects.bulk_create(newbies)

        fields = [
            'status', 'name', 'surname', 
            'firm', 'department', 'title', 
            'worker_type', 'psoft_id', 'work_id',
            'account', 'cost_center', 'modified_on'
        ]
        for field in fields:
            tmp = [rec for rec in records if getattr(rec, field) is not None]
            cls.objects.bulk_update(tmp, [field])
        logger.info("Model/Employee/Sync Fonksiyonu Bitti ")