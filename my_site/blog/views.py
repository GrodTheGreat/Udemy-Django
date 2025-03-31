from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="blog/index.html")


def posts(request: HttpRequest) -> HttpResponse:
    return HttpResponse("posts")


def post(request: HttpRequest, slug: str) -> HttpResponse:
    return HttpResponse(slug)
