from rest_framework import serializers

from app.models import Excuse, Employees


class ExcuseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Excuse
        # fields = '__all__'
        fields = (
            'id', "employee_id", "tr_date", "start", "end", "work_time", "time_type", "excuse_type",
            "excuse_day", "day_model", "account", "pay_type", "description", "created_by", 'source_db', 'day_types')


class ExcuseApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excuse
        fields = ('verify_status',)


class ExcuseDetailSerializer(serializers.ModelSerializer):
    # source_db = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    # modified_by = serializers.StringRelatedField()
    # employee = serializers.StringRelatedField()
    title = serializers.StringRelatedField()

    class Meta:
        model = Excuse
        fields = (
            "id", "employee_id", "title", "tr_date", "start", "end", "work_time", "description", "excuse_day",
            "day_model", "day_types",
            "created_by")


class ExcuseAllAproveSerializer(serializers.Serializer):
    excuse_ids = serializers.ListField(child=serializers.IntegerField())
    verify_status = serializers.IntegerField(required=True)


class ExcuseAllDeleteSerializer(serializers.Serializer):
    excuse_ids = serializers.ListField(child=serializers.IntegerField())
