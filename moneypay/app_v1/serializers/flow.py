from rest_framework import serializers

from bti.models.flow import Flow

class FlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flow
        fields = "__all__"