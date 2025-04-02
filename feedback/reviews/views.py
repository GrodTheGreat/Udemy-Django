from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm


# Create your views here.
def review(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ReviewForm(data=request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect(redirect_to="/thank-you")
    else:
        form = ReviewForm()

    context = {"form": form}

    return render(
        request=request, template_name="reviews/review.html", context=context
    )


def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="reviews/thank-you.html")
