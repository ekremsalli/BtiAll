from rest_framework import generics, serializers
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from common.views import Bti, Pagination
from app.serializers.overtime import OvertimeSerializer
from geco.models import Ttagzei
from app.models.base import DB
from app.models import Employees


class OvertimeView(Bti, generics.ListAPIView):
    swagger_schema = None
    serializer_class = OvertimeSerializer
    ordering_fields = [
        'idnr',
        'tze_datum',
        'tze_istzeit'
    ]
    pagination_class = Pagination

    def list(self, request, *args, **kwargs):

        db_param = request.query_params.get('db')
        if db_param:
            db = DB.get_db(db_param)
        else:
            db = DB.objects.filter(is_active=True).first()

        if db is None:
            raise APIException('Undefined database!')

        employees = {i.nr: i for i in Employees.objects.prefetch_related(
            'source_db').filter(source_db=db)}

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            for p in page:
                p.employee = employees[p.tze_persnr]
                p.firm = employees[p.tze_persnr].firm
                p.tr_date = p.tze_datum
                p.interval = p.tze_istzeit

            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        for p in queryset:
            p.tr_date = p.tze_datum
            p.interval = p.tze_istzeit
            p.firm = employees[p.tze_persnr].firm
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        db_param = self.request.query_params.get('db')

        if db_param is None:
            db = DB.objects.filter(is_active=True).first()
            if db is None:
                raise APIException('Undefined database!')
            db_param = db.code
        else:
            db = DB.get_db(db_param)

        fm_filter = self.request.query_params.getlist('fm_filter[]')
        qs = Ttagzei.objects.using(db_param).exclude(tze_istzeit=0)
        tze_datum__gte = self.request.query_params.get('tze_datum__gte')

        if tze_datum__gte:
            qs = qs.filter(tze_datum__gte=tze_datum__gte)
        tze_datum__lte = self.request.query_params.get('tze_datum__lte')
        if tze_datum__lte:
            qs = qs.filter(tze_datum__lte=tze_datum__lte)

        if fm_filter:
            qs = qs.filter(tze_zeitart__in=fm_filter)
        else:
            qs = qs.filter(tze_zeitart__in=['FM1', 'FM2', 'FM3', 'FM4'])

        qs = qs.order_by('tze_datum')

        firm = self.request.query_params.getlist('firm[]')

        employee = self.request.query_params.get('employee')

        if firm:
            firm_employees = list(Employees.objects.filter(
                source_db=db,
                firm__in=firm
            ).values_list('nr', flat=True))
            qs = qs.filter(tze_persnr__in=firm_employees)

        if employee:
            qs = qs.filter(tze_persnr=employee)

        worker_type = self.request.query_params.get('worker_type')
        if worker_type:
            # 1 = beyaz yaka B
            # 2 = mavi yaka M
            qs = qs.extra(
                where=[
                    'tze_persnr in (SELECT per_persnr FROM Tpertab WHERE per_grp3=%s)'
                ],
                params=['B' if worker_type == 1 else 'M']
            )
        return qs
