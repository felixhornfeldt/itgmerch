from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .social import validate_usr
from social_django.models import UserSocialAuth
from django.conf import settings
import re

# Create your views here.


def success(request):
    from_email = settings.EMAIL_HOST_USER

    if request.method == "GET":
        usr_email = request.session['email']
        to_email = [from_email, usr_email]
        name = request.session['name']
        if re.match('^[\w!#$%&*+\/=?^`{|}~-]+(?:\.[\w!#$%&*+\/=?`{|}~-]+)*@+(?:itggot\.se)$', usr_email):
            send_mail(
                'Test email',
                'Here is the message.',
                'test.itgmarket@gmail.com',
                to_email,
                fail_silently=False,
            )

            return HttpResponse("Congratulations " + name + "! Email sent.")
        else:
            return HttpResponseRedirect('/order/failed?email=' + usr_email)


def index(request):
    return HttpResponseRedirect("/soc/login/google-oauth2/?next=/success")


def failed(request):
    if request.method == "GET":
        email = request.GET.get('email', '')
        return HttpResponse("It looks like your email " + email + " didn't pass as an ITG-connected one.")
    else:
        return HttpResponse("Something went wrong.")


def review(request):
    if request.method == "GET":
        email = request.GET.get('email', 'a')
        request.session['email'] = email

        name = request.GET.get('name', 'John Doe')
        request.session['name'] = name

        return HttpResponse("Name: " + name + " and email: " + email + " correct? Click <a href='success'>Continue</a>")