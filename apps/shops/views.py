from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from shared.paginations import CustomPageNumberPagination
from shops.models import Country
from shops.serializers import CountryModelSerializer


@extend_schema(tags=['users'])
class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
    authentication_classes = ()
    pagination_class = CustomPageNumberPagination
