"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from rest_framework import serializers

from bti.models import Flow


class FlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flow
        fields = "__all__"
