"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from rest_framework import serializers

from .models import *

class GittiGidiyorProductMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GittiGidiyorProductMatch
        fields = "__all__"

class GittiGidiyorProductMismatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GittiGidiyorProductMismatch
        fields = "__all__"

class GittiGidiyorLineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = GittiGidiyorLineLog
        fields = "__all__"

class GittiGidiyorLogSerializer(serializers.ModelSerializer):
    lines = GittiGidiyorLineLogSerializer(
        source='GittiGidiyorlinelog_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = GittiGidiyorLog
        fields = [
            'pk', 'order_number', 'order_id', 'raw', 'internal_ref',
            'created', 'lines'
        ]

class GittiGidiyorCargoMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = GittiGidiyorCargoMap
        fields = "__all__"

class GittiGidiyorCargoMismatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GittiGidiyorCargoMismatch
        fields = "__all__"
