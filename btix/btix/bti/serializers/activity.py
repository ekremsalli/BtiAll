"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from rest_framework import serializers

from bti.models import TaskActivity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivity
        fields = "__all__"
