"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.cs.roll import CSRoll as iCSRoll
from erp.integration.cs.transfer import CSTransfer as iCSTransfer

class CSRoll(API):
    serializer_class = iCSRoll

class CSTransfer(API):
    serializer_class = iCSTransfer