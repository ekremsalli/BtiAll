"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.unit import (
    Unitset as iUnitset
)

class Unitset(API):
    serializer_class = iUnitset
