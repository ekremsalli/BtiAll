import json
from django.conf import settings


from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from bti.views.base import Bti, Pagination
from erp.active import Active

from app.serializers import DispatchCreateSerializer
from app.models import DispatchTrack

import logging
logger = logging.getLogger("app")


class Dispatch(Bti, APIView):
    @swagger_auto_schema(
        request_body=DispatchCreateSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def post(self, request, format=None):
        logger.error('Dispatch post: ' + json.dumps(request.data))
        dispatch = DispatchCreateSerializer(data=request.data)
        dispatch.is_valid(raise_exception=True)
        data = dispatch.data

        if 'firm' in data and data.get('firm') != 1:
            return Response({
                'status': False,
                'description': 'Geçersiz firma!'
            }, status=status.HTTP_400_BAD_REQUEST)


        if "firm" in data:
            Active.load_firm_via_nr(data.get('firm'))

        check = DispatchTrack.control({
            'firm': Active.name,
            'identifier': data.get('doc_tracking_number')
        })
        if check:
            return Response(check.in_track(
                f'Bu irsaliye {check.fmt_created} tarihinde kayıt olmuş.'
            ), status=status.HTTP_208_ALREADY_REPORTED)

        object = DispatchTrack.create_dispatch(data)
        Active.clear_cache()
        if object and object.flow.success and object.flow.internal_ref:
            return Response({
                'status': True,
                'description': 'İrsaliye başarıyla kaydedildi!',
                'logical_ref': object.flow.internal_ref,
                'pid': object.flow.pid,
                'flow': object.flow.id
            })
        else:
            return Response({
                'status': False,
                'description': 'İrsaliye aktarılamadı!',
                'pid': object.flow.pid,
                'flow': object.flow.id
            }, status=status.HTTP_400_BAD_REQUEST)
