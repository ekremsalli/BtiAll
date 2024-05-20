from rest_framework import serializers

from bti.models.flow import Flow
from erp.models.friendly import Items

class ErpItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ["code", "active"]

class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flow
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ["code", "name"]

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = [
            "code",
            "name",
            "vat"
        ]

class TrendyolProductAttributeSerializer(serializers.Serializer):
    attributeId = serializers.IntegerField()
    attributeValueId = serializers.IntegerField(required=False)
    customAttributeValue = serializers.CharField(required=False)

class TrendyolProductImageSerializer(serializers.Serializer):
    url = serializers.CharField()

class TrendyolProductSerializer(serializers.Serializer):
    barcode = serializers.CharField(max_length=40)
    title = serializers.CharField(max_length=100)
    product_main_id = serializers.CharField(max_length=40)
    brand_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    stock_code = serializers.CharField(required=False, default='', allow_blank=True)
    dimensional_weight = serializers.FloatField()
    description = serializers.CharField()
    currency_type = serializers.CharField()
    list_price = serializers.FloatField()
    sale_price = serializers.FloatField()
    cargo_company_id = serializers.IntegerField()
    images = serializers.ListSerializer(child=TrendyolProductImageSerializer())
    vat_rate = serializers.IntegerField()
    attributes = serializers.ListSerializer(
        child=TrendyolProductAttributeSerializer(), allow_empty=True)
