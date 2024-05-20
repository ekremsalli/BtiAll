"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import logging
from datetime import datetime, date
import re

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

from erp.integration import base

logger = logging.getLogger("erp")

class Command(BaseCommand):
    help = "Convert fixture to serializer"
    robj = re.compile(r"<(.+)>\s(.+)(Integer|Byte|Zstring|Real|PString|İnteger|ZString|Longint|Double)(\s{0,}•)?\s?(\d+)\s{0,}(.+)\s(.+)",
        re.VERBOSE)

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *a, **kw):
        blacklist = [
            'TOTAL_DISCOUNTED',
            'TOTAL_VAT',
            'TOTAL_GROSS',
            'TOTAL_NET',
            'RC_NET',
            'CREATED_BY',
            'DATE_CREATED',
            'HOUR_CREATED',
            'MIN_CREATED',
            'SEC_CREATED',
            'MODIFIED_BY',
            'DATE_MODIFIED',
            'HOUR_MODIFIED',
            'MIN_MODIFIED',
            'SEC_MODIFIED',
            'VAT_AMOUNT',
            'VAT_BASE',
            'DATA_REFERENCE'
        ]
        with open(kw['path']) as fp:
            data = fp.readlines()
            for item in data:
                if len(item.strip()) == 0:
                    continue
                result = self.robj.findall(item.strip())
                if result and result[0]:
                    name, label, itype, req, size, table, field = result[0]

                    name = name.replace(' ', '_')
                    if name in blacklist:
                        continue

                    ext = ""
                    tfield = ""
                    if itype == 'Integer' or itype == 'Longint' or itype == 'İnteger':
                        tfield = 'IntegerField'
                    if itype == 'Byte':
                        tfield = 'IntegerField'
                        ext = """,min_value=0, max_value=1"""
                    if itype.lower() == 'zstring' or itype.lower() == 'pstring':
                        tfield = 'CharField'
                        ext = f",max_length={size}"
                    if itype == 'Double' or itype == 'Float':
                        tfield = 'FloatField'
                    if req:
                        ext += ",required=True"
                    else:
                        ext += ",required=False"
                    print(f"""\t{name} = base.{tfield}(label="{label.strip()}", table="{table}",field="{field}"{ext})""", end="\n")
                else:
                    raise Exception(item)
