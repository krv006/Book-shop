from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import Author, User


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['email']
