import logging
import json

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from bti.views.base import Bti
from erp.active import Active

from app_v1.models import InvoiceQue
from app_v1.serializers.arp import ArpSerializer

logger = logging.getLogger("app")

class ARPView(Bti, APIView):
    @swagger_auto_schema(
        request_body=ArpSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def put(self, request, format=None):
        logger.info('ARP Post: ' + json.dumps(request.data))
        idata = ArpSerializer(data=request.data)
        idata.is_valid(raise_exception=True)
        data = idata.data
        config = Active.settings

        card = InvoiceQue.get_arp_card(data.get('uid'))
        if card:
            status, object = InvoiceQue.update_arp_card(data, config)
        else:
            status, object = InvoiceQue.create_arp_card(data, config)

        
        if object and object.flow.success and object.flow.internal_ref:
            return Response({
                'status': True,
                'description': 'Cari kart başarıyla eklendi/güncellendi!',
                'logical_ref': object.flow.internal_ref,
                'pid': object.flow.pid,
                'flow': object.flow.id
            })
        else:
            return Response({
                'status': False,
                'description': 'Cari kart aktarılamadı!',
                'pid': object.flow.pid,
                'flow': object.flow.id
            }, status=status.HTTP_400_BAD_REQUEST)