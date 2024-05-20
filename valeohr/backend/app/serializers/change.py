from rest_framework import serializers

from app.models import Changes
from app.serializers.transaction import TransactionSerializer
from app.serializers.anomaly import AnomalySerializer
from app.serializers.employee import EmployeeSerializer


class ChangeDetailSerializer(serializers.ModelSerializer):
    source_db = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    modified_by = serializers.StringRelatedField()
    employee = serializers.StringRelatedField()
    transaction = TransactionSerializer()
    anomaly = AnomalySerializer()

    class Meta:
        model = Changes
        fields = "__all__"

    def get_verify_status(self, obj):
        return obj.get_verify_status_display()


class ChangeSerializer(serializers.ModelSerializer):
    source_db = serializers.StringRelatedField()
    verify_status = serializers.SerializerMethodField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Changes
        fields = "__all__"

    def get_verify_status(self, obj):
        return obj.get_verify_status_display()


