from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(
        request=request,
        template_name="books/index.html",
        context={"books": books},
    )


def book_detail(request: HttpRequest, id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=id)
    return render(
        request=request,
        template_name="books/book_detail.html",
        context={
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestselling,
        },
    )
