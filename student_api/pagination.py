from rest_framework.pagination import PageNumberPagination

class SmallPageNumberPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param="sayfa"

from rest_framework.pagination import LimitOffsetPagination
class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    # limit_query_param = 'how_many'  # Defaults to 'limit'.


from rest_framework.pagination import CursorPagination
class MycursorPagination(CursorPagination):
    page_size= 12
    ordering = "-id"
    #? reverse order (200,199,198.......) 👆