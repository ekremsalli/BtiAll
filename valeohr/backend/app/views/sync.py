import logging

from django.apps import apps
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from common.views import Bti
from app.models.base import DB
from app.serializers.db import DBSerializer

logger = logging.getLogger("app")

class Firms:
    firms_selected =["A05", "B55ESE1", "B55ESE2", "C01", "C09", "C31", "C99", "D10", "D18", "D26", 
                     "D31", "D41", "EGRUP", "EGRUP OSB", "EUROSEVE", "EUROSERVE IST","EUROSEVRE OSB",
                     "H26", "H26 IST", "M14", "M88", "T68", "T70", "T95", "T99", "W26"]
                     #İleride müşterinin seçebileceği bir ekran eklenebilir
                     
class Sync(Bti, APIView):
    def get(self, request, format=None):
        serializer = DBSerializer(DB.objects.all(), many=True)
        return Response({
            'db': serializer.data
        })

    def post(self, request, format=None):
        from datetime import datetime
        logger.info("Sync/View Başladı")
        data = request.data

        if 'start' in data:
            start = datetime.strptime(data.get('start', None), '%Y/%m/%d')
        else:
            start = None
        if 'end' in data:
            end = datetime.strptime(data.get('end', None), '%Y/%m/%d')
        else:
            end = None

        safest_models = [
            'gecogroups', 'employees', 'gecodefs',
            'transactions', 'anomalies'
        ]
        ranged_models = ['transactions', 'anomalies']
        models = {
            mod.__name__.lower(): mod
            for mod in apps.get_app_config('app').get_models()
        }

        db = DB.objects.filter(pk=data.get('db')).first()
        if db is None:
            raise APIException({
                'custom': True,
                'message': 'Bilinmeyen veritabanı'
            })
        logger.info("Sync/View for loop başladı")
        for model in data.get('models'):
            if model in safest_models:
                if model not in ranged_models:
                    if hasattr(models[model], 'sync'):
                        models[model].sync(db)
                else:
                    models[model].sync(
                        db,
                        year=data.get('year'),
                        month=data.get('month'),
                        start=start,
                        end=end
                    )
        logger.info("Sync/View Tamamlandı")
        return Response({'success': True})
        
