from dateutil.parser import parse
from datetime import datetime, date
import json

from django.db import models
from rest_framework.exceptions import APIException
from django.core.exceptions import ObjectDoesNotExist
from erp.active import Active
from third_party.elogo.api import Elogo
from bti.helpers import dict_key_upper
from erp.models.current import LG_CLCARD
from erp.helpers import calculate_logo_time
from erp.models.friendly import Itmunita
from erp.asking.invoice import SalesInvoice

from bti.models.track import Track
from bti.models.que import Que

from app.api.clcard import ExtApiClCard



class InvoiceTrack(Track):
    @classmethod
    def create_invoice(cls, data, odata):
        kodlama = Active.settings['KODLAMA']
        invdata = kodlama['SATIS_FATURASI'].copy()
        try:
            current = LG_CLCARD.objects.filter(edino=data.get('customer')).last()
        except ObjectDoesNotExist:
            raise Exception('Bilinmeyen cari hesap')
        order_date = datetime.strptime(data.get('date'), '%d.%m.%Y')
        if current is None:
            raise Exception({
                'status': False,
                'message': 'Geçersiz cari kart'
            })

        invdata.update({
            'ARP_CODE': current.code,
            'DOC_TRACK_NR': data.get('OrderKey')[0:21],
            'DATE': order_date.strftime('%Y-%m-%d'),
            'TIME': 0,
            'DOC_DATE': date.today().strftime('%Y-%m-%d'),
            'FTIME': calculate_logo_time(datetime.now()),
            'NOTES1': data.get('exp'),
            'NOTES4': data.get('OrderKey'),
            'VATEXCEPT_REASON': '17/4-e Banka ve Sigorta Muameleleri Vergisi Kapsamına Giren İşlemler',
            'VATEXCEPT_CODE': '209'
        })

        if data.get('specode'):
            invdata.update({
                'AUXIL_CODE': data.get('specode')
            })

        if data.get('exp2'):
            desc = data.get('exp2')

            invdata.update({
                'NOTES2': desc[0:50]
            })
            if desc[50:100]:
                invdata.update({
                    'NOTES3': desc[50:100]
                })


        if current.accepteinv and current.accepteinv == 1:
            invdata.update({
                'EINVOICE': 1,
                'PROFILE_ID': 1
            })
        else:
            invdata.update({
                'EINVOICE': 2,
                'EARCHIVEDETR_SENDMOD': 2,
                'EARCHIVEDETR_EARCHIVESTATUS': 0
            })
        items = data['invoice_lines']['line']
        transactions = []
        for item in items:
            temp = kodlama['SATIS_FATURASI_SATIRI'].copy()
            code = item.get('itemCode')
            price = item.get('price')
            quantity = int(item.get('quantity'))
            product = Itmunita.objects.filter(
                itemref__code=code,
                linenr=1).first()
            if product:
                if product.unitlineref and product.unitlineref.code:
                    temp.update({
                        'UNIT_CODE': product.unitlineref.code
                    })
            if code == 'BSMV':
                temp.update({'TYPE': 3})
            else:
                temp.update({'TYPE': 4})
            temp.update({
                'MASTER_CODE': code,
                'QUANTITY': quantity,
                'UNIT_CONV1': 1,
                'UNIT_CONV2': 1,
                'PRICE': price,
                'DESCRIPTION': data.get('OrderKey')[0:31],
            })
            if code == 'GELIR01':
                temp.update({
                    'UNIT_CODE': 'ADET',
                    'MASTER_DEF': 'ÖDEME HİZMETİ KOMİSYON BEDELİ',
                    'GL_CODE1': kodlama['GELIR01_GL_KOD'],
                    'VATEXCEPT_CODE': '209',
                    'VATEXCEPT_REASON': '17/4-e Banka ve Sigorta Muameleleri Vergisi Kapsamına Giren İşlemler',
                })
            else:
                temp.update({
                    'TYPE': 3,
                    'MASTER_CODE': "BSMV",
                    'MASTER_DEF': 'BSMV',
                    'DETAIL_LEVEL': 1,
                    'GL_CODE1': kodlama['BSMV_GL_KOD'],
                    'VATEXCEPT_REASON': "17/4-e Banka ve Sigorta Muameleleri Vergisi Kapsamına Giren İşlemler",
                    'VATEXCEPT_CODE': "209"
                })
                temp.pop('UNIT_CONV1')
                temp.pop('UNIT_CONV2')

            if item.get('add_tax_amount'):
                temp.update({
                    'ADD_TAX_AMOUNT': item.get('add_tax_amount'),
                    'ADD_TAX_AMNT_IS_UPD': 1
                })

            transactions.append(temp)

        lmap = {line['MASTER_CODE']: line for line in transactions}

        if 'GELIR01' in lmap and 'BSMV' in lmap:
            xprice = lmap['GELIR01']['PRICE']
            bsmv = lmap['BSMV']['PRICE']
            calc = bsmv / xprice * 100
            lmap['BSMV']['DISCOUNT_RATE'] = calc
            lmap['BSMV'].pop('PRICE')
            #lmap['GELIR01']['PRICE'] = calc


        invdata.update({
            'TRANSACTIONS': {
                'items': transactions
            }
        })
        si = SalesInvoice(user=Active.default_rest_user, data=invdata)
        if si.is_valid(raise_exception=True):
            si.set_data(si.get_data())
            si.create()
            si.flow.data = json.dumps(odata)
            si.flow.save()
            if si.flow.success and si.flow.internal_ref:
                track = cls(
                    firm=Active.name,
                    identifier=data.get('OrderKey'),
                    flow=si.flow)
                track.save()
        return si
        
    @classmethod
    def delete_invoice(cls, id):

        return

