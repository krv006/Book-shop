from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ManyToManyField
from django_ckeditor_5.fields import CKEditor5Field


class User(AbstractUser):
    wishlist = ManyToManyField('shops.Book', blank=True)


class Author(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    description = CKEditor5Field(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
