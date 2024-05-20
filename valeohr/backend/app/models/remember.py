from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class PreventManager(models.Manager):
    def get_queryset(self):
        from datetime import datetime, timedelta
        qs = super().get_queryset()
        diff = datetime.now() - timedelta(
            minutes=settings.RESET_MAIL_WAIT_FOR_RESEND_AGAIN_MIN
        )
        return qs.filter(created__gt=diff)

class ValidManager(models.Manager):
    def get_queryset(self):
        from datetime import datetime
        qs = super().get_queryset()
        return qs.filter(
            valid_until__gt=datetime.now(),
            is_completed=False
        )

class Remember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(unique=True, max_length=64)
    request_ip = models.GenericIPAddressField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    sent = models.DateTimeField(null=True, blank=True)
    valid_until = models.DateTimeField(db_index=True)
    completed = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False, db_index=True)

    prevent_objects = PreventManager()
    valid_objects = ValidManager()
    objects = models.Manager()

    @classmethod
    def generate(cls, user, ip):
        from uuid import uuid4
        from datetime import datetime, timedelta
        token = uuid4().hex[-7:]
        valid_until= datetime.now() + timedelta(
            minutes=settings.RESET_MAIL_ACTIVE_FOR_MIN
        )

        return cls(
            user=user,
            token=token,
            request_ip=ip,
            valid_until=valid_until
        )

    def send(self):
        from datetime import datetime
        from django.core.mail import send_mail

        body = f"""
            Merhaba,
            Şifreni sıfırlamak için gerekli anahtar {self.token}
            
            Eğer böyle bir talebin yoksa lütfen bu e-postayı dikkate alma.        
        """

        send_mail(
            'ValeoHR şifre sıfırlama isteği',
            body,
            settings.DEFAULT_EMAIL_SENDER,
            [self.user.username],
        )
        self.sent = datetime.now()
        self.save()
