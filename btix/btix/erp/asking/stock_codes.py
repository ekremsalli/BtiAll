"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.stock_codes import (
    StockCodes as iStockCodes
)

class StockCodes(API):
    serializer_class = iStockCodes
