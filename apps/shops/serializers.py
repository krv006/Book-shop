from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from shared.utils import get_currency_rates, get_currency
from shops.models import Book
from users.serializers import AuthorModelSerializer, AuthorDetailModelSerializer


def convert_price(price, target_currency='USD'):
    if price is None:
        return None
    rates = get_currency_rates()
    usd_rate = rates.get('USD', 1)
    target_rate = rates.get(target_currency, usd_rate)
    return price / usd_rate * target_rate if usd_rate != 0 else price


class BookDetailModelSerializer(ModelSerializer):
    author = AuthorDetailModelSerializer(many=True, read_only=True)
    used_good_price = SerializerMethodField()
    ebook_price = SerializerMethodField()
    audiobook_price = SerializerMethodField()
    new_price = SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'title', 'slug', 'author', 'image', 'overview', 'used_good_price',
            'ebook_price', 'audiobook_price', 'reviews_count', 'new_price', 'features'
        )

    def get_used_good_price(self, obj):
        currency = self.context.get('currency', 'USD')
        return convert_price(obj.used_good_price, currency)

    def get_ebook_price(self, obj):
        currency = self.context.get('currency', 'USD')
        return convert_price(obj.ebook_price, currency)

    def get_audiobook_price(self, obj):
        currency = self.context.get('currency', 'USD')
        return convert_price(obj.audiobook_price, currency)

    def get_new_price(self, obj):
        currency = self.context.get('currency', 'USD')
        return convert_price(obj.new_price, currency)


class BookListModelSerializer(ModelSerializer):
    author = AuthorModelSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'slug', 'author', 'image')
