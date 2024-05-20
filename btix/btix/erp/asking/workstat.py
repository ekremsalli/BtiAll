"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.workstat.cost import WorkStatCost as iWorkStatCost
from erp.integration.workstat.group import WorkStatGroup as iWorkStatGroup
from erp.integration.workstat.std_cost import (
    WorkStatStdCost as iWorkStatStdCost
)
from erp.integration.workstat.workstat import (
    WorkStat as iWorkStat,
    WorkStatChar as iWorkStatChar
)

class WorkStatCost(API):
    serializer_class = iWorkStatCost

class WorkStatGroup(API):
    serializer_class = iWorkStatGroup

class WorkStatStdCost(API):
    serializer_class = iWorkStatStdCost

class WorkStat(API):
    serializer_class = iWorkStat

class WorkStatChar(API):
    serializer_class = iWorkStatChar