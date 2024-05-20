"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import re
from collections.abc import Iterable
from django.db.models import Q


def var_conversion(var):
    # convert var_name to VarName ex: unit_code=UnitCode
    var = var.replace('_', ' ')
    return re.sub(
        r'\w+', lambda m:m.group(0).capitalize(), var).replace(' ', '')

def dict_key_upper(var):
    # convert dict keys to upper
    if isinstance(var, dict):
        return {k.upper():v for k,v in var.items()}
    return var

def convert_dict_to_orm_filter(data, key, val):
    if isinstance(val, Iterable):
        qx = list()
        qx = [Q(**{key: data[v]}) for v in val]
    else:
        qx = [Q(**{key: data[val]})]
    query = qx.pop()
    for q in qx:
        query |= q
    return query
