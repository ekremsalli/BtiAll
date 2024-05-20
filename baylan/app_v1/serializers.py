from rest_framework import serializers
from erp.models.friendly import (
    Orfiche,
    Items,
    Emcenter,
    Emuhacc,
    Payplans
)


class OrderCancellableSerializer(serializers.ModelSerializer):
    TRCODE = serializers.IntegerField(source='trcode')
    LOGICALREF = serializers.IntegerField(source='pk')
    FICHENO = serializers.CharField(source='ficheno')
    BRANCH = serializers.IntegerField(source='branch')
    CODE = serializers.CharField(source='clientref.code')
    DEFINITION_ = serializers.CharField(source='clientref.definition_field')

    class Meta:
        model = Orfiche
        fields = [
            'TRCODE',
            'LOGICALREF',
            'FICHENO',
            'BRANCH',
            'CODE',
            'DEFINITION_',
        ]


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


class InvoiceSerializer(serializers.ModelSerializer):
    EINVOICE = serializers.IntegerField(source='einvoice')
    FICHENO = serializers.CharField(source='ficheno')
    DATE_ = serializers.DateTimeField(source='date_field')
    DEFINITION_ = serializers.CharField(source='clientref.definition_field')
    NETTOTAL = serializers.FloatField(source='nettotal')

    class Meta:
        model = Orfiche
        fields = [
            'EINVOICE',
            'FICHENO',
            'DATE_',
            'DEFINITION_',
            'NETTOTAL',
        ]


class EmcenterSerializer(serializers.ModelSerializer):
    EmcCode = serializers.CharField(source='code')
    EmcDef = serializers.CharField(source='definition_field')
    class Meta:
        model = Emcenter
        fields = [
            'EmcCode',
            'EmcDef',
        ]


class AccountCodeSerializer(serializers.ModelSerializer):
    LOGICALREF = serializers.IntegerField(source='pk')
    CODE  = serializers.CharField(source='code')
    DEFINITION_ = serializers.CharField(source='definition_field')

    class Meta:
        model = Emuhacc
        fields = [
            'LOGICALREF',
            'CODE',
            'DEFINITION_',
        ]


class PayplanSerializer(serializers.ModelSerializer):
    LOGICALREF = serializers.IntegerField(source='pk')
    CODE  = serializers.CharField(source='code')
    DEFINITION_ = serializers.CharField(source='definition_field')

    class Meta:
        model = Payplans
        fields = [
            'LOGICALREF',
            'CODE',
            'DEFINITION_',
        ]
