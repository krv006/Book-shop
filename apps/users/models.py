from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, BooleanField, OneToOneField, RESTRICT
from django.db.models import Model, CharField, ManyToManyField
from django_ckeditor_5.fields import CKEditor5Field

from users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = EmailField(unique=True)
    name = CharField(max_length=255)
    is_active = BooleanField(default=False)
    shipping_address = OneToOneField('shops.Address', RESTRICT, null=True, blank=True, related_name='shipping_user')
    billing_address = OneToOneField('shops.Address', RESTRICT, null=True, blank=True, related_name='billing_user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    wishlist = ManyToManyField('shops.Book', blank=True, related_name='wishlist')


class Author(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    description = CKEditor5Field(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
