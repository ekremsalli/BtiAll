import json
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework import status

from django.core.cache import cache


from erp.models.friendly import Items
from erp.active import Active
from bti.views.base import Bti, Pagination
from bti.models.flow import Flow
from third_party.bazaars.trendyol import Trendyol
from third_party.bazaars.trendyol.models import (
    TrendyolProductMatch as TrendyolProductMatchTable,
    TrendyolProductMismatch,
    TrendyolLog
)

from app.models import TrendyolTrack

from third_party.bazaars.trendyol.serializers import (
    TrendyolProductMatchSerializer,
    TrendyolProductMismatchSerializer,
    TrendyolLogSerializer
)

from portal.serializers.integration import *

class TrendyolTransfer(Bti, APIView):
    swagger_schema = None
    def post(self, request, format=None):
        id = request.data.get('id')
        log = TrendyolLog.objects.filter(pk=id).first()
        data = json.loads(log.raw)
        if log is None:
            return Response({
                'status': False,
                'description': 'Geçersiz sipariş!'
            })
        from erp.active import Active
        check = TrendyolTrack.control({
            'firm': Active.name,
            'identifier': log.order_number
        })
        if check is None:
            try:
                ok = TrendyolTrack.create_sales_order(data)
                print(status)
            except Exception as e:
                print(e)
                return Response({
                    'status': False,
                    'description': f'Bilinmeyen bir hata oluştu! ({e})'
                })
            else:
                if ok and ok.flow.internal_ref:
                    return Response({
                        'status': True,
                        'description': 'Başarıyla aktarıldı!'
                    })
                else:
                    return Response({
                        'status': False,
                        'description': 'Sipariş aktarılamadı'
                    })
        else:
            return Response(check.in_track(
                f'Bu sipariş {check.fmt_created} tarihinde kayıt olmuş.'
            ), status=status.HTTP_208_ALREADY_REPORTED)

class TrendyolLogView(Bti, generics.ListAPIView):
    swagger_schema = None
    pagination_class = Pagination
    serializer_class = TrendyolLogSerializer
    ordering_fields = []

    def get_queryset(self):
        qs = TrendyolLog.objects.prefetch_related('trendyollinelog_set').all().order_by("-created")
        return qs

class TrendyolMismatch(Bti, generics.ListAPIView):
    swagger_schema = None
    serializer_class = TrendyolProductMismatchSerializer
    ordering_fields = []

    def get_queryset(self):
        qs = TrendyolProductMismatch.objects.filter(
            resolved=False).order_by("-created")
        return qs

class TrendyolProduct(Bti, APIView):
    swagger_schema = None
    def post(self, request, format=None):
        product = TrendyolProductSerializer(data=request.data)
        product.is_valid(raise_exception=True)
        data = product.data
        if "TRENDYOL" not in Active.settings:
            raise APIException('Trendyol ayarları bulunamadı!')
        trendyol = Trendyol(**Active.settings['TRENDYOL'])
        items = {
            'items': [data]
        }
        transfer = trendyol.create_product(**items)
        return Response({
            'transfer': transfer
        })

class List(Bti, generics.ListAPIView):
    swagger_schema = None
    pagination_class = Pagination
    serializer_class = IntegrationSerializer
    ordering_fields = []

    def get_queryset(self):
        qs = Flow.objects.all().order_by("-id")
        return qs

class SearchProduct(Bti, generics.ListAPIView):
    swagger_schema = None
    pagination_class = Pagination
    queryset = Items.objects.filter(active=0).order_by('name')
    serializer_class = ProductSerializer
    filterset_fields = {
        'code': ['startswith'],
        'name': ['icontains'],
    }
    ordering_fields = ["code", "name"]

class ProductDetail(Bti, APIView):
    swagger_schema = None
    def get(self, request, format=None):
        code = request.query_params.get('code', None)
        if code is None:
            raise APIException('Ürün kodu belirtin!')
        item = Items.objects.prefetch_related(
            'erp_lg_unitbarcode_itemref').filter(active=0, code=code).first()
        barcode = ''
        try:
            barcode = item.erp_lg_unitbarcode_itemref.first().barcode
        except Exception as e:
            print(e)
        return Response({
            'product': ProductDetailSerializer(item).data,
            'barcode': barcode
        })

class TrendyolAttrs(Bti, APIView):
    swagger_schema = None
    def get(self, request, format=None):
        if "TRENDYOL" not in Active.settings:
            raise APIException('Trendyol ayarları bulunamadı!')
        trendyol = Trendyol(**Active.settings['TRENDYOL'])
        id = request.query_params.get('id', None)
        if id is None:
            raise APIException('Kategori belirtin!')
        return Response({
            'attrs': trendyol.get_category_attributes(id)
        })

