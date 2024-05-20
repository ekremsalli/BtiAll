"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.sales.sales_route import SalesRoute as iSalesRoute
from erp.integration.sales.sales_target import SalesTarget as iSalesTarget

class SalesRoute(API):
    serializer_class = iSalesRoute

class SalesTarget(API):
    serializer_class = iSalesTarget