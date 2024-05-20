import json
from datetime import datetime, date
from dateutil.parser import parse
from django.db import models
from rest_framework.exceptions import APIException

from erp.helpers import calculate_logo_time
from erp.models.friendly import (
    Clcard, Orfline, Stfiche, Emuhacc, Shipinfo,
    CardAccountRef, Items, Itmunita,
    Orfiche

)
from erp.asking.dispatch import SalesDispatchXML
from erp.asking.orders import SalesOrderXML
from erp.asking.account import AccountCard
from erp.asking.current import ClShipment, ClCard as iClcard
from erp.asking.invoice import SalesInvoiceXML
from third_party.elogo.api import Elogo
from third_party.bazaars.trendyol.models import (
    TrendyolProductMismatch,
    TrendyolLog,
    TrendyolLineLog,
    TrendyolProductMatch as TPM
)
from erp.active import Active

from bti.models.track import Track
from bti.models.que import Que

from app.arvato import Arvato

idea_choices = [
    ('waiting_for_approval', 'waiting_for_approval'),
    ('approved', 'approved'),
    ('fulfilled', 'fulfilled'),
    ('cancelled', 'cancelled'),
    ('delivered', 'delivered'),
    ('on_accumulation', 'on_accumulation'),
    ('waiting_for_payment', 'waiting_for_payment'),
    ('being_prepared', 'being_prepared'),
    ('refunded', 'refunded'),
    ('deleted', 'deleted')
]

class TrendyolStatusLog(models.Model):
    trendyol = models.ForeignKey(
        TrendyolLog,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="trendyolstatus_log"
    )
    status = models.CharField(max_length=20, db_index=True)
    invoice = models.CharField(null=True, blank=True, max_length=255)
    order_id = models.BigIntegerField(db_index=True)
    request = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    exception = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

class IdeaCargoLog(models.Model):
    order = models.IntegerField(db_index=True)
    data = models.TextField()
    request = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    exception = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class IdeaLog(models.Model):
    order = models.IntegerField(db_index=True)
    status = models.CharField(
        choices=idea_choices,
        max_length=60,
        db_index=True
    )
    request = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    exception = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

class IdeaStockLog(models.Model):
    order = models.IntegerField(db_index=True)
    stock_amount = models.IntegerField()
    request = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    exception = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class ArvatoLog(models.Model):
    trendyol = models.ForeignKey(
        TrendyolLog,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="arvato_trendyol_log"
    )
    order = models.IntegerField(db_index=True)
    request = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    exception = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_order_number(self):
        import json
        if self.response:
            try:
                data = json.loads(self.response)
                return int(data['data'][0]['orderNumber'])
            except:
                pass
        return None



