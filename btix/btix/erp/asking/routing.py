"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.routing import (
    ProductionRouting as iProductionRouting
)

class ProductionRouting(API):
    serializer_class = iProductionRouting