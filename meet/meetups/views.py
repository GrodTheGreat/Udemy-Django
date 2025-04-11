from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import RegistrationForm
from .models import Meetup, Participant


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
                user_email = registration_form.cleaned_data.get("email")
                participant, _ = Participant.objects.get_or_create(
                    email=user_email
                )
                selected_meetup.participants.add(participant)
                return redirect(
                    to="confirm-registration",
                    slug=selected_meetup.slug,
                )
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
    except Exception as ex:
        print(ex)
        context = {"found": False}
        return render(
            request=request,
            template_name="meetups/meetup-details.html",
            context=context,
        )


def confirm_registration(request: HttpRequest, slug: str) -> HttpResponse:
    meetup = Meetup.objects.get(slug=slug)
    context = {"meetup": meetup}
    return render(
        request=request,
        template_name="meetups/registration-success.html",
        context=context,
    )
