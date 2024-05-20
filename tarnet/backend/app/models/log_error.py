from django.db import models
from django.utils import timezone


class LogoApiErrors(models.Model):
    """
    Logo gönderim esnasında oluşan hataları buraya kayıt eder
    """
    organization_id = models.CharField(max_length=250, help_text="organizasyon id ", null=True, blank=True)
    unique_id = models.CharField(max_length=50, help_text="kullanıcı TC No", default="")
    full_name = models.CharField(max_length=150, default="", null=True, blank=True)
    message = models.CharField(max_length=350, null=True, blank=True)
    msg_list = models.TextField(help_text="logo dan gelen msg_list", null=True, blank=True)
    query_text = models.TextField(help_text="logo ya iletilecek query text", null=True, blank=True)
    code = models.CharField(max_length=250, help_text="logo daki personel kodu", null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    date_time = models.CharField(max_length=30, default="", null=True, blank=True)
    is_active = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'logo_api_error'

    def is_activate(self):
        self.is_active = True
        self.save()
