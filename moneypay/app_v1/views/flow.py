from rest_framework import generics

from bti.views.base import Bti, Pagination
from bti.models.flow import Flow

from common.permissions import BaseModelPerm

from app_v1.serializers.flow import FlowSerializer


class FlowView(Bti, generics.ListAPIView):
    swagger_schema = None
    pagination_class = Pagination
    serializer_class = FlowSerializer
    queryset = Flow.objects.all().order_by("-created") 
    permission_classes = [BaseModelPerm]
    ordering_fields = [
        'company', 'period', 'user', 
        'handler', 'endpoint', 'method', 
        'data', 'related_object', 'internal_ref',
        'request', 'response', 'exception',
        'success', 'next_flow', 'prev_flow', 'error_code',
        'pid', 'took', 'created'
    ]
    filterset_fields = {
        'data': ['contains'],
        'method': ['contains']        
    }

    def get_queryset(self):
        qs = super().get_queryset()
        success = self.request.query_params.get('success')
        if success:            
            qs = qs.filter(success = success == '1')
        return qs
