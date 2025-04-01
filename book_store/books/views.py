from django.db.models import Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    average_rating = books.aggregate(Avg("rating"))
    return render(
        request=request,
        template_name="books/index.html",
        context={
            "books": books,
            "total_number_of_books": num_books,
            "average_rating": average_rating,
        },
    )


def book_detail(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    return render(
        request=request,
        template_name="books/book-detail.html",
        context={
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestselling,
        },
    )
