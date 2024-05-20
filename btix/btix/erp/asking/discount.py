"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.discount import (
    SalesDiscount as iSalesDiscount,
    PurchaseDiscount as iPurchaseDiscount
)

class SalesDiscount(API):
    serializer_class = iSalesDiscount

class PurchaseDiscount(API):
    serializer_class = iPurchaseDiscount