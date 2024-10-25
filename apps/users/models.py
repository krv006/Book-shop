from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, BooleanField, OneToOneField, RESTRICT, DateTimeField, IntegerField, CASCADE, \
    TextField
from django.db.models import Model, CharField, ManyToManyField
from django.utils import timezone

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
    description = TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class LoginAttempt(Model):
    user = OneToOneField('users.User', CASCADE)
    attempts = IntegerField(default=0)
    last_attempt_time = DateTimeField(null=True, blank=True)
    blocked_until = DateTimeField(null=True, blank=True)

    def block_for_five_minutes(self):
        self.blocked_until = timezone.now() + timedelta(minutes=5)
        self.save()

    def reset_attempts(self):
        self.attempts = 0
        self.save()

    def increment_attempts(self):
        self.attempts += 1
        self.last_attempt_time = timezone.now()
        self.save()

    def is_blocked(self):
        if self.blocked_until and self.blocked_until > timezone.now():
            return True
        return False
