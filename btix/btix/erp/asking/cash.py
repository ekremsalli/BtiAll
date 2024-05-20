"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.cash.card import CashCard as iCashCard
from erp.integration.cash.slip import CashSlip as iCashSlip

class CashCard(API):
    serializer_class = iCashCard

class CashSlip(API):
    serializer_class = iCashSlip