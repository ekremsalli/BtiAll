"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import json
from rest_framework.serializers import Serializer as BaseSerialiazer
from rest_framework import serializers
from dicttoxml import dicttoxml
from erp.helpers import calculate_logo_time

class Serializer(BaseSerialiazer):
    @classmethod
    def calculate_logo_time(cls, dt):
        return calculate_logo_time(dt)

    @property
    def data_object(self):
        return self.Meta.DATA_OBJECT

    def apply_root(self, raw):
        template = """<{root}>{raw}</{root}>"""
        return template.format(
            root=self.Meta.XML_ROOT,
            raw=raw
        )

    def apply_subroot(self, raw, op=None):
        template = """<{subroot} DBOP="{op}">{raw}</{subroot}>"""
        return template.format(
            subroot=self.Meta.XML_SUBROOT,
            op=self.Meta.XML_OP if op is None else op,
            raw=raw
        )

    def get_data(self):
        if self.is_valid():
            return self.validated_data
        return None

    def to_json(self):
        if self.is_valid():
            return json.dumps(self.validated_data)
        return None

    def to_xml(self, subroot=True, root=True, op='INS', item_name=None, data_reference=None):
        if self.is_valid():
            if (hasattr(self.Meta, 'XML_ROOT') and
                hasattr(self.Meta, 'XML_SUBROOT')):
                if op is None and hasattr(self.Meta, 'XML_OP') is False:
                    raise Exception('XML_OP tanımlanmamış!')
                data = self.validated_data
                if data_reference is not None:
                    #data['INTERNAL_REFERENCE'] = data_reference
                    data['DATA_REFERENCE'] = data_reference
                attrs = {
                    'attr_type': False,
                    'root': False
                }
                if item_name:
                    def nx(x):
                        if x in item_name:
                            return item_name[x]
                        return x
                    if isinstance(item_name, str):
                        item_name_func = lambda x: item_name
                    if isinstance(item_name, dict):
                        item_name_func = lambda x: nx(x)
                    attrs['item_func'] = item_name_func

                raw = dicttoxml(data, **attrs).decode('utf-8')


                if subroot:
                    raw = self.apply_subroot(raw, op=op)
                if root:
                    raw = self.apply_root(raw)
                return raw
            else:
                raise Exception('XML parametreleri ayarlanmamış!')
        return None

class ExtField:
    def __init__(self, *args, **kwargs):
        if 'table' in kwargs:
            self.table = kwargs.pop('table')
        if 'field' in kwargs:
            self.field = kwargs.pop('field')
        super().__init__(*args, **kwargs)

class DateField(ExtField, serializers.DateField):
    pass

class IntegerField(ExtField, serializers.IntegerField):
    pass

class CharField(ExtField, serializers.CharField):
    pass

class FloatField(ExtField, serializers.FloatField):
    pass

class BooleanField(ExtField,serializers.BooleanField):
    pass