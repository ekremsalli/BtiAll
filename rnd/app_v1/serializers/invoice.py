from datetime import date
from rest_framework import serializers
from erp.active import Active
from erp.models.friendly import (
    Invoice,
    Clcard,
    Capiwhouse,
    Stfiche,
    Stline,
    Itmunita,
    EarchiveDet,
)


class InvoiceEArchiveInfoSerializer(serializers.Serializer):
    SendingType = serializers.IntegerField(source='sendmod')
    EArchiveType = serializers.IntegerField(source='earchivestatus')
    PaymentMethod = serializers.IntegerField(source='intpaymenttype')
    PaymentDate = serializers.SerializerMethodField()
    PayingAgent = serializers.CharField(source='intpaymentagent')
    InstallationNumber = serializers.CharField(source='installmentnumber')
    WebAddress = serializers.CharField(source='intsalesaddr')

    def get_PaymentDate(self, obj):
        if obj.intpaymentdate:
            dx = obj.intpaymentdate
            try:
                year = int(dx / 65536)
                month = int((dx % 65536) / 256)
                day = int((dx % 65536) % 256)
                return date(year, month, day).isoformat()
            except:
                pass
        return None

    class Meta:
        model = EarchiveDet
        fields = [
            'SendingType',
            'EArchiveType',
            'PaymentMethod',
            'PaymentDate',
            'PayingAgent',
            'InstallationNumber',
            'WebAddress',
        ]


class InvoiceDetailLineSerializer(serializers.ModelSerializer):
    LineType = serializers.IntegerField(source='linetype')
    LineTypeDisplay = serializers.CharField(source='get_linetype_display')
    Code = serializers.CharField(source='stockref.code')
    Barcode = serializers.SerializerMethodField()
    LineDescription = serializers.CharField(source='lineexp')
    Quantity = serializers.FloatField(source='amount')
    UnitPrice = serializers.FloatField(source='price')
    VAT = serializers.FloatField(source='vat')
    Total = serializers.FloatField(source='total')
    VatAmount = serializers.FloatField(source='vatamnt')

    def get_Barcode(self, obj):
        itmunit = Itmunita.objects.filter(
            itemref=obj.stockref,
            unitlineref=obj.uomref
        ).first()
        if itmunit:
            return itmunit.barcode
        return None

    class Meta:
        model = Stline
        fields = [
            'LineType',
            'LineTypeDisplay',
            'Code',
            'Barcode',
            'LineDescription',
            'Quantity',
            'UnitPrice',
            'VAT',
            'Total',
            'VatAmount',
        ]


class InvoiceDetailCLSerializer(serializers.ModelSerializer):
    Code = serializers.CharField(source='code')
    Title = serializers.CharField(source='definition_field')

    class Meta:
        model = Clcard
        fields = ['Code', 'Title']


