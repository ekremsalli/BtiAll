"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from rest_framework import serializers

from .models import *

class CiceksepetiProductMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiceksepetiProductMatch
        fields = "__all__"

class CiceksepetiProductMismatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiceksepetiProductMismatch
        fields = "__all__"

class CiceksepetiLineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiceksepetiLineLog
        fields = "__all__"

class CiceksepetiLogSerializer(serializers.ModelSerializer):
    lines = CiceksepetiLineLogSerializer(
        source='ciceksepetilinelog_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = CiceksepetiLog
        fields = [
            'pk', 'order_number', 'order_id', 'raw', 'internal_ref',
            'created', 'lines'
        ]

class CiceksepetiCargoMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiceksepetiCargoMap
        fields = "__all__"

class CiceksepetiCargoMismatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiceksepetiCargoMismatch
        fields = "__all__"
