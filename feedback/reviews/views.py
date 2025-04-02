from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def review(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        entered_name = request.POST.get("name")
        print(entered_name)
        return HttpResponseRedirect("/thank-you")

    return render(request=request, template_name="reviews/review.html")


def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="reviews/thank-you.html")
