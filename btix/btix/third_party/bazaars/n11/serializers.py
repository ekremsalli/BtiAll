"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from rest_framework import serializers

from .models import *

class N11ProductMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = N11ProductMatch
        fields = "__all__"

class N11ProductMismatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = N11ProductMismatch
        fields = "__all__"

class N11LineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = N11LineLog
        fields = "__all__"

class N11LogSerializer(serializers.ModelSerializer):
    lines = N11LineLogSerializer(
        source='n11linelog_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = N11Log
        fields = [
            'pk', 'order_number', 'order_id', 'raw', 'internal_ref',
            'created', 'lines'
        ]


class N11CargoMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = N11CargoMap
        fields = "__all__"

class N11CargoMismatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = N11CargoMismatch
        fields = "__all__"