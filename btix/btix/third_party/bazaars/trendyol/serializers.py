"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from rest_framework import serializers

from .models import *

class TrendyolProductMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendyolProductMatch
        fields = "__all__"

class TrendyolProductMismatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendyolProductMismatch
        fields = "__all__"

class TrendyolLineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendyolLineLog
        fields = "__all__"

class TrendyolLogSerializer(serializers.ModelSerializer):
    lines = TrendyolLineLogSerializer(
        source='trendyollinelog_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = TrendyolLog
        fields = [
            'pk', 'order_number', 'order_id', 'raw', 'internal_ref',
            'created', 'lines'
        ]


class TrendyolCargoMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendyolCargoMap
        fields = "__all__"

class TrendyolCargoMismatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendyolCargoMismatch
        fields = "__all__"