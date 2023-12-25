from django.urls import path

from .views import BookListView

urlpatterns = [
    # path("", book_list, name="book-list"),
    # path("", IndexView.as_view(), name="book-list"),
    path("", BookListView.as_view(), name="book-list"),
    # path("details/",book_details , name='book-details'),
]
