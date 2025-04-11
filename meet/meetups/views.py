from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

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
        if request.method == "GET":
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
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participants.add(participant)
                return redirect(to="confirm-registration")
            else:
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
    except Exception as e:
        print(e)
        context = {"found": False}
        return render(
            request=request,
            template_name="meetups/meetup-details.html",
            context=context,
        )


def confirm_registration(request: HttpRequest) -> HttpResponse:
    return render(
        request=request, template_name="meetups/registration-success.html"
    )
