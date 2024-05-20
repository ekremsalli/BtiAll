from django_filters import rest_framework as filters
from django_filters.constants import EMPTY_VALUES

from erp.models.friendly import Stfiche


class DocNoFilter(filters.CharFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        return qs.filter(docode__startswith=value)


class StartDateFilter(filters.DateTimeFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        return qs.filter(date_field__gte=value)


class EndDateFilter(filters.DateTimeFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        return qs.filter(date_field__lte=value)


class WarehouseFilter(filters.NumberFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        return qs.filter(sourceindex=value)
    

class DispatchTypeFilter(filters.NumberFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        return qs.filter(trcode=value)


class DispatchListFilter(filters.FilterSet):
    startDocNoWith = DocNoFilter()
    startDate = StartDateFilter()
    endDate = EndDateFilter()
    warehouse = WarehouseFilter()
    DispatchType = DispatchTypeFilter()

    class Meta:
        model = Stfiche
        fields = {
            'logicalref': ['exact']
        }