class ArvatoTrack(Track):
    @classmethod
    def create_sales_order(cls, data, check_record=True, arvato_token=None):
        if TrendyolTrack.validate_materials(data.get('lines')) is False:
            return False
        if check_record:
            logo = TrendyolLog.objects.filter(
                order_number=data.get('orderNumber')).first()
            if logo is None or logo.internal_ref is None:
                raise Exception('Sipariş logoya aktarılmamış!')
        else:
            logo = None

        # check arvato object
        arvato = Arvato(*Active.settings['ARVATO']['API'].values())
        if arvato_token is None:
            arvato_token = arvato.generate_token()
        else:
            arvato.token = arvato_token

        kodlama = Active.settings['ARVATO']['KODLAMA']

        ana = kodlama['SATIS_SIPARISI'].copy()

        veri = kodlama['SATIS_SIPARISI_LISTE'].copy()

        dt = datetime.fromtimestamp(data['orderDate'] / 1000.0)
        veri.update({
            'orderNumber': logo.internal_ref if logo else 0,
            'orderTime': dt.strftime('%Y-%m-%dT%H:%M:%S'),
            'customerOrderNumber': data.get('orderNumber'),
        })
        ctn = int(str(data.get('cargoTrackingNumber'))[0:3])
        if ctn in Active.settings['ARVATO']['KARGO_ESLEME']:
            veri.update({
                'carrierCode': Active.settings['ARVATO']['KARGO_ESLEME'][ctn]
            })
        veri.update({
            'orderQuantity': sum([line['quantity']
                for line in data.get('lines')]) or 0
        })

        veri.update({
            'MarketPlaceCargoKey': str(data.get('cargoTrackingNumber'))
        })

        fat = data.get('invoiceAddress')
        ta = data.get('shipmentAddress')
        veri.update({
            'OrderPartyDetailList': [
                {
                    'typeCode': 'FAT',
                    'name': fat.get('firstName').strip(),
                    'surname': fat.get('lastName').strip(),
                    'countryCode': fat.get('countryCode').upper(),
                    'cityCode': fat.get('city').strip(),
                    'townCode': fat.get('district').strip(),
                    'email': data.get('customerEmail'),
                    'addressText': fat.get('fullAddress').strip()
                },
                {
                    'typeCode': 'TA',
                    'name': ta.get('firstName').strip(),
                    'surname': ta.get('lastName').strip(),
                    'countryCode': ta.get('countryCode').upper(),
                    'cityCode': ta.get('city').strip(),
                    'townCode': ta.get('district').strip(),
                    'email': data.get('customerEmail'),
                    'addressText': ta.get('fullAddress').strip()
                }
            ]
        })
        odlist = list()
        for line in data.get('lines'):
            material = TrendyolTrack.get_material(line)
            ref = Orfline.objects.filter(lineexp=line.get('id')).first()
            temp = kodlama['SATIS_SIPARISI_DETAY_SATIRI'].copy()

            temp.update({
                'lineNumber': str(line.get('id')),
                'itemCode': material.code,
                'quantity': line.get('quantity'),
                'itemReferenceNumber': ref.pk if ref else 0
            })
            odlist.append(temp)
        veri.update({
            'orderDetailList': odlist
        })
        ivlist = []
        calc_percent_inc = lambda amnt, tx:  amnt / ( 1 + ( tx / 100.0))
        for line in data.get('lines'):
            temp = kodlama['SATIS_SIPARISI_FATURA'].copy()
            tax_inc_price = line.get('amount') * line.get('quantity')
            discounted_tax_inc = sum(
                [i['lineItemPrice'] for i in line.get('discountDetails')])
            discount_amount_tax_inc = line.get('discount') * line.get('quantity')
            unit_price_tax_inc = line.get('amount')
            unit_price_discounted_tax_inc = line.get('price')
            unit_discount_amount_tax_inc = line.get('discount')
            vat_amount = line.get('vatBaseAmount')

            temp.update({
                'CurrencyCode': line.get('currencyCode'),
                'CurrencyDate': datetime.now().isoformat(),
                'InvoiceAmount': discounted_tax_inc
            })
            detail = kodlama['SATIS_SIPARISI_FATURA_DETAY'].copy()
            detail.update({
                'OrderDetailLineNumber': line.get('id'),
                'LineNumber': line.get('id'),
                'LineTextCode': line.get('merchantSku'),
                'LineTextQuantity': line.get('quantity'),
                'CurrencyCode': line.get('currencyCode'),
                'CurrencyDate': datetime.now().isoformat(),
                'TaxValueCode': str(int(vat_amount)),
                'UnitPrice': calc_percent_inc(tax_inc_price, vat_amount),
                'UnitDiscountAmount': calc_percent_inc(
                    line.get('discount'),
                    vat_amount),
                'UnitDiscountAmountTaxIncluded': line.get('discount'),
                'UnitTaxAmount': line.get('price') - calc_percent_inc(
                    line.get('price'),
                    vat_amount),
                'LinePrice': calc_percent_inc(line.get('price'), vat_amount),
                'LinePriceTaxIncluded': line.get('price'),
                'LineDiscountAmount': line.get('discount'),
                'LineDiscountAmountTaxIncluded': discount_amount_tax_inc,
                'LineTaxAmount': calc_percent_inc(
                    discounted_tax_inc, vat_amount) * vat_amount,
                'UnitPriceDiscounted': calc_percent_inc(
                    line.get('price'), vat_amount),
                'UnitPriceDiscountedTaxIncluded': line.get('price'),
                'LinePriceDiscounted': calc_percent_inc(
                    discounted_tax_inc, vat_amount),
                'LinePriceDiscountedTaxIncluded': discounted_tax_inc,
                'AdditionalDiscountAmount': 0,

            })
            temp.update({
                'InvoiceDetails': [detail],
                'InvoiceTaxDetails': [],
                'InvoiceDiscountDetails': []
            })

            ivlist.append(temp)
        veri.update({
            'InvoiceList': ivlist
        })

        ana.update({
            'ItemList': [veri]
        })
        try:
            result = arvato.add_outbound_order(ana)
        except Exception as e:
            ArvatoLog(
                trendyol=logo,
                order=data.get('orderNumber'),
                request=json.dumps(ana),
                exception=str(e)
            ).save()
        else:
            ArvatoLog(
                trendyol=logo,
                order=data.get('orderNumber'),
                request=json.dumps(ana),
                response=json.dumps(result)
            ).save()
            if result:
                if result['isSuccess'] and result['data']:
                    check1 = all([i['isValid'] for i in result['data']])
                    if check1:
                        track = cls(
                            firm=Active.name,
                            identifier=data.get('orderNumber'),
                        )
                        track.save()

