"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.orders import (
    PurchaseOrder as iPurchaseOrder,
    SalesOrder as iSalesOrder,
    PurchaseOrderXML as iPurchaseOrderXML,
    SalesOrderXML as iSalesOrderXML
)

class PurchaseOrder(API):
    serializer_class = iPurchaseOrder

class SalesOrder(API):
    serializer_class = iSalesOrder

class PurchaseOrderXML(API):
    serializer_class = iPurchaseOrderXML

class SalesOrderXML(API):
    serializer_class = iSalesOrderXML
