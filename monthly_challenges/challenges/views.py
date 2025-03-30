from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse(content="It works!")


def february(request):
    return HttpResponse(content="It works!")
