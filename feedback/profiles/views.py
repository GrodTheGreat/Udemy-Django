from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.


def store_file(file: UploadedFile):
    with open(file="temp/image.png", mode="wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request: HttpRequest):
        return render(request, "profiles/create-profile.html")

    def post(self, request: HttpRequest):
        store_file(request.FILES["image"])
        return HttpResponseRedirect(redirect_to="/profiles")
