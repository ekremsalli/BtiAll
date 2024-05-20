from django.db import models
from django.contrib.auth.models import User


class DB(models.Model):
    code = models.CharField(max_length=16, unique=True)
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(
        default=True
    )

    @classmethod
    def get_db(cls, db):
        dbo = cls.objects.filter(code=db).first()
        if dbo is None:
            return cls.objects.create(code=db, title=db)
        return dbo

    def __str__(self):
        return self.title


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=0)


class DeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=-1)


class BaseModel(models.Model):
    STATUS = [
        (0, 'Geçerli'),
        (-1, 'Silinmiş')
    ]

    status = models.SmallIntegerField(
        choices=STATUS,
        help_text='Kayıt durumu',
        default=0,
        db_index=True
    )

    source_db = models.ForeignKey(
        DB,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text='Oluşturulma'
    )
    created_by = models.ForeignKey(
        User,
        null=True,
        help_text='Oluşturan',
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_cby'
    )

    modified_on = models.DateTimeField(
        auto_now=True,
        help_text='Güncelleme'
    )
    modified_by = models.ForeignKey(
        User,
        null=True,
        help_text='Güncelleyen',
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_mby'
    )

    class Meta:
        abstract = True


class BaseTransaction(BaseModel):
    EXCUSE_DAY_TYPES = [
        (0, 'Tam gün'),
        (1, 'Öğleden önce'),
        (2, 'Öğleden sonra')
    ]
    employee = models.ForeignKey(
        'Employees', null=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_employee'
    )
    tr_date = models.DateField(help_text='Hareket tarihi', null=True)
    start = models.TimeField(help_text='Giriş saati', null=True)
    end = models.TimeField(help_text='Çıkış saati', null=True)
    work_time = models.IntegerField(
        default=0,
        help_text='Çalışma süresi Saat * 100 + Dakika'
    )
    time_type = models.CharField(
        max_length=6, help_text='Zaman tipi',
        null=True, blank=True
    )
    excuse_type = models.CharField(
        max_length=5, help_text='Mazeret tipi',
        null=True, blank=True
    )
    excuse_day = models.SmallIntegerField(
        choices=EXCUSE_DAY_TYPES,
        null=True, blank=True
    )
    day_model = models.CharField(
        max_length=5, help_text='Gün modeli kayıt numarası',
        null=True, blank=True
    )
    account = models.CharField(
        max_length=20, help_text='Hesaplama grubu',
        null=True, blank=True
    )
    pay_type = models.CharField(
        max_length=6, help_text='Puantaj tipi',
        null=True, blank=True
    )
    geco_user = models.CharField(
        max_length=20,
        help_text='Geco kaydını düzenleyen kullanıcı',
        null=True, blank=True
    )

    class Meta:
        abstract = True
    #h