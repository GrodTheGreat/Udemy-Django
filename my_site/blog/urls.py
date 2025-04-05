from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.IndexView.as_view(), name="index"),
    path(route="posts", view=views.AllPostsView.as_view(), name="posts"),
    path(
        route="posts/<slug:slug>",
        view=views.PostDetailView.as_view(),
        name="post",
    ),
    path(
        route="read-later",
        view=views.ReadLaterView.as_view(),
        name="read-later",
    ),
]
