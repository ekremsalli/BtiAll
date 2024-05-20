from rest_framework import serializers

from app.models import Transactions


class TransactionSerializer(serializers.ModelSerializer):
    source_db = serializers.SerializerMethodField()
    employee = serializers.SerializerMethodField()
    tr_date = serializers.SerializerMethodField()
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    employee_id = serializers.SerializerMethodField()

    class Meta:
        model = Transactions
        fields = "__all__"

    def get_source_db(self, obj):
        if obj.employee is None:
            return ""
        return obj.source_db.title

    def get_employee_id(self, obj):
        if obj.employee is None:
            return ""
        return obj.employee.id

    def get_employee(self, obj):
        if obj.employee is None:
            return ""
        else:
            name = obj.employee.name.capitalize()
            surname = obj.employee.surname.capitalize()
            return f'({obj.employee.nr}) {name} {surname} [{obj.source_db.title}]'

    def get_start(self, obj):
        if obj.start:
            return obj.start.strftime('%H:%M')
        return ''

    def get_end(self, obj):
        if obj.end:
            return obj.end.strftime('%H:%M')
        return ''

    def get_tr_date(self, obj):
        if obj.tr_date:
            return obj.tr_date.strftime('%Y-%m-%d')
        return ''


class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ("account", "created_by", "created_on", "day_model", "description", "employee", "employee_id",)