class TrendyolTrack(Track):
    @classmethod
    def create_sales_order(cls, data):
        cls.log(data)
        if cls.validate_materials(data.get('lines')) is False:
            for line in data.get('lines'):
                material = cls.get_material(line)
                if material is None:
                    TrendyolProductMismatch.objects.get_or_create(
                        order=data.get('orderNumber'),
                        barcode=line.get('barcode'),
                        product_code=line.get('productCode'),
                        merchant_sku=line.get('merchantSku'),
                        defaults={
                            'line': json.dumps(line),
                            'body': json.dumps(data)
                        }
                    )
            return False
        dt = datetime.fromtimestamp(data['orderDate'] / 1000.0)
        kodlama = Active.settings['TRENDYOL']['KODLAMA']
        fiche = kodlama.get('SATIS_SIPARISI').copy()
        fiche.update({
            'DOC_NUMBER': data.get('id'),
            'DATE': dt.strftime('%d.%m.%Y'),
            'TIME': calculate_logo_time(dt),
            'NOTES1': data.get('orderNumber')
        })
        created, arp = cls.get_or_create_arp_card_via_id(data)
        if created:
            arp_obj = arp.flow.get_related_obj()
            prev_flow = arp.flow
        else:
            arp_obj = arp
            prev_flow = None

        created, invoice_shipment = cls.get_or_create_shipment_card(data, 'invoiceAddress', arp=arp_obj, prev_flow=prev_flow)
        if created:
            prev_flow = invoice_shipment.flow

        created, shipment = cls.get_or_create_shipment_card(data, 'shipmentAddress', arp=arp_obj, prev_flow=prev_flow)
        if created:
            shipment_obj = shipment.flow.get_related_obj()
            prev_flow = shipment.flow
        else:
            shipment_obj = shipment

        account = CardAccountRef.objects.select_related(
            'accountref').filter(
                trcode=5, typ=1, cardref=arp_obj.logicalref).first()
        fiche.update({
            'ARP_CODE': arp_obj.code,
            'SHIPLOC_CODE': shipment_obj.code
        })
        if account and account.accountref:
            fiche.update({
                'GL_CODE': account.accountref.code
            })
        lines = []


        for line in data.get('lines'):
            item = cls.get_material(line)
            if item is None:
                raise Exception(f'Geçersiz ürün! Barkod: {line["barcode"]}')
            item_account = CardAccountRef.objects.select_related(
                'accountref').filter(
                    trcode=1, cardref=arp_obj.logicalref).first()

            satir = kodlama.get('SATIS_SIPARISI_SATIR').copy()
            satir.update({
                'QUANTITY': line.get('quantity'),
                'ORG_QUANTITY': line.get('quantity'),
                'PRICE': line.get('amount'),
                'PC_PRICE': line.get('amount'),
                'EDT_PRICE': line.get('amount'),
                'VAT_RATE': line.get('vatBaseAmount'),
                'AUXIL_CODE': data.get('orderNumber'),
                'TRANS_DESCRIPTION': line.get('id'),
                'VAT_INCLUDED': 1,
                'MASTER_CODE': item.code
            })

            if item_account and item_account.accountref:
                satir.update({
                    'GL_CODE1': item_account.accountref.code
                })
            itmunita = Itmunita.objects.filter(itemref=item, linenr=1).first()
            if itmunita and itmunita.unitlineref and itmunita.unitlineref.code:
                satir.update({
                    'UNIT_CODE': itmunita.unitlineref.code
                })

            lines.append(satir)

        fiche.update({
            'TRANSACTIONS': lines
        })
        so = SalesOrderXML(
            user=Active.default_rest_user,
            data=fiche,
            prev_flow=prev_flow
        )
        so.is_valid(raise_exception=True)
        so.transfer_via_xml(item_name='TRANSACTION')
        #so.set_data(so.get_data())
        #so.create()
        if so.flow.success and so.flow.internal_ref:
            track = cls(
                firm=Active.name,
                identifier=data.get('orderNumber'),
                flow=so.flow
            )
            track.save()
            so.flow.data = json.dumps(data)
            so.flow.save()
            # logs
            print(so.flow.response)
            if so.flow.internal_ref:
                log = TrendyolLog.objects.filter(
                    order_number=data.get('orderNumber')).first()
                if log:
                    print(so.flow.internal_ref)
                    log.internal_ref = so.flow.internal_ref
                    log.save()
        return so

    @classmethod
    def create_invoice(cls, data):
        cls.log(data)
        if cls.validate_materials(data.get('lines')) is False:
            for line in data.get('lines'):
                material = cls.get_material(line)
                if material is None:
                    TrendyolProductMismatch.objects.get_or_create(
                        order=data.get('orderNumber'),
                        barcode=line.get('barcode'),
                        product_code=line.get('productCode'),
                        defaults={
                            'line': json.dumps(line),
                            'body': json.dumps(data)
                        }
                    )
            return False

        dt = datetime.fromtimestamp(data['orderDate'] / 1000.0)
        kodlama = Active.settings['TRENDYOL']['KODLAMA']
        fiche = kodlama.get('SATIS_FATURASI').copy()
        fiche.update({
            'DOC_TRACK_NR': data.get('orderNumber'),
            'DATE': dt.strftime('%d.%m.%Y'),
            'DOC_DATE': datetime.now().strftime('%d.%m.%Y'),
            'TIME': calculate_logo_time(dt)
        })
        created, arp = cls.get_or_create_arp_card_via_id(data)
        if created:
            arp_obj = arp.flow.get_related_obj()
            prev_flow = arp.flow
        else:
            arp_obj = arp
            prev_flow = None


        created, invoice_shipment = cls.get_or_create_shipment_card(data, 'invoiceAddress', arp=arp_obj, prev_flow=prev_flow)
        if created:
            prev_flow = invoice_shipment.flow

        created, shipment = cls.get_or_create_shipment_card(data, 'shipmentAddress', arp=arp_obj, prev_flow=prev_flow)
        if created:
            shipment_obj = shipment.flow.get_related_obj()
            prev_flow = shipment.flow
        else:
            shipment_obj = shipment

        account = CardAccountRef.objects.select_related(
            'accountref').filter(
                trcode=5, typ=1, cardref=arp_obj.logicalref).first()
        fiche.update({
            'ARP_CODE': arp_obj.code,
            'SHIPLOC_CODE': shipment_obj.code,
            'TOTAL': data.get('totalPrice')
        })
        if account and account.accountref:
            fiche.update({
                'GL_CODE': account.accountref.code
            })
        lines = []


        for line in data.get('lines'):

            item = cls.get_material(line)
            if item is None:
                raise Exception(f'Geçersiz ürün! Barkod: {line["barcode"]}')
            item_account = CardAccountRef.objects.select_related(
                'accountref').filter(
                    trcode=1, cardref=arp_obj.logicalref).first()

            satir = kodlama.get('SATIS_FATURASI_SATIR').copy()
            satir.update({
                'TYPE': 0,
                'MASTER_CODE': item.code,
                'VAT_RATE': line.get('vatBaseAmount'),
                'QUANTITY': line.get('quantity'),
                'PRICE': line.get('amount'),
                'DESCRIPTION': line.get('id')
            })

            if item_account and item_account.accountref:
                satir.update({
                    'GL_CODE1': item_account.accountref.code
                })
            itmunita = Itmunita.objects.filter(itemref=item, linenr=1).first()
            if itmunita and itmunita.unitlineref and itmunita.unitlineref.code:
                satir.update({
                    'UNIT_CODE': itmunita.unitlineref.code
                })

            lines.append(satir)

        """
        satir_toplam = sum([line['PRICE'] * line['QUANTITY'] for line in lines])

        if satir_toplam > data.get('totalPrice'):
            lines.append({
                'TYPE': 2,
                'DETAIL_LEVEL': 1,
                'DISEXP_CALC': 1,
                'DISCOUNT_RATE': data.get('totalPrice') * 100 / satir_toplam,
                'VAT_INCLUDED_GRS': 1
            })
        """
        fiche.update({
            'TRANSACTIONS': lines
        })
        si = SalesInvoiceXML(
            user=Active.default_rest_user,
            data=fiche,
            prev_flow=prev_flow
        )
        si.is_valid(raise_exception=True)
        si.transfer_via_xml(item_name='TRANSACTION')

        if si.flow.success and si.flow.internal_ref:
            track = cls(
                firm=Active.name,
                identifier=data.get('orderNumber'),
                flow=si.flow
            )
            track.save()
            si.flow.data = json.dumps(data)
            si.flow.save()
            # logs
            print(si.flow.response)
            if si.flow.internal_ref:
                log = TrendyolLog.objects.filter(
                    order_number=data.get('orderNumber')).first()
                if log:
                    log.internal_ref = si.flow.internal_ref
                    log.save()


        return si

    @classmethod
    def log(cls, data):
        if TrendyolLog.objects.filter(order_number=data.get('orderNumber')).exists() is False:
            obj = TrendyolLog.objects.create(
                order_number=data.get('orderNumber'),
                order_id=data.get('id'),
                internal_ref=None,
                raw=json.dumps(data)
            )
            for line in data.get('lines'):
                TrendyolLineLog.objects.create(
                    log=obj,
                    line=line.get('id'),
                    raw=json.dumps(line)
                )

    @classmethod
    def validate_materials(cls, lines):
        check = []
        for line in lines:
            check.append(cls.get_material(line))
        return None not in check

    @classmethod
    def get_material(cls, line):
        from erp.models.friendly import Items
        from third_party.bazaars.trendyol.models import (
            TrendyolProductMatch as TPM
        )
        ayarlar = Active.settings['TRENDYOL']
        filter = {}
        if 'BIREBIR_ESLEME_KULLAN' in ayarlar and ayarlar['BIREBIR_ESLEME_KULLAN']:
            filter.update({
                'check_erp_first': True,
                'erp_filter': ayarlar['BIREBIR_ESLEME']
            })
        else:
            filter.update({
                'check_erp_first': False
            })

        filter.update({
            'trd_filter': ayarlar['URUN_ESLEME']
        })
        material = TPM.get_erp_item(
            line,
            **filter
        )
        return material


    @classmethod
    def get_or_create_shipment_card(cls, data, pointer, arp=None, prev_flow=None):
        kodlama = Active.settings['TRENDYOL']['KODLAMA']
        address = data.get(pointer)
        code = f'{kodlama["SEVKIYAT_KODU_ONEK"]}{address["id"]}'
        ship = Shipinfo.objects.filter(
            clientref=arp,
            code=code,
            specode=kodlama.get('SEVKIYAT_KARTI').get('AUXIL_CODE')
        ).first()
        if ship:
            return (False, ship)
        else:
            if arp is None:
                raise Exception('Geçersiz cari kart!')

            taxnr = data.get('taxNumber')
            tckno = data.get('tcIdentityNumber')

            yapi = Active.settings['TRENDYOL']['KODLAMA']['SEVKIYAT_KARTI'].copy()
            full_address = address.get('fullAddress').strip()
            line1 = full_address[0:255].strip()
            line2 = full_address[255:510].strip()
            yapi.update({
                'ARP_CODE': arp.code,
                'CODE': code,
                'DESCRIPTION': address.get('fullName'),
                #'EMAIL_ADDR': data.get('customerEmail'),
                #'INCHANGE': address.get('fullName')[0:21],
                'TAX_NR': taxnr if taxnr else tckno,
                'CITY': address.get('city').strip(),
                'TOWN': address.get('district').strip()
            })
            if len(line1):
                yapi.update({
                    'ADDRESS1': line1
                })
            if len(line2):
                yapi.update({
                    'ADDRESS2': line2
                })


            shipment = ClShipment(
                user=Active.default_rest_user,
                data=yapi,
                prev_flow=prev_flow
            )
            shipment.is_valid(raise_exception=True)
            shipment.transfer_via_xml(item_name='TRANSACTION')
            shipment.flow.data = json.dumps(data)
            shipment.flow.save()
            return (True, shipment)

    @classmethod
    def get_or_create_gl(cls, data):
        kodlama = Active.settings['TRENDYOL']['KODLAMA']
        gl_code = None
        if 'MUHASEBE_HESABI_OLUSTURULSUN' in kodlama and kodlama['MUHASEBE_HESABI_OLUSTURULSUN']:
            gl_code = cls.next_gl_code()
            yapi = Active.settings['TRENDYOL']['KODLAMA']['MUHASEBE_KARTI']
            yapi.update({
                'CODE': gl_code,
                'DESCRIPTION': data.get('invoiceAddress').get('fullName')
            })
            card = AccountCard(
                user=Active.default_rest_user,
                data=yapi
            )
            card.is_valid(raise_exception=True)
            card.transfer_via_xml(item_name='TRANSACTION')
            card.flow.data = json.dumps(data)
            card.flow.save()
            return (card.flow, gl_code)
        else:
            if 'SABIT_MUHASEBE_HESABI' in kodlama:
                gl_code = kodlama['SABIT_MUHASEBE_HESABI']
        return (None, gl_code)

    @classmethod
    def create_arp_card(cls, code, data):
        kodlama = Active.settings['TRENDYOL']['KODLAMA']
        prev_flow, gl_code = cls.get_or_create_gl(data)
        yapi = Active.settings['TRENDYOL']['KODLAMA']['CARI_KART'].copy()
        ia = data.get('invoiceAddress')
        taxnr = data.get('taxNumber')
        tckno = data.get('tcIdentityNumber')
        if taxnr:
            identity = taxnr
        else:
            identity = tckno
        full_address = data.get('invoiceAddress').get('fullAddress').strip()
        line1 = full_address[0:255].strip()
        line2 = full_address[255:510].strip()

        yapi.update({
            'E_COMM_ID': data.get('customerId'),
            'CODE': code,
            'TITLE': data.get('invoiceAddress').get('fullName'),
            'CITY': data.get('invoiceAddress').get('city').strip(),
            'TOWN': data.get('invoiceAddress').get('district').strip(),
            'E_MAIL': data.get('customerEmail')
        })
        if len(line1):
            yapi.update({
                'ADDRESS1': line1
            })
        if len(line2):
            yapi.update({
                'ADDRESS2': line2
            })

        if gl_code:
            yapi.update({
                'GL_CODE': gl_code
            })
        if ia.get('postalCode'):
            yapi.update({
                'POSTAL_CODE': ia.get('postalCode'),
            })
        if taxnr:
            yapi.update({
                'TAX_ID': taxnr
            })
        else:
            yapi.update({
                'PERSCOMPANY': 1,
                'NAME': data.get('invoiceAddress').get('firstName'),
                'SURNAME': data.get('invoiceAddress').get('lastName')
            })
            # 'TCKNO': tckno,
            if tckno not in kodlama['MERNIS_KARALISTE']:
                yapi.update({
                    'TCKNO': tckno
                })
        if identity not in kodlama['MERNIS_KARALISTE']:
            yapi = cls.echeck(identity, yapi)

        card = iClcard(
            user=Active.default_rest_user,
            data=yapi,
            prev_flow=prev_flow
        )
        card.is_valid(raise_exception=True)
        card.transfer_via_xml()
        card.flow.data = json.dumps(data)
        card.flow.save()
        return (True, card)

    @classmethod
    def get_or_create_arp_card_via_edi(cls, data):
        kodlama = Active.settings['TRENDYOL']['KODLAMA']
        auxil_code = kodlama['CARI_KART']['AUXIL_CODE']
        edino = data.get('customerId')
        card = Clcard.objects.filter(
            specode=auxil_code,
            edino=edino
        ).first()
        if card:
            return (False, card)
        else:
            code = cls.next_arp_code()
            return cls.create_arp_card(code, data)

    @classmethod
    def get_or_create_arp_card_via_id(cls, data):
        kodlama = Active.settings['TRENDYOL']['KODLAMA']
        auxil_code = kodlama['CARI_KART']['AUXIL_CODE']
        code = f'{kodlama["CARI_KODU_ONEK"]}{data["customerId"]}'
        card = Clcard.objects.filter(
            specode=auxil_code,
            code=code
        ).first()
        if card:
            return (False, card)
        else:
            return cls.create_arp_card(code, data)

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
                data['POST_LABEL'] = gib.get('EINVOICEPKALIAS', '')
                data['SENDER_LABEL'] = gib.get('EDESPATCHGBALIAS', '')
                if len(gib.get('EDESPATCHGBALIAS', '')):
                    data['ACCEPT_DESP'] = 1
                    data['SENDER_LABEL_CODE_DESP'] = gib.get(
                        'EDESPATCHGBALIAS', '')
                    data['POST_LABEL_CODE_DESP'] = gib.get(
                        'EDESPATCHPKALIAS', '')
        return data

    @classmethod
    def next_gl_code(cls):
        from django.db.models.functions import Length
        kodlama = Active.settings['TRENDYOL']['KODLAMA']
        let = len(kodlama['MUHASEBE_KART_SABLON'])
        let += 1
        let += len(kodlama['MUHASEBE_KART_NUMARALAMA'])

        next_code = Emuhacc.objects.annotate(
            text_len=Length('code')).filter(
                text_len=let,
                code__startswith=kodlama['MUHASEBE_KART_NUMARALAMA']
        ).aggregate(next=models.Max('code'))
        if next_code['next'] is None:
            code = "1".zfill(len(kodlama['MUHASEBE_KART_SABLON']))
            code = f"{kodlama['MUHASEBE_KART_NUMARALAMA']}.{code}"
        else:
            code = next_code['next']
            _, ncode = code.split(kodlama['MUHASEBE_KART_NUMARALAMA'])
            code = int(ncode[1:]) + 1
            code = str(code).zfill(len(kodlama['MUHASEBE_KART_SABLON']))
            code = f"{kodlama['MUHASEBE_KART_NUMARALAMA']}.{code}"
        return code

    @classmethod
    def next_arp_code(cls):
        from django.db.models.functions import Length
        kodlama = Active.settings['TRENDYOL']['KODLAMA']
        let = len(kodlama['CARI_KART_SABLON'])
        let += 1
        let += len(kodlama['CARI_KART_NUMARALAMA'])

        next_code = Clcard.objects.annotate(
            text_len=Length('code')).filter(
                text_len=let,
                code__startswith=kodlama['CARI_KART_NUMARALAMA']
        ).aggregate(next=models.Max('code'))
        if next_code['next'] is None:
            code = "1".zfill(len(kodlama['CARI_KART_SABLON']))
            code = f"{kodlama['CARI_KART_NUMARALAMA']}.{code}"
        else:
            code = next_code['next']
            _, ncode = code.split(kodlama['CARI_KART_NUMARALAMA'])
            code = int(ncode[1:]) + 1
            code = str(code).zfill(len(kodlama['CARI_KART_SABLON']))
            code = f"{kodlama['CARI_KART_NUMARALAMA']}.{code}"
        return code


