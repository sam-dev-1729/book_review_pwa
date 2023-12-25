# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import ReviewForm
from .models import Book, Review


@login_required
def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "index.html", context=context)


class BookListViewForLogin(LoginRequiredMixin, ListView):
    model = Book
    template_name = "book/book_list.html"


class BookListView(ListView):
    model = Book
    template_name = "book/book_list.html"


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {"book": book}
    return render(request, "/book/book_details.html", context=context)


class BookDetailView(DetailView):
    model = Book
    template_name = "book/book_details.html"
    context_object_name = "book"


class IndexView(TemplateView):
    template_name = "index.html"


class AboutUsView(TemplateView):
    template_name = "about.html"


class ContantView(TemplateView):
    template_name = "contact.html"


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "forms/review.html"

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs["book_id"])
        form.instance.book = book
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "book_detail", kwargs={"pk": self.kwargs["book_id"]}
        )
