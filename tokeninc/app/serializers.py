from rest_framework import serializers

class Lines(serializers.Serializer):
    itemCode = serializers.CharField(max_length=50)
    price = serializers.FloatField()
    quantity = serializers.FloatField()
    add_tax_amount = serializers.FloatField(default=0)

class Line(serializers.Serializer):
    line = serializers.ListSerializer(child=Lines())


class InvSerializer(serializers.Serializer):
    date = serializers.CharField(max_length=10, min_length=10, label="Tarih")
    customer = serializers.IntegerField(label="Müşteri numarası")
    OrderKey = serializers.CharField(label="Fatura numarası")
    exp = serializers.CharField(label="Açıklama")
    exp2 = serializers.CharField(label='Açıklama 2', required=False)
    specode = serializers.CharField(label='Özel kod', required=False, max_length=10)
    invoice_lines = Line()



class ArpCardSerializer(serializers.Serializer):
    client_title = serializers.CharField(
        max_length=180,
        required=True,
        label='Tanım'
    )
    client_adress = serializers.CharField(
        max_length=255,
        required=True,
        label="Adres satırı"
    )
    client_city = serializers.CharField(
        max_length=51,
        required=True,
        label="Şehir"
    )
    country = serializers.CharField(
        max_length=21,
        required=False,
        label="Ülke",
        default="TURKIYE"
    )
    client_email = serializers.CharField(
        max_length=251,
        label="E-posta",
        required=True
    )
    client_merchantId = serializers.IntegerField(
        label="Merchant id",
        required=True
    )
    client_website = serializers.CharField(
        max_length=101,
        label='Web adresi',
        required=False
    )
    client_type = serializers.CharField(
        max_length=10,
        label='Yetki kodu',
        required=True
    )
    client_name = serializers.CharField(
        max_length=15,
        label='Ad',
        required=False
    )
    client_surname = serializers.CharField(
        max_length=15,
        label='Soyad',
        required=False
    )
    client_taxnumber = serializers.CharField(
        max_length=11,
        label='VKN / T.C. Kimlik',
        required=True
    )
    client_taxoffice = serializers.CharField(
        max_length=30,
        label='Vergi dairesi',
        required=True,
        allow_blank=True
    )
