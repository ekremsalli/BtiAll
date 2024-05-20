from rest_framework import viewsets

from bti.models import TaskActivity
from bti.serializers.activity import ActivitySerializer
from bti.views.base import Bti, Pagination
from bti.permissions import BaseModelPerm


class ActivityViewSet(Bti, viewsets.ReadOnlyModelViewSet):
    queryset = TaskActivity.objects.all()
    serializer_class = ActivitySerializer
    pagination_class = Pagination
    permission_classes = [BaseModelPerm]
    ordering_fields = "__all__"
    filterset_fields = {
        'name': ['contains'],
        'exception': ['contains'],
        'is_success': ['exact'],
    }