class P_CLCARD(LG_CLCARD):
    class Meta:
        proxy = True
        target_db = 'erp'

    @classmethod
    def do_update(cls, data, id):
        from app.api.clcard import DatExt
        current = LG_CLCARD.objects.filter(pk=id).first()
        if current is None:
            raise APIException({
                'status': False,
                'message': 'Bilinmeyen cari kart!'
            })
        kodlama = Active.settings['KODLAMA']
        kart = kodlama['CARI_KART'].copy()
        kart.update({
            'CODE': current.code,
            'TITLE': data.get('client_title'),
            'ADDRESS1': data.get('client_adress', ''),
            'CITY': data.get('client_city', ''),
            'COUNTRY': data.get('country'),
            'E_MAIL': data.get('client_email', ''),
            'AUXIL_CODE': data.get('client_type', ''),
            'E_COMM_ID': data.get('client_merchantId'),
            'ITR_SEND_MAIL_ADR': data.get('client_email'),
        })

        kart.update({
            'APPL_DATEXT_1': {
                'CMERCHANT_ID': data.get('client_merchantId')
            }
        })
        identity = data.get('client_taxnumber')

        if data.get('client_taxoffice'):
            kart.update({
                'TAX_OFFICE': data.get('client_taxoffice')
            })
        if data.get('client_website'):
            kart.update({
                'WEB_URL' :  data.get('client_website')
            })

        if len(identity) == 11:
            kart.update({
                'TCKNO': identity,
                'PERSCOMPANY': 1,
                'NAME': data.get('client_name', '.'),
                'SURNAME': data.get('client_surname', '.')
            })
        else:
            kart.update({
                'TAX_ID': identity
            })

        kart = P_CLCARD.echeck(identity, kart)
        clcard = ExtApiClCard(user=Active.default_rest_user, data=kart)
        if clcard.is_valid(raise_exception=True):
            clcard.set_data(clcard.get_data())
            clcard.update(suffix=id)
        return clcard


    @classmethod
    def do_create(cls, data):
        from app.api.clcard import DatExt

        if LG_CLCARD.objects.filter(edino=data.get('client_merchantId')).count() > 0:
            raise APIException({
                'status': False,
                'message': 'Cari kart daha önce tanımlanmış (merchantId kullanımda!)'
            })

        code = P_CLCARD.next_code()
        kodlama = Active.settings['KODLAMA']
        kart = kodlama['CARI_KART'].copy()
        identity = data.get('client_taxnumber')
        kart.update({
            'CODE': code,
            'TITLE': data.get('client_title'),
            'ADDRESS1': data.get('client_adress', ''),
            'CITY': data.get('client_city', ''),
            'COUNTRY': data.get('country'),
            'E_MAIL': data.get('client_email', ''),
            'ITR_SEND_MAIL_ADR': data.get('client_email'),
            'AUXIL_CODE': data.get('client_type', ''),
            'E_COMM_ID': data.get('client_merchantId')
        })
        kart.update({
            'APPL_DATEXT_1': {
                'CMERCHANT_ID': data.get('client_merchantId')
            }
        })

        if data.get('client_taxoffice'):
            kart.update({
                'TAX_OFFICE': data.get('client_taxoffice')
            })
        if data.get('client_website'):
            kart.update({
                'WEB_URL' :  data.get('client_website')
            })

        if len(identity) == 11:
            kart.update({
                'TCKNO': identity,
                'PERSCOMPANY': 1,
                'NAME': data.get('client_name'),
                'SURNAME': data.get('client_surname')
            })
        else:
            kart.update({
                'TAX_ID': identity
            })

        kart = P_CLCARD.echeck(identity, kart)
        clcard = ExtApiClCard(user=Active.default_rest_user, data=kart)
        if clcard.is_valid(raise_exception=True):
            clcard.set_data(clcard.get_data())
            clcard.create()
        return clcard

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
                data['SENDER_LABEL'] = gib.get('EDESPATCHGBALIAS', '-')
                if len(data['SENDER_LABEL'].strip()) == 0:
                    data.pop('SENDER_LABEL')
                if len(gib.get('EDESPATCHGBALIAS', '')):
                    data['ACCEPT_DESP'] = 1
                    data['SENDER_LABEL_CODE_DESP'] = gib.get(
                        'EDESPATCHGBALIAS', '')
                    data['POST_LABEL_CODE_DESP'] = gib.get(
                        'EDESPATCHPKALIAS', '')
        return data

    @classmethod
    def next_code(cls):
        from django.db.models.functions import Length

        kodlama = Active.settings['KODLAMA']
        let = len(kodlama['CARI_KART_SABLON'])
        let += 1
        let += len(kodlama['CARI_KART_NUMARALAMA'])

        next_code = LG_CLCARD.objects.annotate(
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
