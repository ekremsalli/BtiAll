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
    help = "Test integrator"

    def handle(self, *a, **kw):
        from erp.helpers import calculate_logo_time
        """
        from erp.integration.material.slip import (
            MaterialSlip,
            MaterialLineTransaction,
            MaterialLineTransactionHolder,
            MaterialLineSlDetail,
            MaterialLineDetail
        )
        """
        """
        ms = MaterialSlip(data={
            'GROUP': 3,
            'TYPE': 13,
            'NUMBER': 'D.U_EMR_003',
            'DOC_TRACK_NR': 'FİŞ',
            'CURRSEL_TOTALS': 1,
            'DATE': '2021-04-18',
            'TIME': MaterialSlip.calculate_logo_time(datetime.now()),
            'AUXIL_CODE': 'URETIM',
            'TRANSACTIONS':
                [
                    {
                        'ITEM_CODE': '12.170.1610.0086',
                        'LINE_TYPE': 0,
                        'QUANTITY': 2,
                        'UNIT_CODE': 'ADET',
                        'UNIT_CONV1': 1,
                        'UNIT_CONV2': 1,
                        'PRICE': 0.21
                    }
                ]
        })
        """

        data = {
        'GROUP': 3,
        'TYPE': 13,
        'NUMBER': 'D.U_EMR_008',
        'DOC_TRACK_NR': 'FİŞ',
        'CURRSEL_TOTALS': 1,
        'DATE': '18.04.2021',
        'TIME': calculate_logo_time(datetime.now()),
        'AUXIL_CODE': 'URETIM',
        'TRANSACTIONS':
            [
                {
                    'ITEM_CODE': '12.170.1610.0086',
                    'LINE_TYPE': 0,
                    'QUANTITY': 2,
                    'UNIT_CODE': 'ADET',
                    'UNIT_CONV1': 1,
                    'UNIT_CONV2': 1,
                    'PRICE': 0.21
                }
            ]
        }

        # ms.is_valid(raise_exception=True)
        from erp.asking.material import MaterialFiche as askMaterial
        for i in range(1,3):
            data['NUMBER'] = 'D.U_EMR_{}'.format(str(i).zfill(3))
            user = "BTI" if i % 2 == 0 else 'DepoX'
            ask = askMaterial(user=user, data=data)
            if ask.is_valid():
                ask.transfer_via_xml(item_name='TRANSACTION')
                #ask.set_user('DepoX')
                #ask.transfer_via_xml(item_name='TRANSACTION', ignore_pid_check=True)
                #ask.transfer_via_rest()

        #ask.set_xml(ms.to_xml())
        #resp = ask.create_xml()
        #print(ask.flow)
        """
        # xml ok!
        try:
            context = zmq.Context()
            socket = context.socket(zmq.REQ)
            socket.connect("tcp://192.168.1.9:5555")
            socket.setsockopt(zmq.RCVTIMEO, 5000)
            cmd = {
                'do': ms.data_object,
                'data': ms.to_xml(item_name='TRANSACTION'),
                'pid': 1
            }
            socket.send_string(json.dumps(cmd))
            message = socket.recv()
            socket.close()
        except zmq.error.Again:
            print("hatali gonderim!")
        else :
            print(message)
        """
