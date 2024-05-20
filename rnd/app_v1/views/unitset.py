from django.conf import settings
from rest_framework.response import Response
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
import logging
import json

from bti.views.base import Bti, Pagination
from erp.models.friendly import Payplans

from app_v1.serializers.unitset import *

logger = logging.getLogger("app")

class UnitsetView(Bti, generics.ListAPIView):
    queryset = Unitsetl.objects.all()
    serializer_class = UnitsetSerializer
    filterset_fields = {
        'code': ['startswith', 'icontains', 'endswith', 'exact'],
        'name': ['startswith', 'icontains', 'endswith', 'exact']
    }
