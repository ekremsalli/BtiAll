"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.service import (
    SalesService as iSalesService,
    PurchaseService as iPurchaseService
)

class SalesService(API):
    serializer_class = iSalesService

class PurchaseService(API):
    serializer_class = iPurchaseService