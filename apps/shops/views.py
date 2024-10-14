from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from shops.models import Address, Country
from shops.serializers import AddressModelSerializer, CountryModelSerializer


@extend_schema(tags=['users'])
class AddressListCreateAPIView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressModelSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@extend_schema(tags=['users'])
class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
    authentication_classes = ()