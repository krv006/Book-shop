from rest_framework.serializers import ModelSerializer

from shops.models import Book
from users.serializers import AuthorModelSerializer, AuthorDetailModelSerializer


class BookListModelSerializer(ModelSerializer):
    author = AuthorModelSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'slug', 'author', 'image')


class BookDetailModelSerializer(ModelSerializer):
    author = AuthorDetailModelSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            'title', 'slug', 'author', 'image', 'overview', 'used_good_price', 'ebook_price', 'audiobook_price',
            'reviews_count', 'new_price', 'features')
