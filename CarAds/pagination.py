from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.number),
            ('total_pages', self.page.paginator.num_pages),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
