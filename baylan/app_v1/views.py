from datetime import datetime
import logging
import json
from string import Template

from django.db import connections
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from erp.active import Active
from erp.asking.orders import (
    PurchaseOrder,
    SalesOrder,
)
from erp.asking.material import (
    MaterialFiche,
)
from erp.models.friendly import (
    Orfiche,
    Items,
    Itmunita,
    Stfiche,
    Invoice,
    Emcenter,
    Emuhacc,
    Payplans,
)

from common.utils import (
    convert_dict_to_sql_where_clause,
    dict_fetch_all,
    remove_empty_from_dict,
)
from .converters import (
    WantageConverter,
    WantageItemConverter,
    WantageItemConsumedConverter,
    TransferConverter,
    TransferLineConverter,
)
from .models import (
    PurchaseOrderQue,
    PurchaseDispatchQue,
    ExpanseQue,
    RefundQue,
    TransferQue,
    Other,
    CommonQue,
    SlipQue
)
from .serializers import (
    OrderCancellableSerializer,
    WantageSerializer,
    InvoiceSerializer,
    EmcenterSerializer,
    AccountCodeSerializer,
    PayplanSerializer,
)

logger = logging.getLogger("app")


class OrderView(APIView):
    def get(self, request, **kwargs):
        params = request.GET.get('param', '').split('-')
        filters = {}
        if params and len(params) and params[0]:
            filters['CLC.CODE'] = f'T.İ.{params[0]}'
        if params and len(params) > 1 and params[1]:
            filters['ORF.BRANCH'] = params[1]

        if 'param' in kwargs and kwargs.get('param'):
            params = kwargs.get('param', '').split('-')
            if params and len(params) and params[0]:
                filters['CLC.CODE'] = f'T.İ.{params[0]}'

            if params and len(params) > 1 and params[1]:
                filters['ORF.BRANCH'] = params[1]

        with open('app_v1/resources/purchase_order.sql', 'r', encoding='utf-8') as fp:
            where = ''
            if convert_dict_to_sql_where_clause(filters):
                where = 'AND {}'.format(convert_dict_to_sql_where_clause(filters))

            template = Template(fp.read())
            query = template.substitute(
                NS=Active.namespace,
                PER=Active.period,
                WHERE=where
            )
            with connections['erp'].cursor() as cursor:
                cursor.execute(query)
                results = dict_fetch_all(cursor)

                return Response({
                    'serviceName': 'purchaseorder',
                    'data': results
                })

    def post(self, request):
        logger.info('Order post: ' + json.dumps(request.data))

        data = request.data

        if data.get('type') == 'add':
            identifier = PurchaseOrderQue.generate_identifier(data.get('data'))

            check = PurchaseOrderQue.control({
                'firm': Active.name,
                'identifier': identifier
            })
            if check:
                return Response(check.in_que(
                    f'Bu istek {check.fmt_created} tarihinde kayıt olmuş.'
                ), status=status.HTTP_208_ALREADY_REPORTED)

            feed = remove_empty_from_dict(data.get('data'))
            PurchaseOrderQue.validate(feed)
            data.update({'data': feed})

            item = PurchaseOrderQue.create_request(
                identifier,
                data
            )
            if item:
                return Response({
                    'status': True,
                    'message': 'Satınalma siparişi başarıyla kuyruğa alındı!',
                    'LOGICALREF': item.id
                })
            return Response({
                'status': False,
                'message': 'İstek alınamadı!'
            })
        elif data.get('type') == 'salesOrder':
            request = Active.settings['DEFAULT_SALES_ORDER'].copy()
            feed = remove_empty_from_dict(data.get('data'))
            request.update(feed)

            so = SalesOrder(
                data=request
            )
            so.is_valid(raise_exception=True)
            so.transfer_via_rest()

            check = all([
                so.flow,
                so.flow.success,
                so.flow.internal_ref
            ])
            if check:
                return Response({
                    'status': True,
                    'message': 'Satış siparişi başarıyla oluşturuldu!',
                    'LOGICALREF': so.flow.internal_ref,
                    'flow': so.flow.pid
                })
            else:
                return Response({
                    'status': False,
                    'message': 'Satış siparişi oluşturulamadı!',
                    'flow': so.flow.pid
                })
        elif data.get('type') == 'cancelOrder':
            request = Active.settings['CANCEL_PURCHASE_ORDER'].copy()
            po = PurchaseOrder(
                data=request,
                partial=True
            )
            po.is_valid(raise_exception=True)
            po.partial_update(pk=data.get('LOGICALREF'))
            check = all([
                po.flow,
                po.flow.success,
                po.flow.internal_ref
            ])
            if check:
                return Response({
                    'status': True,
                    'message': 'Satınalma Siparişi İptal Edildi',
                    'flow': po.flow.pid
                })
            return Response({
                'status': False,
                'message': 'Satınalma Siparişi İptal Edilemedi',
                'flow': po.flow.pid
            })
        else:
            return Response({
                'status': False,
                'message': 'Type alanı boş olamaz!'
            }, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderCancellable(APIView):
    def get(self, request):
        items = Orfiche.objects.filter(cancelled=0)
        return Response({
            'serviceName': 'purchaseorder',
            'data': OrderCancellableSerializer(items, many=True).data
        })


class DispatchView(APIView):

    def post(self, request):
        logger.info('Dispatch post: ' + json.dumps(request.data))

        data = request.data

        if data.get('type') == 'add':
            identifier = PurchaseDispatchQue.generate_identifier(data.get('data'))

            check = PurchaseDispatchQue.control({
                'firm': Active.name,
                'identifier': identifier
            })
            if check:
                return Response(check.in_que(
                    f'Bu istek {check.fmt_created} tarihinde kayıt olmuş.'
                ), status=status.HTTP_208_ALREADY_REPORTED)

            feed = remove_empty_from_dict(data.get('data'))
            if 'DISPATCHES' not in feed:
                feed['DISPATCHES'] = []
            if 'PAYMENT_LIST' not in feed:
                feed['PAYMENT_LIST'] = []

            PurchaseDispatchQue.validate(feed)
            data.update({'data': feed})

            item = PurchaseDispatchQue.create_request(
                identifier,
                data
            )
            if item:
                return Response({
                    'status': True,
                    'message': 'Satınalma irsaliyesi başarıyla kuyruğa alındı!',
                    'LOGICALREF': item.id
                })
            return Response({
                'status': False,
                'message': 'İstek alınamadı!'
            })
        elif data.get('type') == 'expanse':
            identifier = ExpanseQue.generate_identifier(data.get('data'))

            check = ExpanseQue.control({
                'firm': Active.name,
                'identifier': identifier
            })
            if check:
                return Response(check.in_que(
                    f'Bu istek {check.fmt_created} tarihinde kayıt olmuş.'
                ), status=status.HTTP_208_ALREADY_REPORTED)

            feed = remove_empty_from_dict(data.get('data'))

            if 'DISPATCHES' not in feed:
                feed['DISPATCHES'] = {
                    'items': []
                }
            if 'PAYMENT_LIST' not in feed:
                feed['PAYMENT_LIST'] = {
                    'items': []
                }

            ExpanseQue.validate(feed)
            data.update({'data': feed})

            item = ExpanseQue.create_request(
                identifier,
                data
            )
            if item:
                return Response({
                    'status': True,
                    'message': 'Satınalma faturası başarıyla kuyruğa alındı!',
                    'LOGICALREF': item.id
                })
            return Response({
                'status': False,
                'message': 'İstek alınamadı!'
            })
        else:
            return Response({
                'status': False,
                'message': 'Type alanı boş olamaz!'
            }, status=status.HTTP_400_BAD_REQUEST)


class TransferRefundView(APIView):
    def post(self, request):
        logger.info('TransferRefund post: ' + json.dumps(request.data))

        data = request.data

        if data.get('type') == 'refund':
            identifier = RefundQue.generate_identifier(data.get('data'))

            check = RefundQue.control({
                'firm': Active.name,
                'identifier': identifier
            })
            if check:
                return Response(check.in_que(
                    f'Bu istek {check.fmt_created} tarihinde kayıt olmuş.'
                ), status=status.HTTP_208_ALREADY_REPORTED)

            feed = remove_empty_from_dict(data.get('data'))

            RefundQue.validate(feed)
            data.update({'data': feed})

            item = RefundQue.create_request(
                identifier,
                data
            )
            if item:
                return Response({
                    'status': True,
                    'message': 'İade fişi başarıyla kuyruğa alındı!',
                    'LOGICALREF': item.id
                })
            return Response({
                'status': False,
                'message': 'İstek alınamadı!'
            })
        else:
            identifier = TransferQue.generate_identifier(data.get('Data'))

            check = TransferQue.control({
                'firm': Active.name,
                'identifier': identifier
            })
            if check:
                return Response(check.in_que(
                    f'Bu istek {check.fmt_created} tarihinde kayıt olmuş.'
                ), status=status.HTTP_208_ALREADY_REPORTED)

            feed = remove_empty_from_dict(data.get('Data'))

            request = Active.settings['DEFAULT_TRANSFER'].copy()
            header = TransferConverter(
                feed,
                settings.MAPPING['TRANSFER']
            ).data

            items = []
            for item in feed.get('LINES'):
                reqline = Active.settings['DEFAULT_TRANSFER_LINE'].copy()
                line = TransferLineConverter(
                    item,
                    settings.MAPPING['TRANSFER_LINE']
                ).data
                reqline.update(line)
                items.append(reqline)

            request.update(header)
            request['TRANSACTIONS'] = {
                'items': items
            }

            TransferQue.validate(request)
            data.update({'data': request})

            item = TransferQue.create_request(
                identifier,
                data
            )
            if item:
                return Response({
                    'status': True,
                    'message': 'Transfer fişi başarıyla kuyruğa alındı!',
                    'LOGICALREF': item.id
                })
            return Response({
                'status': False,
                'message': 'İstek alınamadı!'
            })


class WantageView(APIView):
    def post(self, request):
        logger.info('Wantage post: ' + json.dumps(request.data))
        idata = WantageSerializer(data=request.data)
        idata.is_valid(raise_exception=True)
        data = idata.data

        request = Active.settings['DEFAULT_WANTAGE'].copy()
        header = WantageConverter(
            data,
            settings.MAPPING['WANTAGE']
        ).data

        request.update(header)
        uref = CommonQue.generate_identifier(data)
        reqlines = []

        for line in data.get('ITEMS'):
            is_prod = Other.production_items(line.get('UrunKod'))
            item = Items.objects.filter(code=line.get('UrunKod')).last()

            if is_prod is False:
                Other.call_consume_products(
                    item.pk,
                    item.pk,
                    line.get('Miktar'),
                    Active.number,
                    data.get('SUBE_KOD'),
                    5,
                    uref
                )
            else:
                temp = Active.settings['DEFAULT_WANTAGE_ITEM'].copy()
                temp_line = WantageItemConverter(
                    line,
                    settings.MAPPING['WANTAGE_ITEM']
                ).data
                temp.update(temp_line)
                temp.update({
                    'SOURCEINDEX': data.get('SUBE_KOD')
                })

                itmunita = Itmunita.objects.filter(itemref=item, linenr=1).first()
                if itmunita and itmunita.unitlineref and itmunita.unitlineref.code:
                    temp.update({
                        'UNIT_CODE': itmunita.unitlineref.code,
                        'UNIT_CONV1': 1,
                        'UNIT_CONV2': 1
                    })
                reqlines.append(temp)

        consumed = Other.get_consumed_products(
            branch=data.get('SUBE_KOD'),
            typ=5,
            ref=uref
        )
        waste = []

        for line in consumed:
            temp = Active.settings['DEFAULT_WANTAGE_ITEM'].copy()
            temp_line = WantageItemConsumedConverter(
                line,
                settings.MAPPING['WANTAGE_ITEM_CONSUMED']
            ).data
            temp.update(temp_line)
            temp.update({
                'SOURCEINDEX': data.get('SUBE_KOD'),
                'UNIT_CONV1': 1,
                'UNIT_CONV2': 1,
                'QUANTITY': line.get('QUANTITY')
            })

            reqlines.append(temp)

            if line.get('LOSTFACTOR') > 0:
                wasted = (line.get('LOSTFACTOR') / 100) * line.get('QUANTITY')
                if wasted:
                    wtemp = Active.settings['DEFAULT_WANTAGE_ITEM'].copy()
                    wtemp_line = WantageItemConsumedConverter(
                        line,
                        settings.MAPPING['WANTAGE_ITEM_CONSUMED']
                    ).data

                    wtemp.update(wtemp_line)
                    wtemp.update({
                        'SOURCEINDEX': data.get('SUBE_KOD'),
                        'UNIT_CONV1': 1,
                        'UNIT_CONV2': 1,
                        'QUANTITY': wasted
                    })
                    wasted.append(wtemp)

        request.update({
            'TRANSACTIONS': {'items': reqlines}
        })

        si = MaterialFiche(
            data=request
        )
        si.is_valid(raise_exception=True)
        si.transfer_via_rest()

        if si and si.flow and si.flow.is_success():
            cons_res = Stfiche.objects.get(pk=si.flow.internal_ref)

            if waste:
                request.update({
                    'TYPE': 23,
                    'TRANSACTIONS': {'items': waste} 
                })

                wi = MaterialFiche(
                    data=request,
                    prev_flow=si.flow
                )
                wi.is_valid(raise_exception=True)
                wi.transfer_via_rest()

                if wi and wi.flow and wi.flow.is_success():
                    wast_res = Stfiche.objects.get(pk=wi.flow.internal_ref)
                    return Response({
                        'consumption_ref': cons_res.pk,
                        'consumption_ficheno': cons_res.ficheno,
                        'consumption_result': True,
                        'consumption_desc': 'Başarı ile tamamlandı',
                        'waste_ref': wast_res.pk,
                        'waste_ficheno': wast_res.ficheno,
                        'waste_result': True,
                        'waste_desc': 'Başarı ile tamamlandı',
                    })
                else:
                    return Response({
                        'consumption_ref': cons_res.pk,
                        'consumption_ficheno': cons_res.ficheno,
                        'consumption_result': True,
                        'consumption_desc': 'Başarı ile tamamlandı',
                        'waste_ref': -1,
                        'waste_ficheno': -1,
                        'waste_result': False,
                        'waste_desc': wi.flow.exception if wi and wi.flow else '?'
                    })
            else:
                return Response({
                    'consumption_ref': cons_res.pk,
                    'consumption_ficheno': cons_res.ficheno,
                    'consumption_result': True,
                    'consumption_desc': 'Başarı ile tamamlandı',
                    'waste_ref': -1,
                    'waste_ficheno': -1,
                    'waste_result': True,
                    'waste_desc': -1
                })
        else:
            return Response({
                'consumption_ref': -1,
                'consumption_ficheno': -1,
                'consumption_result': False,
                'consumption_desc': si.flow.exception if si and si.flow else '?',
                'waste_ref': -1,
                'waste_ficheno': -1,
                'waste_result': False,
                'waste_desc': -1
            })


class InvoiceView(APIView):
    def get(self, request):
        items = Invoice.objects.filter()
        params = request.GET
        parse_day = lambda d: datetime.strptime(d, '%Y-%m-%d')

        if 'initDate' in params and params['initDate']:
            items = items.filter(
                date_field__gte=parse_day(params['initDate'])
            )

        if 'endDate' in params and params['endDate']:
            items = items.filter(
                date_field__lte=parse_day(params['endDate'])
            )

        return Response({
            'serviceName': 'invoice',
            'data': InvoiceSerializer(items, many=True).data
        })


class EmcenterView(APIView):
    def get(self, request, **kwargs):
        items = Emcenter.objects.all()
        params = request.GET
        if 'code' in params and params.get('code'):
            items = items.filter(code__startswith=params.get('code'))

        if 'code' in kwargs and kwargs.get('code'):
            items = items.filter(code__startswith=kwargs.get('code'))

        return Response({
            'serviceName': 'emcCenter',
            'data': EmcenterSerializer(items, many=True).data
        })


class ItemView(APIView):
    def get(self, request, **kwargs):
        params = request.GET
        filters = {}
        if 'code' in params and params.get('code', None):
            filters['CLC.CODE'] = params.get('code')
        if 'endDate' in params and params.get('endDate', None):
            filters['POF.POFFERENDDT'] = ('>=', params.get('endDate'))

        if 'code' in kwargs and kwargs.get('code'):
            filters['CLC.CODE'] = kwargs.get('code')

        if 'end_date' in kwargs and kwargs.get('end_date'):
            filters['POF.POFFERENDDT'] = ('>=', kwargs.get('end_date'))

        with open('app_v1/resources/items.sql', 'r', encoding='utf-8') as fp:
            where = ''
            if convert_dict_to_sql_where_clause(filters):
                where = 'AND {}'.format(convert_dict_to_sql_where_clause(filters))

            template = Template(fp.read())
            query = template.substitute(
                NS=Active.namespace,
                PER=Active.period,
                WHERE=where
            )
            with connections['erp'].cursor() as cursor:
                cursor.execute(query)
                results = dict_fetch_all(cursor)

                return Response({
                    'serviceName': 'items',
                    'data': results
                })


class ItemCodesView(APIView):
    def get(self, request, **kwargs):
        params = request.GET
        filters = {}
        if 'code' in params and params.get('code', None):
            filters['ITM.CODE'] = params.get('code')
        if 'active' in params:
            filters['ITM.ACTIVE'] = params.get('active')

        if 'code' in kwargs and kwargs.get('code'):
            filters['ITM.CODE'] = kwargs.get('code')

        if 'active' in kwargs and kwargs.get('active'):
            filters['ITM.ACTIVE'] = kwargs.get('active')

        with open('app_v1/resources/item_codes.sql', 'r', encoding='utf-8') as fp:
            where = ''
            if convert_dict_to_sql_where_clause(filters):
                where = 'AND {}'.format(convert_dict_to_sql_where_clause(filters))

            template = Template(fp.read())
            query = template.substitute(
                NS=Active.namespace,
                PER=Active.period,
                WHERE=where
            )
            with connections['erp'].cursor() as cursor:
                cursor.execute(query)
                results = dict_fetch_all(cursor)

                return Response({
                    'serviceName': 'itemsCodeList',
                    'data': results
                })


class AccountView(APIView):
    def get(self, request, **kwargs):
        items = Emuhacc.objects.filter(level_field__gt=1, active=0)

        params = request.GET
        if 'code' in params and params.get('code'):
            items = items.filter(code__startswith=params.get('code'))

        if 'code' in kwargs and kwargs.get('code'):
            items = items.filter(code__startswith=kwargs.get('code'))

        items = items.values('pk', 'code', 'definition_field')

        return Response({
            'serviceName': 'accountCode',
            'data': AccountCodeSerializer(items, many=True).data
        })


class PayPlanView(APIView):
    def get(self, request, **kwargs):
        items = Payplans.objects.exclude(code__startswith='X')

        params = request.GET
        if 'code' in params and params.get('code'):
            items = items.filter(code__startswith=params.get('code'))

        if 'code' in kwargs and kwargs.get('code'):
            items = items.filter(code__startswith=kwargs.get('code'))

        items = items.values('pk', 'code', 'definition_field')

        return Response({
            'serviceName': 'paymentPlans',
            'data': PayplanSerializer(items, many=True).data
        })


class ARPView(APIView):
    def get(self, request, **kwargs):
        filters = {}
        if 'kind' in kwargs and kwargs.get('kind'):
            kind = kwargs.get('kind')
            if kind == 'SUPPLIER':
                filters['CLC.CODE'] = (' LIKE ', 'T.İ%')
            elif kind == 'SHELL':
                filters['CLC.SPECODE3'] = 'SHELL'
            elif kind == 'YURTDISI':
                filters['CLC.SPECODE3'] = 'YURTDISI'
            else:
                filters['CLC.DEFINITION_'] = (' LIKE ', f'{kind}%')

        with open('app_v1/resources/arp.sql', 'r', encoding='utf-8') as fp:
            where = ''
            if convert_dict_to_sql_where_clause(filters):
                where = 'AND {}'.format(convert_dict_to_sql_where_clause(filters))

            template = Template(fp.read())
            query = template.substitute(
                NS=Active.namespace,
                PER=Active.period,
                WHERE=where
            )

            with connections['erp'].cursor() as cursor:
                cursor.execute(query)
                results = dict_fetch_all(cursor)

                if results:
                    return Response({
                        'status': True,
                        'serviceName': 'arpCard',
                        'data': results
                    })
                else:
                    return Response({
                        'status': False,
                        'message': 'Cari Kart Bulunamadı'
                    })


class SlipView(APIView):
    def post(self, request):
        logger.info('Slip post: ' + json.dumps(request.data))
        data = request.data
        docode =  data.get('data').get('productionVoucher').get('DOC_NUMBER')

        if Stfiche.objects.filter(trcode__in=[11,12,13], docode=docode).exists():
            return Response({
                'status': False,
                'message': f'Aynı numaralı bir fiş daha var! (DOCODE={docode})'
            })

        check = SlipQue.control({
            'firm': Active.name,
            'identifier': docode
        })
        if check:
            return Response(check.in_que(
                f'Bu istek {check.fmt_created} tarihinde kayıt olmuş.'
            ), status=status.HTTP_208_ALREADY_REPORTED)

        production = remove_empty_from_dict(
            data.get('data').get('productionVoucher')
        )
        prod_mf = MaterialFiche(
            data=production
        )
        prod_mf.is_valid(raise_exception=True)

        consume = remove_empty_from_dict(
            data.get('data').get('consumeVoucher')
        )
        cons_mf = MaterialFiche(
            data=consume
        )
        cons_mf.is_valid(raise_exception=True)

        slip = SlipQue.create_request(
            docode,
            data
        )

        return Response({
            'status': True,
            'message': 'Hızlı üretim fişi kuyruğa alındı!',
            'logoId': slip.id
        })