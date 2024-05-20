from rest_framework import serializers
from django.contrib.auth.models import User

from app.models import LogoApiErrors


class LogErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoApiErrors
        fields = ('id', 'unique_id', 'full_name', 'message', 'msg_list', "code", "date_time")


class SendErrorSerializers(serializers.Serializer):
    id = serializers.IntegerField()

    class Meta:
        fields = ('id',)


class TotalSendSerializers(serializers.Serializer):
    organization_id = serializers.CharField(required=True)
