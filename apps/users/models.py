from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField


class User(AbstractUser):
    pass


class Author(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
