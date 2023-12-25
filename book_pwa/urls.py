from django.urls import path

from .views import BookDetailView, BookListView, ReviewCreateView

app_name = "book"
urlpatterns = [
    # path("", book_list, name="list"),
    # path("", IndexView.as_view(), name="list"),
    path("", BookListView.as_view(), name="list"),
    # path("details/",book_details , name='details'),
    path("<int:pk>/", BookDetailView.as_view(), name="details"),
    path("<int:pk>/review/", ReviewCreateView.as_view(), name="add_review"),
]
