from django.contrib import admin

from shops.models import Book, Address


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    pass
