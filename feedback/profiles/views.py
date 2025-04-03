from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ProfileForm

# Create your views here.


def store_file(file: UploadedFile):
    with open(file="temp/image.png", mode="wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request: HttpRequest):
        form = ProfileForm()
        return render(
            request=request,
            template_name="profiles/create-profile.html",
            context={"form": form},
        )

    def post(self, request: HttpRequest):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            store_file(request.FILES["image"])
            return HttpResponseRedirect(redirect_to="/profiles")

        return render(
            request=request,
            template_name="profiles/create-profile.html",
            context={"form": form},
        )
