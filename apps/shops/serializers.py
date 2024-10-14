from rest_framework.serializers import ModelSerializer

from shops.models import Address, Country


class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class AddressModelSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def to_representation(self, instance: Address):
        repr = super().to_representation(instance)
        repr['country'] = CountryModelSerializer(instance.country).data
        return repr
