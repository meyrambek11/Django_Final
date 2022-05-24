from django.contrib import admin

from api.models import Book, Journal
# Register your models here.


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'description', 'type', 'publisher')
    list_display = ('name', 'price')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'description', 'num_pages', 'genre')
    list_display = ('name', 'price')
