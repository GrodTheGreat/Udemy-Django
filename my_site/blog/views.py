from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(
        request=request,
        template_name="blog/index.html",
        context={"posts": latest_posts},
    )


def all_posts(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-date")

    return render(
        request=request,
        template_name="blog/posts.html",
        context={"posts": posts},
    )


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    identified_post = get_object_or_404(Post, slug=slug)

    return render(
        request=request,
        template_name="blog/post-detail.html",
        context={"post": identified_post, "tags": identified_post.tags.all()},
    )
