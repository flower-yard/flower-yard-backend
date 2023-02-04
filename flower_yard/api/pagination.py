from rest_framework.pagination import PageNumberPagination

from flower_yard.settings import PAGE_SIZE


class ProductAPiPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size = PAGE_SIZE

