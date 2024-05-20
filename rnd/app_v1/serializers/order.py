from rest_framework import serializers
from erp.models.friendly import Clcard

from .invoice import EArchiveInfoSerializer


class ArpCardSerializer(serializers.ModelSerializer):
    INTERNAL_REFERENCE = serializers.IntegerField(source='logicalref')
    CODE = serializers.CharField(source='code')
    TITLE = serializers.CharField(source='definition_field')
    ADDRESS1 = serializers.CharField(source='addr1')
    ADDRESS2 = serializers.CharField(source='addr2')
    E_MAIL = serializers.CharField(source='emailaddr')
    TCKNO = serializers.CharField(source='tckno')
    NAME = serializers.CharField(source='name')
    SURNAME = serializers.CharField(source='surname')
    TAX_ID = serializers.CharField(source='taxnr')
    TAX_OFFICE = serializers.CharField(source="taxoffice")
    ACTIVE = serializers.CharField(source='active')
    CITY = serializers.CharField(source='city')
    TOWN = serializers.CharField(source='town')
    DISTRICT = serializers.CharField(source='district')

    class Meta:
        model = Clcard
        fields = [
            'INTERNAL_REFERENCE',
            'CODE',
            'TITLE',
            'ADDRESS1',
            'ADDRESS2',
            'E_MAIL',
            'TCKNO',
            'NAME',
            'SURNAME',
            'TAX_ID',
            'TAX_OFFICE',
            'ACTIVE',
            'CITY',
            'TOWN',
            'DISTRICT',
        ]


class ArpUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(label='Cari adı', required=False)
    address1 = serializers.CharField(label='Adres satırı 1', required=False)
    address2 = serializers.CharField(label='Adres satırı 2', required=False, default='')
    town = serializers.CharField(label='İlçe', required=False)
    city = serializers.CharField(label='İl', required=False)
    district = serializers.CharField(label='Semt', required=False)
    telephone1 = serializers.CharField(label='Telefon', required=False)
    e_mail = serializers.CharField(label='E-posta adresi', required=False)
    web_url = serializers.CharField(label='Web adresi', required=False, default='')
    perscompany = serializers.IntegerField(
        min_value=0, max_value=1, label='Gerçek kişi için 1', required=False)
    tckno = serializers.CharField(label='Mernis', required=False)
    name = serializers.CharField(label='Müşteri adı', required=False)
    surname = serializers.CharField(label='Müşteri soyadı', required=False)
    tax_id = serializers.CharField(label='Vergi kimlik numarası', required=False)
    tax_office = serializers.CharField(label='Vergi dairesi', required=False)
    postal_code = serializers.CharField(label='Posta kodu', required=False, max_length=11)

    account_type = serializers.IntegerField(
        label='Cari hesap kart türü', default=3)
    country_code = serializers.CharField(label='Ülke kodu', default='TR')
    country = serializers.CharField(label='Ülke', default='Türkiye')
    corresp_lang = serializers.IntegerField(label='Yazışma dili', default=1)
    cl_ord_freq = serializers.IntegerField(default=1)
    ord_day = serializers.IntegerField(default=127)
    purchbrws = serializers.IntegerField(default=1)
    salesbrws = serializers.IntegerField(default=1)
    impbrws = serializers.IntegerField(default=1)
    expbrws = serializers.IntegerField(default=1)
    finbrws = serializers.IntegerField(default=1)


