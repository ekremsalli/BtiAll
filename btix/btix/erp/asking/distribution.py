"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.distribution.order import DistOrder as iDistOrder
from erp.integration.distribution.routing import DistributionRouting as iDistributionRouting
from erp.integration.distribution.vehicle import DistributionVehicle as iDistributionVehicle


class DistOrder(API):
    serializer_class = iDistOrder

class DistributionRouting(API):
    serializer_class = iDistributionRouting

class DistributionVehicle(API):
    serializer_class = iDistributionVehicle