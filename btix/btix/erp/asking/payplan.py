"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.payplan import (
    Payplan as iPayplan,
)

class Payplan(API):
    serializer_class = iPayplan