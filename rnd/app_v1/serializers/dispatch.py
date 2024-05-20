from rest_framework import serializers

from erp.active import Active
from erp.models.friendly import Stfiche, Stline, Capiwhouse

from app_v1.serializers.barcode import BarcodeSerializer

class DispatchLineSerializer(serializers.ModelSerializer):
    LineType = serializers.IntegerField(source='linetype')
    Code = serializers.CharField(source='stockref.code')
    Barcode = serializers.SerializerMethodField('get_barcode')
    LineDescription = serializers.CharField(source='lineexp')
    Quantity = serializers.IntegerField(source='amount')
    UnitPrice = serializers.FloatField(source='price')
    VAT = serializers.IntegerField(source='vat')
    TOTAL = serializers.FloatField(source='total')
    DeliveryCode = serializers.CharField(source='delvrycode')

    def get_barcode(self, obj):
        try:
            qs = obj.stockref.erp_lg_unitbarcode_itemref.first()
            if qs:
                return qs.barcode
        except:
            pass
        return ''


    class Meta:
        model = Stline
        fields = [
            "LineType",
            "Code",
            "Barcode",
            "LineDescription",
            "Quantity",
            "UnitPrice",
            "VAT",
            "TOTAL",
            "DeliveryCode",
        ]

class DispatchSerializer(serializers.ModelSerializer):
    DispatchDate = serializers.DateTimeField(source='date_field')
    FicheNo = serializers.CharField(source='ficheno', max_length=16)
    DocumentNo = serializers.CharField(source='docode')
    ArpCode = serializers.CharField(source='clientref.code')
    ClCardTitle = serializers.CharField(source='clientref.definition_field')
    Warehouse = serializers.IntegerField(source='sourceindex')
    WarehouseName = serializers.SerializerMethodField('get_warehouse')
    DispatchType = serializers.IntegerField(source='trcode')
    ProjectCode = serializers.CharField(source='projectref.code')
    DocumentTrackingNumber = serializers.CharField(source='doctrackingnr')
    InvoiceNo = serializers.CharField(source='invno')
    Lines = serializers.SerializerMethodField('get_lines')

    def get_lines(self, obj):
        qs = obj.erp_lg_stline_stficheref.all()
        return DispatchLineSerializer(qs, many=True, read_only=True).data


    def get_warehouse(self, obj):
        return Capiwhouse.objects.filter(
            nr=obj.sourceindex, 
            firm=Active.number
        ).values_list('name', flat=True).first()

    class Meta:
        model = Stfiche
        fields = [
            "DispatchDate", 
            "FicheNo",
            "DocumentNo",
            "ArpCode",
            "ClCardTitle",
            "Warehouse",
            "WarehouseName",
            "DispatchType",
            "ProjectCode",
            "DocumentTrackingNumber",
            "InvoiceNo",
            "Lines",
        ]
