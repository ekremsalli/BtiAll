import json
import calendar
import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from app.serializers.integration import ArmonSerializer
from common.views import BaseView
from app.armon_integration import ArmonApi
from common.permission import IsAdmin
from app.models.employee import EmployeeLogs


class ArmonApiView(BaseView, APIView):

    @swagger_auto_schema(operation_description="Armon API integration", request_body=ArmonSerializer, tags=['ArmonAPI'])
    def post(self, request):
        # EmployeeLogs.truncate()
        start_date = request.data.get("start_date")
        grant_type_id = request.data.get("grant_type_id")

        start = start_date.split("-")
        currentDate = datetime.date(
            int(start[0]), int(start[1]), int(start[2]))
        end_date = datetime.date(currentDate.year, currentDate.month,
                                 calendar.monthrange(currentDate.year, currentDate.month)[1])

        start_date = str(start_date + "T00:00:00.000Z")
        end_date = str(str(end_date) + "T00:59:59.000Z")

        # org_grant_type = ArmonApi.get_grand_type_id(username=ArmonApi.USERNAME)
        #
        # for i in range(len(org_grant_type)):
        #     obj, created = Organization.objects.update_or_create(organization_id=org_grant_type[i].get("id"),
        #                                                          organization_name=org_grant_type[i].get("name"),
        #                                                          grant_type_id=org_grant_type[i].get("authentications")[
        #                                                              0].get("id"))

        login = ArmonApi.get_token(
            grant_type_id, ArmonApi.USERNAME, ArmonApi.PASSWORD)

        token = login.get("token")
        org_id = login.get("organization_id")
        log = ArmonApi.organization_users_log(
            token, org_id, start_date, end_date)

        if log:
            log_list = [EmployeeLogs(**value)
                        for value in log if value is not None]
            EmployeeLogs.objects.bulk_create(log_list, batch_size=1000)
            return Response(
                {"message": "Success", "start_date": request.data.get(
                    "start_date"), "organization_id": org_id},
                status=status.HTTP_200_OK)

        return Response({"data": False}, status=status.HTTP_404_NOT_FOUND)
