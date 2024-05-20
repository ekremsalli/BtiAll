import json
from django.db import models
from django.conf import settings
from rest_framework.exceptions import APIException


from erp.active import Active
from bti.models.track import Track
from erp.asking.material import MaterialCard
from erp.asking.current import ClCard
from erp.asking.orders import (
    SalesOrder,
    PurchaseOrder,
)
from erp.asking.invoice import (
    SalesInvoice,
)

from erp.models.friendly import (
    Clcard,
    UnitBarcode,
    Stfiche,
    Stline,
    Itmunita,
)
from erp.helpers import calculate_logo_time
from third_party.elogo.api import Elogo

from dateutil import parser
from app_v1.converters import (
    InvoiceConverter,
    InvoiceLineConverter,
    EConverter
)


class ArpTrack(Track):
    data_map = {
        'CODE': 'code',
        # 'TITLE': 'title',
        'TITLE2': 'title2',
        'ADDRESS1': 'address1',
        'ADDRESS2': 'address2',
        'TOWN': 'town',
        'CITY': 'city',
        'TELEPHONE1': 'telephone1',
        'TELEPHONE2': 'telephone2',
        'E_MAIL': 'e_mail',
        'WEB_URL': 'web_url',
        'PERSCOMPANY': 'perscompany',
        'TCKNO': 'tckno',
        'NAME': 'name',
        'SURNAME': 'surname',
        'TAX_ID': 'tax_id',
        'TAX_OFFICE': 'tax_office',
        'ACCOUNT_TYPE': 'account_type',
        'COUNTRY_CODE': 'country_code',
        'COUNTRY': 'country',
        'CORRESP_LANG': 'corresp_lang',
        'CL_ORD_FREQ': 'cl_ord_freq',
        'ORD_DAY': 'ord_day',
        'PURCHBRWS': 'purchbrws',
        'SALESBRWS': 'salesbrws',
        'IMPBRWS': 'impbrws',
        'EXPBRWS': 'expbrws',
        'FINBRWS': 'finbrws',
        'POSTAL_CODE': 'postal_code',
        'DISTRICT': 'district',
        'TRADING_GRP': 'trading_group',
    }

    @staticmethod
    def echeck(identity, data):
        elogo = Elogo(
            Active.settings['ELOGO_USER'],
            Active.settings['ELOGO_PWD']
        )
        elogo.login()
        gib = elogo.validate_gib(identity)
        if gib:
            if gib['ISGIBUSER'] == "1":
                data['ACCEPT_EINV'] = 1
                data['POST_LABEL'] = gib.get('EINVOICEPKALIAS', '-')
                data['SENDER_LABEL'] = gib.get('EDESPATCHGBALIAS', '-')
                if len(gib.get('EDESPATCHGBALIAS', '')):
                    data['ACCEPT_DESP'] = 1
                    data['SENDER_LABEL_CODE_DESP'] = gib.get(
                        'EDESPATCHGBALIAS', '-')
                    data['POST_LABEL_CODE_DESP'] = gib.get(
                        'EDESPATCHPKALIAS', '-')
        return data

    @classmethod
    def update_card(cls, data, pk):
        veri = {}
        for k, v in cls.data_map.items():
            if data.get(v):
                veri.update({k: data.get(v)})

        mc = ClCard(data=veri, partial=True)
        mc.is_valid(raise_exception=True)
        mc.partial_update(pk)

        return mc

    @classmethod
    def create_card(cls, data):
        kodlama = Active.settings['KODLAMA']
        veri = kodlama['CARI_KART'].copy()

        for k, v in cls.data_map.items():
            if data.get(v):
                veri.update({k: data.get(v)})

        elogo = Elogo(
            Active.settings['ELOGO_USER'],
            Active.settings['ELOGO_PWD']
        )
        elogo.login()

        identity = None
        if data.get('tax_id'):
            identity = data.get('tax_id')
        elif data.get('tckno'):
            identity = data.get('tckno')
        if identity:
            veri = cls.echeck(identity, veri)

        check_user = elogo.checkGibUser(identity)

        if check_user and 'userList' in check_user and 'Title' in check_user['userList']:
            title = check_user['userList']['Title']
            veri.update({'TITLE': title})
        else:
            title = data.get('title', '')
            veri.update({'TITLE': title})

        mc = ClCard(data=veri)
        mc.is_valid(raise_exception=True)
        mc.create()

        if mc.flow.success and mc.flow.internal_ref:
            mc.flow.data = json.dumps(data)
            mc.flow.save()
        return mc, title, mc.flow


