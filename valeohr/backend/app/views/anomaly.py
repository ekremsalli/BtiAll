from rest_framework import generics, serializers

from common.views import Bti, Pagination
from app.serializers.employee import ShortEmployeeSerializer
from app.serializers.anomaly import AnomalySerializer
from app.views.sync import Firms

from app.models import Employees, Anomalies


class AnomalyView(Bti, generics.ListAPIView):
    # swagger_schema = None
    serializer_class = AnomalySerializer
    ordering_fields = [
        "id", "source_db", 'tr_date'
    ]
    filterset_fields = {
        'tr_date': ['gte', 'lte', 'exact'],
    }
    pagination_class = Pagination

    def get_queryset(self):
        qs = Anomalies.active_objects.select_related(
            'source_db', 'employee')

        worker_type = self.request.query_params.get('worker_type')
        if worker_type:
            empx = Employees.objects.filter(
                worker_type=worker_type).values_list('id', flat=True)
            if empx:
                qs = qs.filter(employee_id__in=empx)

        employee = self.request.query_params.get('employee')
        if employee:
            qs = qs.filter(employee_id=employee)

        firm = self.request.query_params.getlist('firm[]')
        if firm:
            qs = qs.filter(employee__firm__in=firm)

        ano_text = self.request.query_params.get('ano_text')
        if ano_text:
            qs = qs.filter(ano_text=ano_text)
        return qs

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        serializer = ShortEmployeeSerializer(
            Employees.active_objects.select_related(
                'source_db').order_by('name', 'surname').filter(firm__in=Firms.firms_selected),
            many=True
        )
        response.data['employees'] = serializer.data
        ano_types = set(Anomalies.objects.values_list('ano_text', flat=True))
        response.data['ano_types'] = list(ano_types)

        return response
