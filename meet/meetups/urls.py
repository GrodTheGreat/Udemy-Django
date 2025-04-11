from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.index, name="meetup-list"),
    path(
        route="success",
        view=views.confirm_registration,
        name="confirm-registration",
    ),
    path(route="<slug:slug>", view=views.meetup_details, name="meetup-details"),
]
