"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.std_cost_period import (
    StdCostPeriod as iStdCostPeriod
)

class StdCostPeriod(API):
    serializer_class = iStdCostPeriod