class OrderTrack(Track):
    @classmethod
    def cancel_order(cls, number, fiche, sales_order):
        veri = {
            'ORDER_STATUS': 2,
            'NUMBER': f'K-{number}',
            'DATE': fiche.date_field.strftime('%Y-%m-%d')
        }
        if sales_order:
            so = SalesOrder(data=veri)
        else:
            so = PurchaseOrder(data=veri)

        so.partial_update(fiche.pk)
        return so

    @classmethod
    def create_order(cls, data, pk=None, sales_order=None):
        kodlama = Active.settings['KODLAMA']
        veri = kodlama['SIPARIS_KARTI'].copy()
        data_map = {
            "DOC_NUMBER": "doc_number",
            "AUTH_CODE": "auth_code",
            "SOURCE_WH": "source_wh",
            "SHIPPING_AGENT": "shipping_agent",
            "NOTES1": "notes1",
            "NOTES2": "notes2",
            "NOTES3": "notes3",
            "NOTES4": "notes4",
            "PROJECT_CODE": "project_code",
            "VATEXCEPT_CODE": "vatexcept_code",
            "VATEXCEPT_REASON": "vatexcept_reason",
            "DOC_TRACK_NR": "doctrackingnr"
        }
        dt = parser.parse(data.get('date'))
        veri.update({
            'NUMBER': data.get('number'),
            'DATE': dt.strftime('%Y-%m-%d'),
            'TIME': calculate_logo_time(dt),
        })

        einfo = EConverter(
            data.get('EArchiveInfo'),
            settings.MAPPING['ECONVERTER']
        ).data

        veri.update(einfo)

        for k, v in data_map.items():
            if data.get(v):
                veri.update({k: data.get(v)})
        # query arp!
        arp = data.get('arp')
        card = Clcard.objects.filter(code=arp.get('code')).first()
        aobj = None
        ctitle = ""
        if card is None:
            aobj, title, cflow = ArpTrack.create_card(arp)
            ctitle += title
            card = Clcard.objects.filter(code=arp.get('code')).first()
        veri.update({
            'ARP_CODE': card.code
        })

        if card.accepteinv == 1:
            veri.update({
                'EINVOICE': 1,
                'EINVOICE_PROFILEID': card.profileid
            })

        items = []
        for item in data.get('transactions'):

            line = kodlama['SIPARIS_KARTI_SATIRI'].copy()
            if 'barcode' in item:
                xunit = UnitBarcode.objects.filter(
                    barcode=item.get('barcode')).first()
                if xunit and xunit.itemref:
                    line.update({
                        'MASTER_CODE': xunit.itemref.code,
                    })

            if 'master_code' in item:
                line.update({
                    'MASTER_CODE': item.get('master_code')
                })

            line.update({
                'TYPE': item.get('type'),
                'ORDER_CLOSED': item.get('order_closed')
            })

            if 'quantity' in item and item.get('quantity'):
                line.update({
                    'QUANTITY': item.get('quantity'),
                })
            if 'price' in item and item.get('price'):
                line.update({
                    'PRICE': item.get('price'),
                })
            if 'total' in item and item.get('total'):
                line.update({
                    'TOTAL': item.get('total'),
                })

            if 'vat_rate' in item and item.get('vat_rate'):
                line.update({
                    'VAT_RATE': item.get('vat_rate'),
                })
            if 'unit_code' in item and item.get('unit_code'):
                line.update({
                    'UNIT_CODE': item.get('unit_code'),
                })
            if 'unit_conv1' in item and item.get('unit_conv1'):
                line.update({
                    'UNIT_CONV1': item.get('unit_conv1'),
                })
            if 'unit_conv2' in item and item.get('unit_conv2'):
                line.update({
                    'UNIT_CONV2': item.get('unit_conv2'),
                })
            if 'project_code' in item and item.get('project_code'):
                line.update({
                    'PROJECT_CODE': item.get('project_code')
                })

            if 'vatexcept_reason' in item and item.get('vatexcept_reason'):
                line.update({
                    'VATEXCEPT_REASON': item.get('vatexcept_reason')
                })

            if 'vatexcept_code' in item and item.get('vatexcept_code'):
                line.update({
                    'VATEXCEPT_CODE': item.get('vatexcept_code')
                })
            if 'vat_included' in item:
                line.update({
                    'VAT_INCLUDED': 1 if item.get('vat_included') == True else 0
                })

            if 'discount_rate' in item:
                line.update({
                    'DISCOUNT_RATE': item.get('discount_rate')
                })

            if 'detail_level' in item:
                line.update({
                    'DETAIL_LEVEL': item.get('detail_level')
                })

            if 'calc_type' in item:
                line.update({
                    'CALC_TYPE': item.get('calc_type')
                })

            items.append(line)

        if len(items) == 0:
            raise APIException('Sipariş satırları boş!')

        veri.update({
            'TRANSACTIONS': {
                'items': items
            }
        })

        if sales_order is None:
            if data.get('sales_order'):
                so = SalesOrder(
                    data=veri, prev_flow=aobj.flow if aobj else None)
            else:
                so = PurchaseOrder(
                    data=veri, prev_flow=aobj.flow if aobj else None)
        else:
            if sales_order:
                so = SalesOrder(
                    data=veri, prev_flow=aobj.flow if aobj else None)
            else:
                so = PurchaseOrder(
                    data=veri, prev_flow=aobj.flow if aobj else None)

        so.is_valid(raise_exception=True)

        if pk:
            so.update(pk=pk)
            if so.flow.success and so.flow.internal_ref:
                so.flow.data = json.dumps(data)
                so.flow.save()
        else:
            so.create()
            if so.flow.success and so.flow.internal_ref:
                so.flow.data = json.dumps(data)
                so.flow.save()
        return so, aobj, ctitle


