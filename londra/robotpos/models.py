from datetime import datetime
import json

from django.db import models
from django.db.models import Q
from django.db import connections

from bti.models import FileRotate, Que, QueLog
from erp.active import Active
from erp.asking.current import ClFicheXML
from erp.asking.material import (
    MaterialFiche,
    MaterialFicheXML
)

from erp.helpers import dict_fetch_all
from erp.models.friendly import (
    Items,
    Stfiche,
    Stline,
)

from robotpos.converters import (
    RevenueConverter,
    RevenueLineConverter,
    SalesConverter,
    SalesLineConverter,
    ProductionConverter,
    ConsumptionConverter,
    WasteConverter,
)


MAX_CHAR_LIMIT_FOR_XML = 65534

class RobotposWaitingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_accounted=False,
        ).filter(
            Q(is_empty=True) | Q(is_error=True)
        )


class RobotposReadyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_accounted=False,
            is_empty=False,
            is_error=False
        )


class Robotpos(FileRotate):
    class GENRES(models.TextChoices):
        branch_revenue = 'branch_revenue', 'branch_revenue' # 1
        sales = 'sales', 'sales' # 3
        pcw = 'pcw', 'pcw' # 3
        sales_invoice = 'sales_invoice', 'sales_invoice' # 5
        accounting = 'accounting', 'accounting' # 7
        wantage = 'wantage', 'wantage' # 8
        refund = 'refund', 'refund' # 6

    day = models.DateField(
        db_index=True
    )
    genre = models.CharField(
        max_length=32,
        choices=GENRES.choices,
        db_index=True,
    )
    branch = models.CharField(
        db_index=True,
        max_length=10
    )
    data = models.TextField()
    is_empty = models.BooleanField(
        default=True,
        db_index=True
    )
    is_error = models.BooleanField(
        default=False,
        db_index=True
    )
    is_accounted = models.BooleanField(
        default=False,
        db_index=True
    )
    last_error = models.TextField(
        null=True
    )
    last_synced = models.DateTimeField(null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    objects = models.Manager()
    waiting = RobotposWaitingManager()
    ready = RobotposReadyManager()

    def get_identifier(self):
        genre = "".join([c for c in self.genre.title() if c.isupper()])
        return f'RP-{genre}-{self.pk}'

    class Meta:
        unique_together = [
            'day',
            'genre',
            'branch'
        ]

    def get_data(self):        
        return json.loads(self.data)

    @classmethod
    def is_exists(cls, day, genre, branch):
        return cls.objects.filter(
            day=day,
            genre=genre,
            branch=branch
        ).count() > 0


class PaymentError(models.Model):
    branch = models.CharField(db_index=True, max_length=10)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [
            'branch',
            'name',
        ]


class PaymentMap(models.Model):
    branch = models.CharField(null=True, db_index=True, max_length=10)
    payment = models.CharField(max_length=50, db_index=True)
    account_code = models.CharField(max_length=50, null=True)
    custom_field1 = models.CharField(max_length=50, null=True)
    custom_field2 = models.CharField(max_length=50, null=True)

    @classmethod
    def get_items(cls, branch):
        items = {item.payment: item for item in cls.objects.filter(branch__isnull=True)}
        for item in cls.objects.filter(branch=branch):
            items[item.payment] = item
        return items


class PaymentBlacklist(models.Model):
    branch = models.CharField(null=True, db_index=True, max_length=10)
    payment = models.CharField(max_length=80, db_index=True)

    @classmethod
    def get_blacklist(cls, branch):
        return set(cls.objects \
            .filter(Q(branch=branch) | Q(branch__isnull=True)) \
            .values_list('payment', flat=True))


class RevenueQue(Que):
    robotpos = models.ForeignKey(Robotpos, on_delete=models.PROTECT)

    @classmethod
    def create_request(cls, robotpos, identifier, data):
        return cls.objects.create(
            firm=Active.name,
            identifier=identifier,
            data=json.dumps(data),
            robotpos=robotpos
        )

    @classmethod
    def validate(cls, data):
        request = Active.settings['DEFAULT_REVENUE'].copy()
        request.update(data)
        cf = ClFicheXML(
            data=request
        )
        cf.is_valid(raise_exception=True)

    @classmethod
    def check_payments(cls, data, robotpos):
        blacklist = PaymentBlacklist.get_blacklist(robotpos.branch)
        payments = PaymentMap.get_items(robotpos.branch)

        issues = []
        lines = []

        for item in data:
            if item.get('Tutar') == 0:
                continue
            if item.get('AnaTip') in blacklist or item.get('AltTip') in blacklist:
                continue

            if item.get('AnaTip') not in payments and item.get('AltTip') not in payments:
                issues.append(item)
            else:
                lines.append(item)

        return issues, lines

    @classmethod
    def generate_fiche(cls, lines, robotpos):
        payments = PaymentMap.get_items(robotpos.branch)

        request = Active.settings['DEFAULT_REVENUE'].copy()
        header = RevenueConverter(lines, {}).data
        request.update(header)
        request.update({
            'NOTES5': robotpos.id
        })
        transactions = []

        for line in lines:
            if line.get('AltTip') in payments:
                payment = payments[line.get('AltTip')]
            elif line.get('AnaTip') in payments:
                payment = payments[line.get('AnaTip')]

            reqline = Active.settings['DEFAULT_REVENUE_LINE'].copy()
            item = RevenueLineConverter(
                line,
                {}
            ).data
            reqline.update(item)

            if payment.custom_field1:
                reqline.update({
                    'BANKACC_CODE': payment.custom_field1,
                    #'GL_CODE2': payment.custom_field1
                })
            if payment.custom_field2:
                reqline.update({
                    'ARP_CODE': payment.custom_field2,
                    'GL_CODE1': payment.custom_field2
                })
            if payment.account_code:
                reqline.update({
                    'BANK_GL_CODE': payment.account_code
                })

            transactions.append(reqline)

        request.update({
            'TRANSACTIONS': transactions
        })
        fiche = ClFicheXML(
            user=Active.settings['DEFAULT_XML_USER'],
            data=request,
            keyword1=robotpos.day,
            keyword2='revenue',
            keyword3=robotpos.id
        )
        fiche.is_valid(raise_exception=True)
        fiche.transfer_via_xml(
            item_name={
                'TRANSACTIONS': 'TRANSACTION'
            },
            fill_acc_codes=True
        )
        return fiche


class RevenueQueLog(QueLog):
    pass


class SalesQue(Que):
    robotpos = models.ForeignKey(Robotpos, on_delete=models.PROTECT)

    @classmethod
    def call_consume_products(cls, *params):
        cursor = connections['erp'].cursor()
        try:
            sql = 'exec [dbo].[spBTI_SubItemsNew] %s, %s, %s, %s, %s, %s, %s'
            cursor.execute(sql, params)
        finally:
            cursor.close()
        return True

    @classmethod
    def clear_consumed_products(cls, **kw):
        raw_sql = """
        DELETE FROM 
            BTI_SUBITEMSNE_{namespace} 
        WHERE 
            TYP_={typ} AND 
            UNIQUEID='{ref}'
        """
        sql = raw_sql.format(
            namespace=Active.namespace,
            **kw
        )
        with connections['erp'].cursor() as cursor:
            cursor.execute(sql)

    @classmethod
    def get_consumed_products(cls, **kw):
        raw_sql = """
        SELECT 
            '3' AS 'GROUP',
            '20' AS 'TYPE',
            'FİŞ' AS 'DOCTRACKNR',
            'SATIS' AS 'AUXILCODE_HEADER',
            'TOPLU' AS 'FOOTNOTE2',
            '353' AS 'CREATEDBY',
            '0' AS 'LINETYPE',
            '1' AS '1',
            '1' AS 'CURRSELTOTALS',
            '1' AS 'UNITCONV1',
            '1' AS 'UNITCONV2',
            IT.CODE AS 'ITEMCODE',
            UN.CODE AS 'UNITCODE',
            NULL AS 'PRICE',
            '1' AS 'COSTRATE',
            SUM(
                ROUND(SI.AMOUNT, 4)
            ) AS 'QUANTITY',
            IT2.CODE AS 'AUXILCODE',
            SI.LOSTFACTOR
        FROM
            [BTI_SUBITEMSNE_{namespace}] as SI 
            LEFT OUTER JOIN LG_{namespace}_ITEMS AS IT WITH (NOLOCK)
                ON SI.ITEMREF = IT.LOGICALREF
            LEFT OUTER JOIN LG_{namespace}_UNITSETL AS UN WITH (NOLOCK)
                ON SI.UOMREF = UN.LOGICALREF
            LEFT OUTER JOIN LG_{namespace}_ITEMS AS IT2 WITH (NOLOCK)
                ON SI.MAINITEMREF = IT2.LOGICALREF
        WHERE 
            BRANCHNO = {branch} AND
            TYP_ = {typ} AND
            UNIQUEID = '{ref}'
        GROUP BY 
            IT.CODE, 
            UN.CODE, 
            IT2.CODE, 
            SI.LOSTFACTOR
        """
        sql = raw_sql.format(
            namespace=Active.namespace,
            **kw
        )
        with connections['erp'].cursor() as cursor:
            cursor.execute(sql)
            items = dict_fetch_all(cursor)
            return items
        return []

    @classmethod
    def production_items(cls, code):
        raw_sql = """
        SELECT 
            ITM.ACTIVE, 
            ITM.LOGICALREF, 
            ITM.CODE, 
            ITM.NAME, 
            ITM.VAT, 
            SETL.CODE AS MAINCODE,
            AC.CODE AS GLCODE,
            ITM.CARDTYPE,
            ISNULL(CR.TYP,0) AS GLTYP
        FROM LG_{NS}_ITEMS ITM
        LEFT JOIN LG_{NS}_CRDACREF CR WITH (NOLOCK) 
            ON ITM.LOGICALREF = CR.CARDREF AND CR.TRCODE=1
        LEFT JOIN LG_{NS}_EMUHACC AC WITH (NOLOCK) 
            ON AC.LOGICALREF = CR.ACCOUNTREF
        LEFT OUTER JOIN LG_{NS}_UNITSETL SETL 
            ON SETL.UNITSETREF=ITM.UNITSETREF AND SETL.LINENR=1
        WHERE 
            ITM.CARDTYPE NOT IN (4,22) AND 
            ITM.CARDTYPE = 12 AND
            ITM.CODE = '{CODE}'
        """
        sql = raw_sql.format(NS=Active.namespace, CODE=code)
        items = list(Items.objects.raw(sql))
        return len(items) > 0

    @classmethod
    def create_request(cls, robotpos, identifier, data):
        return cls.objects.create(
            firm=Active.name,
            identifier=identifier,
            data=json.dumps(data),
            robotpos=robotpos
        )

    @classmethod
    def validate_items(cls, data):
        return all([
            Items.objects.filter(code=item.get('UrunKod'), active=0).exists()
            for item in data
        ])

    @classmethod
    def generate_fiche(cls, data, robotpos, sales):
        request = Active.settings['DEFAULT_SALES'].copy()
        header = SalesConverter(data, {}).data
        request.update(header)

        request.update({
            'NOTES5': robotpos.id
        })

        transactions = []

        for line in data:
            if line.get('UrunKod', None) is None:
                continue

            reqline = Active.settings['DEFAULT_SALES_LINE'].copy()
            item = SalesLineConverter(
                line,
                {}
            ).data

            reqline.update(item)
            transactions.append(reqline)

        request.update({
            'TRANSACTIONS': transactions
        })

        if len(json.dumps(request)) > MAX_CHAR_LIMIT_FOR_XML:
            request.update({
                'TRANSACTIONS': {
                    'items': transactions
                }
            })

            request.update({
                'DATE': datetime.strptime(request.get('DATE'), '%d.%m.%Y').strftime('%Y-%m-%d')
            })
            fiche = MaterialFiche(
                data=request,
                keyword1=robotpos.day,
                keyword2='sales',
                keyword3=robotpos.id
            )
            fiche.is_valid(raise_exception=True)
            fiche.transfer_via_rest()
        else:
            fiche = MaterialFicheXML(
                user=Active.settings['DEFAULT_XML_USER'],
                data=request,
                keyword1=robotpos.day,
                keyword2='sales',
                keyword3=robotpos.id
            )
            fiche.is_valid(raise_exception=True)
            fiche.transfer_via_xml(
                item_name={
                    'TRANSACTIONS': 'TRANSACTION'
                },
                fill_acc_codes=True
            )

        if fiche.flow.success and fiche.flow.internal_ref:
            defaults = {
                'data': robotpos.data,
                'robotpos': robotpos,
                'sales': sales
            }

            # check before insert!
            ProductionQue.objects.update_or_create(
                firm=Active.name,
                identifier=fiche.flow.internal_ref,
                defaults=defaults
            )
            ConsumptionQue.objects.update_or_create(
                firm=Active.name,
                identifier=fiche.flow.internal_ref,
                defaults=defaults
            )
            WasteQue.objects.update_or_create(
                firm=Active.name,
                identifier=fiche.flow.internal_ref,
                defaults=defaults
            )

        return fiche


class SalesQueLog(QueLog):
    pass


class ProductionQue(Que):
    robotpos = models.ForeignKey(Robotpos, on_delete=models.PROTECT)
    sales = models.ForeignKey(SalesQue, on_delete=models.PROTECT)

    @classmethod
    def generate_fiche(cls, identifier, robotpos, sales, instance):
        stfiche = Stfiche.objects.filter(pk=identifier).first()

        if stfiche is None:
            instance.is_cancelled = True
            instance.cancellation_reason = f'Unknown stfiche! {identifier}'
            instance.save()

            raise Exception('Unknown stfiche!')

        request = Active.settings['DEFAULT_PRODUCTION'].copy()
        header = ProductionConverter(stfiche, {}).data
        request.update(header)

        lines = Stline.objects\
            .select_related('stockref', 'stockref__unitsetref')\
                .filter(stficheref__pk=identifier)


        activate = []
        prod_lines = []

        for line in lines:
            if line.stockref is None:
                continue

            is_prod = SalesQue.production_items(line.stockref.code)
            is_combo = line.stockref.code[0:2] == '30'
            if is_prod and is_combo is False:
                if line.stockref.active == 1:
                    activate.append(line.stockref.logicalref)
                prod_lines.append(line)

        if activate:
            Items.objects.filter(
                logicalref__in=activate).update(active=0)


        reqlines = []
        for item in prod_lines:
            temp = Active.settings['DEFAULT_PRODUCTION_LINE'].copy()

            temp.update({
                'ITEM_CODE': item.stockref.code,
                'QUANTITY': item.amount,
                'AUXIL_CODE': item.stockref.code,
                'SOURCEINDEX': stfiche.sourceindex,
                'TRANS_DESCRIPTION': item.lineexp
            })
            try:
                item.uomref
            except models.ObjectDoesNotExist:
                pass
            else:
                temp.update({
                    'UNIT_CODE': item.uomref.code
                })

            reqlines.append(temp)

        request.update({
            'TRANSACTIONS': reqlines,
        })

        if len(json.dumps(request)) > MAX_CHAR_LIMIT_FOR_XML:
            request.update({
                'TRANSACTIONS': {
                    'items': reqlines
                }
            })

            request.update({
                'DATE': stfiche.date_field.strftime('%Y-%m-%d')
            })
            si = MaterialFiche(
                data=request,
                keyword1=robotpos.day,
                keyword2='production',
                keyword3=robotpos.id
            )
            si.is_valid(raise_exception=True)
            si.transfer_via_rest()
        else:
            si = MaterialFicheXML(
                user=Active.settings['DEFAULT_XML_USER'],
                data=request,
                keyword1=robotpos.day,
                keyword2='production',
                keyword3=robotpos.id
            )
            si.is_valid(raise_exception=True)
            si.transfer_via_xml(
                item_name={
                    'TRANSACTIONS': 'TRANSACTION',
                },
                fill_acc_codes=True
            )

        if activate:
            Items.objects.filter(
                logicalref__in=activate).update(active=1)

        return si



class ProductionQueLog(QueLog):
    pass


class ConsumptionQue(Que):
    robotpos = models.ForeignKey(Robotpos, on_delete=models.PROTECT)
    sales = models.ForeignKey(SalesQue, on_delete=models.PROTECT)

    @classmethod
    def generate_fiche(cls, identifier, robotpos, sales, instance):
        stfiche = Stfiche.objects.filter(pk=identifier).first()

        if stfiche is None:
            instance.is_cancelled = True
            instance.cancellation_reason = f'Unknown stfiche! {identifier}'
            instance.save()

            raise Exception('Unknown stfiche!')

        request = Active.settings['DEFAULT_CONSUMPTION'].copy()
        header = ConsumptionConverter(stfiche, {}).data
        request.update(header)

        lines = Stline.objects\
            .select_related('stockref', 'stockref__unitsetref')\
                .filter(stficheref__pk=identifier)

        uref = f'URT-{identifier}'

        for line in lines:
            if line.stockref is None:
                continue
            is_prod = SalesQue.production_items(line.stockref.code)
            if is_prod:
                SalesQue.call_consume_products(
                    line.stockref.pk,
                    line.stockref.pk,
                    line.amount,
                    Active.number,
                    stfiche.sourceindex,
                    5,
                    uref
                )


        consumed = SalesQue.get_consumed_products(
            branch=stfiche.sourceindex,
            typ=5,
            ref=uref
        )

        activate = []

        codes = [i['ITEMCODE'] for i in consumed]

        item_ref = {i.code: i for i in Items.objects.filter(code__in=codes)}

        for line in consumed:
            code = line['ITEMCODE']
            item = item_ref[code]
            if item.active == 1:
                activate.append(item.logicalref)
        if activate:
            Items.objects.filter(logicalref__in=activate).update(active=0)

        reqlines = []
        for line in consumed:
            temp = Active.settings['DEFAULT_CONSUMPTION_LINE'].copy()

            temp.update({
                'ITEM_CODE': line.get('ITEMCODE'),
                'UNIT_CODE': line.get('UNITCODE'),                
                'QUANTITY': line.get('QUANTITY'),                
                'SOURCEINDEX': stfiche.sourceindex,
            })

            if 'AUXILCODE' in line and line['AUXILCODE']:
                temp.update({
                    'AUXIL_CODE': line.get('AUXILCODE')
                })

            reqlines.append(temp)

        SalesQue.clear_consumed_products(
            typ=5,
            ref=uref
        )

        request.update({
            'TRANSACTIONS': reqlines,
        })

        if len(json.dumps(request)) > MAX_CHAR_LIMIT_FOR_XML:
            request.update({
                'TRANSACTIONS': {
                    'items': reqlines
                }
            })

            request.update({
                'DATE': stfiche.date_field.strftime('%Y-%m-%d')
            })
            si = MaterialFiche(
                data=request,
                keyword1=robotpos.day,
                keyword2='consumption',
                keyword3=robotpos.id
            )
            si.is_valid(raise_exception=True)
            si.transfer_via_rest()
        else:
            si = MaterialFicheXML(
                user=Active.settings['DEFAULT_XML_USER'],
                data=request,
                keyword1=robotpos.day,
                keyword2='consumption',
                keyword3=robotpos.id
            )
            si.is_valid(raise_exception=True)
            si.transfer_via_xml(
                item_name={
                    'TRANSACTIONS': 'TRANSACTION'
                },
                fill_acc_codes=True
            )

        if activate:
            Items.objects.filter(
                logicalref__in=activate).update(active=1)

        return si


class ConsumptionQueLog(QueLog):
    pass


class WasteQue(Que):
    robotpos = models.ForeignKey(Robotpos, on_delete=models.PROTECT)
    sales = models.ForeignKey(SalesQue, on_delete=models.PROTECT)

    @classmethod
    def generate_fiche(cls, identifier, robotpos, sales, instance):
        stfiche = Stfiche.objects.filter(pk=identifier).first()

        if stfiche is None:
            instance.is_cancelled = True
            instance.cancellation_reason = f'Unknown stfiche! {identifier}'
            instance.save()

            raise Exception('Unknown stfiche!')

        request = Active.settings['DEFAULT_WASTE'].copy()
        header = WasteConverter(stfiche, {}).data
        request.update(header)

        lines = Stline.objects\
            .select_related('stockref', 'stockref__unitsetref')\
                .filter(stficheref__pk=identifier)

        uref = f'SRF-{identifier}'

        for line in lines:
            if line.stockref is None:
                continue

            is_prod = SalesQue.production_items(line.stockref.code)

            if is_prod is False:

                SalesQue.call_consume_products(
                    line.stockref.pk,
                    line.stockref.pk,
                    line.amount,
                    Active.number,
                    stfiche.sourceindex,
                    5,
                    uref
                )

        consumed = [i for i in SalesQue.get_consumed_products(
            branch=stfiche.sourceindex,
            typ=5,
            ref=uref
        ) if i['LOSTFACTOR'] > 0]

        activate = []

        codes = [i['ITEMCODE'] for i in consumed]

        item_ref = {i.code: i for i in Items.objects.filter(code__in=codes)}

        for line in consumed:
            code = line['ITEMCODE']
            item = item_ref[code]
            if item.active == 1:
                activate.append(item.logicalref)

        if activate:
            Items.objects.filter(logicalref__in=activate).update(active=0)

        reqlines = []

        for line in consumed:
            code = line.get('ITEMCODE')

            temp = Active.settings['DEFAULT_WASTE_LINE'].copy()

            quantity = (line.get('LOSTFACTOR') / 100.0) * line.get('QUANTITY')

            temp.update({
                'ITEM_CODE': code,
                'UNIT_CODE': line.get('UNITCODE'),                
                'QUANTITY': quantity,
                'SOURCEINDEX': stfiche.sourceindex
            })

            if 'AUXILCODE' in line and line['AUXILCODE']:
                temp.update({
                    'AUXIL_CODE': line.get('AUXILCODE')
                })
            reqlines.append(temp)

        SalesQue.clear_consumed_products(
            typ=5,
            ref=uref
        )

        request.update({
            'TRANSACTIONS': reqlines,
        })

        if len(json.dumps(request)) > MAX_CHAR_LIMIT_FOR_XML:
            request.update({
                'TRANSACTIONS': {
                    'items': reqlines
                }
            })

            request.update({
                'DATE': stfiche.date_field.strftime('%Y-%m-%d')
            })
            si = MaterialFiche(
                data=request,
                keyword1=robotpos.day,
                keyword2='waste',
                keyword3=robotpos.id
            )
            si.is_valid(raise_exception=True)
            si.transfer_via_rest()
        else:
            si = MaterialFicheXML(
                user=Active.settings['DEFAULT_XML_USER'],
                data=request,
                keyword1=robotpos.day,
                keyword2='waste',
                keyword3=robotpos.id
            )

            si.is_valid(raise_exception=True)
            si.transfer_via_xml(
                item_name={
                    'TRANSACTIONS': 'TRANSACTION'
                },
                fill_acc_codes=True
            )

        if activate:
            Items.objects.filter(
                logicalref__in=activate).update(active=1)

        return si


class WasteQueLog(QueLog):
    pass
