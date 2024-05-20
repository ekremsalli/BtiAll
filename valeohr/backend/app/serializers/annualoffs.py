from rest_framework import serializers


class AnnualOffSerializer(serializers.Serializer):
    source_db = serializers.CharField()
    employee = serializers.CharField()
    tr_date = serializers.SerializerMethodField()
    excuse = serializers.CharField()
    excuse_day = serializers.CharField()
    color = serializers.CharField()
    day = serializers.IntegerField()
    week = serializers.IntegerField()
    tr_day = serializers.IntegerField()

    def get_tr_date(self, obj):
        if obj.tr_date:
            return obj.tr_date.strftime('%Y-%m-%d')
        return ''



