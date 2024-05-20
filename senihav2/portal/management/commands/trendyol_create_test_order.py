import logging
from datetime import datetime, date
import zmq
import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

import random
import requests

from erp.active import Active
from third_party.bazaars.trendyol import Trendyol

class Command(BaseCommand):
    help = "Trendyol test siparisi olusturma"

    def handle(self, *a, **kw):
        sett = Active.settings['TRENDYOL']
        trendyol = Trendyol(**sett)
        products = trendyol.get_products(approved=True)
        names = requests.get('https://raw.githubusercontent.com/dominictarr/random-name/master/names.json').json()
        name, surname = random.choice(names), random.choice(names)
        addresses = requests.get('https://raw.githubusercontent.com/EthanRBrown/rrad/master/addresses-us-100.json').json()
        address = random.choice(addresses['addresses'])
        order = {
            'customer': {
                'customerFirstName': name,
                'customerLastName': surname
            },
            'invoiceAddress': {
                'addressText': address['address1'],
                'city': address['city'],
                'company': '',
                'email': f'{name}@{surname}.com'.lower(),
                'invoiceFirstName': name,
                'invoiceLastName': surname,
                'latitude': address['coordinates']['lat'],
                'longitude': address['coordinates']['lng'],
                'neighborhood': '',
                'phone': '',
                'postalCode': address['postalCode'],
            },
            'seller': {
                'sellerId': 0 # int(sett['supplier'])
            },
            'shipmentAddress': {
                'addressText': address['address1'],
                'city': address['city'],
                'company': '',
                'district': '',
                'email': f'{name}@{surname}.com',
                'neighborhood': '',
                'phone': '',
                'shippingFirstName': name,
                'shippingLastName': surname,
                'latitude': address['coordinates']['lat'],
                'longitude': address['coordinates']['lng'],
                'postalCode': address['postalCode'],
            }
        }
        order['lines'] = list()
        from pprint import pprint as pp

        nproducts = [p for p in products['content'] if p['quantity'] > 0 and p['salePrice'] > 0 and p['listPrice'] > 0 and len(p['stockCode']) and p['approved'] and p['onSale'] and p['locked'] is False]



        for i in range(random.randint(1,2)):
            product = random.choice(nproducts)
            order['lines'].append({
                'barcode': product['barcode'],
                'quantity': 0 #random.randint(1, 20)
            })
            pp(product)
        pp(order)
        print(trendyol.create_test_order(order))
        print("-"*10)
        #print(products)
