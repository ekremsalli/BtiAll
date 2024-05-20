from rest_framework import viewsets

from bti.models import Flow
from bti.serializers.flow import FlowSerializer
from bti.views.base import Bti, Pagination
from bti.permissions import BaseModelPerm


class FlowViewSet(Bti, viewsets.ReadOnlyModelViewSet):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer
    pagination_class = Pagination
    permission_classes = [BaseModelPerm]
    ordering_fields = "__all__"
    filterset_fields = {
        'method': ['contains'],
        'endpoint': ['contains'],
        'related_object': ['contains'],
        'internal_ref': ['exact'],
        'pid': ['exact'],
    }

