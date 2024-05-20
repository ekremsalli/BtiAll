"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.service_price import (
    ServiceSalesPrice as iServiceSalesPrice,
    ServicePurchasePrice as iServicePurchasePrice
)

class ServiceSalesPrice(API):
    serializer_class = iServiceSalesPrice

class ServicePurchasePrice(API):
    serializer_class = iServicePurchasePrice