import logging
from datetime import datetime
import json


from django.core.management import call_command
from bti.command import BCommand


import logging
logger = logging.getLogger('app')


class Command(BCommand):
    NAME = 'rp_all'

    def process(self, *args, **kwargs):
        commands = [
            'rp_pull',
            'rp_check',
            'rp_push',
            'rp_revenue',
            'rp_sales',
            'rp_production',
            'rp_consumption',
            'rp_waste'
        ]
        for cmd in commands:
            result = call_command(cmd)
            if result:
                print(result)
