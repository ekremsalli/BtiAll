import logging
import requests


from erp.active import Active
from erp.auth import Token
from bti.command import BCommand

logger = logging.getLogger('app')


class Command(BCommand):
    NAME = 'send_invoice_from_file'


    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            'path',
            type=str,
            help='JSON file path',
        )

    def process(self, *args, **kwargs):
        path = kwargs.get('path')

        with open(path, 'r') as fp:
            data = fp.read()

        url = f'{Active.rest_url}{Active.rest_version}/salesInvoices'

        token_req = Token.generate_token('BayRobotPos').json()

        print(token_req)
        token = token_req.get('access_token')

        headers = {
            'Authorization': f'Bearer {token}'
        }

        print(url)

        req = requests.post(url, json=data, headers=headers)
        print(req)
        print(req.json())

        req = requests.get(url, headers=headers)
        print(req)
        print(req.json())




