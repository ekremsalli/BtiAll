import json
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework import status

from common.views import Bti, Pagination
from app.serializers.employee import EmployeeSerializer
from app.models import Employees
from app.models.base import DB


class EmployeeView(Bti, generics.ListAPIView):
    swagger_schema = None
    pagination_class = Pagination
    serializer_class = EmployeeSerializer
    ordering_fields = [
        'nr', 'id', 'source_db', 'name',
        'surname', 'firm', 'department', 'title',
        'worker_type', 'account', 'cost_center',
        'psoft_id', 'work_id', 'created_on',
        'modified_on', 'ceated_by', 'modified_by'
    ]
    filterset_fields = {
        'name': ['contains'],
        'surname': ['contains']
    }

    def get_queryset(self):
        qs = Employees.objects.filter(
            status=0).order_by("name", "surname")

        firm = self.request.query_params.getlist('firm[]')
        if firm:
            qs = qs.filter(firm__in=firm)

        nr = self.request.query_params.get('nr')
        if nr:
            qs = qs.filter(nr=nr)

        source_db = self.request.query_params.get('source_db')
        if source_db:
            db = DB.get_db(source_db)
            qs = qs.filter(source_db=db)

        return qs


class EmployeeEdit(generics.UpdateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
