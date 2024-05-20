"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.bank.account import BankAccount as iBankAccount
from erp.integration.bank.card import BankCard as iBankCard
from erp.integration.bank.fiche import BankFiche as iBankFiche


class BankAccount(API):
    serializer_class = iBankAccount

class BankCard(API):
    serializer_class = iBankCard

class BankFiche(API):
    serializer_class = iBankFiche

