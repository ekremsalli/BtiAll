"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.employee.cost import EmployeeCost as iEmployeeCost
from erp.integration.employee.employee import Employee as iEmployee
from erp.integration.employee.group import EmployeeGroup as iEmployeeGroup
from erp.integration.employee.shift import EmployeeShift as iEmployeeShift
from erp.integration.employee.shift import EmployeeShiftAssign as iEmployeeShiftAssign

class EmployeeCost(API):
    serializer_class = iEmployeeCost

class Employee(API):
    serializer_class = iEmployee

class EmployeeGroup(API):
    serializer_class = iEmployeeGroup

class EmployeeShift(API):
    serializer_class = iEmployeeShift

class EmployeeShiftAssign(API):
    serializer_class = iEmployeeShiftAssign

