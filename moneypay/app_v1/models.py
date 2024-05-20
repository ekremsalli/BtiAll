import json
from uuid import uuid4
from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models

from bti.models.que import Que, QueLog
from bti.models.flow import Flow
from erp.active import Active
from erp.models.friendly import (
    Clcard,
    Shipinfo,
)
from erp.asking.current import ClCard as iClcard
from erp.asking.current import ClShipment
from erp.asking.invoice import SalesInvoice, SalesInvoiceXML
from erp.asking.account import Emfiche, EmficheXML


from app_v1.helper import Helper


class Operation(models.Model):
    code = models.CharField(max_length=64, unique=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["code"]


class OperationDetail(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.DO_NOTHING)
    field = models.CharField(max_length=64)
    account = models.CharField(max_length=64)
    is_debit = models.BooleanField(default=True)
    formula = models.TextField(default='n')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["pk"]


class TaskActivity(models.Model):
    name = models.CharField(max_length=65, db_index=True)
    is_success = models.BooleanField(db_index=True)
    params = models.TextField(null=True, blank=True)
    exception = models.TextField(null=True, blank=True)
    took = models.FloatField(default=0)
    created = models.DateTimeField(auto_now=True)


class XT_100(models.Model):
    logref = models.AutoField(db_column='LOGREF', primary_key=True)
    parlogref = models.IntegerField(
        db_column='PARLOGREF', unique=True, blank=True, null=True)
    uuid = models.CharField(db_column='UUID', max_length=100,
                            db_collation='Turkish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = f'LG_XT100_{Active.namespace}'
        target_db = 'erp'


class InvoiceBucket(Que):
    day = models.DateField(db_index=True)
    uid = models.CharField(max_length=128, db_index=True)
    is_company = models.BooleanField(db_index=True, default=False)

    def get_data(self):
        return json.loads(self.data)

    @classmethod
    def create_request(cls, ref, data):
        obj, _ = cls.objects.update_or_create(
            firm=Active.name,
            identifier=ref,
            defaults={
                'data': json.dumps(data),
                'day': data.get('day'),
                'uid': data.get('uid'),
                'is_company': data.get('is_company')
            }
        )
        return obj


class InvoiceBucketLog(QueLog):
    pass


class InvoiceQue(Que, Helper):
    is_company = models.BooleanField(db_index=True, default=False)
    items = models.ManyToManyField(InvoiceBucket)
    invoice_ref = models.IntegerField(null=True, blank=True)
    flow = models.ForeignKey(Flow,
                             null=True,
                             on_delete=models.SET_NULL
                             )

    def get_data(self):
        return json.loads(self.data)

    @classmethod
    def get_or_create_shipment_card(cls, data, arp=None):
        config = Active.settings

        taxnr = data.get('taxnr')
        mernis = data.get('mernis')

        identifier = data.get('address_id', None)
        if identifier is None:
            identifier = taxnr and len(taxnr) if taxnr else mernis

            if len(identifier) == 0:
                identifier = data.get('uid')

        ship = Shipinfo.objects.filter(
            code=f'A-{identifier}'
        ).last()
        if ship:
            return ship
        else:
            request = config['SEVKIYAT']['SEVKIYAT_KARTI'].copy()

            if arp is not None:
                request.update({
                    'ARP_CODE': arp
                })

            request.update({
                'CODE': f'A-{identifier}'
            })

            full_name = data.get('name') + ' ' + data.get('surname')
            if full_name and len(full_name.strip()) > 0:
                request.update({
                    'INCHANGE': full_name
                })

            request.update({
                'DESCRIPTION': data.get('uid')
            })

            if data.get('title'):
                request.update({
                    'TITLE': data.get('title')
                })

            if data.get('gsm'):
                request.update({
                    'TELEPHONE1': data.get('gsm')
                })

            request.update({
                'TAX_NR': identifier
            })

            if data.get('city'):
                request.update({
                    'CITY': data.get('city')
                })

            if data.get('district'):
                request.update({
                    'TOWN': data.get('district')
                })

            if data.get('email'):
                request.update({
                    'EMAIL_ADDR': data.get('email')[0:50]
                })

            if data.get('zipcode'):
                request.update({
                    'POSTAL_CODE': data.get('zipcode')[0:11]
                })

            if data.get('tax_office'):
                request.update({
                    'TAX_OFFICE': data.get('tax_office')[0:16]
                })

            if data.get('country'):
                if data.get('country').lower() == 'turkey':
                    request.update({
                        'COUNTRY': 'TÜRKİYE',
                        'COUNTRY_CODE': 'TR'
                    })
                else:
                    request.update({
                        'COUNTRY': data.get('country')
                    })

            if data.get('address'):
                line1 = data.get('address')[0:255]
                line2 = data.get('address')[255:510]
                if line1:
                    request.update({
                        'ADDRESS1': line1
                    })
                if line2:
                    request.update({
                        'ADDRESS2': line2
                    })

            shipment = ClShipment(
                user=config['AKTARIM_KULLANICISI'],
                data=request,
            )
            shipment.is_valid(raise_exception=True)

            if ('XML_AKTARIMI_KULLAN' in config and
                    config['XML_AKTARIMI_KULLAN']):
                shipment.transfer_via_xml()
            else:
                shipment.transfer_via_rest()
            shipment.flow.data = json.dumps(data)
            shipment.flow.save()

            ship = Shipinfo.objects.filter(
                code=f'A-{identifier}'
            ).last()
            if ship:
                return ship

            raise Exception('Sevkiyat adresi oluşturulamadı!')

    @classmethod
    def update_arp_card(cls, data, config):
        card = cls.get_arp_card(data.get('uid'))
        request = config['CARI']['CARI_KART'].copy()
        address = data.get('address')
        if address:
            line1 = address[0:255]
            line2 = address[255:510]
        else:
            line1 = None
            line2 = None

        request.update({
            'CODE': card.code,
        })

        if data.get('payment_code'):
            request.update({
                'PAYMENT_CODE': data.get('payment_code')
            })

        if data.get('title'):
            request.update({
                'TITLE': data.get('title')
            })

        if data.get('name'):
            request.update({
                'NAME': data.get('name')
            })

        if data.get('surname'):
            request.update({
                'SURNAME': data.get('surname')
            })

        if data.get('city'):
            request.update({
                'CITY': data.get('city')
            })

        if data.get('cost_code'):
            request.update({
                'OHP_CODE': data.get('cost_code')
            })

        if data.get('district'):
            request.update({
                'DISTRICT': data.get('district')
            })

        if data.get('country'):
            request.update({
                'COUNTY': data.get('country')
            })

        if data.get('gsm'):
            request.update({
                'TELEPHONE1': data.get('gsm')
            })

        if data.get('tax_office'):
            request.update({
                'TAX_OFFICE': data.get('tax_office')[0:16]
            })

        if data.get('zipcode'):
            request.update({
                'POSTAL_CODE': data.get('zipcode')
            })

        if line1:
            request.update({
                'ADDRESS1': line1
            })
        if line2:
            request.update({
                'ADDRESS2': line2
            })

        request = cls.prepare_glcode(request, card)

        taxnr = data.get('taxnr')
        mernis = data.get('mernis')

        identifier = taxnr and len(taxnr) if taxnr else mernis

        if identifier:
            if len(identifier) != 11:
                request.update({
                    'TAX_ID': identifier
                })
            else:
                request.update({
                    'PERSCOMPANY': 1,
                    'NAME': data.get('name'),
                    'SURNAME': data.get('surname')
                })
                if identifier not in config['CARI']['MERNIS_KARALISTE']:
                    request.update({
                        'TCKNO': identifier
                    })

            request = cls.echeck(identifier, request)

        card = iClcard(
            user=config['AKTARIM_KULLANICISI'],
            data=request,
        )
        card.is_valid(raise_exception=True)
        if ('XML_AKTARIMI_KULLAN' in config and config['XML_AKTARIMI_KULLAN']):
            card.update_via_xml(card.pk)
        else:
            card.update(pk=card.pk)

        card.flow.data = json.dumps(data)
        card.flow.save()
        return (True, card)

    @classmethod
    def create_arp_card(cls, data, config):

        print(data)

        if 'customer_type' in data and data.get('customer_type') == 2:
            gl_prefix = config['MUHASEBE']['MUHABASE_KART_VADELI_NUMARALAMA']
            cl_prefix = config['CARI']['CARI_KART_VADELI_NUMARALAMA']
        else:
            gl_prefix = config['MUHASEBE']['MUHASEBE_KART_PESIN_NUMARALAMA']
            cl_prefix = config['CARI']['CARI_KART_PESIN_NUMARALAMA']

        title = None

        if data.get('title'):
            title = data.get('title')

        if title is None:
            title = data.get('name')
            title += ' '
            title += data.get('surname')

        if len(title.strip()) == 0:
            title = data.get('uid')

        prev_flow, gl_code = cls.create_gl_card(
            title,
            config,
            gl_prefix=gl_prefix
        )

        request = config['CARI']['CARI_KART'].copy()
        address = data.get('address')
        if address:
            line1 = address[0:255]
            line2 = address[255:510]
        else:
            line1 = None
            line2 = None

        code = Clcard.next_code(
            'code',
            config['CARI']['CARI_KART_SABLON'],
            cl_prefix
        )
        request.update({
            'CODE': code,
        })

        if data.get('payment_code'):
            request.update({
                'PAYMENT_CODE': data.get('payment_code')
            })

        if data.get('title'):
            request.update({
                'TITLE': data.get('title')
            })

        if data.get('cost_code'):
            request.update({
                'OHP_CODE': data.get('cost_code')
            })

        if data.get('name') and len(data.get('name').strip()) > 0:
            request.update({
                'NAME': data.get('name')
            })

        if data.get('surname') and len(data.get('surname').strip()) > 0:
            request.update({
                'SURNAME': data.get('surname')
            })

        if data.get('city'):
            request.update({
                'CITY': data.get('city')
            })

        if data.get('district'):
            request.update({
                'DISTRICT': data.get('district')
            })

        if data.get('country'):
            request.update({
                'COUNTY': data.get('country')
            })

        if data.get('gsm'):
            request.update({
                'TELEPHONE1': data.get('gsm')
            })

        if data.get('tax_office'):
            request.update({
                'TAX_OFFICE': data.get('tax_office')[0:16]
            })

        if data.get('zipcode'):
            request.update({
                'POSTAL_CODE': data.get('zipcode')[0:11]
            })

        if line1:
            request.update({
                'ADDRESS1': line1
            })
        if line2:
            request.update({
                'ADDRESS2': line2
            })

        if gl_code:
            request.update({
                'GL_CODE': gl_code
            })

        identifier = data.get('uid')
        if identifier:
            if len(identifier) != 11:
                request.update({
                    'TAX_ID': identifier
                })
            else:
                request.update({
                    'PERSCOMPANY': 1,
                })
                if identifier not in config['CARI']['MERNIS_KARALISTE']:
                    request.update({
                        'TCKNO': identifier
                    })

            request = cls.echeck(identifier, request)

        card = iClcard(
            user=config['AKTARIM_KULLANICISI'],
            data=request,
            prev_flow=prev_flow
        )
        card.is_valid(raise_exception=True)
        if ('XML_AKTARIMI_KULLAN' in config and config['XML_AKTARIMI_KULLAN']):
            card.transfer_via_xml()
        else:
            card.transfer_via_rest()

        if card.flow.success and card.flow.internal_ref:
            XT_100.objects.create(
                parlogref=card.flow.internal_ref,
                uuid=data.get('uid')
            )

        card.flow.data = json.dumps(data)
        card.flow.save()

        return (True, card)

    @classmethod
    def generate_invoice(cls, instance):
        config = Active.settings
        print(instance.pk, instance)

        # fetch from items!
        if instance.is_company:
            # kurumsal cari olustur
            print(instance.items)
            item = instance.items.first()
            data = item.get_data()
            org = datetime.strptime(data.get('day'), '%Y-%m-%d')
            if ('XML_AKTARIMI_KULLAN' in config and config['XML_AKTARIMI_KULLAN']):
                all_day = org.strftime('%d.%m.%Y')
            else:
                all_day = org.strftime('%Y-%m-%d')

            created, arp = cls.get_or_create_arp_card(
                data,
                config
            )
            if created:
                arp_obj = arp.flow.get_related_obj()
                prev_flow = arp.flow
            else:
                arp_obj = arp
                prev_flow = None
            # print("-*-*-*-*-arp = ", arp_obj.code)
            shipment = cls.get_or_create_shipment_card(
                data,
                arp=arp_obj.code
            )

            request = config['FATURA']['KURUMSAL_FATURA_KARTI'].copy()

            request.update({
                'SHIPLOC_CODE': shipment.code
            })

            request.update({
                'DATE': all_day,
                'TIME': 0,
                'AUXIL_CODE': data.get('op_code'),
                'NOTES5': (data.get('uid') + '/' + data.get('pid'))[0:50],
                'DOC_DATE': all_day,
                'TEXTINC': 1,
                'EARCHIVEDETR_INTPATMENTDATE': all_day,
                'DataObjectParameter': {
                    'ReplicMode': False,
                    'CheckParams': False,
                    'CheckRight': False,
                    'Validation': True,
                    'FormSeriLotLinesOnPreSave': False,
                    'ApplyCampaignOnPreSave': False,
                    'ApplyConditionOnPreSave': False,
                    'FillAccCodesOnPreSave': True
                }
            })
            if data.get('itext'):
                request.update({'ITEXT': data.get('itext')})

            if data.get('payment_code'):
                request.update({
                    'PAYMENT_CODE': data.get('payment_code')
                })
            # if data.get('cost_code'):
            #    request.update({
            #        'OHP_CODE1': data.get('cost_code')
            #    })
            if data.get('order_id'):
                request.update({
                    'NOTES1': data.get('order_id'),
                })

            if data.get('discount'):
                request.update({
                    'NOTES2': data.get('discount'),
                })
            if data.get('op_code'):
                request.update({
                    'NOTES4': data.get('op_code'),
                })

            if data.get('po_number'):
                request.update({
                    'NOTES3': data.get('po_number')
                })

            # if data.get('other_desc'):
            #     request.update({
            #         'NOTES6': data.get('other_desc')[0:50]
            #     })

            if data.get('cost_code'):
                request.update({
                    'OHP_CODE': data.get('cost_code')
                })

            if arp_obj and arp_obj.code:
                request.update({
                    'ARP_CODE': arp_obj.code
                })
            request = cls.prepare_einvoice(request, arp_obj, config)
            lines = []
            reqline = config['FATURA']['KURUMSAL_FATURA_KARTI_SATIRI'].copy()
            reqline.update({
                'PRICE': data.get('invoice_gross_amount'),
                'QUANTITY': 1,
                'TOTAL_NET': data.get('invoice_net_amount'),
                'TOTAL': data.get('invoice_gross_amount'),
            })

            if data.get("service_type") == 1:
                if data.get('cost_code') == "110":
                    reqline.update({'MASTER_CODE': '336.03.01.001'})
                elif data.get('cost_code') == "112":
                    reqline.update({'MASTER_CODE': '336.03.01.001'})
                elif data.get('cost_code') == "113":
                    reqline.update({'MASTER_CODE': '336.03.01.001'})
                elif data.get('cost_code') == "116":
                    reqline.update({'MASTER_CODE': '108.01.08.001'})
                elif data.get('cost_code') == "117":
                    reqline.update({'MASTER_CODE': '108.01.05.001'})
                elif data.get('cost_code') == "123":
                    reqline.update({'MASTER_CODE': '108.01.06.001'})
                elif data.get('cost_code') == "124":
                    reqline.update({'MASTER_CODE': '108.01.07.001'})
                elif data.get('cost_code') == "127":
                    reqline.update({'MASTER_CODE': '108.01.09.001'})
                elif data.get('cost_code') == "126":
                    reqline.update({'MASTER_CODE': '108.01.10.001'})
                elif data.get('cost_code') == "136":
                    reqline.update({'MASTER_CODE': '108.01.11.001'})
                # reqline.update({'MASTER_CODE': '336.03.01.001'})
            if data.get("service_type") == 2:
                reqline.update({'MASTER_CODE': '336.03.01.003'})

            if data.get('cost_code'):
                reqline.update({
                    'OHP_CODE1': data.get('cost_code'),
                    'OHP_CODE2': data.get('cost_code'),
                    'OHP_CODE3': data.get('cost_code'),
                    'OHP_CODE4': data.get('cost_code'),
                })

            if data.get('desc'):
                reqline.update({
                    'DESCRIPTION': data.get('desc')[0:250]
                })

            if data.get('invoice_discount_amount') and data.get('invoice_discount_amount') > 0:
                reqline.update({
                    'DISCOUNT_DISTR': data.get('invoice_discount_amount')
                })
                disline = {
                    'TYPE': 2,
                    'DETAIL_LEVEL': 1,
                    'DISCEXP_CALC': 1,
                    'TOTAL': data.get('invoice_discount_amount'),
                    'BASE_AMOUNT': data.get('invoice_gross_amount')
                }
            else:
                disline = None

            lines.append(reqline)
            if disline:
                lines.append(disline)
            pays = []
            payline = config['FATURA']['KURUMSAL_FATURA_ODEME_SATIRI'].copy()
            payline.update({
                'DATE': all_day,
                'TOTAL': data.get('invoice_gross_amount'),
            })
            pays.append(payline)

            if ('XML_AKTARIMI_KULLAN' in config and config['XML_AKTARIMI_KULLAN']):
                request.update({
                    'TRANSACTIONS': lines,
                    'PAYMENT_LIST': pays
                })
                si = SalesInvoiceXML(
                    user=config['AKTARIM_KULLANICISI'],
                    data=request,
                    prev_flow=prev_flow
                )

                si.is_valid(raise_exception=True)
                si.transfer_via_xml(
                    item_name={
                        'TRANSACTIONS': 'TRANSACTION',
                        'PAYMENT_LIST': 'PAYMENT'
                    },
                    fill_acc_codes=True
                )
            else:
                request.update({
                    'TRANSACTIONS': {'items': lines},
                    'PAYMENT_LIST': {'items': pays},
                    'DISPATCHES': {'items': []}
                })
                si = SalesInvoice(
                    user=config['AKTARIM_KULLANICISI'],
                    data=request,
                    prev_flow=prev_flow
                )
                si.is_valid(raise_exception=True)
                si.transfer_via_rest()

            if si.flow.success and si.flow.internal_ref:
                si.flow.data = json.dumps(data)
                si.flow.save()

            return si
        else:
            # bireysel tane tane oge olustur!
            header = instance.items.first()
            print(header)
            data = header.get_data()

            org = datetime.strptime(data.get('day'), '%Y-%m-%d')
            if ('XML_AKTARIMI_KULLAN' in config and config['XML_AKTARIMI_KULLAN']):
                all_day = org.strftime('%d.%m.%Y')
            else:
                all_day = org.strftime('%Y-%m-%d')

            shipment = cls.get_or_create_shipment_card(
                data
            )

            request = config['FATURA']['BIREYSEL_FATURA_KARTI'].copy()
            request.update({
                'DATE': all_day,
                'TIME': 0,
                'NOTES5': data.get('uid'),
                'DOC_DATE': all_day,
                'EARCHIVEDETR_INTPATMENTDATE': all_day,
                'DataObjectParameter': {
                    'ReplicMode': False,
                    'CheckParams': False,
                    'CheckRight': False,
                    'Validation': True,
                    'FormSeriLotLinesOnPreSave': False,
                    'ApplyCampaignOnPreSave': False,
                    'ApplyConditionOnPreSave': False,
                    'FillAccCodesOnPreSave': True
                }
            })

            request.update({
                'SHIPLOC_CODE': shipment.code
            })

            request = cls.prepare_einvoice(request, None, config)
            lines = []
            pays = []
            for item in instance.items.all():
                idata = item.get_data()
                reqline = config['FATURA']['BIREYSEL_FATURA_KARTI_SATIRI'].copy()
                reqline.update({
                    'PRICE': idata.get('invoice_gross_amount'),
                    'QUANTITY': 1,
                    'TOTAL_NET': idata.get('invoice_net_amount'),
                    'TOTAL': idata.get('invoice_gross_amount'),
                    'TRANS_DESCRIPTION': idata.get('desc'),
                })
                if idata.get("service_type") == 1:
                    if data.get('cost_code') == "110":
                        reqline.update({'MASTER_CODE': '336.03.01.001'})
                    elif data.get('cost_code') == "112":
                        reqline.update({'MASTER_CODE': '336.03.01.001'})
                    elif data.get('cost_code') == "113":
                        reqline.update({'MASTER_CODE': '336.03.01.001'})
                    elif data.get('cost_code') == "116":
                        reqline.update({'MASTER_CODE': '108.01.08.001'})
                    elif data.get('cost_code') == "117":
                        reqline.update({'MASTER_CODE': '108.01.05.001'})
                    elif data.get('cost_code') == "123":
                        reqline.update({'MASTER_CODE': '108.01.06.001'})
                    elif data.get('cost_code') == "124":
                        reqline.update({'MASTER_CODE': '108.01.07.001'})
                    elif data.get('cost_code') == "127":
                        reqline.update({'MASTER_CODE': '108.01.09.001'})
                    elif data.get('cost_code') == "126":
                        reqline.update({'MASTER_CODE': '108.01.10.001'})
                    elif data.get('cost_code') == "136":
                        reqline.update({'MASTER_CODE': '108.01.11.001'})
                    # reqline.update({'MASTER_CODE': '336.03.01.001'})
                if idata.get("service_type") == 2:
                    reqline.update({'MASTER_CODE': '336.03.01.003'})

                if idata.get('cost_code'):
                    reqline.update({
                        'OHP_CODE1': idata.get('cost_code'),
                        'OHP_CODE2': idata.get('cost_code'),
                        'OHP_CODE3': idata.get('cost_code'),
                        'OHP_CODE4': idata.get('cost_code')
                    })
                if data.get('cost_code'):
                    request.update({
                        'OHP_CODE': data.get('cost_code')
                    })

                if idata.get('invoice_discount_amount') and idata.get('invoice_discount_amount') > 0:
                    reqline.update({
                        'DISCOUNT_DISTR': idata.get('invoice_discount_amount')
                    })
                    disline = {
                        'TYPE': 2,
                        'DETAIL_LEVEL': 1,
                        'DISCEXP_CALC': 1,
                        'TOTAL': idata.get('invoice_discount_amount'),
                        'BASE_AMOUNT': idata.get('invoice_gross_amount')
                    }
                else:
                    disline = None
                lines.append(reqline)
                if disline:
                    lines.append(disline)

                pays = []
                payline = config['FATURA']['BIREYSEL_FATURA_ODEME_SATIRI'].copy()
                payline.update({
                    'DATE': all_day,
                    'TOTAL': idata.get('invoice_gross_amount'),
                })
                pays.append(payline)

            if ('XML_AKTARIMI_KULLAN' in config and config['XML_AKTARIMI_KULLAN']):
                request.update({
                    'TRANSACTIONS': lines,
                    'PAYMENT_LIST': pays
                })
                si = SalesInvoiceXML(
                    user=config['AKTARIM_KULLANICISI'],
                    data=request
                )

                si.is_valid(raise_exception=True)
                si.transfer_via_xml(
                    item_name={
                        'TRANSACTIONS': 'TRANSACTION',
                        'PAYMENT_LIST': 'PAYMENT'
                    },
                    fill_acc_codes=True
                )
            else:
                request.update({
                    'TRANSACTIONS': {'items': lines},
                    'PAYMENT_LIST': {'items': pays},
                    'DISPATCHES': {'items': []}
                })
                si = SalesInvoice(
                    user=config['AKTARIM_KULLANICISI'],
                    data=request
                )
                si.is_valid(raise_exception=True)
                si.transfer_via_rest()

            if si.flow.success and si.flow.internal_ref:
                si.flow.data = json.dumps(data)
                si.flow.save()

            return si

    @classmethod
    def create_request(cls, is_company, ref, data, items):
        obj, _ = cls.objects.update_or_create(
            firm=Active.name,
            is_company=is_company,
            identifier=ref,
            defaults={
                'data': data,
            }
        )
        for item in items:
            obj.items.add(item)

        return obj


class InvoiceQueLog(QueLog):
    pass


class EmptyOperationError(Exception):
    pass


class SlipQue(Que):
    day = models.DateField(db_index=True)
    op_code = models.CharField(max_length=64, db_index=True)

    def get_data(self):
        return json.loads(self.data)

    @classmethod
    def generate_slip(cls, slip):
        config = Active.settings
        data = slip.get_data()
        print(slip.day)
        op = Operation.objects.get(code=slip.op_code)
        if ('XML_AKTARIMI_KULLAN' in config and config['XML_AKTARIMI_KULLAN']):
            all_day = slip.day.strftime('%d.%m.%Y')
        else:
            all_day = slip.day.strftime('%Y-%m-%d')

        request = config['MUHASEBE']['MUHASEBE_FISI'].copy()
        request.update({
            'DATE': all_day,
            'DOC_DATE': all_day
        })

        if op.description:
            request.update({
                'NOTES1': op.code,
                'NOTES2': op.description[0:50],
            })

        lines = []

        for det in op.operationdetail_set.all():
            def formula(n): return eval(det.formula)
            line = config['MUHASEBE']['MUHASEBE_FISI_SATIR'].copy()
            line.update({
                'GL_CODE': det.account,
                'DOC_DATE': all_day,
                'AUXIL_CODE': op.code
            })
            if '.' in det.account:
                line.update({
                    'PARENT_GLCODE': det.account.split('.')[0]
                })

            calc = formula(data[det.field])
            line.update({
                'DESCRIPTION': f'Formula {det.formula} Field: {det.field} Value: {data[det.field]}'
            })

            if det.is_debit:
                line.update({
                    'DEBIT': calc
                })
            else:
                line.update({
                    'CREDIT': calc,
                    'SIGN': 1
                })
            lines.append(line)

        em = None
        if lines:
            if ('XML_AKTARIMI_KULLAN' in config and config['XML_AKTARIMI_KULLAN']):
                request.update({
                    'TRANSACTIONS': lines
                })
                em = EmficheXML(
                    user=config['AKTARIM_KULLANICISI'],
                    data=request
                )
                em.is_valid(raise_exception=True)
                em.transfer_via_xml(
                    item_name={
                        'TRANSACTIONS': 'TRANSACTION'
                    }
                )
                if em.flow.success and em.flow.internal_ref:
                    em.flow.data = json.dumps(data)
                    em.flow.save()
            else:
                request.update({
                    'TRANSACTIONS': {'items': lines}
                })
                em = Emfiche(
                    user=config['AKTARIM_KULLANICISI'],
                    data=request
                )
                em.is_valid(raise_exception=True)
                em.transfer_via_rest()

                if em.flow.success and em.flow.internal_ref:
                    em.flow.data = json.dumps(data)
                    em.flow.save()
        else:
            raise EmptyOperationError

        return em

    @classmethod
    def create_request(cls, day, op_code, data):
        obj, _ = cls.objects.update_or_create(
            firm=Active.name,
            identifier=uuid4().hex,
            day=day,
            op_code=op_code,
            defaults={
                'data': json.dumps(data, cls=DjangoJSONEncoder)
            }
        )
        return obj


class SlipQueLog(QueLog):
    pass


class OpQue(Que):
    day = models.DateField(db_index=True)
    op_code = models.CharField(max_length=64, db_index=True)
    commission_amount = models.FloatField(default=0, db_index=True)
    is_invoice = models.BooleanField(default=False, db_index=True)


class OpQueLog(QueLog):
    pass
