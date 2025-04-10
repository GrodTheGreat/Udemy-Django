from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.index),
    path(route="<slug:slug>", view=views.meetup_details),
]
