from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.


class CreateProfileView(View):
    def get(self, request: HttpRequest):
        return render(request, "profiles/create-profile.html")

    def post(self, request: HttpRequest):
        print(request.FILES["image"])
        return HttpResponseRedirect(redirect_to="/profiles")
