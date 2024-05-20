"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.address import (
    Country as iCountry,
    City as iCity,
    District as iDistrict,
    Town as iTown,
    Postcode as iPostcode,
)

class Country(API):
    serializer_class = iCountry

class City(API):
    serializer_class = iCity

class District(API):
    serializer_class = iDistrict

class Town(API):
    serializer_class = iTown

class Postcode(API):
    serializer_class = iPostcode