class DispatchTrack(Track):
    @classmethod
    def create_dispatch(cls, data):
        identifier = data.get('doc_tracking_number')
        arp_code = data.get('arp_code', None)

        if arp_code is None or len(arp_code) == 0:
            orfiche = Orfiche.objects.filter(doctrackingnr=identifier).last()
            if orfiche and orfiche.clientref:
                arp_code = orfiche.clientref.code

        dispdata = Active.settings['KODLAMA']['IRSALIYE_KARTI'].copy()
        card = Clcard.objects.filter(code=arp_code).first()
        if card is None:
            raise APIException({
                'status': False,
                'description': 'Geçersiz cari kart'
            })
        # tilda check
        if Stfiche.objects.filter(ficheno='~').count() > 0:
            raise APIException({
                'status': False,
                'description': 'Sistemde tilda olması nedeniyle, irsaliye aktarılamadı'
            })

        dt = parse(data.get('date'))
        dispdata.update({
            'ARP_CODE': card.code,
            'DATE': dt.strftime('%d.%m.%Y'),
            'TIME': calculate_logo_time(dt),
            'DOC_TRACK_NR': data.get('doc_tracking_number'),
            'DOC_NUMBER': data.get('doc_number'),
            'SOURCE_WH': data.get('source_wh'),
            'SOURCE_COST_GRP': data.get('source_cost_grp')
        })
        if data.get('auxil_code', None):
            dispdata.update({
                'AUXIL_CODE': data.get('auxil_code')
            })
        for i in range(1,6):
            if data.get(f'notes{i}', None):
                dispdata.update({
                    f'NOTES{i}': data.get(f'notes{i}')
                })
        items = list()
        for item in data.get('items'):
            pd = parse(item.get('date'))

            temp = {
                'MASTER_CODE': item.get('master_code'),
                'DATE': pd.strftime('%d.%m.%Y'),
                'FTIME': calculate_logo_time(pd),
                'SOURCEINDEX': item.get('source_index'),
                'SOURCECOSTGRP': item.get('source_cost_grp'),
                'QUANTITY': item.get('quantity'),
                'DESCRIPTION': item.get('description'),
                'UNIT_CODE': item.get('unit_code')
            }
            if item.get('vat_rate'):
                temp.update({
                    'VAT_RATE': item.get('vat_rate'),
                })
            if item.get('price'):
                temp.update({
                    'PRICE': item.get('price')
                })

            order_ref = Orfline.objects.select_related(
                'ordficheref',
                'stockref').filter(
                    stockref__code=item.get('master_code'),
                    ordficheref__ficheno=data.get('doc_tracking_number')
            ).first()
            if order_ref:
                temp.update({
                    'ORDER_REFERENCE': order_ref.pk
                })
            items.append(temp)
        dispdata.update({
            'TRANSACTIONS': items
        })
        if card.acceptedesp == 1:
            if 'ship_date' in data:
                ship_date = parse(data.get('ship_date'))
                ship_time = calculate_logo_time(ship_date)

                dispdata.update({
                    'SHIP_DATE': ship_date.strftime('%d.%m.%Y'),
                    'SHIP_TIME': calculate_logo_time(ship_date),
                })
            if 'doc_date' in data:
                doc_date = parse(data.get('doc_date'))
                dispdata.update({
                    'DOC_DATE': doc_date.strftime('%d.%m.%Y'),
                    'DOC_TIME': calculate_logo_time(doc_date)
                })
            dispdata.update({
                'EDESPATCH': card.acceptedesp,
                'EDESPATCH_PROFILEID': card.profileiddesp,
                'EINVOICE': card.accepteinv,
                'EINVOICE_PROFILEID': card.profileid,
                'EINVOICE_DRIVERNAME1': data.get('driver_name'),
                'EINVOICE_DRIVERSURNAME1': data.get('driver_surname'),
                'EINVOICE_DRIVERTCKNO1': data.get('driver_tckno'),
                'EINVOICE_PLATENUM1': data.get('plate')
            })

        sadisp = SalesDispatchXML(data=dispdata, user=Active.default_rest_user)
        sadisp.is_valid(raise_exception=True)
        sadisp.transfer_via_xml(item_name='TRANSACTION')

        if sadisp.flow.success and sadisp.flow.internal_ref:
            track = cls(
                firm=Active.name,
                identifier=identifier,
                flow=sadisp.flow
            )
            track.save()
        return sadisp

