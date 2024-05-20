"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from rest_framework import serializers

from .models import *

class HepsiburadaProductMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = HepsiburadaProductMatch
        fields = "__all__"

class HepsiburadaProductMismatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = HepsiburadaProductMismatch
        fields = "__all__"

class HepsiburadaLineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HepsiburadaLineLog
        fields = "__all__"

class HepsiburadaLogSerializer(serializers.ModelSerializer):
    lines = HepsiburadaLineLogSerializer(
        source='hepsiburadalinelog_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = HepsiburadaLog
        fields = [
            'pk', 'order_number', 'order_id', 'raw', 'internal_ref',
            'created', 'lines'
        ]

class HepsiburadaCargoMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = HepsiburadaCargoMap
        fields = "__all__"

class HepsiburadaCargoMismatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = HepsiburadaCargoMismatch
        fields = "__all__"
