from rest_framework import generics, serializers
from rest_framework.exceptions import APIException
from rest_framework.fields import is_simple_callable
from rest_framework.response import Response
from rest_framework.views import APIView
from app.views.sync import Firms

from common.views import Bti, Pagination

from app.serializers.annualoffs import AnnualOffSerializer
from app.serializers.db import DBSerializer
from app.serializers.employee import EmployeeSerializer

from geco.models import Ttagles
from app.models.base import DB
from app.models import Employees




class DBView(Bti, APIView):
    def get(self, request, format=None):
        from django.conf import settings
        from app.models import GecoGroups
        from app.serializers.geco import GecoGroupSerializer

        dbs = DB.objects.filter(is_active=True).all()
        default_db = DB.objects.filter(is_active=True).first()
        employees = Employees.objects.prefetch_related('source_db').filter(source_db=default_db)

        MAPP = settings.GECO_MAPPING['GROUP_MAP']
        gtypes = [
            MAPP['COMPANIES'],
        ]

        all_items = GecoGroups.active_objects.prefetch_related('source_db').select_related('source_db').filter(
            source_db=default_db,
            gtype__in=gtypes,
            code__in=Firms.firms_selected,
        )
        companies = sorted([n for n in all_items if n.gtype == MAPP['COMPANIES']], key=lambda o: o.code)

        return Response({
            'default': DBSerializer(default_db).data,
            'dbs': DBSerializer(dbs, many=True).data,
            'employees': EmployeeSerializer(employees, many=True).data,
            'companies': GecoGroupSerializer(companies, many=True).data
        })


class AnnualOffView(Bti, APIView):
    employees = []

    def report(self, qs):

        excuses = {x.excuse: [] for x in qs}
        for excuse in excuses:
            for item in qs:
                if item.excuse == excuse:
                    excuses[excuse].append(1 if item.excuse_day == "0" else .5)
        data = []
        for k, w in excuses.items():
            data.append({'type': k, 'sum': sum(w)})
        return data

    def prepare_qs(self, db, year, month):
        from app.models.other import get_week_of_month

        qs = Ttagles.objects.using(db.code).filter(
            tle_abwtag__isnull=False).order_by("idnr")
        employee_id = self.request.query_params.get('employee')
        employee = Employees.objects.filter(source_db=db, id=employee_id).first()

        if employee:
            qs = qs.filter(tle_persnr=employee.nr)

        qs = qs.filter(tle_datum__year=year)
        if month is not None:
            qs = qs.filter(tle_datum__month=month)

        firm = self.request.query_params.get('firm')
        if firm:
            firm_employees = list(Employees.objects.filter(
                source_db=db,
                firm=firm
            ).values_list('nr', flat=True))
            qs = qs.filter(tle_persnr__in=firm_employees)

        for p in qs:
            p.employee = self.employees[p.tle_persnr]
            p.source_db = db
            p.tr_date = p.tle_datum
            p.day = p.tr_date.weekday()
            p.tr_day = p.tr_date.day
            p.week = get_week_of_month(p.tr_date)
            p.excuse = p.tle_abwart
            p.excuse_day = p.tle_abwtag
            if hasattr(p, 'abw_colorkey'):
                p.color = p.abw_colorkey
            else:
                p.color = ''
        return list(qs)

    def get(self, request, *args, **kwargs):

        from app.models import Changes
        from datetime import date
        from dateutil.relativedelta import relativedelta
        from django.db.models import Q
        from calendar import day_name, monthrange

        db_param = self.request.query_params.get('db')

        if db_param is None:
            db = DB.objects.filter(is_active=True).first()

            if db is None:
                raise APIException('Undefined database!')
            db_param = db.code
        else:
            db = DB.get_db(db_param)

        self.employees = {e.nr: e for e in Employees.objects.filter(source_db=db)}

        year = int(self.request.query_params.get('year'))
        month = self.request.query_params.get('month')

        if month is not None:

            month = int(month)

            day = date(year, month, 1)

            cur_data = self.prepare_qs(db, day.year, day.month)
            prev = day - relativedelta(months=1)
            pre_data = self.prepare_qs(db, prev.year, prev.month)
            next = day + relativedelta(months=1)
            nxt_data = self.prepare_qs(db, next.year, next.month)

            qs = Changes.objects.filter(
                verify_status__in=[0, 1],
                is_annual_off=True,
                source_db=db
            )
            worker_type = self.request.query_params.get('white_collar')
            employee_id = self.request.query_params.get('employee')
            employee = Employees.objects.filter(source_db=db, pk=employee_id, worker_type=worker_type).first()

            if employee:
                qs = qs.filter(employee=employee)

            start_qs = date(prev.year, prev.month, 1)
            end_qs = date(next.year, next.month, monthrange(next.year, next.month)[1])
            qs = qs.filter(
                start_annual__gte=start_qs,
                end_annual__lte=end_qs
            )
            xpre_data = AnnualOffSerializer(pre_data, many=True).data
            xcur_data = AnnualOffSerializer(cur_data, many=True).data
            xnxt_data = AnnualOffSerializer(nxt_data, many=True).data

            for exp in qs.all():
                spans = exp.annual_span()
                for span in spans:
                    if span['year'] == prev.year and span['month'] == prev.month:
                        xpre_data.append(span)
                    if span['year'] == day.year and span['month'] == day.month:
                        xcur_data.append(span)
                    if span['year'] == next.year and span['month'] == next.month:
                        xnxt_data.append(span)

            return Response({
                'data_type': "month",
                'pre_data': xpre_data,
                'pre_report': self.report(pre_data),
                'pre_weekday': prev.weekday(),
                'pre_name': {'year': prev.year, 'month': prev.month},
                'cur_data': xcur_data,
                'cur_report': self.report(cur_data),
                'cur_weekday': day.weekday(),
                'cur_name': {'year': day.year, 'month': day.month},
                'nxt_data': xnxt_data,
                'nxt_report': self.report(nxt_data),
                'nxt_weekday': next.weekday(),
                'nxt_name': {'year': next.year, 'month': next.month},

            })

        else:
            year = int(self.request.query_params.get('year'))

            qs = Changes.objects.filter(
                verify_status__in=[0, 1],
                is_annual_off=True,
                source_db=db
            )
            worker_type = self.request.query_params.get('white_collar')
            employee_id = self.request.query_params.get('employee')
            employee = Employees.objects.filter(source_db=db, pk=employee_id, worker_type=worker_type).first()

            if employee:
                qs = qs.filter(employee=employee)

            qs = qs.filter(
                start_annual__year=str(year),
                end_annual__year=str(year)
            )
            cur_data = self.prepare_qs(db, year, None)
            serializer = AnnualOffSerializer(cur_data, many=True).data

            for exp in qs.all():
                spans = exp.annual_span()
                for span in spans:
                    if span['year'] == year:
                        serializer.append(span)

            return Response({
                'data_type': "year",
                "cur_data": serializer,
                "report": self.report(cur_data)
            })