class TrendyolCancelTrack(Track):
    @classmethod
    def cancel_order(cls, order):
        arvato = Arvato(*Active.settings['ARVATO']['API'].values())
        alog = ArvatoLog.objects.filter(order=order.get('orderNumber')).exclude(response=None).last()
        if alog:
            target = alog.get_order_number()
            if target:
                arvato.generate_token()
                response = arvato.cancel_order({
                    'accountCode': 'Seniha',
                    'orders': [
                        {
                            'orderNumber': f'{target}',
                            'cancellationReason': 'CANCELLEDBYCUSTOMER'
                        }
                    ]
                })
                if response and response['isValid']:
                    obj = TrendyolLog.objects.filter(
                        order_number=order.get('orderNumber')).first()
                    if obj and obj.internal_ref:
                        data = {
                            'CANCELLED': 1,
                            'ORDER_STATUS': 2
                        }
                        sd = SalesOrderXML(
                            partial=True,
                            user=Active.default_rest_user
                        )
                        result = sd.update_via_object(sd.xml_endpoint, {
                            'ref': obj.internal_ref,
                        }, CANCELLED=1, ORDER_STATUS=3)

                        track = cls(
                            firm=Active.name,
                            identifier=order.get('orderNumber'),
                            flow=sd.flow
                        )
                        track.save()