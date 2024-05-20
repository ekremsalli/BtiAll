"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.salesman import (
    Salesman as iSalesman
)

class Salesman(API):
    serializer_class = iSalesman