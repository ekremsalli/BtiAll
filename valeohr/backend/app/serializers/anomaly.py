from rest_framework import serializers

from app.models import Anomalies

class AnomalySerializer(serializers.ModelSerializer):
    source_db = serializers.SerializerMethodField()
    employee = serializers.SerializerMethodField()    
    tr_date = serializers.SerializerMethodField()

    class Meta:
        model = Anomalies
        fields = "__all__"

    def get_source_db(self, obj):
        return obj.source_db.title

    def get_employee(self, obj):
        name = obj.employee.name.capitalize()
        surname = obj.employee.surname.capitalize()
        return f'({obj.employee.nr}) {name} {surname} [{obj.source_db.title}]'

    def get_tr_date(self, obj):
        if obj.tr_date:
            return obj.tr_date.strftime('%Y-%m-%d')
        return ''