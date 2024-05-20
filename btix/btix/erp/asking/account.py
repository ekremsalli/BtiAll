"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.account.card import AccountCard as iAccountCard
from erp.integration.account.emcenter import Emcenter as iEmcenter
from erp.integration.account.fiche import Emfiche as iEmfiche
from erp.integration.account.fiche import EmficheXML as iEmficheXML

class AccountCard(API):
    serializer_class = iAccountCard

class Emcenter(API):
    serializer_class = iEmcenter

class Emfiche(API):
    serializer_class = iEmfiche

class EmficheXML(API):
    serializer_class = iEmficheXML