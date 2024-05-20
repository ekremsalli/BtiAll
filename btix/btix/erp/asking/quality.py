"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.quality import (
    Qset as iQset
)

class Qset(API):
    serializer_class = iQset