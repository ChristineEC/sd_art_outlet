from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib import messages
from .models import ContactUs
from .forms import ContactUsForm


def contact_us(request):
    """
    Enables a site visitor to send a 
    message to the business without
    logging in.
    """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        name = form["name"]
        email = form["email"]
        phone = form["phone"]
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
            HttpResponseRedirect(reverse('home'))
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
