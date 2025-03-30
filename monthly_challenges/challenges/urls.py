from django.urls import path

from . import views

urlpatterns = [
    path(route="<month>", view=views.monthly_challenge),
]
