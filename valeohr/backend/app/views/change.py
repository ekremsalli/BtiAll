import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from drf_yasg.utils import swagger_auto_schema

from common.views import Bti
from common.permissions import IsAdminOrChangeEditPermission
from app.models import Transactions, Changes, Anomalies
from app.models.base import DB
from app.serializers.change import ChangeSerializer, ChangeDetailSerializer, AnomalySerializer
from app.serializers.transaction import TransactionSerializer


class ForApprove(Bti, generics.ListAPIView):
    permission_classes = (IsAdminOrChangeEditPermission,)
    pagination_class = None
    queryset = Changes.waiting_for_approve.select_related(
        'source_db',
        'employee',
        'employee__source_db',
        'transaction',
        'anomaly',
        'created_by'
    ).all()
    serializer_class = ChangeDetailSerializer


class ForSend(Bti, generics.ListAPIView):
    permission_classes = (IsAdminOrChangeEditPermission,)
    pagination_class = None
    queryset = Changes.waiting_for_send.select_related(
        'source_db',
        'employee',
        'employee__source_db',
        'transaction',
        'anomaly',
        'created_by',
        'modified_by'
    ).all()
    serializer_class = ChangeDetailSerializer


class ChangeBulkSendView(Bti, generics.GenericAPIView):
    def patch(self, request, *args, **kwargs):
        from datetime import datetime
        items = request.data.get('items')
        op = request.data.get('op')
        exps, errors, success = [], [], []

        for item in items:
            try:
                instance = Changes.objects.get(pk=item)
                check = instance.send()
            except Exception as e:
                print(e)
                exps.append(str(e))
            else:
                if check:
                    instance.verify_status = op
                    instance.sent_by = request.user
                    instance.sent_on = datetime.now()
                    instance.save()
                    success.append(instance.pk)
                else:
                    errors.append(instance.pk)

        return Response({
            'exps': len(exps),
            'errors': len(errors),
            'success': len(success)
        })


