from django.urls import path
from django.http import HttpResponse

from .views import (
    item, unitset, barcode, order, aws, dispatch,
    invoice
)


def test_view(request):
    return HttpResponse(f"Test! {request.META}")


urlpatterns = [
    path('item', item.ItemView.as_view(), name='item_view'),
    path('item/<str:barcode>', item.ItemDetailView.as_view(),
         name='item_detail_view'),
    path('item_next', item.ItemCodeView.as_view(), name='item_code_view'),
    path('unitset', unitset.UnitsetView.as_view(), name='unitset_view'),
    path('barcode', barcode.BarcodeView.as_view(), name='barcode_view'),
    path('arp', order.ARPView.as_view(), name='arp_view'),
    path('arp/<str:code>', order.ArpDetailView.as_view(), name='arp_detail_view'),
    path('order', order.OrderView.as_view(), name='order_view'),
    path('order/po/<str:number>', order.OrderUpdateView.as_view(),
         {'sales_order': False}, name='order_po_update_view'),
    path('order/so/<str:number>', order.OrderUpdateView.as_view(),
         {'sales_order': True}, name='order_so_update_view'),
    path('order_cancel/po/<str:number>', order.OrderCancelView.as_view(), {'sales_order': False},
         name='order_po_cancel_view'),
    path('order_cancel/so/<str:number>', order.OrderCancelView.as_view(), {'sales_order': True},
         name='order_so_cancel_view'),
    path('s3', aws.S3View.as_view(), name='aws_s3_view'),
    path('s3/<str:prefix>', aws.S3DetailView.as_view(), name='aws_s3_detail'),

    path('dispatch', dispatch.DispatchView.as_view(), name='dispatch_view'),
    path('dispatch/<str:docno>/<int:warehouse>',
         dispatch.DispatchDetailView.as_view(), name='dispatch_detail_view'),

    path('invoice', invoice.InvoiceView.as_view(), name='invoice_view'),
    path('invoice/detail', invoice.InvoiceDetailView.as_view(),
         name='invoice_detail'),
    path('invoice/pdf', invoice.InvoicePDF.as_view(), name='invoice_pdf'),
    path('invoice/read', invoice.InvoiceReadView.as_view(), name='invoice_read'),
    path('validate/gibUser', invoice.GetValidateGIBUserView.as_view(),
         name='validate_gib_user'),

    path('return/invoice', invoice.ReturnInvoicesView.as_view(),
         name='return-invoice'),

]
