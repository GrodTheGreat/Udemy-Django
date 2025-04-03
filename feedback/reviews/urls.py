from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.ReviewView.as_view(), name="index"),
    path(route="thank-you", view=views.ThankYouView.as_view()),
]
