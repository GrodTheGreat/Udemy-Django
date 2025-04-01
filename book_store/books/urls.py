from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.index),
    path(route="<int:id>", view=views.book_detail, name="book-detail"),
]
