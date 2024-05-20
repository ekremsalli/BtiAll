from rest_framework import serializers

from app_v1.models import TaskActivity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivity
        fields = "__all__"