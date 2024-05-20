"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.delivery import (
    DeliveryCode as iDeliveryCode
)

class DeliveryCode(API):
    serializer_class = iDeliveryCode