class InvoiceDetailSerializer(serializers.ModelSerializer):
    InvoiceNo = serializers.CharField(source='ficheno')
    DateTime = serializers.SerializerMethodField()
    DocumentNo = serializers.CharField(source='docode')
    AuxilCode = serializers.CharField(source='specode')
    CLCard = InvoiceDetailCLSerializer(source='clientref')
    Warehouse = serializers.IntegerField(source='sourceindex')
    WarehouseName = serializers.SerializerMethodField()
    InvoiceType = serializers.IntegerField(source='trcode')
    InvoiceTypeDisplay = serializers.CharField(source='get_trcode_display')
    ProjectCode = serializers.CharField(source='projectref.code')
    AuxilCode = serializers.CharField(source='specode')
    EarchiveInfo = serializers.SerializerMethodField()
    Description = serializers.SerializerMethodField()
    DocumentTrackNo = serializers.CharField(source='doctrackingnr')
    ShipmentAgentCode = serializers.CharField(source='shpagncod')
    Dispatches = serializers.SerializerMethodField()
    Lines = serializers.SerializerMethodField()

    def get_EarchiveInfo(self, obj):
        return InvoiceEArchiveInfoSerializer(
            EarchiveDet.objects.filter(invoiceref=obj).first()
        ).data

    def get_Lines(self, obj):
        return InvoiceDetailLineSerializer(
            Stline.objects.filter(invoiceref=obj),
            many=True
        ).data

    def get_Dispatches(self, obj):
        filter = Active.settings['KODLAMA']['IRSALIYE_SORGU']
        return Stfiche.objects.filter(
            invoiceref=obj, **filter).values_list('ficheno', flat=True)

    def get_Description(self, obj):
        return [
            obj.genexp1,
            obj.genexp2,
            obj.genexp3,
            obj.genexp4,
            obj.genexp5,
            obj.genexp6
        ]

    def get_WarehouseName(self, obj):
        warehouse = Capiwhouse.objects.filter(
            nr=obj.sourceindex,
            firm=Active.number).first()
        if warehouse:
            return warehouse.name
        return ''

    def get_DateTime(self, obj):
        hour = int(obj.time_field / (65536 * 256))
        mod1 = obj.time_field % (65536 * 256)
        minute = int(mod1 / 65536)
        second = int((mod1 % 65536) / 256)
        return obj.date_field.replace(
            hour=hour,
            minute=minute,
            second=second
        ).isoformat()

    class Meta:
        model = Invoice
        fields = [
            'InvoiceNo',
            'DateTime',
            'DocumentNo',
            'AuxilCode',
            'CLCard',
            'Warehouse',
            'WarehouseName',
            'InvoiceType',
            'InvoiceTypeDisplay',
            'ProjectCode',
            'AuxilCode',
            'EarchiveInfo',
            'Description',
            'DocumentTrackNo',
            'ShipmentAgentCode',
            'Dispatches',
            'Lines',
        ]


class LineSerializer(serializers.Serializer):
    LineType = serializers.IntegerField()
    Code = serializers.CharField(required=False)
    Quantity = serializers.IntegerField(required=True)
    UnitPrice = serializers.FloatField(required=True)
    VAT = serializers.FloatField(required=True)
    LineDescription = serializers.CharField(required=False)
    UnitCode = serializers.CharField(required=False)
    UnitConv1 = serializers.FloatField(required=False)
    UnitConv2 = serializers.FloatField(required=False)
    vatexcept_reason = serializers.CharField(
        label='KDV İstisna nedeni', required=False)
    vatexcept_code = serializers.CharField(
        label='KDV İstisna kodu', required=False)
    discexp_calc = serializers.IntegerField(required=False)
    discount_rate = serializers.FloatField(required=False)
    calc_type = serializers.IntegerField(required=False)
    detail_level = serializers.IntegerField(required=False)

    ret_cost_type = serializers.IntegerField(
        label="İade maliyeti türü", required=False)
    source_reference = serializers.IntegerField(
        label="Connection of Resource Transaction in Returns", required=False)

    # def validate_source_reference(self, value):
    #
    #     self.initial_data['source_reference'] = value
    #     self.initial_data['ret_cost_type'] = value
    #
    #     # .is_valid() yöntemini çağırın
    #     self.is_valid()
    #
    #     ret_cost_type = self.validated_data.get('ret_cost_type')
    #     source_reference = self.validated_data.get('source_reference')
    #
    #
    #     if ret_cost_type == 0 and not source_reference:
    #         raise serializers.ValidationError('Source Reference field is required for Ret Cost Type 0')
    #     elif ret_cost_type == 1 and source_reference:
    #         raise serializers.ValidationError('Source Reference field must be blank for Ret Cost Type 1')
    #
    #     return value


