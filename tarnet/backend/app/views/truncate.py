from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from app.serializers.integration import ArmonSerializer
from common.views import BaseView
from app.armon_integration import ArmonApi
from common.permission import IsAdmin
from app.models.employee import EmployeeLogs


class TruncateView(BaseView, APIView):
    permission_classes = (IsAdmin,)

    @swagger_auto_schema(
        operation_description="Armon API ile gelen verileri logo ya aktardıktan sonra tablo truncate edilebilir",
        tags=['Truncate'])
    def get(self, request):
        EmployeeLogs.truncate()
        return Response({"status": "success"}, status=status.HTTP_200_OK)
