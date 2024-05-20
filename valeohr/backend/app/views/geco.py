from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from common.views import Bti, Pagination
from app.serializers.geco import GecoGroupSerializer, GecoDefSerializer
from app.models import GecoGroups, GecoDefs


class GecoGroupView(Bti, generics.ListAPIView):
    swagger_schema = None
    pagination_class = Pagination
    serializer_class = GecoGroupSerializer
    queryset = GecoGroups.active_objects.prefetch_related('source_db').all()
    ordering_fields = [
        "id", "source_db", "gtype", "code", "description",
        "created_on", "created_by", "modified_on",
        "modified_by", "geco_id"
    ]

    filterset_fields = {
        'gtype': ['exact'],
        'code': ['contains'],
        'description': ['contains'],
    }

    def get_queryset(self):
        from app.models.base import DB
        qs = GecoGroups.active_objects.prefetch_related('source_db').all()
        source_db = self.request.query_params.get('source_db')
        if source_db:
            db = DB.get_db(source_db)
            qs = qs.filter(source_db=db)

        gtype = self.request.query_params.getlist('gtype[]')
        if gtype:
            qs = qs.filter(gtype__in=gtype)

        return qs

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        response.data['group_types'] = [
            {'id': kx, 'value': vx} for kx, vx in list(GecoGroups.GROUP_TYPES)
        ]
        return response


class GecoDefView(Bti, generics.ListAPIView):
    swagger_schema = None
    pagination_class = Pagination
    serializer_class = GecoDefSerializer
    queryset = GecoDefs.active_objects.prefetch_related('source_db').all()
    ordering_fields = [
        "id", "source_db", "def_type",
        "code", "name", "short_code",
        "link_code", "created_on", "created_by",
        "modified_on", "modified_by", "geco_id"
    ]
    filterset_fields = {
        'code': ['contains'],
        'name': ['contains'],
    }

    def get_queryset(self):
        from app.models.base import DB
        qs = GecoDefs.active_objects.prefetch_related('source_db').all()

        source_db = self.request.query_params.get('source_db')
        if source_db:
            db = DB.get_db(source_db)
            qs = qs.filter(source_db=db)

        def_type = self.request.query_params.get('def_type')
        if def_type:
            qs = qs.filter(def_type=def_type)
        return qs

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        response.data['def_types'] = [{'id': kx, 'value': vx}
                                      for kx, vx in list(GecoDefs.DEF_TYPES)]
        return response


class APIDefs(Bti, APIView):
    def get(self, request, format=None):
        from django.conf import settings
        from app.models.base import DB

        source_db = self.request.query_params.get('source_db')
        if source_db:
            db = DB.get_db(source_db)
        else:
            db = DB.objects.filter(is_active=True).first()

        MAPP = settings.GECO_MAPPING['DEF_MAP']
        all_items = GecoDefs.active_objects.select_related(
            'source_db').filter(source_db=db)

        time_types = [n for n in all_items
                      if n.def_type == MAPP['TIME_TYPES']]
        excuse_types = [n for n in all_items
                        if n.def_type == MAPP['EXCUSE_TYPES']]
        day_models = [n for n in all_items
                      if n.def_type == MAPP['DAY_MODELS']]
        pay_types = [n for n in all_items
                     if n.def_type == MAPP['PAY_TYPES']]
        pay_models = [n for n in all_items
                      if n.def_type == MAPP['PAY_MODELS']]
        shift_models = [n for n in all_items
                        if n.def_type == MAPP['SHIFT_MODELS']]
        flex_shift_models = [n for n in all_items
                             if n.def_type == MAPP['FLEX_SHIFT_MODELS']]

        return Response({
            'db': db.code,
            'time_types': GecoDefSerializer(time_types, many=True).data,
            'excuse_types': GecoDefSerializer(excuse_types, many=True).data,
            'day_models': GecoDefSerializer(day_models, many=True).data,
            'pay_types': GecoDefSerializer(pay_types, many=True).data,
            'pay_models': GecoDefSerializer(pay_models, many=True).data,
            'shift_models': GecoDefSerializer(shift_models, many=True).data,
            'flex_shift_models': GecoDefSerializer(
                flex_shift_models, many=True).data
        })


class APIGroups(Bti, APIView):
    def get(self, request, format=None):
        from django.conf import settings
        MAPP = settings.GECO_MAPPING['GROUP_MAP']
        gtypes = [
            MAPP['COMPANIES'],
            MAPP['DEPARTMENTS'],
            MAPP['TITLES'],
            MAPP['ACCOUNTS']
        ]
        all_items = GecoGroups.active_objects.select_related(
            'source_db').filter(gtype__in=gtypes)
        companies = [n for n in all_items if n.gtype == MAPP['COMPANIES']]
        departments = [n for n in all_items if n.gtype == MAPP['DEPARTMENTS']]
        titles = [n for n in all_items if n.gtype == MAPP['TITLES']]
        accounts = [n for n in all_items if n.gtype == MAPP['ACCOUNTS']]

        return Response({
            'companies': GecoGroupSerializer(companies, many=True).data,
            'departments': GecoGroupSerializer(departments, many=True).data,
            'titles': GecoGroupSerializer(titles, many=True).data,
            'accounts': GecoGroupSerializer(accounts, many=True).data,
            'group_types': GecoGroups.GROUP_TYPES
        })
