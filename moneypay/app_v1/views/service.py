import logging
import json

from django.db import IntegrityError
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from bti.views.base import Bti

from app_v1.serializers.service import *
from app_v1.models import OpQue


logger = logging.getLogger("app")


class ServiceView(Bti, APIView):
    @swagger_auto_schema(
        request_body=RequestSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def post(self, request, format=None):
        idata = RequestSerializer(data=request.data)
        if idata.is_valid() is False:
            logger.error('Request post validation error: ' +
                         json.dumps(request.data))
            raise ValidationError(idata.errors)

        data = idata.data
        errors = []
        added = []
        try:
            for line in data.get('lines'):
                try:
                    is_invoice = sum([
                        line.get('invoice_gross_amount', 0),
                        line.get('invoice_net_amount', 0)
                    ]) > 0
                    OpQue.objects.create(
                        day=line.get('day'),
                        identifier=line.get('pid'),
                        op_code=line.get('op_code'),
                        commission_amount=line.get('commission_amount'),
                        is_invoice=is_invoice,
                        data=json.dumps(line)
                    )
                except IntegrityError as e:
                    errors.append(line.get('pid'))
                else:
                    added.append(line.get('pid'))
            return Response({
                'status': True,
                'added': len(added),
                'integrity': errors
            })
        except Exception as e:
            raise APIException(e)
