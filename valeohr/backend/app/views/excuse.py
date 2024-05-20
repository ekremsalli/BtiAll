import json

from datetime import datetime
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from drf_yasg.utils import swagger_auto_schema

from common.views import Bti
from app.models import Excuse, Employees, DB
from app.serializers.excuse import ExcuseSerializers, ExcuseApproveSerializer, ExcuseDetailSerializer, \
    ExcuseAllAproveSerializer, ExcuseAllDeleteSerializer
from common.permissions import IsAdminOrChangeEditPermission


class ExcuseView(Bti, APIView):

    @swagger_auto_schema(operation_description="Yeni mazeretleri listele", tags=['Excuse'])
    def get(self, request):
        queryset = Excuse.waiting_for_approve.select_related(
            'source_db',
            'created_by'
        ).all()
        serializer = ExcuseDetailSerializer(queryset, many=True)
        data = serializer.data
        data = json.loads(json.dumps(data))

        for i in range(len(data)):
            obj = Employees.objects.get(nr=data[i].get('employee_id'))
            data[i].update({
                "employee": f"({data[i].get('employee_id')}) {obj.name} {obj.surname}"
            })

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Yeni mazeret ekle", request_body=ExcuseSerializers, tags=['Excuse'])
    def post(self, request):
        data = request.data
        created_by = request.user
        source_db = Employees.objects.get(nr=request.data.get('employee_id')).source_db_id
        db = DB.objects.get(id=source_db)
        data.update({
            'created_by': created_by.id,
            "source_db": db.id
        })
        serializer = ExcuseSerializers(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExcuseDetailView(Bti, APIView):
    @swagger_auto_schema(operation_description="Onaylama 1. onay = 1, 2. onay = 2  reddet için 3 gönder",
                         request_body=ExcuseApproveSerializer, tags=['Excuse'])
    def patch(self, request, pk):
        obj = Excuse.objects.filter(pk=pk)
        excuse = Excuse.objects.get(pk=pk)
        verify_status = request.data.get('verify_status')
        if obj.exists():
            if verify_status == 1:
                excuse.approve(verify_status)
            elif verify_status == 2:
                excuse.approve(verify_status)
                data = {
                    'tle_persnr': excuse.employee_id,
                    "tle_datum": excuse.tr_date,
                    "tle_vonzeit": excuse.start,
                    "tle_biszeit": excuse.end,
                    "tle_istzeit": excuse.work_time,
                    "tle_zeitart": excuse.time_type,
                    "tle_abwart": excuse.excuse_type,
                    "tle_abwtag": excuse.excuse_day,
                    "tle_perkstnr": excuse.account,
                    "tle_tagmod": excuse.day_model,
                    "tle_benutzer": f"b-{excuse.created_by.username}"[0:20],
                    "tle_beginnkz": excuse.day_types,
                    "tle_infkz": "",
                    "tle_timestamp": excuse.created_on,
                }
                if excuse.excuse_day is None:
                    data.update({
                        "tle_info": ""
                    })
                else:
                    data.update({
                        "tle_info": "m"
                    })

                excuse.send_approve(data, excuse.source_db.code)
            elif verify_status == 3:
                excuse.approve(verify_status)
            return Response({'status': "success"}, status=status.HTTP_200_OK)
        return Response({'status': f"{pk} not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="delete ", tags=['Excuse'])
    def delete(self, request, pk):
        obj = Excuse.objects.filter(pk=pk)
        excuse = Excuse.objects.get(pk=pk)
        if obj.exists():
            excuse.delete()
            return Response({'status': "success"}, status=status.HTTP_200_OK)
        return Response({'status': f"{pk} not found"}, status=status.HTTP_404_NOT_FOUND)


class ExcuseApproveSend(Bti, APIView):

    @swagger_auto_schema(operation_description="İkinci onay bekleyenler", tags=['Excuse'])
    def get(self, request):
        queryset = Excuse.waiting_for_send.select_related(
            'source_db',
            'created_by'
        ).all()
        serializer = ExcuseDetailSerializer(queryset, many=True)
        data = serializer.data
        data = json.loads(json.dumps(data))

        for i in range(len(data)):
            obj = Employees.objects.get(nr=data[i].get('employee_id'))
            data[i].update({
                "employee": f"({data[i].get('employee_id')}) {obj.name} {obj.surname}"
            })

        return Response(data, status=status.HTTP_200_OK)


class ExcuseAllAproveView(Bti, APIView):

    @swagger_auto_schema(operation_description="Tümünü Onaylama 1. onay = 1, 2. onay = 2  reddet için 3 gönder",
                         request_body=ExcuseAllAproveSerializer, tags=['Excuse'])
    def post(self, request):
        data = request.data
        ids = data.get('excuse_ids')
        verify_status = data.get('verify_status')
        excuses = Excuse.objects.filter(pk__in=ids)
        if excuses.exists():
            if verify_status == 1:
                for obj in excuses:
                    obj.approve(verify_status)
            elif verify_status == 2:
                for obj in excuses:
                    obj.approve(verify_status)
                    obj.approve(verify_status)
                    data = {
                        'tle_persnr': obj.employee_id,
                        "tle_datum": obj.tr_date,
                        "tle_vonzeit": obj.start,
                        "tle_biszeit": obj.end,
                        "tle_istzeit": obj.work_time,
                        "tle_zeitart": obj.time_type,
                        "tle_abwart": obj.excuse_type,
                        "tle_abwtag": obj.excuse_day,
                        "tle_perkstnr": obj.account,
                        "tle_infkz": "",
                        "tle_timestamp": obj.created_on,
                        "tle_tagmod": obj.day_model,
                        "tle_benutzer": request.user.username[:20]
                    }
                    obj.send_approve(data, obj.source_db.code)

            elif verify_status == 3:
                for obj in excuses:
                    obj.approve(verify_status)

            return Response({'status': "success"}, status=status.HTTP_200_OK)

        return Response({'status': f"{ids} not found"}, status=status.HTTP_404_NOT_FOUND)


class ExcuseAllDeleteView(Bti, APIView):
    @swagger_auto_schema(operation_description="Tümünü sil",
                         request_body=ExcuseAllDeleteSerializer, tags=['Excuse'])
    def post(self, request):
        data = request.data
        ids = data.get('excuse_ids')
        excuses = Excuse.objects.filter(pk__in=ids)
        if excuses.exists():
            excuses.delete()
            return Response({'status': "success"}, status=status.HTTP_200_OK)
        return Response({'status': f"{ids} not found"}, status=status.HTTP_404_NOT_FOUND)
