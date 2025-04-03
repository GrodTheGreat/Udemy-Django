from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm

# from .models import Review


# Create your views here.
def review(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        # existing_review = Review.objects.get(pk=1)
        form = ReviewForm(
            data=request.POST,
            # To update an existing model with a ModelForm
            # instance=existing_review
        )

        if form.is_valid():
            # This isn't needed for a ModelForm
            # review = Review(
            #     name=form.cleaned_data.get("name"),
            #     review_text=form.cleaned_data.get("review_text"),
            #     rating=form.cleaned_data.get("rating"),
            # )
            form.save()
            return HttpResponseRedirect(redirect_to="/thank-you")
    else:
        form = ReviewForm()

    context = {"form": form}

    return render(
        request=request, template_name="reviews/review.html", context=context
    )


def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="reviews/thank-you.html")
