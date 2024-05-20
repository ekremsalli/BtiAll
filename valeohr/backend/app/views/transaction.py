from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from app.views.sync import Firms

from common.views import Bti, Pagination
from app.serializers.employee import ShortEmployeeSerializer
from app.serializers.transaction import TransactionSerializer, CreateTransactionSerializer
from app.serializers.db import DBSerializer

from app.models import Employees, Transactions
from app.models.base import DB


class TransactionView(Bti, generics.ListAPIView):
    swagger_schema = None
    serializer_class = TransactionSerializer
    ordering_fields = [
        "id", "source_db", 'tr_date'
    ]
    filterset_fields = {
        'tr_date': ['gte', 'lte', 'exact'],
        'start': ['isnull'],
        'end': ['isnull'],
        'excuse_type': ['exact']
    }
    pagination_class = Pagination

    def get_queryset(self):
        qs = Transactions.active_objects.select_related(
            'source_db', 'employee')
        employee = self.request.query_params.get('employee')
        if employee:
            qs = qs.filter(employee_id=employee)

        firm = self.request.query_params.getlist('firm[]')
        if firm:
            qs = qs.filter(employee__firm__in=firm)

        start = self.request.query_params.get('start__isnull')
        if start:
            qs = qs.filter(end__isnull=False)

        end = self.request.query_params.get('end__isnull')
        if end:
            qs = qs.filter(start__isnull=False)

        excuse_type = self.request.query_params.get('excuse_type')
        if excuse_type:
            qs = qs.filter(excuse_type=excuse_type)
        return qs

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        serializer = ShortEmployeeSerializer(
            Employees.active_objects.select_related(
                'source_db').order_by('name', 'surname').filter(firm__in=Firms.firms_selected),
            many=True
        )
        response.data['employees'] = serializer.data
        return response
