from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.review, name="index"),
    path(route="thank-you", view=views.thank_you),
]
