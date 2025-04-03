# from django.core.files.uploadedfile import UploadedFile
# from django.http import HttpRequest, HttpResponseRedirect
# from django.shortcuts import render
# from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView

# from .forms import ProfileForm
from .models import UserProfile

# Create your views here.


# def store_file(file: UploadedFile):
#     with open(file="temp/image.png", mode="wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


# class CreateProfileView(View):
#     def get(self, request: HttpRequest):
#         form = ProfileForm()
#         return render(
#             request=request,
#             template_name="profiles/create-profile.html",
#             context={"form": form},
#         )

#     def post(self, request: HttpRequest):
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = UserProfile(image=request.FILES["image"])
#             profile.save()
#             # store_file(request.FILES["image"])
#             return HttpResponseRedirect(redirect_to="/profiles")

#         return render(
#             request=request,
#             template_name="profiles/create-profile.html",
#             context={"form": form},
#         )


class CreateProfileView(CreateView):
    template_name = "profiles/create-profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user-profiles.html"
    context_object_name = "profiles"
