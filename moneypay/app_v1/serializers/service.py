from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from app_v1.models import Operation


class RequestLineSerializer(serializers.Serializer):
    day = serializers.DateField(label='Tarih', required=True)
    uid = serializers.CharField(
        label='Kullanıcı kimliği',
        min_length=10,
        max_length=11,
        required=False,
        allow_blank=True
    )
    pid = serializers.CharField(label='İşlem kimliği', required=True)
    name = serializers.CharField(label='Ad', required=False, allow_blank=True)
    surname = serializers.CharField(
        label='Soyad', required=False, allow_blank=True)
    gsm = serializers.CharField(label='Telefon numarası', required=False)
    mernis = serializers.CharField(
        label='Mernis', required=False, allow_blank=True)
    taxnr = serializers.CharField(
        label='Vergi numarası', required=False, allow_blank=True)
    city = serializers.CharField(label='İl', required=False, allow_blank=True)
    district = serializers.CharField(
        label='İlçe', required=False, allow_blank=True)
    zipcode = serializers.CharField(
        label='Posta kodu', required=False, allow_blank=True)
    op_code = serializers.CharField(label='İşlem kodu', required=True)
    desc = serializers.CharField(
        label='İşlem açıklaması', required=True, allow_blank=True)
    amount = serializers.FloatField(label='Tutar', required=True)
    total_amount = serializers.FloatField(label='Toplam tutar', required=True)
    commission_amount = serializers.FloatField(
        label='Komisyon tutarı', required=True)
    customer_type = serializers.IntegerField(
        label='Müşteri tipi (1=Peşin / 2=Vadeli)',
        default=1
    )
    order_id = serializers.CharField(label="Sipariş numarası", required=False)
    discount = serializers.FloatField(label="İndirim tutarı", required=False)
    tax_office = serializers.CharField(label="Vergi dairesi", required=False)
    title = serializers.CharField(label="Ünvan", required=False)
    country = serializers.CharField(label="Ülke", required=False)
    address = serializers.CharField(label="Açık adres", required=False)
    is_company = serializers.BooleanField(
        label="Bireysel/Kurumsal", required=False)
    po_number = serializers.CharField(label="", required=False)
    op_desc = serializers.CharField(
        label="İşlem kodu açıklaması", required=False)
    invoice_gross_amount = serializers.FloatField(required=False)
    invoice_net_amount = serializers.FloatField(required=False)
    invoice_discount_amount = serializers.FloatField(required=False)
    itext = serializers.CharField(label="Detay Bilgi", required=False)
    payment_code = serializers.CharField(
        label="Ödeme planı kodu", required=False)

    address_id = serializers.IntegerField(required=False)
    service_type = serializers.IntegerField(
        label="Hizmet Tipi, Pro = 1, Bono = 2", required=True)  # servic_type zorunlu alan olmalı Yoksa MASTER_CODE eklenmiyor bundan dolayı Fatura satırları oluşmuyor

    # other_desc = serializers.CharField(label="Diğer açıklama", required=False)

    email = serializers.CharField(label="E-posta", required=False)
    cost_code = serializers.CharField(
        label="Masraf Merkezi Kodu", required=False)

    def validate(self, data):
        x1 = data.get('invoice_gross_amount')
        x2 = data.get('invoice_net_amount')
        if x1 or x2:
            total = 0
            if x1:
                total += x1
            if x2:
                total += x2

            if total > 0:
                if data.get('is_company', None) is None:
                    raise ValidationError('is_company required field!')
        return data


class RequestSerializer(serializers.Serializer):
    lines = serializers.ListField(child=RequestLineSerializer())

    def validate_lines(self, lines):
        codes = list(set(
            [line.get('op_code') for line in lines]
        ))
        if Operation.objects.filter(code__in=codes).count() != len(codes):
            current = Operation.objects.filter(
                code__in=codes).values_list('code', flat=True)
            missing = [c for c in codes if c not in current]
            raise ValidationError(
                f'Bilinmeyen operasyon kodu / kodları ({missing})!')
        return lines
