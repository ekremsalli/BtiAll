from rest_framework import serializers


class LogoApiSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField(format="%Y-%m-%d")
    organization_id = serializers.CharField(required=False)

    class Meta:
        fields = ('start_date',)


class ArmonSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField(default="2022-07-10T21:00:00.000Z")
    grant_type_id = serializers.CharField(required=False)

    class Meta:
        fields = ('start_date',)
