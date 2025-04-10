from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Meetup


def index(request: HttpRequest) -> HttpResponse:
    meetups = Meetup.objects.all()
    context = {
        "show_meetups": True,
        "meetups": meetups,
    }
    return render(
        request=request, template_name="meetups/index.html", context=context
    )


def meetup_details(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        selected_meetup = Meetup.objects.get(slug=slug)
        context = {"meetup": selected_meetup}
        return render(
            request=request,
            template_name="meetups/meetup-details.html",
            context=context,
        )
    except Exception:
        context = {"fail": True}
        return render(
            request=request,
            template_name="meetups/meetup-details.html",
            context=context,
        )
