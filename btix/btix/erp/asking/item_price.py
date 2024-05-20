"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.item_price import (
    SalesItemPrice as iSalesItemPrice,
    PurchaseItemPrice as iPurchaseItemPrice
)

class SalesItemPrice(API):
    serializer_class = iSalesItemPrice

class PurchaseItemPrice(API):
    serializer_class = iPurchaseItemPrice
