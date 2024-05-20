from datetime import datetime

from django.urls import path
from django.http import HttpResponse

from .views import (
    WantageView,
    TransferRefundView,
    ItemCodesView,
    SlipView,
    StoremapView,
    ItemBoomView,
)


def test_view(request):
    return HttpResponse(f"Test! {datetime.now()}")


urlpatterns = [
    path(
        'test',
        test_view,
        name='test'
    ),
    path(
        'itemSlip/itemSlip/wantage',
        WantageView.as_view(),
        name='wantage_view'
    ),
    path(
        'itemslip/itemslip/wantage',
        WantageView.as_view(),
        name='wantage_view'
    ),
    path(
        'itemSlip/itemSlip/wantage/',
        WantageView.as_view(),
        name='wantage_view'
    ),
    path(
        'itemSlip/itemSlip/itemSlip',
        TransferRefundView.as_view(),
        name='transfer_refund_view'
    ),
    path(
        'itemSlip/itemSlip/itemSlip/',
        TransferRefundView.as_view(),
        name='transfer_refund_view'
    ),
    path(
        'itemslip/itemslip/itemslip',
        TransferRefundView.as_view(),
        name='transfer_refund_view'
    ),
    path(
        'itemslip/itemslip/itemslip/',
        TransferRefundView.as_view(),
        name='transfer_refund_view'
    ),
    path(
        'items/items/itemsconsumable',
        ItemCodesView.as_view(),
        name='item_codes_view'
    ),
    path(
        'items/items/itemsconsumable/',
        ItemCodesView.as_view(),
        name='item_codes_view'
    ),
    path(
        'slip/slipapi/slipapi',
        SlipView.as_view(),
        name='slip_view'
    ),
    path(
        'slip/slipapi/slipapi/',
        SlipView.as_view(),
        name='slip_view'
    ),
    path(
        'firm/firm/firmwarehouses',
        StoremapView.as_view(),
        name='storemap_view'
    ),
    path(
        'firm/firm/firmwarehouses/',
        StoremapView.as_view(),
        name='storemap_view'
    ),

    path(
        'firm/firm/firmWareHouses',
        StoremapView.as_view(),
        name='storemap_view'
    ),
    path(
        'firm/firm/firmWareHouses/',
        StoremapView.as_view(),
        name='storemap_view'
    ),
    path(
        'firm/firm/firmwarehouses/nr/<str:nr>',
        StoremapView.as_view(),
        name='storemap_view'
    ),
    path(
        'firm/firm/firmwarehouses/nr/<str:nr>/',
        StoremapView.as_view(),
        name='storemap_view'
    ),
    path(
        'firm/firm/firmwarehouses/NR/<str:nr>',
        StoremapView.as_view(),
        name='storemap_view'
    ),
    path(
        'firm/firm/firmwarehouses/NR/<str:nr>/',
        StoremapView.as_view(),
        name='storemap_view'
    ),
    path(
        'firm/firm/firmWareHouses/nr/<str:nr>/',
        StoremapView.as_view(),
        name='storemap_view'
    ),
    path(
        'firm/firm/firmWareHouses/nr/<str:nr>',
        StoremapView.as_view(),
        name='storemap_view'
    ),
    path(
        'firm/firm/firmWareHouses/NR/<str:nr>/',
        StoremapView.as_view(),
        name='storemap_view'
    ),
    path(
        'firm/firm/firmWareHouses/NR/<str:nr>/',
        StoremapView.as_view(),
        name='storemap_view'
    ),

    path(
        'items/items/itemsboomlist/<str:code>',
        ItemBoomView.as_view(),
        name='item_boom_view'
    ),

]
