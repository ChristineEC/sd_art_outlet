from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import ContactUsForm, CustomOrderRequestForm


def contact_us(request):
    """Enables a site visitomessage to the business without
    logging in"""

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(
                request,
                (
                    'Thank you for your message! '
                    'We will reply as soon as we can. '
                    'Wishing you a lovely day!'
                )
            )
            return redirect(request.path)
        else:
            messages.error(
                           request,
                           (
                            'There seems to be a problem with '
                            'your form. Please ensure you have '
                            'filled in the required fields!'
                           )
            )
    else:
        form = ContactUsForm

    template = "communications/contact_us.html"
    context = {"form": form}
    return render(request, template, context)


def custom_order_request(request):
    """
    Enables a logged in user to send
    a custom_order inquiry
    """
    if request.method == "POST":
        form = CustomOrderRequestForm(request.POST)
        if form.is_valid:
            custom_order_request = form.save(commit=False)
            custom_order_request.user = request.user
            custom_order_request = form.save()
            messages.success(
                request,
                (
                    "Thank you for your custom order "
                    "inquiry. We will reply as soon as we can. "
                    "You can see your custom order inquiries on "
                    "your profile page. Wishing you a lovely day!"
                ),
            )
            return redirect(request.path)
        else:
            messages.error(
                request,
                (
                    "There seems to be a problem with "
                    "your form. Please ensure you have "
                    "filled in the required fields!"
                ),
            )
    else:
        form = CustomOrderRequestForm

    template = "communications/custom_request.html"
    context = {
        "form": form,
        }
    return render(request, template, context)


def display_events(request):
    """Function to display publishable events
    on the events page"""

    events = Event.objects.filter(publish=True).order_by("-start_date")

    template = "communications/events.html"
    context = {"events": events}

    return render(request, template, context)
