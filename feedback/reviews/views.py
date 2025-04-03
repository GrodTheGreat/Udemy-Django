from typing import Any

# from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
# from django.views import View
from django.http import HttpRequest, HttpResponseRedirect
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review


# Create your views here.
# Class based view
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def get(self, request: HttpRequest) -> HttpResponse:
    #     form = ReviewForm()
    #     context = {"form": form}

    #     return render(
    #         request=request,
    #         template_name="reviews/review.html",
    #         context=context,
    #     )

    # def post(self, request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    #     form = ReviewForm(data=request.POST)
    #     if form.is_valid():
    #         form.save()

    #         return HttpResponseRedirect(redirect_to="/thank-you")

    #     context = {"form": form}

    #     return render(
    #         request=request,
    #         template_name="reviews/review.html",
    #         context=context,
    #     )


# Function based view
# def review(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         # existing_review = Review.objects.get(pk=1)
#         form = ReviewForm(
#             data=request.POST,
#             # To update an existing model with a ModelForm
#             # instance=existing_review
#         )

#         if form.is_valid():
#             # This isn't needed for a ModelForm
#             # review = Review(
#             #     name=form.cleaned_data.get("name"),
#             #     review_text=form.cleaned_data.get("review_text"),
#             #     rating=form.cleaned_data.get("rating"),
#             # )
#             form.save()
#             return HttpResponseRedirect(redirect_to="/thank-you")
#     else:
#         form = ReviewForm()

#     context = {"form": form}

#     return render(
#         request=request, template_name="reviews/review.html", context=context
#     )


# def thank_you(request: HttpRequest) -> HttpResponse:
#     return render(request=request, template_name="reviews/thank-you.html")


class ThankYouView(TemplateView):
    template_name = "reviews/thank-you.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"

        return context


class ReviewsList(ListView):
    template_name = "reviews/review-list.html"
    model = Review
    context_object_name = "reviews"  # To define template object name

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     return base_query.filter(rating__gte=4)


class ReviewDetail(DetailView):
    # Will search by either pk or slug, you can define which in urls.py
    template_name = "reviews/review-detail.html"
    model = Review

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session["favorite_review"]
        context["is_favorite"] = favorite_id == str(loaded_review.id)

        return context


class FavoriteView(View):
    def post(self, request: HttpRequest):
        review_id = request.POST.get("review_id")
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect(redirect_to="/reviews/" + review_id)
