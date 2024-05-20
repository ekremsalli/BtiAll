from rest_framework import serializers


class PayrollSerializer(serializers.Serializer):
    db = serializers. CharField()
    start = serializers.CharField()
    end = serializers.CharField()
    firm = serializers.ListField(required=False)
    employees = serializers.ListField(required=False)
    worker_type = serializers.IntegerField(required=False)
