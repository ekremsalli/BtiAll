import json
from django.conf import settings

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from bti.views.base import Bti, Pagination
from erp.active import Active
from third_party.idea.api import Idea
from third_party.bazaars.trendyol import Trendyol

from app.serializers import *
from app.models import *


class TrendyolUnsuppliedStatus(Bti, APIView):
    @swagger_auto_schema(
        request_body=TrendyolUnsuppliedStatusSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def put(self, request, format=None):
        status = TrendyolUnsuppliedStatusSerializer(data=request.data)
        status.is_valid(raise_exception=True)
        data = status.data
        sett = Active.settings['TRENDYOL']
        trendyol = Trendyol(**sett)
        log = TrendyolLog.objects.filter(order_number=data.get('id')).first()
        if log is None:
            raise APIException('Geçersiz sipariş!')

        tdata = json.loads(log.raw)
        try:
            clines = [{
                'lineId': line.get('line'),
                'quantity': line.get('quantity')} for line in data.get('lines')]

            result = trendyol.set_unsupplied(
                tdata.get('id'),
                clines
            )
        except Exception as e:
            tsl = TrendyolStatusLog(
                trendyol=log,
                order_id=data.get('id'),
                status='unsupplied',
                request=json.dumps(data),
                exception=str(e)
            )
            tsl.save()
            return Response({
                'status': False,
                'description': f'Bilinmeyen bir hata oluştu! {str(e)}',
                'lid': tsl.pk
            })
        else:
            tsl = TrendyolStatusLog(
                trendyol=log,
                order_id=data.get('id'),
                status='unsupplied',
                request=json.dumps(data),
                response=json.dumps({
                    'status_code': result.status_code,
                    'response': result.text
                })
            )
            tsl.save()
            if result.status_code == 200:
                return Response({
                    'status': True,
                    'description': f'Statu[UnSupplied] Trendyol\'a bildirildi!',
                    'lid': tsl.pk
                })
            else:
                return Response({
                    'status': False,
                    'description': f'Bir hata oluştu!',
                    'lid': tsl.pk
                })


class TrendyolInvoicedStatus(Bti, APIView):
    @swagger_auto_schema(
        request_body=TrendyolInvoiceStatusSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def put(self, request, format=None):
        status = TrendyolInvoiceStatusSerializer(data=request.data)
        status.is_valid(raise_exception=True)
        data = status.data
        sett = Active.settings['TRENDYOL']
        trendyol = Trendyol(**sett)
        log = TrendyolLog.objects.filter(order_number=data.get('id')).first()
        if log is None:
            raise APIException('Geçersiz sipariş!')
        tdata = json.loads(log.raw)
        try:
            clines = [{
                'lineId': line.get('line'),
                'quantity': line.get('quantity')} for line in data.get('lines')]

            result = trendyol.set_invoiced(
                tdata.get('id'),
                data.get('invoice_number'),
                clines
            )
        except Exception as e:
            tsl = TrendyolStatusLog(
                trendyol=log,
                order_id=data.get('id'),
                invoice=data.get('invoice_number'),
                status='invoiced',
                request=json.dumps(data),
                exception=str(e)
            )
            tsl.save()
            return Response({
                'status': False,
                'description': f'Bilinmeyen bir hata oluştu! {str(e)}',
                'lid': tsl.pk
            })
        else:
            tsl = TrendyolStatusLog(
                trendyol=log,
                order_id=data.get('id'),
                invoice=data.get('invoice_number'),
                status='invoiced',
                request=json.dumps(data),
                response=json.dumps({
                    'status_code': result.status_code,
                    'response': result.text
                })
            )
            tsl.save()
            if result.status_code == 200:
                return Response({
                    'status': True,
                    'description': f'Statu[Invoiced] Trendyol\'a bildirildi!',
                    'lid': tsl.pk
                })
            else:
                return Response({
                    'status': False,
                    'description': f'Bir hata oluştu!',
                    'lid': tsl.pk
                })


class TrendyolCargo(Bti, APIView):
    @swagger_auto_schema(
        request_body=TrendyolCargoSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def put(self, request, format=None):
        status = TrendyolCargoSerializer(data=request.data)
        status.is_valid(raise_exception=True)
        data = status.data
        sett = Active.settings['TRENDYOL']
        trendyol = Trendyol(**sett)
        log = TrendyolLog.objects.filter(order_number=data.get('id')).first()
        if log is None:
            raise APIException('Geçersiz sipariş!')
        tdata = json.loads(log.raw)
        try:
            result = trendyol.set_cargo_number(
                tdata.get('id'),
                data.get('url')
            )
        except Exception as e:
            tsl = TrendyolStatusLog(
                trendyol=log,
                order_id=data.get('id'),
                status='cargo',
                request=json.dumps(data),
                exception=str(e)
            )
            tsl.save()
            return Response({
                'status': False,
                'description': f'Bilinmeyen bir hata oluştu! {str(e)}',
                'lid': tsl.pk
            })
        else:
            tsl = TrendyolStatusLog(
                trendyol=log,
                order_id=data.get('id'),
                status='cargo',
                request=json.dumps(data),
                response=json.dumps({
                    'status_code': result.status_code,
                    'response': result.text
                })
            )
            tsl.save()
            if result.status_code == 200:
                return Response({
                    'status': True,
                    'description': f'Kargo takibi Trendyol\'a bildirildi!',
                    'lid': tsl.pk
                })
            else:
                return Response({
                    'status': False,
                    'description': f'Bir hata oluştu!',
                    'lid': tsl.pk
                })


class TrendyolPickingStatus(Bti, APIView):
    @swagger_auto_schema(
        request_body=TrendyolPickingStatusSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def put(self, request, format=None):
        status = TrendyolPickingStatusSerializer(data=request.data)
        status.is_valid(raise_exception=True)
        data = status.data
        sett = Active.settings['TRENDYOL']
        trendyol = Trendyol(**sett)
        log = TrendyolLog.objects.filter(order_number=data.get('id')).first()
        if log is None:
            raise APIException('Geçersiz sipariş!')
        tdata = json.loads(log.raw)
        try:
            clines = [{
                'lineId': line.get('line'),
                'quantity': line.get('quantity')} for line in data.get('lines')]

            result = trendyol.set_picking(
                tdata.get('id'),
                clines
            )
        except Exception as e:
            tsl = TrendyolStatusLog(
                trendyol=log,
                order_id=data.get('id'),
                status='picking',
                request=json.dumps(data),
                exception=str(e)
            )
            tsl.save()
            return Response({
                'status': False,
                'description': f'Bilinmeyen bir hata oluştu! {str(e)}',
                'lid': tsl.pk
            })
        else:

            tsl = TrendyolStatusLog(
                trendyol=log,
                order_id=data.get('id'),
                status='picking',
                request=json.dumps(data),
                response=json.dumps({
                    'status_code': result.status_code,
                    'response': result.text
                })
            )
            tsl.save()
            if result.status_code == 200:
                return Response({
                    'status': True,
                    'description': f'Statu[Picking] Trendyol\'a bildirildi!',
                    'lid': tsl.pk
                })
            else:
                return Response({
                    'status': False,
                    'description': f'Bir hata oluştu!',
                    'lid': tsl.pk
                })

class IdeaStock(Bti, APIView):
    @swagger_auto_schema(
        request_body=IdeaStockSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def put(self, request, format=None):
        order = IdeaStockSerializer(data=request.data)
        order.is_valid(raise_exception=True)
        data = order.data

        try:
            idea = Idea(Active.settings['IDEA']['URL'])
            idea.read_token_from_ini(Active.settings['IDEA']['TOKEN_PATH'])
        except Exception as e:
            raise Exception('Token dosyası okunamadı!')
        else:
            try:
                resp = idea.update_order(data.get('order'), {
                    'stockAmount': data.get('stock_amount'),
                })
            except Exception as e:
                il = IdeaStockLog(
                    order=data.get('order'),
                    stock_amount=data.get('stock_amount'),
                    request=str(idea.last_request.request.__dict__),
                    response=str(idea.last_request),
                    exception=str(e)
                )
                il.save()
                return Response({
                    'status': False,
                    'description': f'Bilinmeyen bir hata oluştu! {str(e)}',
                    'lid': il.pk
                })
            else:
                il = IdeaStockLog(
                    order=data.get('order'),
                    stock_amount=data.get('stock_amount'),
                    request=str(idea.last_request.request.__dict__),
                    response=json.dumps(resp)
                )
                il.save()
                return Response({
                    'status': True,
                    'description': f'Başarıyla güncellendi!',
                    'lid': il.pk
                })




class IdeaCargo(Bti, APIView):
    @swagger_auto_schema(
        request_body=IdeaCargoSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def put(self, request, format=None):
        order = IdeaCargoSerializer(data=request.data)
        order.is_valid(raise_exception=True)
        data = order.data

        try:
            idea = Idea(Active.settings['IDEA']['URL'])
            idea.read_token_from_ini(Active.settings['IDEA']['TOKEN_PATH'])
        except Exception as e:
            raise Exception('Token dosyası okunamadı!')
        else:
            try:
                resp = idea.update_order(data.get('order'), {
                    'shippingProviderCode': data.get('provider_code'),
                    'shippingCompanyName': data.get('company_name'),
                    'shippingPaymentType': data.get('payment_type'),
                    'shippingTrackingCode': data.get('tracking_code')
                })
            except Exception as e:
                il = IdeaCargoLog(
                    order=data.get('order'),
                    data=json.dumps(data),
                    request=str(idea.last_request.request.__dict__),
                    response=str(idea.last_request),
                    exception=str(e)
                )
                il.save()
                return Response({
                    'status': False,
                    'description': f'Bilinmeyen bir hata oluştu! {str(e)}',
                    'lid': il.pk
                })
            else:
                il = IdeaCargoLog(
                    order=data.get('order'),
                    data=json.dumps(data),
                    request=str(idea.last_request.request.__dict__),
                    response=json.dumps(resp)
                )
                il.save()
                return Response({
                    'status': True,
                    'description': f'Başarıyla güncellendi!',
                    'lid': il.pk
                })


class IdeaOrder(Bti, APIView):
    @swagger_auto_schema(
        request_body=IdeaStatusSerializer,
        responses={
            200: 'status: true/false'
        }
    )
    def put(self, request, format=None):
        order = IdeaStatusSerializer(data=request.data)
        order.is_valid(raise_exception=True)
        data = order.data
        try:
            idea = Idea(Active.settings['IDEA']['URL'])
            idea.read_token_from_ini(Active.settings['IDEA']['TOKEN_PATH'])
        except Exception as e:
            raise Exception('Token dosyası okunamadı!')
        else:
            try:
                resp = idea.update_order(data.get('order'), {
                    'status': data.get('status')
                })
            except Exception as e:
                il = IdeaLog(
                    order=data.get('order'),
                    status=data.get('status'),
                    request=str(idea.last_request.request.__dict__),
                    response=str(idea.last_request),
                    exception=str(e)
                )
                il.save()
                return Response({
                    'status': False,
                    'description': f'Bilinmeyen bir hata oluştu! {str(e)}',
                    'lid': il.pk
                })
            else:
                il = IdeaLog(
                    order=data.get('order'),
                    status=data.get('status'),
                    request=str(idea.last_request.request.__dict__),
                    response=json.dumps(resp)
                )
                il.save()
                return Response({
                    'status': True,
                    'description': f'Başarıyla güncellendi!',
                    'lid': il.pk
                })
