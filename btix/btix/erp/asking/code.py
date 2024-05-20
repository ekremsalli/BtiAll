"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.code import (
    CypCode as iCypCode,
    SpeCode as iSpeCode,
    PrgCode as iPrgCode
)

class CypCode(API):
    serializer_class = iCypCode

class SpeCode(API):
    serializer_class = iSpeCode

class PrgCode(API):
    serializer_class = iPrgCode    