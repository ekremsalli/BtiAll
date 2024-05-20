from rest_framework import serializers

from app.models import Employees


class EmployeeSerializer(serializers.ModelSerializer):
    source_db = serializers.StringRelatedField()
    worker_type = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Employees
        fields = "__all__"

    def get_worker_type(self, obj):
        return obj.get_worker_type_display()

    def get_title(self, obj):
        name = obj.name.capitalize()
        surname = obj.surname.capitalize()
        return f'({obj.nr}) {name} {surname} [{obj.source_db.title}]'


class ShortEmployeeSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    employee_id = serializers.SerializerMethodField()

    class Meta:
        model = Employees
        fields = ["id", "title", "firm", "employee_id"]

    def get_title(self, obj):
        name = obj.name.capitalize()
        surname = obj.surname.capitalize()
        return f'({obj.nr}) {name} {surname} [{obj.source_db.title}]'

    def get_employee_id(self, obj):
        return obj.nr