class TrendyolBrandSearch(Bti, APIView):
    swagger_schema = None
    def get(self, request, format=None):
        if "TRENDYOL" not in Active.settings:
            raise APIException('Trendyol ayarları bulunamadı!')
        trendyol = Trendyol(**Active.settings['TRENDYOL'])
        val = request.query_params.get('val', None)
        if val is None:
            raise APIException('Marka belirtin!')
        return Response({
            'brands': trendyol.brand_by_name(val)
        })

class TrendyolProductMatch(Bti, APIView):
    swagger_schema = None

    def get(self, request, format=None):
        # liste
        from erp.models.friendly import Items

        records = TrendyolProductMatchTable.objects.filter()
        items = Items.objects.filter(code__in=[r.erp_code for r in records])
        item_serializer = ErpItemSerializer(items, many=True)
        serializer = TrendyolProductMatchSerializer(records, many=True)

        return Response({
            'results': list(serializer.data),
            'items': list(item_serializer.data)
        })

    def post(self, request, format=None):
        print(request.data)
        serializer = TrendyolProductMatchSerializer(data=request.data, many=True if type(request.data) is list else False)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            if type(data) is list:
                results = []
                for item in data:
                    check = Items.objects.filter(code=item.get('erp_code')).exists()
                    if check is False:
                        results.append({
                            'durum': 'Oluşturulmadı',
                            'kod': item.get('erp_code'),
                            'hata': 'Bilinmeyen ERP malzeme kodu!'
                        })
                        continue
                    if TrendyolProductMatchTable.objects.filter(**item).exists():
                        results.append({
                            'durum': 'Oluşturulmadı',
                            'kod': item.get('erp_code'),
                            'hata': 'Bu eşleme daha önce oluşturulmuş!'
                        })
                        continue
                    rec = TrendyolProductMatchTable.objects.create(**item)
                    results.append({
                        'durum': 'Oluşturuldu!',
                        'kod': item.get('erp_code'),
                        'hata': ''
                    })
                return Response({
                    'results': results
                })
            else:
                # erp kodu mevcut mu?
                check = Items.objects.filter(code=data.get('erp_code')).exists()
                if check is False:
                    return Response({
                        'status': False,
                        'description': 'Bilinmeyen ERP malzeme kodu!'
                    })
                if TrendyolProductMatchTable.objects.filter(**data).exists():
                    return Response({
                        'status': False,
                        'description': 'Bu eşleme daha önce oluşturulmuş!'
                    })
                try:
                    serializer.save()
                except Exception as e:
                    return Response({
                        'status': False,
                        'description': f'Kayıt esnasında bilinmeyen bir sorun oluştu! ({str(e)})'
                    })
                else:
                    return Response({
                        'status': True,
                        'description': 'Başarıyla kaydedildi!'
                    })



    def put(self, request, format=None):
        # update
        pass

    def delete(self, request, format=None):
        records = request.data.get('records')
        rev = TrendyolProductMatchTable.objects.filter(pk__in=records).delete()
        print(rev)
        return Response({
            'status': True
        })

class TrendyolInit(Bti, APIView):
    swagger_schema = None
    def get(self, request, format=None):
        if "TRENDYOL" not in Active.settings:
            raise APIException('Trendyol ayarları bulunamadı!')
        trendyol = Trendyol(**Active.settings['TRENDYOL'])
        default_timeout = 60 * 60
        prefix = 'b_trendyol_'
        try:

            categories = cache.get(f'{prefix}categories')
            if categories is None  or 'refresh_categories' in request.query_params:
                categories = trendyol.get_category_tree()
                cache.set(f'{prefix}categories', categories, default_timeout)

            cargos = cache.get(f'{prefix}cargos')
            if cargos is None  or 'refresh_cargos' in request.query_params:
                cargos = trendyol.shipment_providers()
                cache.set(f'{prefix}cargos', cargos, default_timeout)

            brands = cache.get(f'{prefix}brands')
            if brands is None  or 'refresh_brands' in request.query_params:
                brands = trendyol.get_brands(size=50)
                cache.set(f'{prefix}brands', brands, default_timeout)
        except Exception as e:
            raise APIException("Trendyol hatası! " + str(e))


        qs = Items.objects.filter(active=0).exclude(name='').order_by('name')
        ps = ProductSerializer(
            qs[0:23],
            many=True
        )
        return Response({
            'categories': categories,
            'cargos': cargos,
            'brands': brands,
            'items': ps.data
        })
