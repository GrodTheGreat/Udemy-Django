from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Learn Django for at least 20 minutes a day!",
}


def monthly_challenge_by_number(request, month: int):
    months = list(MONTHLY_CHALLENGES.keys())

    if not 1 <= month <= 12:
        return HttpResponseNotFound("This month is not supported!")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        viewname="month-challenge", args=[redirect_month]
    )  # /challenge/<month>

    return HttpResponseRedirect(redirect_to=redirect_path)


def monthly_challenge(request, month: str):
    try:
        challenge_text = MONTHLY_CHALLENGES[month.lower()]
        return HttpResponse(content=challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
