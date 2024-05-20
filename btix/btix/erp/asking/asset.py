"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.asset import AssetRecord as iAssetRecord

class AssetRecord(API):
    serializer_class = iAssetRecord