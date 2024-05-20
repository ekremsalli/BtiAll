from django.conf import settings

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


from bti.views.base import Bti, Pagination

from erp.active import Active

from app.serializers import ArpCardSerializer, InvSerializer, Lines
from app.models import P_CLCARD, InvoiceTrack

class SalesInvoice(APIView):
    @swagger_auto_schema(
        request_body=InvSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def post(self, request, format=None):
        invoice = InvSerializer(data=request.data)
        invoice.is_valid(raise_exception=True)
        data = invoice.data
        check = InvoiceTrack.control({
            'firm': Active.name,
            'identifier': data.get('OrderKey')
        })
        if check:
            return Response(check.in_track(
                f'Bu fatura {check.fmt_created} tarihinde kayıt olmuş.'
            ), status=status.HTTP_208_ALREADY_REPORTED)

        invoice = InvoiceTrack.create_invoice(data, request.data)
        if invoice and invoice.flow.success and invoice.flow.internal_ref:
            return Response({
                'status': True,
                'message': 'Fatura başarıyla kaydedildi!',
                'LOGICALREF': invoice.flow.internal_ref,
                'flow': invoice.flow.pid
            })
        else:
            return Response({
                'status': False,
                'message': 'Fatura aktarılamadı!',
                'flow': invoice.flow.pid if invoice.flow else None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, format=None, id=None):
        if id is not None:
            InvoiceTrack.delete_invoice(id)
        else:
            return
            
            

class ArpCard(APIView):
    @swagger_auto_schema(
        request_body=ArpCardSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def post(self, request, format=None, id=None):
        if id is None:
            identity = self.request.query_params.get('id', None)
        else:
            identity = id

        card = ArpCardSerializer(data=request.data)
        card.is_valid(raise_exception=True)
        data = card.data
        if identity:
            obj = P_CLCARD.do_update(data, identity)
            if obj and obj.flow.success:
                return Response({
                    'status': True,
                    'message': 'Cari Kart Güncellendi',
                    'LOGICALREF': obj.flow.internal_ref,
                    'flow': obj.flow.pid
                })
            else:
                return Response({
                    'status': False,
                    'message': 'Bir hata oluştu!',
                    'LOGICALREF': -1,
                    'flow': None
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
           # target_db = P_CLCARD._meta.target_db
           # client_taxnumber = request.data['client_taxnumber']
            #if len(client_taxnumber) == 11:
             #   check_tckno = P_CLCARD.objects.using(target_db).filter(tckno=client_taxnumber).count()
              #  if check_tckno > 0:
               #     return Response({
                #    'status': False,
                 #   'message': f'Aynı TCKNO ya ({client_taxnumber}) sahip birden fazla cari kard oluşturulamaz ',
                  #  'LOGICALREF': -1,
                   # 'flow': None
                #}, status=status.HTTP_400_BAD_REQUEST)

           # else:
            #    check_tckno = P_CLCARD.objects.using(target_db).filter(taxnr=client_taxnumber).count()
            #    if check_tckno > 0:
            #      return Response({
            #         'status': False,
            #        'message': f'Aynı TAXNR ya ({client_taxnumber}) sahip birden fazla cari kard oluşturulamaz ',
            #       'LOGICALREF': -1,
            #      'flow': None
            # }, status=status.HTTP_400_BAD_REQUEST)

            obj = P_CLCARD.do_create(data)
            if obj and obj.flow.success and obj.flow.internal_ref:
                return Response({
                    'status': True,
                    'message': 'Cari Kart TANIMLANDI',
                    'LOGICALREF': obj.flow.internal_ref,
                    'flow': obj.flow.pid
                })
            else:
                return Response({
                    'status': False,
                    'message': 'Bir hata oluştu!',
                    'flow': obj.flow.pid if obj.flow else None
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
