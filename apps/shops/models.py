from django.db.models import CharField, CASCADE, TextField, ImageField, Model, ForeignKey, JSONField, TextChoices, \
    DecimalField, PositiveIntegerField, RESTRICT, PositiveSmallIntegerField, ManyToManyField, BooleanField
from django_ckeditor_5.fields import CKEditor5Field
from mptt.models import MPTTModel, TreeForeignKey

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
    class Format(TextChoices):
        HARDCOVER = 'hardcover', 'Hardcover'
        PAPERCOVER = 'softcover', 'softcover'

    overview = CKEditor5Field()
    features = JSONField()
    # format = CharField(max_length=255, choices=Format, default=Format.HARDCOVER)
    used_good_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    new_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ebook_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    audiobook_price = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    author = ManyToManyField('users.Author')
    reviews_count = PositiveIntegerField(db_default=0)


class Review(TimeBasedModel):
    name = CharField(max_length=255)
    description = CKEditor5Field()
    start = PositiveSmallIntegerField()  # TODO tekshirish kerak (1-10 oraliqdagi son)
    book = ForeignKey('shops.Book', CASCADE, related_name='reviews')

    def __str__(self):
        return self.name


class Country(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Address(TimeBasedModel):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    country = ForeignKey(Country, CASCADE)
    address_line_1 = CharField(max_length=255)
    address_line_2 = CharField(max_length=255, null=True, blank=True)
    city = CharField(max_length=255)
    state = CharField(max_length=255)
    postal_code = PositiveIntegerField(default=0)
    phone_number = CharField(max_length=15)  # todo 998901001010 database da shunday saqlashi kerak + siz
    user = ForeignKey('users.User', RESTRICT)
    shipping_address = BooleanField(default=False)
    billing_address = BooleanField(default=True)

    # TODO 2ta boolean ni qoshish kk

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Cart(TimeBasedModel):
    book = ForeignKey('shops.Book', CASCADE)
    owner = ForeignKey('users.User', CASCADE)
    quantity = PositiveIntegerField(db_default=1)
    '''
    format
    condition
    seller
    ship from
    '''

    def __str__(self):
        return f"{self.owner} - {self.book}"
