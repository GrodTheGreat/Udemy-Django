from django.urls import path

from . import views

urlpatterns = [
    # * ORDER MATTERS!!!
    path(route="<int:month>", view=views.monthly_challenge_by_number),
    path(route="<str:month>", view=views.monthly_challenge),
]
