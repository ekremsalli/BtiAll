"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.invoice import (
    SalesInvoice as iSalesInvoice,
    PurchaseInvoice as iPurchaseInvoice,
    SalesInvoiceXML as iSalesInvoiceXML,
    PurchaseInvoiceXML as iPurchaseInvoiceXML
)

class SalesInvoice(API):
    serializer_class = iSalesInvoice

class PurchaseInvoice(API):
    serializer_class = iPurchaseInvoice

class SalesInvoiceXML(API):
    serializer_class = iSalesInvoiceXML

class PurchaseInvoiceXML(API):
    serializer_class = iPurchaseInvoiceXML
