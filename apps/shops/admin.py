from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from shops.models import Book, Address
from shops.models import Category


@admin.register(Category)
class CategoryModelAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    pass
