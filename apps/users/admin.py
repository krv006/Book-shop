from django.contrib import admin

from users.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
