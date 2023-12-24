from django.contrib import admin

from .models import Book, Genre, Review

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]


admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(Review)
