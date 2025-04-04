# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import get_object_or_404, render
from typing import Any

from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView

from .models import Post


# Create your views here.
# def index(request: HttpRequest) -> HttpResponse:
#     latest_posts = Post.objects.all().order_by("-date")[:3]

#     return render(
#         request=request,
#         template_name="blog/index.html",
#         context={"posts": latest_posts},
#     )


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self) -> QuerySet[Any]:
        # We only need the latest 3 posts
        return super().get_queryset()[:3]


# def all_posts(request: HttpRequest) -> HttpResponse:
#     posts = Post.objects.all().order_by("-date")

#     return render(
#         request=request,
#         template_name="blog/posts.html",
#         context={"posts": posts},
#     )


class AllPostsView(ListView):
    model = Post
    template_name = "blog/posts.html"
    ordering = ["-date"]
    context_object_name = "posts"


# def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
#     identified_post = get_object_or_404(Post, slug=slug)

#     return render(
#         request=request,
#         template_name="blog/post-detail.html",
#         context={"post": identified_post, "tags": identified_post.tags.all()},
#     )


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()

        return context
