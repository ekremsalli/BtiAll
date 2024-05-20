from rest_framework import serializers

from erp.models.friendly import Items, UnitBarcode

item_choices = [
    (1, 'Ticari mal'),
    (2, 'Karma koli'),
    (3, 'Depozitolu mal'),
    (4, 'Sabit kıymet'),
    (10, 'Hammadde'),
    (11, 'Yarımamül'),
    (12, 'Mamül'),
    (13, 'Tüketim malı'),
    (20, 'M. sınıfı (genel)'),
    (21, 'M. sınıfı (tablolu)'),
    (22, 'Firma dosyaları oluşturulurken default olarak eklenen malzeme sınıfı')
]


class_type_choices = [
    (0, 'Malzeme'),
    (20, 'Malzeme sınıfı')
]


class BarcodeSerializer(serializers.ModelSerializer):
    BARCODE = serializers.CharField(source='barcode')

    class Meta:
        model = UnitBarcode
        ref_name = 'item_pers'
        fields = [
            'BARCODE'
        ]


class ItemSerializer(serializers.ModelSerializer):
    INTERNAL_REFERENCE = serializers.IntegerField(source='logicalref')
    CODE = serializers.CharField(source='code')
    CARD_TYPE = serializers.IntegerField(source='cardtype')
    NAME = serializers.CharField(source='name')
    AUXIL_CODE = serializers.CharField(source='specode')
    AUTH_CODE = serializers.CharField(source='cyphcode')
    CREATED = serializers.CharField(source='created')
    UPDATED = serializers.CharField(source='updated')
    ACTIVE = serializers.CharField(source='active')
    
    BARCODES = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = [
            'INTERNAL_REFERENCE',
            'CODE',
            'CARD_TYPE',
            'NAME', 
            'AUXIL_CODE', 
            'AUTH_CODE',
            'CREATED', 
            'UPDATED', 
            'ACTIVE',
            'BARCODES',

        ]

    def get_BARCODES(self, item):
        qs = item.erp_lg_unitbarcode_itemref.all()
        return BarcodeSerializer(qs, many=True, read_only=True).data


class ItemPatchSerializer(serializers.Serializer):
    card_type = serializers.ChoiceField(label="Malzeme türü", choices=item_choices, required=False)
    name = serializers.CharField(label="Açıklama", max_length=51, required=False)
    producer_code = serializers.CharField(label="Üretici Kodu", max_length=25, required=False)
    auxil_code = serializers.CharField(label="Özel Kod", max_length=11,required=False)
    vat = serializers.IntegerField(label="KDV", required=False)
    usef_sales = serializers.IntegerField(label="Kullanım yeri satış-dağıtım", required=False, default=0)
    usef_purchasing = serializers.IntegerField(label="Kullanım yeri satınalma", required=False, default=0)
    usef_mm = serializers.IntegerField(label="Kullanım yeri satınalma", required=False, default=0)
    unitset_code = serializers.CharField(label="Birim seti kodu", max_length=4, required=False)
    sel_vat = serializers.FloatField(label="Satınalma KDV", required=False)
    return_vat = serializers.FloatField(label="Satış KDV", required=False)
    selpr_vat = serializers.FloatField(label="Per. satış KDV", required=False)
    returnpr_vat = serializers.FloatField(label="Per. satış iade KDV", required=False)
    markcode = serializers.CharField(label="Marka kodu", max_length=25, required=False)
    code = serializers.CharField(label="Malzeme kodu", max_length=25, required=False)
    image = serializers.CharField(label="Image base64",required=False)
    img_format = serializers.IntegerField(label= "1 = Bitmap (bmp), 2 = JPEG (jpg), 3 = PNG (png)",required=False)
    # 1 = Bitmap (bmp)
    # 2 = JPEG (jpg)
    # 3 = PNG (png)


class UnitSerializer(serializers.Serializer):
    barcode = serializers.CharField(label="Barkod", required=False)
    unit_code = serializers.CharField(label="Birim", required=False)
    usef_mrtlclass = serializers.IntegerField(label="Kullanım Yeri-Malzeme sınıfı", required=False)
    usef_purchaseclass = serializers.IntegerField(label="Kullanım Yeri-Satınalma", required=False)
    usef_salesclass = serializers.IntegerField(label="Kullanım Yeri-Satış ve Dağıtım", required=False)
    conv_fact1 = serializers.FloatField(label="Çevrim katsayısı 1", required=False)
    conv_fact2 = serializers.FloatField(label="Çevrim katsayısı 2", required=False)


class ItemCreateSerializer(serializers.Serializer):
    card_type = serializers.ChoiceField(label="Malzeme türü", 
        choices=item_choices, default=1, required=False)
    code = serializers.CharField(label="Malzeme kodu", max_length=25, required=True)
    name = serializers.CharField(label="Açıklama", max_length=51, required=False)
    producer_code = serializers.CharField(label="Üretici Kodu", max_length=25, required=False)
    auxil_code = serializers.CharField(label="Özel Kod", max_length=11,required=False)
    vat = serializers.FloatField(label="KDV", required=False)
    usef_sales = serializers.IntegerField(label="Kullanım yeri satış-dağıtım", required=False, default=1)
    usef_purchasing = serializers.IntegerField(label="Kullanım yeri satınalma", required=False, default=0)
    usef_mm = serializers.IntegerField(label="Kullanım yeri satınalma", required=False, default=0)
    unitset_code = serializers.CharField(label="Birim seti kodu", max_length=4, required=False)
    units = serializers.ListSerializer(child=UnitSerializer())
    sel_vat = serializers.FloatField(label="Satınalma KDV", required=False)
    return_vat = serializers.FloatField(label="Satış KDV", required=False)
    selpr_vat = serializers.FloatField(label="Per. satış KDV", required=False)
    returnpr_vat = serializers.FloatField(label="Per. satış iade KDV", required=False)
    markcode = serializers.CharField(label="Marka kodu", max_length=25, required=False)
    image = serializers.CharField(label="Image base64",required=False)
    img_format = serializers.IntegerField(label= "1 = Bitmap (bmp), 2 = JPEG (jpg), 3 = PNG (png)",required=False)


class ItemCodeSerializer(serializers.Serializer):
    pattern = serializers.CharField()
    prefix = serializers.CharField()
    seperator = serializers.CharField(required=False, default="")
