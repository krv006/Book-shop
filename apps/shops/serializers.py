from rest_framework.serializers import ModelSerializer

from shops.models import Country


class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = Country
        exclude = ()


