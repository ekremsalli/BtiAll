"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.campaign import (
    SalesCampaign as iSalesCampaign,
    PurchaseCampaign as iPurchaseCampaign
)

class SalesCampaign(API):
    serializer_class = iSalesCampaign

class PurchaseCampaign(API):
    serializer_class = iPurchaseCampaign