from django.http import (
    Http404,
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

MONTHLY_CHALLENGES = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes a day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes a day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes a day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}


def monthly_challenge_by_number(
    request: HttpRequest, month: int
) -> HttpResponseRedirect | HttpResponseNotFound:
    months = list(MONTHLY_CHALLENGES.keys())

    if not 1 <= month <= 12:
        return HttpResponseNotFound("This month is not supported!")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        viewname="month-challenge", args=[redirect_month]
    )  # /challenge/<month>

    return HttpResponseRedirect(redirect_to=redirect_path)


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse | Http404:
    try:
        challenge_text = MONTHLY_CHALLENGES[month.lower()]
        return render(
            request=request,
            template_name="challenges/challenge.html",
            context={"month": month, "text": challenge_text},
        )
    except:
        raise Http404()  # Looks for 404.html file in templates/ by default


def index(request: HttpRequest) -> HttpResponse:
    months = list(MONTHLY_CHALLENGES.keys())

    return render(
        request=request,
        template_name="challenges/index.html",
        context={"months": months},
    )
