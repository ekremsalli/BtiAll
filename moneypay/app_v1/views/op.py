from django.http import response
from rest_framework import viewsets
from bti.views.base import Bti, Pagination

from common.permissions import BaseModelPerm

from app_v1.models import Operation, OperationDetail
from app_v1.serializers.op import OperationSerializer, OperationDetailSerializer

class OpView(Bti, viewsets.ModelViewSet):
    swagger_schema = None
    pagination_class = Pagination
    queryset =  Operation.objects.all()
    serializer_class = OperationSerializer

class OpDetailView(Bti, viewsets.ModelViewSet):
    swagger_schema = None
    pagination_class = Pagination
    queryset = OperationDetail.objects.all()
    serializer_class = OperationDetailSerializer