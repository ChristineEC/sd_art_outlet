from django.shortcuts import render


def handler404(request, exception):
    """ Error handler 404 - Page not Found """
    return render(request, "errors/404.html", status=400)
