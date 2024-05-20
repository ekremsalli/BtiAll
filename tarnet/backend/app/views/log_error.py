from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from django.http import Http404

from app.serializers.log_error import LogErrorSerializer, SendErrorSerializers, TotalSendSerializers
from common.views import BaseView
from app.models import LogoApiErrors
from app.logo_integration import LogoApi
from common.permission import IsAdmin


class LogoErrorView(BaseView, APIView):

    @swagger_auto_schema(operation_description="New to transfer", request_body=SendErrorSerializers, tags=['Logs'])
    def post(self, request):
        error_id = request.data.get('id')
        logo_url = LogoApi.SERVER_ADDRESS
        logo_client_token = LogoApi.CLIENT_TOKEN
        logo_firm = LogoApi.FIRM_NO
        logo_username = LogoApi.USERNAME
        logo_password = LogoApi.PASSWORD
        auth_token = LogoApi.get_auth_token(
            logo_username, logo_password, logo_client_token, logo_firm, logo_url)
        error = LogoApiErrors.objects.get(id=error_id)
        query_text = error.query_text

        send_data = LogoApi.send_logo(logo_url, logo_client_token, auth_token, query_text,
                                      logo_username)
        if send_data.get('status') <= 0:
            response = send_data.get("msgList")
            return Response(response, status.HTTP_404_NOT_FOUND)
        error.is_activate()
        return Response({"status": "Success"}, status=status.HTTP_200_OK)


class LogoErrorListView(BaseView, APIView):

    @swagger_auto_schema(operation_description="Log list", tags=['Logs'])
    def get(self, request, organization_id):
        data = LogoApiErrors.objects.filter(organization_id=organization_id)
        serializer = LogErrorSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogErrorDetailView(BaseView, APIView):

    def get_object(self, pk):
        try:
            return LogoApiErrors.objects.get(pk=pk)
        except LogoApiErrors.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_description="Log delete", tags=['Logs'])
    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogErrorTotalSend(BaseView, APIView):

    @swagger_auto_schema(operation_description="Total send logo", tags=['Logs'])
    def get(self, request, organization_id):
        organization_id = request.data.get('organization_id')
        logo_url = LogoApi.SERVER_ADDRESS
        logo_client_token = LogoApi.CLIENT_TOKEN
        logo_firm = LogoApi.FIRM_NO

        logo_username = LogoApi.USERNAME
        logo_password = LogoApi.PASSWORD


        auth_token = LogoApi.get_auth_token(
            logo_username, logo_password, logo_client_token, logo_firm, logo_url)
        data = LogoApiErrors.objects.filter(organization_id=organization_id)

        if data:
            response = []
            for index in range(len(data)):
                send_data = LogoApi.send_logo(logo_url, logo_client_token, auth_token, data[index].query_text,
                                              logo_username)
                
                error = LogoApiErrors.objects.get(id=data[index].id)
                if send_data.get('status') <= 0:
                    response.append(send_data.get("msgList"))
                else:
                    error.is_activate()
            if not response:
                return Response({"status": "Success"}, status=status.HTTP_200_OK)
            return Response({"status": "not_ready",
                             "message": "Toplu gönderim gerçekleştirildi ama henüz düzeltilmeyen kayıtlar bulunuyor"},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "veri bulunamadı"}, status=status.HTTP_404_NOT_FOUND)
