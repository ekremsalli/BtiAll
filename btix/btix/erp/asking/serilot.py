"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.serilot import (
    Serilot as iSerilot
)

class Serilot(API):
    serializer_class = iSerilot