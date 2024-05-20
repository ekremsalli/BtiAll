from rest_framework import serializers

from geco.models import Ttagzei


class OvertimeSerializer(serializers.Serializer):
    idnr = serializers.IntegerField()
    tr_date = serializers.SerializerMethodField()
    interval = serializers.SerializerMethodField()
    employee = serializers.CharField()
    firm = serializers.CharField()
    tze_vonzeit = serializers.DateTimeField(format="%H:%M")  # Giriş zamanıl
    tze_biszeit = serializers.DateTimeField(format="%H:%M")  # Çıkış zamanı

    class Meta:
        model = Ttagzei
        fields = ["idnr", "tr_date", "interval", 'tze_vonzeit', "tze_biszeit"]

    def get_interval(self, obj):
        if obj.interval:
            return obj.interval
        return 0

    def get_tr_date(self, obj):
        if obj.tr_date:
            return obj.tr_date.strftime('%Y-%m-%d')
        return ''
