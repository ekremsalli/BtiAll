import logging
import json
from rest_framework import generics, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from erp.active import Active
from bti.views.base import Bti
from erp.models.friendly import Invoice
from third_party.elogo.api import Elogo

from app_v1.serializers.invoice import (
    InvoiceSerializer,
    InvoiceDetailSerializer, InvoiceReadSerializer, ReturnInvoiceSerializer
)
from app_v1.models import InvoiceTrack

logger = logging.getLogger("app")


class InvoicePDF(Bti, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Invoice.objects.exclude()

    def get_object(self):
        docode = self.request.query_params.get('DocumentNo', None)
        ficheno = self.request.query_params.get('InvoiceNo', None)
        if docode is None and ficheno is None:
            raise APIException('Please speficy InvoiceNo or DocumentNo!')

        if (docode and len(docode) == 0) and (ficheno and len(ficheno) == 0):
            raise APIException('Please speficy InvoiceNo or DocumentNo!')

        filter = {}
        if docode and len(docode):
            filter.update({
                'docode': docode
            })
        if ficheno and len(ficheno):
            filter.update({
                'ficheno': ficheno
            })

        object = self.get_queryset().filter(**filter).last()
        if object is None:
            raise APIException('Unknown invoice!')
        return object

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('DocumentNo', openapi.IN_QUERY,
                          type=openapi.TYPE_STRING, description='Documant Number'),
        openapi.Parameter('InvoiceNo', openapi.IN_QUERY, type=openapi.TYPE_STRING, description='Invoice Number')])
    def get(self, request, *args, **kwargs):
        object = self.get_object()

        elogo = Elogo(
            Active.settings['ELOGO_USER'],
            Active.settings['ELOGO_PWD']
        )

        elogo.login()
        try:
            document = elogo.get_document_data(
                object.guid,
                doc_type='EINVOICE' if object.einvoice == 1 else 'EARCHIVE'
            )
        except Exception as e:
            raise APIException(e)
        else:

            if document and 'binaryData' in document:
                pdf = elogo.get_encoded_pdf(document, object.guid)
                return Response({
                    'Pdf': pdf,
                    'InvoiceNo': object.ficheno
                })
            else:
                return Response({}, status=status.HTTP_204_NO_CONTENT)
        finally:
            elogo.logout()


