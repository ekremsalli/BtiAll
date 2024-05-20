from django.conf import settings
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.exceptions import APIException

from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema


import logging
import json

from bti.views.base import Bti, Pagination
from erp.models.friendly import (
    Clcard,
    Orfiche,
    Stline
)
from erp.active import Active
from uritemplate import partial


from app_v1.serializers.order import *
from app_v1.models import OrderTrack, ArpTrack

logger = logging.getLogger("app")

class ArpDetailView(Bti, mixins.RetrieveModelMixin, generics.GenericAPIView):
    lookup_field = 'code'
    queryset = Clcard.objects.all()
    serializer_class = ArpCardSerializer

    @swagger_auto_schema(
        request_body=ArpUpdateSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def patch(self, request, code, format=None):
        logger.info('Arp patch: ' + json.dumps(request.data))
        idata = ArpUpdateSerializer(data=request.data, partial=True)
        idata.is_valid(raise_exception=True)
        data = idata.data
        card = Clcard.objects.filter(code=code).first()
        if card is None:
            raise APIException('Geçersiz cari kart!')
        object = ArpTrack.update_card(data, pk=card.pk)
        if object and object.flow.success and  object.flow.internal_ref:
            return Response({
                'status': True,
                'description': 'Cari kart başarıyla güncellendi!',
                'logical_ref': object.flow.internal_ref,
                'pid': object.flow.pid,
                'flow': object.flow.id
            })
        else:
            return Response({
                'status': False,
                'description': 'Cari kart güncellenemedi!',
                'pid': object.flow.pid,
                'flow': object.flow.id
            }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)            


class ARPView(Bti, generics.ListAPIView):
    queryset = Clcard.objects.all()
    serializer_class = ArpCardSerializer
    filterset_fields = {
        'code': ['startswith', 'icontains', 'endswith', 'exact'],
        'logicalref': ['exact'],
        'definition_field': ['startswith', 'icontains', 'endswith', 'exact'],
        'tckno': ['startswith', 'icontains', 'endswith', 'exact'],
        'emailaddr': ['startswith', 'icontains', 'endswith', 'exact'],
        'taxnr': ['startswith', 'icontains', 'endswith', 'exact']
    }

    @swagger_auto_schema(
        request_body=ArpSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def post(self, request, format=None):
        logger.info('ARP post: ' + json.dumps(request.data))
        idata = ArpSerializer(data=request.data)
        idata.is_valid(raise_exception=True)
        data = idata.data

        check = Clcard.objects.filter(
            code=data.get('code'),
        ).count() != 0

        if check:
            return Response({
                'status': False,
                'description': 'Bu cari kart daha önce kayıt olmuş.',
            }, status=status.HTTP_208_ALREADY_REPORTED)

        object,title,flow = ArpTrack.create_card(data)
        if object and object.flow.success and object.flow.internal_ref:
            return Response({
                'status': True,
                'description': 'Cari kart başarıyla eklendi!',
                'logical_ref': object.flow.internal_ref,
                'pid': object.flow.pid,
                'flow': object.flow.id,
                "title":title
            })
        else:
            return Response({
                'status': False,
                'description': 'Cari kart aktarılamadı!',
                'pid': object.flow.pid,
                'flow': object.flow.id
            }, status=status.HTTP_400_BAD_REQUEST)

class OrderView(Bti, APIView):
    
    @swagger_auto_schema(
        request_body=OrderSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def post(self, request, format=None):
        print('Order post: ' + json.dumps(request.data))
        logger.info('Order post: ' + json.dumps(request.data))
        idata = OrderSerializer(data=request.data)
        idata.is_valid(raise_exception=True)
        data = idata.data

        check = Orfiche.objects.filter(
            ficheno=data.get('number'),
            trcode=1 if data.get('sales_order') else 2
        ).count() != 0

        if check:
            return Response({
                'status': False,
                'description': 'Bu sipariş daha önce kayıt olmuş.',
            }, status=status.HTTP_208_ALREADY_REPORTED)

        object,arp_obj,title = OrderTrack.create_order(data)
        if object and object.flow.success and object.flow.internal_ref:
            return Response({
                'status': True,
                'description': 'Sipariş başarıyla eklendi!',
                'logical_ref': object.flow.internal_ref,
                'pid': object.flow.pid,
                'flow': object.flow.id,
                'arp_ref':arp_obj.flow.internal_ref,
                'arp_title':title
            })
        else:
            return Response({
                'status': False,
                'description': 'Sipariş aktarılamadı!',
                'pid': object.flow.pid,
                'flow': object.flow.id
            }, status=status.HTTP_400_BAD_REQUEST)


class OrderUpdateView(Bti, APIView):
    @swagger_auto_schema(
        request_body=OrderSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def put(self, request, format=None, **kwargs):
        logger.info('OrderUpdate post: ' + json.dumps(request.data))
        idata = OrderSerializer(data=request.data)
        idata.is_valid(raise_exception=True)
        data = idata.data

        check = Orfiche.objects.filter(
            ficheno=kwargs.get('number'),
            trcode=1 if kwargs.get('sales_order') else 2
        ).count() == 0

        if check:
            return Response({
                'status': False,
                'description': 'Bilinmeyen sipariş.',
            }, status=status.HTTP_404_NOT_FOUND)

        fiche = Orfiche.objects.get(
            ficheno=kwargs.get('number'),
            trcode=1 if kwargs.get('sales_order') else 2
        )
        object = OrderTrack.create_order(
            data,
            pk=fiche.pk,
            sales_order=kwargs.get('sales_order')
        )
        if object and object.flow.success and object.flow.internal_ref:
            return Response({
                'status': True,
                'description': 'Sipariş başarıyla güncellendi!',
                'logical_ref': object.flow.internal_ref,
                'pid': object.flow.pid,
                'flow': object.flow.id
            })
        else:
            return Response({
                'status': False,
                'description': 'Sipariş güncelenemedi!',
                'pid': object.flow.pid,
                'flow': object.flow.id
            }, status=status.HTTP_400_BAD_REQUEST)


class OrderCancelView(Bti, APIView):
    @swagger_auto_schema(
        request_body=None,
        responses={
            200: 'status: true/false'
        }
    )
    def post(self, request, format=None, **kwargs):
        fiche = Orfiche.objects.filter(
            ficheno=kwargs.get('number'),
            trcode=1 if kwargs.get('sales_order') else 2
        ).first()

        if fiche is None:
            return Response({
                'status': False,
                'description': 'Bilinmeyen sipariş!'
            }, status=status.HTTP_400_BAD_REQUEST)
        if fiche.status == 2:
            return Response({
                'status': False,
                'description': 'Sipariş daha önce iptal edilmiş!',
                'ref': fiche.logicalref
            }, status=status.HTTP_400_BAD_REQUEST)

        if Stline.objects.filter(ordficheref=fiche).count() > 0:
            return Response({
                'status': False,
                'description': 'Siparişe ait irsaliye mevcut!',
            })

        object = OrderTrack.cancel_order(
            kwargs.get('number'),
            fiche,
            kwargs.get('sales_order')
        )
        if object and object.flow.success and object.flow.internal_ref:
            return Response({
                'status': True,
                'description': 'Sipariş başarıyla iptal edildi!',
                'logical_ref': object.flow.internal_ref,
                'pid': object.flow.pid,
                'flow': object.flow.id
            })
        else:
            return Response({
                'status': False,
                'description': 'Sipariş iptal edilemedi!',
                'pid': object.flow.pid,
                'flow': object.flow.id
            }, status=status.HTTP_400_BAD_REQUEST)
