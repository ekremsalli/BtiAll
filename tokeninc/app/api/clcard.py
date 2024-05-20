from erp.integration import base
from erp.integration.current.card import ClCard
from erp.transport import API

class DatExt(base.BaseSerialiazer):
    CMERCHANT_ID = base.CharField(label='Merchant ID', required=False)

class iClCard(ClCard):    
    APPL_DATEXT_1 = DatExt()

class ExtApiClCard(API):
    serializer_class = iClCard