class ItemTrack(Track):
    @classmethod
    def update_item(cls, data, suffix, items=[]):
        veri = {}
        data_map = {
            'CARD_TYPE': 'card_type',
            'CODE': 'code',
            'NAME': 'name',
            'PRODUCER_CODE': 'producer_code',
            'AUXIL_CODE': 'auxil_code',
            'VAT': 'vat',
            'USEF_SALES': 'usef_sales',
            'USEF_PURCHASING': 'usef_purchasing',
            'USEF_MM': 'usef_mm',
            'UNITSET_CODE': 'unitset_code',
            'SELVAT': 'sel_vat',
            'RETURNVAT': 'return_vat',
            'SELPRVAT': 'sellpr_vat',
            'RETURNPRVAT': 'returnpr_vat',
            'MARKCODE': 'markcode'
        }
        for k, v in data_map.items():
            if data.get(v):
                veri.update({k: data.get(v)})
        veri.update({"IMAGEINC": 1, })

        veri.update({'UNITS': {'items': items}})
        mc = MaterialCard(data=veri, partial=True)
        mc.is_valid(raise_exception=True)
        mc.partial_update(suffix)

        return mc

    @classmethod
    def create_item(cls, data):
        kodlama = Active.settings['KODLAMA']
        print("KODLAMA", kodlama)
        veri = kodlama['MALZEME_KARTI'].copy()
        print("VERİ", kodlama)
        veri.update({
            'CARD_TYPE': data.get('card_type'),
            'CODE': data.get('code'),
            "IMAGEINC": 1,
            'NAME': data.get('name'),
            'PRODUCER_CODE': data.get('producer_code'),
            'AUXIL_CODE': data.get('auxil_code'),
            'VAT': data.get('vat'),
            'UNITSET_CODE': data.get('unitset_code'),
        })

        if data.get('usef_sales') and data.get('usef_sales') == 1:
            veri.update({
                'USEF_SALES': data.get('usef_sales')
            })

        if data.get('usef_purchasing') and data.get('usef_purchasing') == 1:
            veri.update({
                'USEF_PURCHASING': data.get('usef_purchasing'),
            })

        if data.get('usef_mm') and data.get('usef_mm') == 1:
            veri.update({
                'USEF_MM': data.get('usef_mm'),
            })

        if 'sel_vat' in data and data.get('sel_vat'):
            veri.update({
                'SELVAT': data.get('sel_vat')
            })

        if 'return_vat' in data and data.get('return_vat'):
            veri.update({
                'RETURNVAT': data.get('return_vat')
            })

        if 'selpr_vat' in data and data.get('selpr_vat'):
            veri.update({
                'SELPRVAT': data.get('selpr_vat')
            })

        if 'returnpr_vat' in data and data.get('returnpr_vat'):
            veri.update({
                'RETURNPRVAT': data.get('returnpr_vat')
            })

        if 'markcode' in data and data.get('markcode'):
            veri.update({
                'MARKCODE': data.get('markcode')
            })

        birimler = []
        for item in data.get('units'):
            birim = kodlama['MALZEME_KARTI_BIRIM_TANIMI'].copy()
            birim.update({
                'UNIT_CODE': item.get('unit_code'),
                'BARCODE_LIST': {
                    "items": [
                        {
                            "BARCODE": item.get('barcode')
                        }
                    ]
                },
                'CONV_FACT1': item.get('conv_fact1'),
                'CONV_FACT2': item.get('conv_fact2')
            })
            if item.get('usef_mrtlclass') and item.get('usef_mrtlclass') == 1:
                birim.update({
                    'USEF_MRTLCLASS': item.get('usef_mrtlclass'),
                })

            if item.get('usef_purchaseclass') and item.get('usef_purchaseclass') == 1:
                birim.update({
                    'USEF_PURCHASECLASS': item.get('usef_purchaseclass'),
                })

            if item.get('usef_salesclass') and item.get('usef_salesclass') == 1:
                birim.update({
                    'USEF_SALESCLASS': item.get('usef_salesclass'),
                })

            birimler.append(birim)
        veri.update({
            'UNITS': {'items': birimler}
        })
        mc = MaterialCard(data=veri)
        mc.is_valid(raise_exception=True)
        mc.create()
        if mc.flow.success and mc.flow.internal_ref:
            mc.flow.data = json.dumps(data)
            mc.flow.save()

            for item in data.get('units'):
                change = 0
                unit = UnitBarcode.objects.filter(
                    barcode=item.get('barcode')).first()
                if unit and unit.itmunitaref:
                    item_unit = Itmunita.objects.filter(
                        pk=unit.itmunitaref).first()
                    if item_unit:
                        if item.get('usef_mrtlclass') and item.get('usef_mrtlclass') == 1:
                            item_unit.mtrlclas = 1
                            change += 1

                        if item.get('usef_purchaseclass') and item.get('usef_purchaseclass') == 1:
                            item_unit.purchclas = 1
                            change += 1

                        if item.get('usef_salesclass') and item.get('usef_salesclass') == 1:
                            item_unit.salesclas = 1
                            change += 1

                        if change > 0:
                            item_unit.save()

        return mc


