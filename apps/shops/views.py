from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework import status, mixins
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shops.models import Address, Country
from shops.serializers import CountryModelSerializer, AddressListModelSerializer
from users.models import User


@extend_schema(tags=['shops'])
class AddressListCreateAPIView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListModelSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@extend_schema(tags=['shops'])
class AddressDestroyUpdateAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListModelSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user)
        self._can_delete = qs.count() > 1
        return qs

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if self._can_delete:
            _user: User = request.user
            if instance.id in (_user.billing_address_id, _user.shipping_address_id):
                return Response({"message": "maxsus addresslar"})

            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "ozi 1ta qoldi!"})


@extend_schema(tags=['users'])
class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
    authentication_classes = ()
