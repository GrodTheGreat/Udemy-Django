from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
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
