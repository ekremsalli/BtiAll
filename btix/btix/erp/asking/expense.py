"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.expense import (
    SalesExpense as iSalesExpense,
    PurchaseExpense as iPurchaseExpense
)

class SalesExpense(API):
    serializer_class = iSalesExpense

class PurchaseExpense(API):
    serializer_class = iPurchaseExpense
