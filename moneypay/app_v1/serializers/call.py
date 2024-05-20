from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from app_v1.models import Operation


class CallSerializer(serializers.Serializer):
    delta = serializers.IntegerField(label='Delta', default=1)
