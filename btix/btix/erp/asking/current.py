"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.current.card import ClCard as iClCard
from erp.integration.current.fiche import ClFiche as iClFiche
from erp.integration.current.fiche import ClFicheXML as iClFicheXML
from erp.integration.current.shipment import ClShipment as iClShipment

class ClCard(API):
    serializer_class = iClCard

class ClFiche(API):
    serializer_class = iClFiche

class ClShipment(API):
    serializer_class = iClShipment

class ClFicheXML(API):
    serializer_class = iClFicheXML
