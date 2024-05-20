from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Organization(models.Model):
    """
    Armon da tanımlanan Organizasyonlar burda tanımlanır.
    """
    organization_id = models.CharField(max_length=250, help_text="organizasyon id ", unique=True)
    organization_name = models.CharField(max_length=250, help_text="Organizasyon Adı")
    grant_type_id = models.CharField(max_length=250, help_text="grant type id", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=timezone.now())

    class Meta:
        db_table = 'organization'


class OrganizationUser(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_org')
    organization_id = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name="organization")

    class Meta:
        db_table = 'organization_user'

    def create(self,**validated_data):
        return OrganizationUser.objects.create(**validated_data)