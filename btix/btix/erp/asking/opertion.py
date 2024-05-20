"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.opertion import (
    Opertion as iOpertion,
)

class Opertion(API):
    serializer_class = iOpertion