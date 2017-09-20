from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .email import email
import re
from .add_order import add_order


def success(request):
    if request.method == "GET":
        if 'email' not in request.session:
            return HttpResponse("No.")

        usr_email = request.session['email']
        name = request.session['name']
        if re.match('^[\w!#$%&*+\/=?^`{|}~-]+(?:\.[\w!#$%&*+\/=?`{|}~-]+)*@+(?:itggot\.se)$', usr_email):
            # Add order to database
            order_n = add_order(name, usr_email)
            # Send an email
            email(usr_email, name, order_n)
            # Flush session to prevent reordering by reloading
            request.session.flush()

            return render(request, 'order/success.html', {'name': name, 'order_number': order_n, 'email': usr_email})
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
        email = request.session['email']
        name = request.session['name']
        return render(request, 'order/review.html', {'name': name, 'email': email})
