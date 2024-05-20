from rest_framework import serializers
from erp.models.friendly import (
    Items,
)


class WantageItemSerializer(serializers.Serializer):
    UrunKod = serializers.CharField()
    Miktar = serializers.IntegerField()


class WantageSerializer(serializers.Serializer):
    ORDER_KEY = serializers.CharField(required=True)
    TARIH = serializers.DateTimeField(
        required=True,
        input_formats=['%Y-%m-%dT%H:%M:%S']
    )
    SUBE_KOD = serializers.CharField(required=True)
    YETKI_KODU = serializers.CharField(required=True)
    ITEMS = serializers.ListField(
        child=WantageItemSerializer(),
        required=True,
        min_length=1
    )

    def validate(self, attrs):
        codes = set([item.get('UrunKod') for item in attrs.get('ITEMS')])
        control = lambda code: Items.objects.filter(active=0, code=code).exists()
        checks = {code: control(code) for code in codes}

        if all(checks.values()) is False:
            invalid = [key for key, value in checks.items() if value is False]
            raise serializers.ValidationError(
                f'Tanımsız veya aktif olmayan ürünler mevcut! {invalid}'
            )

        return attrs
