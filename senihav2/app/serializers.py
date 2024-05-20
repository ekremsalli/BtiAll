from rest_framework import serializers
from erp.active import Active
from app.models import idea_choices


class TrendyolOrderLineSerializer(serializers.Serializer):
    line = serializers.IntegerField()
    quantity = serializers.IntegerField()

class TrendyolUnsuppliedStatusSerializer(serializers.Serializer):
    id = serializers.CharField()
    lines = TrendyolOrderLineSerializer(many=True)

class TrendyolPickingStatusSerializer(serializers.Serializer):
    id = serializers.CharField()
    lines = TrendyolOrderLineSerializer(many=True)


class TrendyolCargoSerializer(serializers.Serializer):
    id = serializers.CharField()
    url = serializers.CharField()

class TrendyolInvoiceStatusSerializer(serializers.Serializer):
    id = serializers.CharField()
    invoice_number = serializers.CharField()
    lines = TrendyolOrderLineSerializer(many=True)

class IdeaStatusSerializer(serializers.Serializer):
    order = serializers.IntegerField()
    status = serializers.ChoiceField(choices=idea_choices)

class IdeaStockSerializer(serializers.Serializer):
    order = serializers.IntegerField()
    stock_amount = serializers.IntegerField()

class IdeaCargoSerializer(serializers.Serializer):
    order = serializers.IntegerField()
    provider_code = serializers.CharField()
    company_name = serializers.CharField()
    payment_type = serializers.CharField()
    tracking_code = serializers.CharField()

class DispatchItemSerializer(serializers.Serializer):
    master_code = serializers.CharField()
    date = serializers.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ"])
    source_index = serializers.IntegerField(required=False, default=0)
    source_cost_grp = serializers.IntegerField(required=False, default=0)
    quantity = serializers.FloatField()
    unit_code = serializers.CharField()
    price = serializers.FloatField(required=False)
    vat_rate = serializers.FloatField(required=False)
    description = serializers.CharField()

class DispatchCreateSerializer(serializers.Serializer):
    firm = serializers.IntegerField(required=False)
    on_time = serializers.BooleanField(default=False)
    doc_tracking_number = serializers.CharField(required=True)
    date = serializers.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ"])
    doc_number = serializers.CharField(required=True)
    auxil_code = serializers.CharField(required=False)
    arp_code = serializers.CharField(required=False)
    source_wh = serializers.IntegerField(required=False, default=0)
    source_cost_grp = serializers.IntegerField(required=False, default=0)
    notes1 = serializers.CharField(max_length=255, required=False)
    notes2 = serializers.CharField(max_length=255, required=False)
    notes3 = serializers.CharField(max_length=255, required=False)
    notes4 = serializers.CharField(max_length=255, required=False)
    notes5 = serializers.CharField(max_length=255, required=False)
    ship_date = serializers.DateTimeField()
    doc_date = serializers.DateTimeField()
    items = DispatchItemSerializer(many=True, allow_empty=False)
    driver_name = serializers.CharField(required=False, default='')
    driver_surname = serializers.CharField(required=False, default='')
    driver_tckno = serializers.CharField(required=False, default='')
    plate = serializers.CharField(required=False, default='')
