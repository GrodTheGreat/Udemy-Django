from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def review(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="reviews/review.html")
