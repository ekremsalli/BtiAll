from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import connection


class EmployeeLogs(models.Model):
    """
    Armandan gelen çalışanların giriş çıkış bilgileri bu tabloda tutulur
    """
    organization_id = models.CharField(max_length=250, help_text="organizasyon id ")
    unique_id = models.CharField(max_length=50, help_text="kullanıcı TC No", default="")
    tarnet_user_id = models.CharField(max_length=250, help_text="armon api den gelen personel id")
    direction = models.CharField(max_length=5, help_text="1 ise giriş 2 ise çıkış", blank=True, null=True)
    full_name = models.CharField(max_length=150)
    utc = models.DateTimeField()
    in_time = models.DateTimeField(blank=True, null=True)
    out_time = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=timezone.now())

    class Meta:
        db_table = 'employee_log'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE {} RESTART IDENTITY;".format(cls._meta.db_table))
