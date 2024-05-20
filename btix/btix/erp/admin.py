"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.contrib import admin

"""
from erp.models.account.account import *
from erp.models.account.code import *
from erp.models.system.address import *

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('logicalref', 'code', 'definition_field')

@admin.register(CardCode)
class CardCodeAdmin(admin.ModelAdmin):
    list_display = ('logicalref', 'trcode', 'cardref')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('logicalref', 'code', 'name')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('logicalref', 'code', 'name', 'country')


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ('logicalref', 'code', 'name', 'city')

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('logicalref', 'code', 'name')
"""