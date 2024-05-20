"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.promotion import (
    PurchasePromotion as iPurchasePromotion,
    SalesPromotion as iSalesPromotion
)

class PurchasePromotion(API):
    serializer_class = iPurchasePromotion

class SalesPromotion(API):
    serializer_class = iSalesPromotion
