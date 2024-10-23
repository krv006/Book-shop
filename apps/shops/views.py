from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView

from shared.paginations import CustomPageNumberPagination
from shops.models import Country, Book
from shops.serializers import BookListModelSerializer, BookDetailModelSerializer
from users.serializers import CountryModelSerializer


@extend_schema(tags=['users'])
class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
    authentication_classes = ()
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=['shops'])
class BookListAPIView(ListAPIView):
    queryset = Book.objects.order_by('-id')
    serializer_class = BookListModelSerializer
    pagination_class = CustomPageNumberPagination

    # def get_queryset(self):
    #     return Book.objects.order_by('id')


@extend_schema(tags=['shops'])
class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailModelSerializer
    lookup_field = 'slug'
