from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review


# Create your views here.
def review(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ReviewForm(data=request.POST)

        if form.is_valid():
            review = Review(
                name=form.cleaned_data.get("name"),
                review_text=form.cleaned_data.get("review_text"),
                rating=form.cleaned_data.get("rating"),
            )
            review.save()
            return HttpResponseRedirect(redirect_to="/thank-you")
    else:
        form = ReviewForm()

    context = {"form": form}

    return render(
        request=request, template_name="reviews/review.html", context=context
    )


def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="reviews/thank-you.html")
