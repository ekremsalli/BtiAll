"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""
from collections import namedtuple
from django.core.serializers.json import DjangoJSONEncoder


def calculate_logo_time(dt):
    return (dt.hour * 65536 * 256) + (dt.minute * 65536) + (dt.second * 256)


def dict_fetch_all(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def named_tuple_fetch_all(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


class BtiJSONEncoder(DjangoJSONEncoder):
    pass