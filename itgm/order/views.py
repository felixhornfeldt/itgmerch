from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .email import email
import re
from .add_order import add_order


def success(request):
    if request.method == "GET":
        usr_email = request.session['email']
        name = request.session['name']
        if re.match('^[\w!#$%&*+\/=?^`{|}~-]+(?:\.[\w!#$%&*+\/=?`{|}~-]+)*@+(?:itggot\.se)$', usr_email):
            order_n = add_order(name, usr_email)
            email(usr_email, name, order_n)

            # Add order to database
            return HttpResponse("Congratulations " + name + "! Email sent.")
        else:
            return HttpResponseRedirect('/order/failed?email=' + usr_email)


def rdr(request):
    if request.method == "GET":
        request.session['email'] = request.GET.get('email', 'a@example.com')
        request.session['name'] = request.GET.get('name', 'John Doe')

        return HttpResponseRedirect('review')


def index(request):
    # Get order, add to session
    return HttpResponseRedirect("/soc/login/google-oauth2/?next=/order/review")


def failed(request):
    if request.method == "GET":
        email = request.GET.get('email', '')
        return HttpResponse("It looks like your email " + email + " didn't pass as an ITG-connected one.")
    else:
        return HttpResponse("Something went wrong.")


def review(request):
    # if request.method == "POST":

        # email = request.POST.get('email', 'a')
        # request.session['email'] = email

        email = request.session['email']

        name = request.session['name']
        # request.session['name'] = name

        return render(request, 'order/review.html', {'name': name, 'email': email})


