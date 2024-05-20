from rest_framework import serializers

from app.models.base import DB

class DBSerializer(serializers.ModelSerializer):
    class Meta:
        model = DB
        fields = "__all__"