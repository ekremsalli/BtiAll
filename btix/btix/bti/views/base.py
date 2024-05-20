"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from collections import OrderedDict
import django_filters.rest_framework
from rest_framework import filters
from rest_framework import pagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class Bti(object):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.OrderingFilter
    ]


class Pagination(pagination.PageNumberPagination):
    page_size = 23

    def get_paginated_response(self, data):
        ordering = self.request.query_params.get("ordering", "")
        if ordering:
            order = ordering
            if order == 'desc':
                order = ""
        else:
            order = ""

        desc = False
        if order.startswith("-"):
            order = order[1:]
            desc = True


        return Response(OrderedDict([
             ('total', self.page.paginator.count),
             ('page_count', self.page.paginator.num_pages),
             ('page_size', self.page_size),
             ('current', self.page.number),
             ('next', self.get_next_link()),
             ('previous', self.get_previous_link()),
             ('results', data),
             ('ordering', order),
             ('descending', desc)
         ]))