class ChangeSendView(Bti, generics.RetrieveUpdateAPIView):
    queryset = Changes.waiting_for_send.all()
    lookup_url_kwarg = 'pk'
    serializer_class = ChangeDetailSerializer

    def update(self, request, *args, **kwargs):
        from datetime import datetime
        instance = self.get_object()
        try:
            check = instance.send()
        except Exception as e:
            raise APIException({
                'custom': True,
                'message': str(e)
            })

        else:

            if check:
                instance.sent_by = request.user
                instance.sent_on = datetime.now()
                instance.save()
                partial = kwargs.pop('partial', False)
                serializer = self.get_serializer(
                    instance, data=request.data, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(serializer.data)
            else:
                return Response({
                    'custom': True,
                    'message': 'ilgili kullanıcıya ait bu tarihe birden fazla izin girilemez ...'
                }, status=status.HTTP_400_BAD_REQUEST)


class ChangeBulkEditView(Bti, generics.GenericAPIView):

    def delete(self, request, *args, **kwargs):
        items = request.data.get('items')
        if items:
            try:
                Changes.objects.filter(
                    id__in=items
                ).delete()
            except Exception as e:
                raise APIException(e)
            else:
                return Response({})
        else:
            raise APIException({
                'custom': True,
                'message': 'Geçersiz istek!'
            })

    def patch(self, request, *args, **kwargs):
        from datetime import datetime
        items = request.data.get('items')
        op = request.data.get('op')
        if items and op:
            try:
                Changes.objects.filter(
                    id__in=items
                ).update(
                    modified_by=request.user,
                    modified_on=datetime.now(),
                    verify_status=op
                )
            except Exception as e:
                raise APIException(e)
            else:
                return Response({})
        else:
            raise APIException({
                'custom': True,
                'message': 'Geçersiz istek!'
            })


class ChangeEditView(Bti, generics.RetrieveUpdateDestroyAPIView):
    queryset = Changes.objects.all()
    lookup_url_kwarg = 'pk'
    serializer_class = ChangeDetailSerializer

    def update(self, request, *args, **kwargs):
        from datetime import datetime
        instance = self.get_object()
        instance.modified_by = request.user
        instance.modified_on = datetime.now()
        instance.save()
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class ChangeView(Bti, APIView):

    def anomaly(self, request, data):
        anomaly = Anomalies.objects.filter(pk=data.get('id')).first()
        if anomaly is None:
            raise APIException({
                'custom': True,
                'message': 'Geçersiz anormallik!'
            })

        updates = {
            'tr_date': data.get('tr_date'),
            'work_time': data.get('work_time'),
            'start': data.get('start'),
            'end': data.get('end'),
            'time_type': data.get('time_type'),
            'excuse_type': data.get('excuse_type'),
            'day_model': data.get('day_model'),
            'excuse_day': data.get('excuse_day'),
            'account': data.get('account'),
            'pay_type': data.get('pay_type')
        }
        snapshot = {}
        can_insert = Changes.objects.filter(
            geco_anomaly_id=anomaly.geco_id,
            verify_status__in=[0, 1]).count() == 0
        if can_insert is False:
            raise APIException({
                'custom': True,
                'message': 'Bu anormallik için onay bekleyen veya gönderilmeyen kayıt mevcut!'
            })

        try:
            Changes.objects.create(
                source_db=anomaly.source_db,
                geco_anomaly_id=anomaly.geco_id,
                geco_time=anomaly.geco_time,
                description=data.get('description'),
                snapshot=json.dumps(snapshot, cls=DjangoJSONEncoder),
                updates=json.dumps(updates, cls=DjangoJSONEncoder),
                anomaly=anomaly,
                tr_date=anomaly.tr_date,
                employee=anomaly.employee,
                created_by=request.user
            )
        except Exception as e:
            raise APIException({
                'custom': True,
                'message': e
            })
        else:
            return Response({
                'status': True
            })

    def transaction(self, request, data):
        if 'transaction_id' in data:
            id = data.get('transaction_id')
        else:
            id = data.get('id')

        tr = Transactions.objects.filter(pk=id).first()
        if tr is None:
            raise APIException({
                'custom': True,
                'message': 'Geçersiz personel hareketi!'
            })

        updates = {
            'tr_date': data.get('tr_date'),
            'work_time': data.get('work_time'),
            'start': data.get('start'),
            'end': data.get('end'),
            'time_type': data.get('time_type'),
            'excuse_type': data.get('excuse_type'),
            'day_model': data.get('day_model'),
            'excuse_day': data.get('excuse_day'),
            'account': data.get('account'),
            'pay_type': data.get('pay_type')
        }
        snapshot = {
            'tr_date': tr.tr_date.strftime('%Y-%m-%d') if tr.tr_date else None,
            'work_time': tr.work_time,
            'start': tr.start.strftime('%H:%M') if tr.start else '',
            'end': tr.end.strftime('%H:%M') if tr.end else '',
            'time_type': tr.time_type,
            'excuse_type': tr.excuse_type,
            'day_model': tr.day_model,
            'excuse_day': tr.excuse_day,
            'account': tr.account,
            'pay_type': tr.pay_type
        }
        if data.get('is_remove_request') is False and updates == snapshot:
            raise APIException({
                'custom': True,
                'message': 'Hiç bir güncelleme yapmadınız!'
            })

        can_update = Changes.objects.filter(
            geco_id=tr.geco_id,
            verify_status__in=[0, 1]).count() == 0
        if can_update is False:
            raise APIException({
                'custom': True,
                'message': 'Bu hareket için onay bekleyen veya gönderilmeyen kayıt mevcut!'
            })

        try:
            Changes.objects.create(
                source_db=tr.source_db,
                geco_id=tr.geco_id,
                geco_time=tr.geco_time,
                description=data.get('description'),
                snapshot=json.dumps(snapshot, cls=DjangoJSONEncoder),
                updates=json.dumps(updates, cls=DjangoJSONEncoder),
                is_remove_request=data.get('is_remove_request'),
                transaction=tr,
                employee=tr.employee,
                tr_date=tr.tr_date,
                created_by=request.user
            )
        except Exception as e:
            raise APIException({
                'custom': True,
                'message': e
            })
        else:
            return Response({
                'status': True
            })

    def annual_off(self, request, data):
        from datetime import datetime
        if 'employee' not in data:
            raise APIException({
                'custom': True,
                'message': 'Personel zorunludur!'
            })

        if 'excuse_type' not in data:
            raise APIException({
                'custom': True,
                'message': 'İzin tipi zorunludur!'
            })

        try:
            start = datetime.strptime(data.get('start'), '%Y-%m-%d')
        except Exception as e:
            raise e

        try:
            end = datetime.strptime(data.get('end'), '%Y-%m-%d')
        except Exception as e:
            raise e

        db = DB.get_db(data.get('db'))

        record = {
            'description': data.get('description'),
            'snapshot': None,
            'updates': None,
            'is_annual_off': True,
            'employee_id': data.get('employee'),
            'start_annual': start,
            'end_annual': end,
            'source_db': db,
            'created_by': request.user,
            'start_annual_type': data.get('start_annual_type'),
            'end_annual_type': data.get('end_annual_type'),
            'annual_excuse_type': data.get('excuse_type')
        }
        try:
            Changes.objects.create(**record)
        except Exception as e:
            print(e)
            raise APIException({
                'custom': True,
                'message': e
            })
        else:
            return Response({
                'status': True
            })

    def post(self, request, format=None):
        data = request.data
        if 'ano_type' in data:
            return self.anomaly(request, data)
        elif 'annual_off' in data:
            return self.annual_off(request, data)
        else:
            return self.transaction(request, data)


class CheckTransaction(Bti, APIView):
    def get(self, request, format=None):
        geco_id = request.query_params.get('geco_id', None)
        if geco_id is None:
            raise APIException({
                'custom': True,
                'message': 'Geçersiz personel hareketi!'
            })

        t1 = Changes.objects.filter(
            geco_id=geco_id,
            verify_status__in=[0, 1]).count() == 0
        t2 = Changes.objects.filter(
            geco_id=geco_id,
            verify_status__gt=0,
            is_remove_request=True).count() == 0
        can_update = t1 and t2

        history = Changes.objects.filter(geco_id=geco_id)
        serializer = ChangeSerializer(history, many=True)
        return Response({
            'can_update': can_update,
            'history': serializer.data,
            'geco_id': geco_id,
            'is_removed': not t2
        })


class CheckAnomaly(Bti, APIView):
    def get(self, request, format=None):
        geco_anomaly_id = request.query_params.get('geco_anomaly_id', None)
        if geco_anomaly_id is None:
            raise APIException({
                'custom': True,
                'message': 'Geçersiz anormallik!'
            })

        can_insert = Changes.objects.filter(
            geco_anomaly_id=geco_anomaly_id,
            verify_status__in=[0, 1]).count() == 0

        anomaly = Anomalies.objects.filter(geco_id=geco_anomaly_id).first()
        from geco.models import Ttagmos
        day_model = None
        tagmos = Ttagmos.objects.using(anomaly.source_db.code).filter(
            tms_persnr=anomaly.employee.nr,
            tms_datum__date=anomaly.tr_date
        ).first()
        if tagmos and tagmos.tms_tagmod:
            day_model = tagmos.tms_tagmod

        transactions = Transactions.objects.filter(
            source_db=anomaly.source_db,
            employee=anomaly.employee,
            tr_date=anomaly.tr_date
        ).all()
        if transactions:
            tr_data = TransactionSerializer(transactions, many=True).data
        else:
            tr_data = []

        # other anomalies for same day
        anomalies = Anomalies.objects.filter(
            source_db=anomaly.source_db,
            employee=anomaly.employee,
            tr_date=anomaly.tr_date
        ).exclude(pk=anomaly.id)

        return Response({
            'can_update': can_insert,
            'anomaly_id': geco_anomaly_id,
            'day_model': day_model,
            'transactions': tr_data,
            'employee': anomaly.employee.id,
            'anomalies': AnomalySerializer(anomalies, many=True).data
        })
