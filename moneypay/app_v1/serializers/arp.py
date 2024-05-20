from rest_framework import serializers


class ArpSerializer(serializers.Serializer):
    uid = serializers.CharField(label='Kullanıcı kimliği', required=True)
    name = serializers.CharField(label='Ad', required=False)
    surname = serializers.CharField(label='Soyad', required=False)
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
    tax_office = serializers.CharField(label="Vergi dairesi", required=False)
    country = serializers.CharField(label="Ülke", required=False)
    address = serializers.CharField(label="Açık adres", required=False)
    title = serializers.CharField(label='Firma adı', required=False)
    payment_code = serializers.CharField(
        label="Ödeme planı kodu", required=False)
    cost_code = serializers.CharField(
        label="Masraf Merkezi Kodu", required=False)
