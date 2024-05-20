from django.conf import settings
from rest_framework.response import Response
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
import logging
import json

from bti.views.base import Bti, Pagination
from erp.models.friendly import UnitBarcode

from app_v1.serializers.barcode import *

logger = logging.getLogger("app")

class BarcodeView(Bti, generics.ListAPIView):
    queryset = UnitBarcode.objects.select_related('itemref').all()
    serializer_class = BarcodeSerializer
    filterset_fields = {
        'barcode': ['startswith', 'icontains', 'endswith', 'exact'],
    }
