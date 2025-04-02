from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.index, name="index"),
    path(route="posts/", view=views.all_posts, name="posts"),
    path(route="posts/<slug:slug>", view=views.post_detail, name="post"),
]
