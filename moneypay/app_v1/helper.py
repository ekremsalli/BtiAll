import json

from django.contrib.contenttypes.models import ContentType
from django.core.serializers.json import DjangoJSONEncoder

from erp.models.friendly import (
    CardAccountRef,
    Clcard,
    Emuhacc
)
from erp.active import Active
from third_party.elogo.api import Elogo


class Helper:
    @classmethod
    def prepare_glcode(cls, request, arp_obj):
        account = CardAccountRef.objects.select_related(
            'accountref').filter(
                trcode=5, typ=1, cardref=arp_obj.logicalref).first()
        if account and account.accountref:
            request.update({
                'GL_CODE': account.accountref.code
            })
        return request

    @classmethod
    def prepare_einvoice(cls, request, arp_obj, config, payment_day=None):
        from erp.models.other.emukellef import Emukellef
        if arp_obj is None:
            request.update({
                'EINVOICE': 3,
                'EARCHIVEDETR_SENDMOD': 2
            })
        else:
            identifier = arp_obj.tckno or arp_obj.taxnr
            if identifier:
                check = Emukellef.objects.filter(identifier=identifier).first()
                if check:
                    request.update({
                        'EINVOICE': 1,
                        'PROFILE_ID': 1,
                    })
                else:
                    request.update({
                        'EINVOICE': 2,
                        'EARCHIVEDETR_SENDMOD': 2,
                    })
                    if payment_day:
                        request.update({
                            'EARCHIVEDETR_INTPAYMENTDATE': payment_day
                        })
            else:
                if arp_obj.accepteinv and arp_obj.accepteinv == 1:
                    request.update({
                        'EINVOICE': 1,
                        'PROFILE_ID': 1,
                    })
                else:
                    request.update({
                        'EINVOICE': 2,
                        'EARCHIVEDETR_SENDMOD': 2,
                    })
                    if payment_day:
                        request.update({
                            'EARCHIVEDETR_INTPAYMENTDATE': payment_day
                        })

        return request

    @staticmethod
    def echeck(identifier, data):
        from erp.models.other.emukellef import Emukellef
        check = Emukellef.objects.filter(identifier=identifier).first()
        if check:
            data['ACCEPT_EINV'] = 1
            data['POST_LABEL'] = check.aliasinvoicepk
            data['SENDER_LABEL'] = check.aliasinvoicegb
            if check.aliasdespatchadvicegb and len(check.aliasdespatchadvicegb):
                data['ACCEPT_DESP'] = 1
                data['SENDER_LABEL_CODE_DESP'] = check.aliasdespatchadvicegb
                if check.aliasdespatchadvicepk:
                    data['POST_LABEL_CODE_DESP'] = check.aliasdespatchadvicepk
        return data

    @classmethod
    def get_arp_card(cls, uuid):
        # from app_v1.models import XT_100
        # ref = XT_100.objects.filter(uuid=uuid).first()
        # if ref:
        #     return Clcard.objects.filter(pk=ref.parlogref).first()
        # return None

        if len(uuid) == 11:
            return Clcard.objects.filter(tckno=uuid).last()
        else:
            return Clcard.objects.filter(taxnr=uuid).last()


    @classmethod
    def get_or_create_arp_card(cls, data, config, extra={}):
        card = cls.get_arp_card(data.get('uid'))

        if card:
            return (False, card)
        else:
            return cls.create_arp_card(data, config)

    @classmethod
    def create_gl_card(cls, description, config, **kw):
        from erp.asking.account import AccountCard
        gl_code = None
        if ('MUHASEBE_HESABI_OLUSTURULSUN' in config['MUHASEBE'] and 
            config['MUHASEBE']['MUHASEBE_HESABI_OLUSTURULSUN']):
            gl_code = Emuhacc.next_code(
                'code', 
                config['MUHASEBE']['MUHASEBE_KART_SABLON'],
                kw.get('gl_prefix')
            )
            if gl_code:
                request = config['MUHASEBE']['MUHASEBE_KARTI'].copy()
                request.update({
                    'CODE': gl_code,
                    'DESCRIPTION': description[0:100]

                })
                request.update(**kw)
                card = AccountCard(
                    user=config['AKTARIM_KULLANICISI'],
                    data=request
                )
                card.is_valid(raise_exception=True)
                if ('XML_AKTARIMI_KULLAN' in config and 
                    config['XML_AKTARIMI_KULLAN']):
                    card.transfer_via_xml()
                else:
                    card.transfer_via_rest()
                card.flow.data = json.dumps(request)
                card.flow.save()
                return (card.flow, gl_code)
        else:
            if 'SABIT_MUHASEBE_HESABI' in config['MUHASEBE']:
                gl_code = config['MUHASEBE']['SABIT_MUHASEBE_HESABI']
        return (None, gl_code)