class EArchiveInfoSerializer(serializers.Serializer):
    # eInvoice = serializers.IntegerField(
    #     label="0=Kağıt,1 = e-fatura, 2= e-arşiv, 3= e-arşiv internet", required=False)
    InsteadOfDispatch = serializers.IntegerField(
        label="1 = İrsaliye yerine geçer, 0 = boş bırakır", required=False)
    SendingType = serializers.IntegerField(
        label="Gönderim Şekli 1 = Kağıt, 2 = Elektronik ", required=False)
    EArchiveType = serializers.IntegerField(
        label="E-arşiv tipi 1 = Matrah,2=İstisna,3=Araç Tescil,4=Tevkifat,6=komisyoncu,7=Satış", required=False)
    PaymentMethod = serializers.CharField(
        label="Ödeme şekli 0=K.Kart/Bank,1=EFT,2=Kapıda Ödeme,3=Ödeme Aracısı,4=Diğer", required=True)
    PaymentDate = serializers.DateTimeField(label="Ödeme Tarihi",
                                            input_formats=[
                                                "%Y-%m-%dT%H:%M:%S",
                                                "%Y-%m-%dT%H:%M:%S.%f",
                                                "%Y-%m-%dT%H:%M:%SZ"
                                            ])
    PayingAgent = serializers.CharField(label="Ödeme Aracısı", required=True)
    InstallionNumber = serializers.IntegerField(
        label="Tesisat Numarsı", required=False)
    WebAddress = serializers.CharField(label="Web Adresi", required=True)


class InvoiceSerializer(serializers.Serializer):
    InvoiceNo = serializers.CharField(label='Fatura numarası', required=True)
    type = serializers.IntegerField(label='Fatura Type', required=True)
    DateTime = serializers.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"])
    DocumentNo = serializers.CharField(
        max_length=11, label='Belge numarası', required=False)
    ARP_CODE = serializers.CharField(label='Cari hesap kodu', required=True)
    Payments = serializers.CharField(required=False)
    AuxilCode = serializers.CharField(
        max_length=11, label='Yetki kodu', required=False)
    Warehouse = serializers.IntegerField(label='Ambar', required=True)
    EArchiveInfo = EArchiveInfoSerializer()
    Dispatches = serializers.ListSerializer(child=serializers.CharField())
    Lines = serializers.ListSerializer(child=LineSerializer())
    vatexcept_reason = serializers.CharField(
        label='KDV İstisna nedeni', required=False)
    vatexcept_code = serializers.CharField(
        label='KDV İstisna kodu', required=False)


class InvoiceReadSerializer(serializers.Serializer):
    invoice_no = serializers.CharField(label='Fatura numarası')
    order_no = serializers.CharField(label='Sipariş numarası')
    prefix = serializers.CharField(label='Özel kod')
    date_field = serializers.DateField(label='Fatura tarihi')

    def to_representation(self, instance):
        return {
            'invoice_no': instance[0],
            'order_no': instance[1],
            'date_field': instance[2],
            'prefix': instance[3]
        }


class ReturnTransactionSerializer(serializers.Serializer):
    LineType = serializers.IntegerField(label='type')
    # Code = serializers.CharField(required=False)
    Quantity = serializers.IntegerField(required=True)
    # UnitPrice = serializers.FloatField(required=True)
    VAT = serializers.FloatField(label='KDV oran', required=True)
    date_field = serializers.DateField(label='tarih', required=False)
    master_code = serializers.CharField(label="", required=False)
    unit_code = serializers.CharField(label="", required=False)

    ret_cost_type = serializers.IntegerField(
        label="İade maliyeti türü (Giriş/Çıkış maliyeti için gönderilmez , 1 = Güncel maliyet, 2 = İade maliyeti)", required=False)
    rest_cost = serializers.FloatField(label="İade miktarı", required=False)
    source_reference = serializers.IntegerField(
        label="Connection of Resource Transaction in Returns", required=False)


class ReturnInvoiceSerializer(serializers.Serializer):
    ARP_CODE = serializers.CharField(label='Cari hesap kodu', required=True)
    type = serializers.IntegerField(label='Fatura Type', required=True)
    DateTime = serializers.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"])

    Lines = serializers.ListSerializer(child=ReturnTransactionSerializer())
