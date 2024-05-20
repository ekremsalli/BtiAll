from rest_framework import serializers
from django.contrib.auth.models import User

from app.models import Organization, LogoApiErrors, EmployeeLogs


class BulkCreateListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)


        return result


class EmployeeLogSerializer(serializers.ModelSerializer):
    organization_id = serializers.CharField(required=False)
    unique_id = serializers.CharField(required=False)
    tarnet_user_id = serializers.CharField(required=False)
    direction = serializers.CharField(required=False)
    full_name = serializers.CharField(required=False)
    utc = serializers.DateTimeField()
    in_time = serializers.DateTimeField()
    out_time = serializers.DateTimeField()

    class Meta:
        fields = (
            "organization_id", "unique_id", "tarnet_user_id", "direction", "full_name", "utc", "in_time", "out_time")
        list_serializer_class = BulkCreateListSerializer

    def create(self, validated_data):
        return EmployeeLogs.objects.create(**validated_data)
