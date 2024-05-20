from rest_framework import generics
import logging
from rest_framework import mixins

from bti.views.base import Bti
from erp.models.friendly import Stfiche
from app_v1.serializers.dispatch import DispatchSerializer
from app_v1.filters import DispatchListFilter


logger = logging.getLogger("app")

class DispatchView(Bti, generics.ListAPIView):
    queryset = Stfiche.objects.prefetch_related('erp_lg_stline_stficheref').exclude(trcode__gt=10)
    serializer_class = DispatchSerializer
    filter_class = DispatchListFilter


class DispatchDetailView(Bti, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Stfiche.objects.exclude(trcode__gt=10)
    serializer_class = DispatchSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_object(self):
        return self.get_queryset().filter(
            docode=self.kwargs.get('docno'), 
            sourceindex=self.kwargs.get('warehouse')
        ).first()
