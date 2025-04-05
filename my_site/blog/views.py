# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import get_object_or_404, render
from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import CommentForm
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


class PostDetailView(View):
    def is_stored_post(self, request: HttpRequest, post_id: int) -> bool:
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            return post_id in stored_posts

        return False

    def get(self, request: HttpRequest, slug: str):
        post = get_object_or_404(Post, slug=slug)

        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(
                request=request, post_id=post.id
            ),
        }

        return render(
            request=request,
            template_name="blog/post-detail.html",
            context=context,
        )

    def post(
        self, request: HttpRequest, slug: str
    ) -> HttpResponse | HttpResponseRedirect:
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(
                redirect_to=reverse(viewname="post", args=[slug])
            )

        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(
                request=request, post_id=post.id
            ),
        }

        return render(
            request=request,
            template_name="blog/post-detail.html",
            context=context,
        )


class ReadLaterView(View):
    def get(self, request: HttpRequest):
        stored_posts: list = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(
            request=request,
            template_name="blog/stored-posts.html",
            context=context,
        )

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        stored_posts: list = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST.get("post_id"))
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect(redirect_to="/")
