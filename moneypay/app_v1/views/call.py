import logging
import json

from django.core.management import call_command
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema


from bti.views.base import Bti

from app_v1.serializers.call import *


logger = logging.getLogger("app")

class CallView(Bti, APIView):
    @swagger_auto_schema(
        request_body=CallSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    
    def post(self, request, format=None):
        idata = CallSerializer(data=request.data)
        if idata.is_valid() is False:
            logger.error('Call post validation error: ' + json.dumps(request.data))
            raise ValidationError(idata.errors)

        data = idata.data
        que = call_command('process_que', delta=data.get('delta'))
        process = call_command('process_all')
        return Response({
            'que': que,
            'process': process
        })