class InvoiceDetailView(Bti, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Invoice.objects.exclude()
    serializer_class = InvoiceDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_object(self):
        docode = self.request.query_params.get('DocumentNo', None)
        ficheno = self.request.query_params.get('InvoiceNo', None)
        if docode is None and ficheno is None:
            raise APIException('Please speficy InvoiceNo or DocumentNo!')

        if (docode and len(docode) == 0) and (ficheno and len(ficheno) == 0):
            raise APIException('Please speficy InvoiceNo or DocumentNo!')

        filter = {}
        if docode and len(docode):
            filter.update({
                'docode': docode
            })
        if ficheno and len(ficheno):
            filter.update({
                'ficheno': ficheno
            })

        object = self.get_queryset().filter(**filter).last()
        if object is None:
            raise APIException('Unknown invoice!')
        return object


class InvoiceView(Bti, mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = InvoiceSerializer

    def post(self, request, format=None):
        logger.info('Inoice post: ' + json.dumps(request.data))
        idata = InvoiceSerializer(data=request.data)
        idata.is_valid(raise_exception=True)
        data = idata.data

        identifier = data.get('InvoiceNo')
        if identifier == '~':
            identifier = data.get('DocumentNo')
            check = Invoice.objects.filter(
                doctrackingnr=identifier,
                trcode=7,
            ).count() != 0
        else:
            check = Invoice.objects.filter(
                ficheno=identifier,
                trcode=7,
            ).count() != 0

        if check:
            return Response({
                'status': False,
                'description': 'Bu fatura daha önce kayıt olmuş.',
            }, status=status.HTTP_208_ALREADY_REPORTED)

        def validate_order_data(data):
            for line in data.get("Lines", []):
                if line.get("ret_cost_type") == 0 and not line.get("source_reference"):
                    return False
                elif line.get("ret_cost_type") == 1 and line.get("source_reference"):
                    return False
            return True

        if validate_order_data(data):
            object = InvoiceTrack.create_invoice(data, identifier=identifier)
            if object and object.flow.success and object.flow.internal_ref:
                return Response({
                    'status': True,
                    'description': 'Fatura başarıyla eklendi!',
                    'logical_ref': object.flow.internal_ref,
                    'pid': object.flow.pid,
                    'flow': object.flow.id
                })
            else:
                return Response({
                    'status': False,
                    'description': 'Fatura aktarılamadı!',
                    'pid': object.flow.pid,
                    'flow': object.flow.id
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': False,
                'description': 'ret_cost_type alanı 0 olarak set edilirse source_referance alanı zorunlu alan olmalıdır eğer ret cost type 1 set edilirse source reference boş geçilmelidir.',
            }, status=status.HTTP_400_BAD_REQUEST)


class InvoiceReadView(Bti, APIView):
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('start', openapi.IN_QUERY,
                          type=openapi.TYPE_STRING, description='Start Date'),
        openapi.Parameter('end', openapi.IN_QUERY,
                          type=openapi.TYPE_STRING, description='End Date'),
        openapi.Parameter('invoiceType', openapi.IN_QUERY, type=openapi.TYPE_ARRAY, items=openapi.Items(
            type=openapi.TYPE_INTEGER), description=""" Fiş türü"""),
        openapi.Parameter('prefix', openapi.IN_QUERY, type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description="""Fatura özel kod """)])
    def get(self, request, format=None):
        from django.db import connections
        from erp.models.friendly import (
            Stline, Orfiche
        )
        erp = connections['erp'].cursor()
        system = connections['system'].cursor()

        from datetime import datetime
        start = request.query_params.get('start')
        end = request.query_params.get('end')
        invoice_type = request.query_params.get('invoiceType')
        prefix = request.query_params.get('prefix')
        start_date = datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.strptime(end, '%Y-%m-%d')
        invoice_table = Invoice._meta.db_table
        stline_table = Stline._meta.db_table
        orfiche_table = Orfiche._meta.db_table

        sql: str = f"""
            SELECT INV.FICHENO 'invoice_no',
                   ORF.FICHENO 'order_no',
                   CONVERT(NVARCHAR(10), INV.DATE_, 120)  'date_field',
                   INV.SPECODE 'prefix'
                FROM {invoice_table} INV
                         LEFT JOIN {stline_table} STL ON INV.LOGICALREF = STL.INVOICEREF
                         LEFT JOIN {orfiche_table} ORF ON STL.ORDFICHEREF = ORF.LOGICALREF
                WHERE STL.INVOICEREF > 0
                  AND INV.CANCELLED = 0
                  AND INV.ESTATUS = 10
                  AND  INV.DATE_  BETWEEN %s AND %s
                
        """
        if invoice_type:
            sql += f" AND INV.TRCODE = {invoice_type}"

        if prefix:
            sql += f" AND INV.SPECODE = {prefix}"

        sql += "GROUP BY INV.FICHENO, ORF.FICHENO, INV.DATE_,INV.SPECODE;"
        with erp as cursor:
            cursor.execute(sql, (start_date, end_date))
            result = cursor.fetchall()

        serializer = InvoiceReadSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetValidateGIBUserView(Bti, APIView):

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('vkn', openapi.IN_QUERY, type=openapi.TYPE_STRING, description='VKN', required=True)])
    def get(self, request):
        vkn = request.query_params.get('vkn')

        elogo = Elogo(
            Active.settings['ELOGO_USER'],
            Active.settings['ELOGO_PWD']
        )

        try:
            elogo.login()
            gib_data = elogo.gibUserInfo(vkn)
            users = elogo.checkGibUser(vkn=vkn)
            print("******gib", gib_data)

        except Exception as e:
            return Response({'error': str(e)})
        finally:
            elogo.logout()

        labels = []

        if gib_data:
            for i in gib_data['outputList']['string']:
                new_str = ""

                if i.startswith("EINVOICEPKALIAS="):
                    new_str += f"postLabel={i.split('=')[1]}"

                elif i.startswith("EDESPATCHPKALIAS="):
                    new_str += f"postLabelDesp={i.split('=')[1]}"

                elif i.startswith("EINVOICEGBALIAS="):
                    new_str += f"senderLabel={i.split('=')[1]}"

                elif i.startswith("EDESPATCHGBALIAS="):
                    new_str += f"senderLabelDesp={i.split('=')[1]}"
                else:
                    new_str += i

                labels.append(new_str),
            # print("*-*-*",labels)
            result = {}

            for item in labels:
                key, value = item.split('=')
                if key in result:
                    if isinstance(result[key], list):
                        result[key].append(value)
                    else:
                        result[key] = [result[key], value]
                else:
                    result[key] = value

            if users is not None:

                if 'userList' in users and 'Title' in users['userList']:
                    title = users['userList']['Title']
                else:
                    title = ""
                response = {
                    "isGibUser": result['ISGIBUSER'],
                    "title": title,
                    "userType": users['userList'].get('Type'),
                    "labels": result
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response({"message": "Vkn bulunamadı"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "Vkn bulunamadı"}, status=status.HTTP_404_NOT_FOUND)


class ReturnInvoicesView(Bti, generics.GenericAPIView):
    serializer_class = ReturnInvoiceSerializer

    def post(self, request, format=None):

        idata = ReturnInvoiceSerializer(data=request.data)
        idata.is_valid(raise_exception=True)
        data = idata.data
        lines = data.get("Lines")

        def validate_invoice(data):
            result = []
            for line in lines:
                if line.get("ret_cost_type") is None and line.get("source_reference") is not None:
                    result.append(True)
                elif line.get('ret_cost_type') == 1 and line.get("source_reference") is None:
                    result.append(True)
                elif line.get('ret_cost_type') == 2 and line.get("rest_cost") is not None:
                    result.append(True)
                else:
                    result.append(False)
            return all(result)

        check_inv = validate_invoice(lines)
        if check_inv:
            object = InvoiceTrack.create_return_invoice(data)
            if object and object.flow.success and object.flow.internal_ref:
                return Response({
                    'status': True,
                    'description': 'Fatura başarıyla eklendi!',
                    'logical_ref': object.flow.internal_ref,
                    'pid': object.flow.pid,
                    'flow': object.flow.id
                })

            return Response({
                'status': False,
                'description': 'Fatura aktarılamadı!',
                'pid': object.flow.pid,
                'flow': object.flow.id
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "1 -) Giriş/Çıkış Maliyeti -> ret_cost_type gönderilmemeli ve source_reference gönderilmeli 2-)  Güncel Maliyet -> ret_cost_type = 1 olmalı ve ret_cost ile source_reference gönderilmemeli  3-) İade Maliyeti -> ret_cost_type = 2 olmalı ve ret_cost 'iade miktarı' belirtilmeli "}, status=status.HTTP_400_BAD_REQUEST)
