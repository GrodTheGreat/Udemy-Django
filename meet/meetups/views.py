from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import RegistrationForm
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
        registration_form = RegistrationForm()
        context = {
            "meetup": selected_meetup,
            "found": True,
            "form": registration_form,
        }
        return render(
            request=request,
            template_name="meetups/meetup-details.html",
            context=context,
        )
    except Exception:
        context = {"found": False}
        return render(
            request=request,
            template_name="meetups/meetup-details.html",
            context=context,
        )
