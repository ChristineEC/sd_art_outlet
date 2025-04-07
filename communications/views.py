from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .models import ContactUs
from .forms import ContactUsForm, CustomOrderRequestForm, NewsletterSignupForm


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
        name = form["name"]
        email = form["email"]
        phone = form["phone"]
        message = form["message"]
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


def newsletter_signup(request):
    """
    Enables a site visitor to sign up for the
    newsletter without logging in.
    """
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(
                request,
                (
                    "You're all set up to receive our next "
                    "newsletter. Wishing you a lovely day!"
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
        form = NewsletterSignupForm

    template = "communications/newsletter_signup.html"
    context = {
                "form": form,
    }
    return render(request, template, context)
