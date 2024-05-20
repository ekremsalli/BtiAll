from rest_framework import serializers

from erp.models.friendly import UnitBarcode
from .item import ItemSerializer

class BarcodeSerializer(serializers.ModelSerializer):
    BARCODE = serializers.CharField(source='barcode')
    ITEM = ItemSerializer(source='itemref')
    class Meta:
        model = UnitBarcode
        fields = ["BARCODE", "ITEM"]
