from django.conf import settings
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.exceptions import APIException

from drf_yasg.utils import swagger_auto_schema

import logging
import json


from bti.views.base import Bti, Pagination
from app_v1.models import S3Resource

from app_v1.serializers.aws import *

logger = logging.getLogger("app")

class S3View(Bti, generics.CreateAPIView, generics.ListAPIView):
    queryset = S3Resource.objects.all()
    serializer_class = S3ResourceSerializer
    filterset_fields = {
        'prefix': ['startswith', 'icontains', 'endswith', 'exact'],
        'aws_access_key': ['startswith', 'icontains', 'endswith', 'exact'],
        'bucket': ['startswith', 'icontains', 'endswith', 'exact'],
        'region': ['startswith', 'icontains', 'endswith', 'exact']
    }


class S3DetailView(
        Bti, 
        generics.RetrieveAPIView, 
        generics.DestroyAPIView, 
        generics.UpdateAPIView, 
        generics.GenericAPIView):
    allowed_methods = ['GET', 'PATCH', 'DELETE']
    lookup_field = 'prefix'
    queryset = S3Resource.objects.all()
    serializer_class = S3ResourceSerializer

    def put(self, *args, **kwargs):
        raise APIException('Unsupported method')