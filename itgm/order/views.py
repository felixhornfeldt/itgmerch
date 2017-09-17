from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .social import validate_usr
from social_django.models import UserSocialAuth
from django.conf import settings

# Create your views here.

def success(request):
    from_email = settings.EMAIL_HOST_USER
    to_email = []
    name = ''
    if request.method == "GET":
        to_email = [from_email, request.GET.get('email', "a")]
        name = request.GET.get('name', 'John Doe')
    send_mail(
        'Test email',
        'Here is the message.',
        'test.itgmarket@gmail.com',
        to_email,
        fail_silently=False,
    )

    return HttpResponse("Congratulations " + name + "! Email sent.")


def index(request):
    return HttpResponseRedirect("/soc/login/google-oauth2/?next=/success")


def failed(request):
    if request.method == "GET":
        email = request.GET.get('email', '')
        return HttpResponse("It looks like your email " + email + " didn't pass as an ITG-connected one.")
    else:
        return HttpResponse("Something went wrong.")
