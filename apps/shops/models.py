from django.db.models import CharField, CASCADE, TextField, ImageField, Model, ForeignKey, JSONField, TextChoices, \
    DecimalField, IntegerField
from mptt.models import MPTTModel, TreeForeignKey
from django_ckeditor_5.fields import CKEditor5Field

from shared.model import TimeBasedModel, SlugTimeBasedModel


class Section(TimeBasedModel):
    name_image = ImageField(upload_to='shops/categories/name_image/%Y/%m/%d', null=True, blank=True)
    intro = TextField(null=True, blank=True)
    banner = ImageField(upload_to='shops/categories/banner/%Y/%m/%d', null=True, blank=True)


class Category(MPTTModel):
    name = CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='subcategories')
    section = ForeignKey('shops.Section', CASCADE, null=True, blank=True, related_name='categories')

    class MPTTMeta:
        order_insertion_by = ['name']


class Book(SlugTimeBasedModel):
    class BookCover(TextChoices):
        Hardcover = 'hardcover', 'Hardcover'
        Softcover = 'softcover', 'softcover'

    overview = CKEditor5Field()
    features = JSONField()
    book_cover = CharField(max_length=255, choices=BookCover, default=BookCover.Hardcover)
    used_good_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    new_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ebook_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    audiobook_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    author = ForeignKey('users.Author', CASCADE)


class Rating(Model):
    book = ForeignKey('shops.Book', on_delete=CASCADE)
    stars = DecimalField(max_digits=3, decimal_places=1)
    review_count = IntegerField(default=0)

    def __str__(self):
        return f"{self.stars} stars for {self.book.title}"


class Review(TimeBasedModel):
    name = CharField(max_length=255)
    description = CKEditor5Field()
    book = ForeignKey('shops.Book', CASCADE)

    def __str__(self):
        return self.name


class WishList(TimeBasedModel):
    user = ForeignKey('users.User', CASCADE)
    book = ForeignKey('shops.Book', CASCADE)

    class Meta:
        ordering = ['-created_at']
