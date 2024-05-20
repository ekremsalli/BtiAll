"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import logging
from datetime import datetime, date
import zmq
import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

from erp.integration import base

logger = logging.getLogger("erp")

class Command(BaseCommand):
    help = "Test asking"

    def handle(self, *a, **kw):
        from erp.asking.account import (
            AccountCard,
            Emcenter,
            Emfiche
        )

        from erp.asking.bank import (
            BankAccount,
            BankCard,
            BankFiche
        )

        from erp.asking.cash import (
            CashCard,
            CashSlip
        )

        from erp.asking.cs import (
            CSRoll,
            CSTransfer
        )

        from erp.asking.current import (
            ClCard,
            ClFiche,
            ClShipment
        )

        from erp.asking.distribution import (
            DistOrder,
            DistributionRouting,
            DistributionVehicle
        )

        from erp.asking.employee import (
            EmployeeCost,
            Employee,
            EmployeeGroup,
            EmployeeShift,
            EmployeeShiftAssign
        )

        from erp.asking.material import (
            MaterialAlternates,
            BomCost,
            BomParams,
            Bom,
            Bomas,
            MaterialCard,
            MaterialCharacteristics,
            MaterialCost,
            MaterialFiche,
            MaterialGroupCode,
            MaterialTree
        )

        from erp.asking.workstat import (
            WorkStatCost,
            WorkStatGroup,
            WorkStatStdCost,
            WorkStat,
            WorkStatChar
        )

        from erp.asking.address import (
            Country,
            City,
            District,
            Town,
            Postcode
        )

        from erp.asking.asset import (
            AssetRecord
        )

        from erp.asking.campaign import (
            SalesCampaign,
            PurchaseCampaign
        )

        from erp.asking.code import (
            CypCode,
            SpeCode,
            PrgCode
        )

        from erp.asking.delivery import (
            DeliveryCode
        )

        from erp.asking.discount import (
            SalesDiscount,
            PurchaseDiscount
        )

        from erp.asking.dispatch import (
            SalesDispatch,
            PurchaseDispatch
        )

        from erp.asking.expense import (
            SalesExpense,
            PurchaseExpense
        )

        from erp.asking.invoice import (
            SalesInvoice,
            PurchaseInvoice
        )

        from erp.asking.item_price import (
            SalesItemPrice,
            PurchaseItemPrice
        )

        from erp.asking.opertion import (
            Opertion
        )

        from erp.asking.orders import (
            PurchaseOrder,
            SalesOrder
        )

        from erp.asking.payplan import (
            Payplan
        )

        from erp.asking.promotion import (
            PurchasePromotion,
            SalesPromotion
        )

        from erp.asking.quality import (
            Qset
        )

        from erp.asking.routing import (
            ProductionRouting
        )

        from erp.asking.sales import (
            SalesRoute,
            SalesTarget
        )

        from erp.asking.salesman import (
            Salesman
        )

        from erp.asking.serilot import (
            Serilot
        )

        from erp.asking.service_price import (
            ServiceSalesPrice,
            ServicePurchasePrice
        )

        from erp.asking.service import (
            SalesService,
            PurchaseService
        )

        from erp.asking.std_cost_period import (
            StdCostPeriod
        )

        from erp.asking.stock_codes import (
            StockCodes
        )

        from erp.asking.unit import (
            Unitset
        )