import json
from rest_framework import generics

from common.views import Bti, Pagination
from common.permissions import IsAdmin
from app.serializers.db import DBSerializer
from app.models.base import DB




class DBView(Bti, generics.ListAPIView):
    swagger_schema = None
    pagination_class = Pagination
    serializer_class = DBSerializer
    queryset = DB.objects.all().order_by('title')
    ordering_fields = [
        'is_active', 'code', 'title'
    ]


class DBEdit(generics.UpdateAPIView):
    permission_classes = (IsAdmin,)
    queryset = DB.objects.all()
    serializer_class = DBSerializer    