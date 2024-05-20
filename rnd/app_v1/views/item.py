from django.conf import settings
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework import mixins
from rest_framework.exceptions import APIException

from drf_yasg.utils import swagger_auto_schema

import logging
import json

from bti.views.base import Bti
from erp.models.friendly import Items, UnitBarcode
from erp.asking.image import ImageXML


from app_v1.serializers.item import *
from app_v1.models import ItemTrack

logger = logging.getLogger("app")


class ItemDetailView(Bti, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer

    @swagger_auto_schema(
        request_body=ItemPatchSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def patch(self, request, barcode, format=None):
        logger.info('Item patch: ' + json.dumps(request.data))
        idata = ItemPatchSerializer(data=request.data, partial=True)
        idata.is_valid(raise_exception=True)
        data = idata.data
        image_str = data.get('image')
        img_format = data.get('img_format')
        unit = UnitBarcode.objects.filter(barcode=barcode).first()
        if unit is None:
            raise APIException('Geçersiz barkod!')
        item = unit.itemref
        if item is None:
            raise APIException('Geçersiz malzeme!')
        object = ItemTrack.update_item(data, suffix=item.pk)

        img = ImageXML()
        img.upload(0, object.flow.internal_ref, img_format, 1, image=image_str)
        
        if object and object.flow.success and object.flow.internal_ref:
            return Response({
                'status': True,
                'description': 'Malzeme başarıyla güncellendi!',
                'logical_ref': object.flow.internal_ref,
                'pid': object.flow.pid,
                'flow': object.flow.id
            })
        else:
            return Response({
                'status': False,
                'description': 'Malzeme güncellenemedi!',
                'pid': object.flow.pid,
                'flow': object.flow.id
            }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_object(self):
        try:
            unit = UnitBarcode.objects.filter(
                barcode=self.kwargs.get('barcode')
            ).first()
        except:
            raise APIException('Bu barkod herhangi bir ürüne bağlı değil!')
        else:
            if unit is None:
                raise APIException('Bilinmeyen barkod!')
            try:
                ref = unit.itemref
            except:
                raise APIException('Bu barkod herhangi bir ürüne bağlı değil!')
            else:
                return ref


class ItemCodeView(Bti, generics.GenericAPIView):
    @swagger_auto_schema(
        request_body=ItemCodeSerializer,
        responses={
            200: 'next: value'
        }
    )
    def post(self, request, *args, **kwargs):
        idata = ItemCodeSerializer(data=request.data)
        idata.is_valid(raise_exception=True)
        data = idata.data
        ex = {}

        if data.get('prefix') == 'CLK':
            ex.update({
                'code__startswith': 'CLK2'
            })

        next = Items.next_code(
            'code',
            data.get('pattern'),
            data.get('prefix'),
            merge=data.get('seperator', '.'),
            exclude=ex
        )
        return Response({
            'next': next
        })


class ItemView(Bti, generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    filterset_fields = {
        'code': ['startswith', 'icontains', 'endswith', 'exact'],
        'logicalref': ['exact'],
        'name': ['startswith', 'icontains', 'endswith', 'exact'],
        'specode': ['startswith', 'icontains', 'endswith', 'exact'],
        'cyphcode': ['startswith', 'icontains', 'endswith', 'exact']
    }

    @swagger_auto_schema(
        request_body=ItemCreateSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def post(self, request, format=None):
        logger.info('Item post: ' + json.dumps(request.data))
        idata = ItemCreateSerializer(data=request.data)
        idata.is_valid(raise_exception=True)
        data = idata.data
        image_str = data.get('image')
        img_format = data.get('img_format')

        if data.get('units') and len(data.get('units')):
            check = UnitBarcode.objects.filter(
                barcode=data.get('units')[0]['barcode'],
            ).count()
            if check != 0:
                return Response({
                    'status': False,
                    'description': 'Bu malzeme daha önce kayıt olmuş.',
                }, status=status.HTTP_208_ALREADY_REPORTED)

        check = Items.objects.filter(
            cardtype=data.get('card_type'),
            code=data.get('code')).count()

        if check != 0:
            return Response({
                'status': False,
                'description': 'Bu malzeme kodu kullanımda!',
            }, status=status.HTTP_208_ALREADY_REPORTED)

        object = ItemTrack.create_item(data)

        if object and object.flow.success and object.flow.internal_ref:
            img = ImageXML(user="BTI")
            img.upload(0, object.flow.internal_ref, img_format, 1, image=image_str)
            return Response({
                'status': True,
                'description': 'Malzeme başarıyla eklendi!',
                'logical_ref': object.flow.internal_ref,
                'pid': object.flow.pid,
                'flow': object.flow.id
            })
        else:
            return Response({
                'status': False,
                'description': 'Malzeme aktarılamadı!',
                'pid': object.flow.pid,
                'flow': object.flow.id
            }, status=status.HTTP_400_BAD_REQUEST)
