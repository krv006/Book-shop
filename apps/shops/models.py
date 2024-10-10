from django.db.models import CharField, CASCADE, TextField, ImageField, Model, ForeignKey
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
    name = CharField(max_length=255)
    description = CKEditor5Field()


class WishList(TimeBasedModel):
    user = ForeignKey('users.User', CASCADE)
    book = ForeignKey('shops.Book', CASCADE)

    class Meta:
        unique_together = ('user', 'product')
