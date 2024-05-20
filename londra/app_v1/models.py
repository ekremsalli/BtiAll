import hashlib
import json

from django.db import connections
from rest_framework.exceptions import APIException

from bti.models.que import Que, QueLog
from erp.active import Active

from erp.asking.material import (
    MaterialFiche,
)
from erp.models.friendly import Items
from common.utils import (
    dict_fetch_all,
    remove_empty_from_dict,
)


class Other():
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


class CommonQue():
    @classmethod
    def generate_identifier(cls, data):
        if data is None:
            raise APIException('İstek gövdesi boş bırakılamaz!')

        return hashlib.md5(
            json.dumps(data).encode('utf-8')
        ).hexdigest()

    @classmethod
    def create_request(cls, identifier, data):
        return cls.objects.create(
            firm=Active.name,
            identifier=identifier,
            data=json.dumps(data),
        )


class TransferQue(Que, CommonQue):
    @classmethod
    def validate(cls, data):
        request = Active.settings['DEFAULT_TRANSFER'].copy()
        request.update(data)
        mf = MaterialFiche(
            data=request
        )
        mf.is_valid(raise_exception=True)

    @classmethod
    def generate_fiche(cls, data):
        request = Active.settings['DEFAULT_TRANSFER'].copy()
        request.update(data.get('data'))

        mf = MaterialFiche(
            data=request
        )
        mf.is_valid(raise_exception=True)
        mf.transfer_via_rest()
        return mf


class TransferQueLog(QueLog):
    pass


class SlipQue(Que, CommonQue):
    @classmethod
    def generate_fiche(cls, data):
        is_transfer = data.get('data').get('transfer', '0') == '1'

        production = remove_empty_from_dict(
            data.get('data').get('productionVoucher')
        )

        prod_mf = MaterialFiche(
            data=production
        )
        prod_mf.is_valid(raise_exception=True)
        prod_mf.transfer_via_rest()

        if prod_mf:
            prod_mf.flow.data = data
            prod_mf.flow.save()
            if prod_mf.flow and prod_mf.flow.is_success():
                consume = remove_empty_from_dict(
                    data.get('data').get('consumeVoucher')
                )
                cons_mf = MaterialFiche(
                    data=consume,
                    prev_flow=prod_mf.flow
                )
                cons_mf.is_valid(raise_exception=True)
                cons_mf.transfer_via_rest()

                if cons_mf:
                    cons_mf.flow.data = data
                    cons_mf.flow.save()

                    if cons_mf.flow and cons_mf.flow.is_success():
                        if is_transfer:
                            prod_rb = MaterialFiche(skip_flow=True)\
                                .retrieve(
                                    suffix=prod_mf.flow.internal_ref,
                                    params={'expandLevel': 'full'}
                                )
                            cons_rb = MaterialFiche(skip_flow=True)\
                                .retrieve(
                                    suffix=cons_mf.flow.internal_ref,
                                    params={'expandLevel': 'full'}
                                )

                            cons_rb['FROMTRANSFER'] = 1
                            cons_rb['DOC_TRACK_NR'] = prod_rb['NUMBER']
                            cons_rb['TRANSACTIONS']['items'][0].update(
                                {
                                    'RELTRANSLNREF': prod_rb['TRANSACTIONS']['items'][0]['INTERNAL_REFERENCE']
                                }
                            )
                            cons_rb['TRANSACTIONS']['items'][0]['FROMTRANSFER'] = 1

                            rev_cons = MaterialFiche(
                                data=remove_empty_from_dict(cons_rb),
                                prev_flow=cons_mf.flow
                            )
                            rev_cons.is_valid(raise_exception=True)
                            rev_cons.update(pk=cons_mf.flow.internal_ref)

                            prod_rb['FROMTRANSFER'] = 1
                            prod_rb['DOC_TRACK_NR'] = cons_rb['NUMBER']
                            prod_rb['TRANSACTIONS']['items'][0].update(
                                {
                                    'RELTRANSLNREF': cons_rb['TRANSACTIONS']['items'][0]['INTERNAL_REFERENCE']
                                }
                            )
                            prod_rb['TRANSACTIONS']['items'][0]['FROMTRANSFER'] = 1


                            rev_prod = MaterialFiche(
                                data=remove_empty_from_dict(prod_rb),
                                prev_flow=rev_cons.flow
                            )
                            rev_prod.is_valid(raise_exception=True)
                            rev_prod.update(pk=prod_mf.flow.internal_ref)
                            return prod_mf
                        else:
                            return prod_mf
                    else:
                        raise Exception(f'Sarf fişi oluşturulamadı! {cons_mf.flow}')
                else:
                    raise Exception(f'Sarf fişi bulunamadı!')
            else:
                raise Exception(f'Üretim fişi oluşturulamadı! {prod_mf.flow}')
            
        raise Exception(f'İşlem gerçekleştirelemedi! {prod_mf}')  


class SlipQueLog(QueLog):
    pass
