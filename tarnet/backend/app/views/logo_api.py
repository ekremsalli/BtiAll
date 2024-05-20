import json
import calendar
import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from app.serializers.log_error import LogErrorSerializer
from app.serializers.integration import LogoApiSerializer
from common.views import BaseView
from app.models import Organization, LogoApiErrors
from app.armon_integration import ArmonApi
from app.logo_integration import LogoApi
from common.permission import IsAdmin
from app.sql_repo import SqlRepo


class LogoApiView(BaseView, APIView):

    @swagger_auto_schema(operation_description="Send logo", request_body=LogoApiSerializer, tags=['Logo API'])
    def post(self, request):
        from django.db import connection

        logo_url = LogoApi.SERVER_ADDRESS
        logo_client_token = LogoApi.CLIENT_TOKEN

        start_date = request.data.get('start_date')
        organization_id = request.data.get('organization_id')
        logo_firm = LogoApi.FIRM_NO
       
        logo_username = LogoApi.USERNAME
        logo_password = LogoApi.PASSWORD

        auth_token = LogoApi.get_auth_token(
            logo_username, logo_password, logo_client_token, logo_firm, logo_url)

        start_date = request.data.get('start_date')
        organization_id = request.data.get('organization_id')

        start = start_date.split("-")

        currentDate = datetime.date(
            int(start[0]), int(start[1]), int(start[2]))
        end_date = datetime.date(currentDate.year, currentDate.month,
                                 calendar.monthrange(currentDate.year, currentDate.month)[1])
        with connection.cursor() as cursor:
            cursor.execute(SqlRepo.organization_sql, [
                           start_date, end_date, organization_id])
            max_value = cursor.fetchone()[0]
            max_value = json.loads(max_value)  # sunucuda ekle

        if max_value:
            data_filter = LogoApi.data_to_string(max_value, start_date)

            test_log_list = []
            for i in range(len(data_filter)):
                data = LogoApi.send_logo(logo_url, logo_client_token, auth_token, data_filter[i].get("query_text"),
                                         logo_username)

                test_log_list.append(data)
                if data.get("status") <= 0:
                    obj = LogoApiErrors(
                        organization_id=organization_id,
                        unique_id=data.get("data").get("identityNr"),
                        full_name=data.get("data").get("fullName"),
                        message=data.get("message"),
                        query_text=data_filter[i].get("query_text"),
                        msg_list=" ".join(data.get("msgList")),
                        status=data.get("status"),
                        code=data.get("data").get("code"),
                        date_time=data_filter[i].get("start_date"),
                        is_active=False
                    )
                    obj.save()

            return Response({"transfer": True}, status=status.HTTP_200_OK)
        return Response({"message": "Veri bulunamadı"}, status=status.HTTP_404_NOT_FOUND)
