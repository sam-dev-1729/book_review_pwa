# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Book


@login_required
def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "index.html", context=context)


def book_details(request):
    pass


class BookListView(ListView):
    model = Book
    template_name = "book/book_list.html"


class IndexView(TemplateView):
    template_name = "index.html"
