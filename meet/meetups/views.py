from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    meetups = [
        {
            "title": "A First Meetup",
        },
        {
            "title": "A Second Meetup",
        },
    ]
    context = {"meetups": meetups, "show_meetups": True}
    return render(
        request=request, template_name="meetups/index.html", context=context
    )
