from django.contrib import admin

from .models import Author, Book, Genre, Review

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    list_filter = ["genre"]
    search_fields = ["title", "author"]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "rating"]
    list_display_links = ["user", "rating"]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
