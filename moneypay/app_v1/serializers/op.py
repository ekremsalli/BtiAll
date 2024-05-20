from rest_framework import serializers

from app_v1.models import Operation, OperationDetail

class OperationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationDetail
        fields = "__all__"

class OperationSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField('get_details')

    def get_details(self, obj):
        serializer = OperationDetailSerializer(obj.operationdetail_set.all(), many=True)
        return serializer.data

    class Meta:
        model = Operation
        fields = ["id", "code", "description", "created", "details"]