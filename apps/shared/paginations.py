from rest_framework.pagination import CursorPagination, PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 5


class CustomCursorPagination(CursorPagination):
    ordering = '-created_at'
