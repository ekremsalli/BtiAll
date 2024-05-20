"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.dispatch import (
    SalesDispatch as iSalesDispatch,
    PurchaseDispatch as iPurchaseDispatch,
    SalesDispatchXML as iSalesDispatchXML,
    PurchaseDispatchXML as iPurchaseDispatchXML
)

class SalesDispatch(API):
    serializer_class = iSalesDispatch

class PurchaseDispatch(API):
    serializer_class = iPurchaseDispatch

class SalesDispatchXML(API):
    serializer_class = iSalesDispatchXML

class PurchaseDispatchXML(API):
    serializer_class = iPurchaseDispatchXML