class ArpSerializer(serializers.Serializer):
    code = serializers.CharField(label='Cari hesap kodu', required=True)
    title = serializers.CharField(label='Cari adı', required=False)
    title2 = serializers.CharField(label='Cari adı 2', required=False)
    address1 = serializers.CharField(label='Adres satırı 1', required=False)
    address2 = serializers.CharField(label='Adres satırı 2', required=False, default='')
    town = serializers.CharField(label='İlçe', required=False)
    city = serializers.CharField(label='İl', required=False)
    district = serializers.CharField(label='Semt', required=False)
    telephone1 = serializers.CharField(label='Telefon', required=False)
    e_mail = serializers.CharField(label='E-posta adresi', required=False)
    web_url = serializers.CharField(label='Web adresi', required=False, default='')
    perscompany = serializers.IntegerField(
        min_value=0, max_value=1, label='Gerçek kişi için 1', required=False)
    tckno = serializers.CharField(label='Mernis', required=False)
    name = serializers.CharField(label='Müşteri adı', required=False)
    surname = serializers.CharField(label='Müşteri soyadı', required=False)
    tax_id = serializers.CharField(label='Vergi kimlik numarası', required=False)
    tax_office = serializers.CharField(label='Vergi dairesi', required=False)
    postal_code = serializers.CharField(label='Posta kodu', required=False, max_length=11)

    account_type = serializers.IntegerField(
        label='Cari hesap kart türü', default=3)
    country_code = serializers.CharField(label='Ülke kodu', default='TR')
    country = serializers.CharField(label='Ülke', default='Türkiye')
    corresp_lang = serializers.IntegerField(label='Yazışma dili', default=1)
    cl_ord_freq = serializers.IntegerField(default=1)
    ord_day = serializers.IntegerField(default=127)
    purchbrws = serializers.IntegerField(default=1)
    salesbrws = serializers.IntegerField(default=1)
    impbrws = serializers.IntegerField(default=1)
    expbrws = serializers.IntegerField(default=1)
    finbrws = serializers.IntegerField(default=1)


class TransactionSerializer(serializers.Serializer):
    type = serializers.IntegerField(label='Satır tipi')
    master_code = serializers.CharField(label='Ürün/Hizmet kodu', required=False)
    barcode = serializers.CharField(label='Barkod', required=False)
    quantity = serializers.FloatField(label='Miktar', required=False)
    price = serializers.FloatField(label='Birim fiyat', required=False)
    vat_rate = serializers.FloatField(label='KDV oranı', required=False)
    unit_code = serializers.CharField(label='Malzeme kodu', required=False)
    unit_conv1 = serializers.FloatField(label='Birim çevrimi 1', required=False)
    unit_conv2 = serializers.FloatField(label='Birim çevrimi 2', required=False)
    project_code = serializers.CharField(label='Proje kodu', required=False)
    vat_included = serializers.BooleanField(label='KDV Dahil', default=True)
    detail_level = serializers.IntegerField(required=False)
    total = serializers.FloatField(required=False)
    discount_rate = serializers.FloatField(required=False)
    calc_type = serializers.IntegerField(required=False)
    vatexcept_reason = serializers.CharField(label='KDV İstisna nedeni', required=False, allow_blank=True)
    vatexcept_code = serializers.CharField(label='KDV İstisna kodu', required=False, allow_blank=True)
    order_closed = serializers.IntegerField(label="Kapanan sipariler", min_value=0,max_value=1, required=False)


class OrderSerializer(serializers.Serializer):
    number = serializers.CharField(label='Sipariş numarası', required=True)
    date = serializers.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ"])
    auth_code = serializers.CharField(
        max_length=11, label='Yetki kodu', required=False)

    doc_number = serializers.CharField(label='Belge numarası', required=False)
    arp = ArpSerializer()
    source_wh = serializers.IntegerField(label='Kaynak ambar', required=False)
    shipping_agent = serializers.CharField(label='Kargo firması', required=False)
    notes1 = serializers.CharField(label='Not 1', required=False)
    notes2 = serializers.CharField(label='Not 2', required=False)
    notes3 = serializers.CharField(label='Not 3', required=False)
    notes4 = serializers.CharField(label='Not 4', required=False)
    project_code = serializers.CharField(label='Proje kodu', required=False)

    vatexcept_reason = serializers.CharField(label='KDV İstisna nedeni', required=False, allow_blank=True)
    vatexcept_code = serializers.CharField(label='KDV İstisna kodu', required=False, allow_blank=True)
    sales_order = serializers.BooleanField(label='Satış siparişi', required=False, default=True)
    doctrackingnr = serializers.CharField(label="Doküman izleme numarası", max_length=21, required=False)

    transactions = serializers.ListSerializer(child=TransactionSerializer())
    EArchiveInfo = EArchiveInfoSerializer()