class S3Resource(models.Model):
    prefix = models.CharField(max_length=6, unique=True)
    aws_access_key = models.CharField(max_length=255)
    aws_access_secret = models.CharField(max_length=255)
    bucket = models.CharField(max_length=255)
    region = models.CharField(max_length=100)


class InvoiceTrack(Track):
    @classmethod
    def create_invoice(cls, data, identifier):
        config = Active.settings.get('KODLAMA')

        request = config.get('FATURA').copy()

        header = InvoiceConverter(
            data,
            settings.MAPPING['INVOICE']
        ).data

        einfo = EConverter(
            data.get('EArchiveInfo'),
            settings.MAPPING['ECONVERTER']
        ).data
        request.update(header)
        request.update(einfo)

        arp = Clcard.objects.filter(code=data.get('ARP_CODE')).first()
        if arp:
            if arp.accepteinv == 1:
                request.update({
                    'EINVOICE': 1,
                    'EINVOICE_PROFILEID': arp.profileid
                })

        reqlines = []
        dispatches = []

        if data.get('Dispatches'):
            xdispatch = Stfiche.objects.filter(
                ficheno=data.get('Dispatches')[0],
                **config.get('IRSALIYE_SORGU')
            ).first()

            if xdispatch and xdispatch.shpagncod:
                request.update({
                    'SHIPPING_AGENT': xdispatch.shpagncod
                })

            if xdispatch:
                request.update({
                    'EDESPATCH': xdispatch.edespatch,
                    'EDESPATCH_STATUS': xdispatch.edespstatus,
                })

        dispatch_origins = {}

        # iterate dispatches!
        for ficheno in data.get('Dispatches'):
            dispatch = Stfiche.objects.filter(
                ficheno=ficheno,
                **config.get('IRSALIYE_SORGU')
            ).first()
            if dispatch:
                dispatch_origins[ficheno] = {
                    'created': dispatch.created,
                    'genexp1': dispatch.genexp1,
                    'genexp2': dispatch.genexp2,
                    'genexp3': dispatch.genexp3,
                    'genexp4': dispatch.genexp4,
                    'genexp5': dispatch.genexp5,
                    'genexp6': dispatch.genexp6,
                    'specode': dispatch.specode,
                    'cyphcode': dispatch.cyphcode,
                }

                new_dispatch = config.get('FATURA_IRSALIYE').copy()
                new_dispatch.update({
                    'TYPE': dispatch.trcode,
                    'NUMBER': dispatch.ficheno,
                    'DATE': dispatch.date_field.strftime('%Y-%m-%d'),
                    'TIME': dispatch.ftime,
                    'DIVISION': dispatch.branch,
                    'DATA_REFERENCE': dispatch.pk,
                    'DISP_STATUS': dispatch.dispstatus,
                    'GUID': dispatch.guid,
                    'SOURCE_WH': header.get('SOURCE_WH'),
                    # 'ARP_CODE': header.get('ARP_CODE'),
                    'SHIP_DATE': dispatch.shipdate.strftime('%Y-%m-%d'),
                    'SHIP_TIME': dispatch.shiptime,
                })
                if dispatch.docode:
                    new_dispatch.update({
                        'DOC_NUMBER': dispatch.docode
                    })

                arp = Clcard.objects.filter(code=data.get('ARP_CODE')).first()
                if arp:
                    if arp.accepteinv == 1:
                        new_dispatch.update({
                            'EINVOICE': 1,
                            'EINVOICE_PROFILEID': arp.profileid
                        })
                else:
                    new_dispatch.update({
                        'ENVOICE': 2
                    })

                new_dispatch.update({
                    'EDESPATCH': dispatch.edespatch,
                    'EDESPATCH_STATUS': dispatch.edespstatus,
                })
                if dispatch.shpagncod:
                    new_dispatch.update({
                        'SHIPPING_AGENT': dispatch.shpagncod
                    })

                dispatches.append(new_dispatch)

                for line in Stline.objects.filter(stficheref=dispatch):
                    if line.linetype == 0:
                        new_line = config.get('FATURA_SATIR').copy()
                        new_line.update({
                            'TYPE': line.linetype,
                            'SOURCEINDEX': line.sourceindex,
                            'QUANTITY': line.amount,
                            'PRICE': line.price,
                            'UNIT_CONV1': line.uinfo1,
                            'UNIT_CONV2': line.uinfo2,
                            'UNIT_CONV3': line.uinfo3,
                            'UNIT_CONV4': line.uinfo4,
                            'UNIT_CONV5': line.uinfo5,
                            'VAT_RATE': line.vat,
                            'PROJECT_CODE': header.get('PROJECT_CODE'),
                            'DISPATCH_NUMBER': dispatch.ficheno,
                            'DATA_REFERENCE': line.pk,
                            # 'ORDER_REFERENCE': line.ordficheref.pk
                        })
                        if line.lineexp:
                            new_line.update({
                                'DESCRIPTION': line.lineexp
                            })
                        if header.get('PAYMENT_CODE'):
                            new_line.update({
                                'PAYMENT_CODE': header.get('PAYMENT_CODE'),
                            })
                        if line.stockref and line.stockref.code:
                            new_line.update({
                                'MASTER_CODE': line.stockref.code,
                            })
                        try:
                            if line.accountref and line.accountref.code:
                                new_line.update({
                                    'GL_CODE1': line.accountref.code,
                                })
                        except:
                            pass

                        try:
                            if line.vataccref and line.vataccref.code:
                                new_line.update({
                                    'GL_CODE2': line.vataccref.code,
                                })
                        except:
                            pass
                        try:
                            if line.uomref and line.uomref.code:
                                new_line.update({
                                    'UNIT_CODE': line.uomref.code,
                                })
                        except:
                            pass
                        reqlines.append(new_line)
                    else:
                        new_line = {
                            'TYPE': line.linetype,
                            'DISPATCH_NUMBER': dispatch.ficheno,
                            'DATA_REFERENCE': line.pk,
                            'STFICHEREF': dispatch.pk,
                        }

                        if line.calctype == 1:
                            new_line.update({
                                'CALC_TYPE': line.calctype,
                                'DETAIL_LEVEL': line.detline,
                                'TOTAL': line.total,
                                'DISCEXP_CALC': 1,
                            })
                        else:
                            new_line.update({
                                'DISCOUNT_RATE': line.discper
                            })
                        reqlines.append(new_line)

        for line_data in data.get('Lines'):
            new_line = config.get('FATURA_SATIR_HARICI').copy()
            extline = InvoiceLineConverter(
                line_data,
                settings.MAPPING['INVOICE_LINE']
            ).data
            new_line.update(extline)

            if 'detail_level' in line_data:
                new_line.update({
                    'DETAIL_LEVEL': line_data.get('detail_level')
                })

            if 'calc_type' in line_data:
                new_line.update({
                    'CALC_TYPE': line_data.get('calc_type')
                })

            if 'discexp_calc' in line_data:
                new_line.update({
                    'DISCEXP_CALC': line_data.get('discexp_calc')
                })

            if 'discount_rate' in line_data:
                new_line.update({
                    'DISCOUNT_RATE': line_data.get('discount_rate')
                })

            reqlines.append(new_line)

        request.update({
            'TRANSACTIONS': {
                'items': reqlines,
            },
            'DISPATCHES': {
                'items': dispatches
            },
            'PAYMENT_LIST': {
                'items': []
            }
        })

        si = SalesInvoice(
            data=request
        )
        si.is_valid(raise_exception=True)
        si.transfer_via_rest()

        if si.flow.success and si.flow.internal_ref:
            si.flow.data = json.dumps(data)
            si.flow.save()

        for fno, fblock in dispatch_origins.items():
            for fkey, fval in fblock.items():
                if fval:
                    Stfiche.objects.filter(
                        ficheno=fno,
                        **config.get('IRSALIYE_SORGU')
                    ).update(
                        **{fkey: fval}
                    )

        return si

    @classmethod
    def create_return_invoice(cls, data):

        config = Active.settings.get('KODLAMA')
        request = config.get('FATURA').copy()

        request.update({'NUMBER': '~'})
        if data.get('DateTime'):
            request.update({'DATE': data.get('DateTime')})
        if data.get('ARP_CODE'):
            request.update({'ARP_CODE': data.get('ARP_CODE')})

        if data.get('type'):
            request.update({'TYPE': data.get('type')})

        satir = data.get('Lines')
        new_line = []

        if satir:
            for line in satir:
                lines = config.get('FATURA_SATIR').copy()
                if line.get('LineType'):
                    lines.update({
                        "TRCODE": line.get('LineType')
                    })
                if line.get('Quantity'):
                    lines.update({
                        "QUANTITY": line.get('Quantity')
                    })

                # if line.get('UnitPrice'):
                #     lines.update({
                #         "PRICE": line.get('UnitPrice')
                #     })

                if line.get('VAT'):
                    lines.update({
                        "VAT_RATE": line.get('VAT')
                    })

                if line.get('date_field'):
                    lines.update({
                        "DATE": line.get('date_field')
                    })
                if line.get('master_code'):
                    lines.update({
                        "MASTER_CODE": line.get('master_code')
                    })

                if line.get('unit_code'):
                    lines.update({
                        "UNIT_CODE": line.get('unit_code')
                    })

                if line.get('source_reference'):
                    lines.update({
                        "SOURCE_REFERENCE": line.get('source_reference')
                    })

                if line.get('ret_cost_type'):
                    lines.update({
                        "RET_COST_TYPE": line.get('ret_cost_type')
                    })

                if line.get('rest_cost'):
                    lines.update({
                        "RET_COST": line.get('rest_cost')
                    })

                new_line.append(lines)

        request.update({
            'TRANSACTIONS': {
                'items': new_line,
            },
            'DISPATCHES': {
                'items': []
            },
            'PAYMENT_LIST': {
                'items': []
            }
        })

        si = SalesInvoice(data=request)
        si.is_valid(raise_exception=True)
        si.transfer_via_rest()

        return si
