
from django.db.models import Q
from rest_framework import viewsets

from bti.views.base import Bti, Pagination

from common.permissions import BaseModelPerm

from app_v1.models import TaskActivity

from app_v1.serializers.activity import ActivitySerializer

class ActivityView(Bti, viewsets.ReadOnlyModelViewSet):
    swagger_schema = None
    permission_classes = [BaseModelPerm]    
    pagination_class = Pagination
    serializer_class = ActivitySerializer
    queryset = TaskActivity.objects.all().order_by("-created")
    ordering_fields = [
        'id', 'name', 'is_success', 
        'params', 'exception', 'took', 
        'created'
    ]
    filterset_fields = {
        'name': ['contains'],
    }

    def get_queryset(self):
        qs = super().get_queryset()        
        is_success = self.request.query_params.get('is_success')
        if is_success:            
            qs = qs.filter(is_success = is_success == '1')
        return qs
