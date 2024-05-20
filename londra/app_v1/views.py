import logging
import json
from string import Template

from django.db import connections
from django.conf import settings
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from erp.active import Active

from erp.asking.material import (
    MaterialFiche,
)
from erp.models.friendly import (
    Items,
    Itmunita,
    Stfiche,
)

from common.utils import (
    remove_empty_from_dict,
    convert_dict_to_sql_where_clause,
    dict_fetch_all,
)
from .converters import (
    WantageConverter,
    WantageItemConverter,
    WantageItemConsumedConverter,
    TransferConverter,
    TransferLineConverter,
)
from .models import (
    Other,
    CommonQue,
    TransferQue,
    SlipQue,
)
from .idea_models import (
    Storemap,
)
from .serializers import (
    WantageSerializer,
)

logger = logging.getLogger("app")


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


class TransferRefundView(APIView):
    def post(self, request):
        logger.info('TransferRefund post: ' + json.dumps(request.data))
        data = request.data

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


class ItemCodesView(APIView):
    def get(self, request, **kwargs):
        params = request.GET
        filters = {}
        if 'code' in params and params.get('code', None):
            code =  params.get('code')
            filters['ITM.CODE'] = (' LIKE ', f'%{code}%')

        if 'active' in params:
            filters['ITM.ACTIVE'] = params.get('active')

        if 'ITM.NAME4' in params and params.get('ITM.NAME4', None):
            name4 = params.get('ITM.NAME4')
            filters['ITM.NAME4'] = (' LIKE ', f'%{name4}%')

        if 'ITM_NAME4' in params and params.get('ITM_NAME4', None):
            name4 = params.get('ITM_NAME4')
            filters['ITM.NAME4'] = (' LIKE ', f'%{name4}%')

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


class StoremapView(APIView):
    def get(self, request, **kwargs):
        params = request.GET
        number = None
        if 'NR' in params and params.get('NR', None):
            number =  params.get('NR')

        if 'nr' in params and params.get('nr', None):
            number =  params.get('nr')

        if 'nr' in kwargs and kwargs.get('nr'):
            number = kwargs.get('nr')

        items = Storemap.objects.filter(
            firmnr=Active.number
        ).exclude(
            status='KAPANDI'
        )

        if number:
            items = items.filter(store_nr=number)

        data = []
        blacklist = ['id']
        for item in items:
            temp = {}
            pack = item.__dict__
            for key, value in pack.items():
                if key.startswith('_'):
                    continue

                if key in blacklist:
                    temp.update({key: value})
                else:
                    temp.update({key.upper(): value})
            data.append(temp)

        return Response({
            'serviceName': 'firmWareHouses',
            'data': data
        })


class ItemBoomView(APIView):
    def get(self, request, **kwargs):
        filters = {}
        if 'code' in kwargs and kwargs.get('code') and kwargs.get('code') != '1':
            filters['ITM_U.CODE'] = kwargs.get('code')


        with open('app_v1/resources/item_boom.sql', 'r', encoding='utf-8') as fp:
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
                if len(results) == 0:
                    return Response({
                        'status': False,
                        'message': 'Ürün Reçete Bilgisi Bulunamadı'
                    })

                return Response({
                    'serviceName': 'itemsCodeList',
                    'data': results
                })
