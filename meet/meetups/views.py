from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    meetups = [
        {
            "title": "A First Meetup",
            "location": "New York",
            "slug": "a-first-meetup",
        },
        {
            "title": "A Second Meetup",
            "location": "Paris",
            "slug": "a-second-meetup",
        },
    ]
    context = {"meetups": meetups, "show_meetups": True}
    return render(
        request=request, template_name="meetups/index.html", context=context
    )


def meetup_details(request: HttpRequest) -> HttpResponse:
    selected_meetup = {
        "title": "A First Meetup",
        "location": "New York",
        "slug": "a-first-meetup",
        "description": "This is the first meetup!",
    }
    context = {"meetup": selected_meetup}
    return render(
        request=request,
        template_name="meetups/meetup-details.html",
        context=context,
    )
