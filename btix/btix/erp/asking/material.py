"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API
from erp.integration.material.alternates import (
    MaterialAlternates as iMaterialAlternates
)
from erp.integration.material.bom_cost import BomCost as iBomCost
from erp.integration.material.bom_params import BomParams as iBomParams
from erp.integration.material.bom import Bom as iBom
from erp.integration.material.bomas import Bomas as iBomas
from erp.integration.material.card import MaterialCard as iMaterialCard
from erp.integration.material.char import (
    MaterialCharacteristics as iMaterialCharacteristics
)
from erp.integration.material.cost import MaterialCost as iMaterialCost
from erp.integration.material.fiche import MaterialFiche as iMaterialFiche
from erp.integration.material.fiche import MaterialFicheXML as iMaterialFicheXML

from erp.integration.material.group import (
    MaterialGroupCode as iMaterialGroupCode
)
from erp.integration.material.tree import MaterialTree as iMaterialTree

class MaterialAlternates(API):
    serializer_class = iMaterialAlternates

class BomCost(API):
    serializer_class = iBomCost

class BomParams(API):
    serializer_class = iBomParams

class Bom(API):
    serializer_class = iBom

class Bomas(API):
    serializer_class = iBomas

class MaterialCard(API):
    serializer_class = iMaterialCard

class MaterialCharacteristics(API):
    serializer_class = iMaterialCharacteristics

class MaterialCost(API):
    serializer_class = iMaterialCost

class MaterialFiche(API):
    serializer_class = iMaterialFiche


class MaterialFicheXML(API):
    serializer_class = iMaterialFicheXML

class MaterialGroupCode(API):
    serializer_class = iMaterialGroupCode

class MaterialTree(API):
    serializer_class = iMaterialTree
