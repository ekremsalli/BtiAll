"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from rest_framework import serializers
from django.conf import settings

class Base(serializers.Serializer):
    identifier = serializers.CharField(help_text='İstek no')
    firm = serializers.ChoiceField(
        choices=list(settings.FIRMS.keys()),
        default="default", help_text='Firma')

class Que(serializers.Serializer):
    on_time = serializers.BooleanField(
        default=False,
        help_text='Senkron işle'
    )

class Owner(serializers.Serializer):
    owner = serializers.CharField(
        default="DEFAULT_REST_USER",
        help_text='Aktarım kullanıcısı'
    )
