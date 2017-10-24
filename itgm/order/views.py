from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .email import email
import re
from .add_order import add_order
from django.views.decorators.csrf import csrf_exempt


def success(request):
    if request.method == "GET":
        if 'email' not in request.session:
            return HttpResponseRedirect('error?err=2')

        usr_email = request.session['email']
        name = request.session['name']
        order_text = request.session['order']
        if re.match('^[\w!#$%&*+\/=?^`{|}~-]+(?:\.[\w!#$%&*+\/=?`{|}~-]+)*@+(?:itggot\.se)$', usr_email):
            # Add order to database
            order_n = add_order(name, usr_email, order_text)
            # Send an email
            email(usr_email, name, order_n, order_text)
            # Flush session to prevent reordering by reloading
            request.session.flush()

            return render(request, 'order/success.html', {'name': name, 'order_number': order_n, 'email': usr_email})
        else:
            return HttpResponseRedirect('/order/error?err=1')


def rdr(request):
    if request.method == "GET":
        request.session['email'] = request.GET.get('email', 'example@example.com')
        request.session['name'] = request.GET.get('name', 'John Doe')

        return HttpResponseRedirect('review')


@csrf_exempt
def index(request):
    # Get order, add to session
    if request.method == "POST":
        order_dict = request.POST
        if order_dict['itemCount'] == '0':
            return HttpResponseRedirect('/')

        request.session['order'] = order_dict
    return HttpResponseRedirect("/soc/login/google-oauth2/?next=/order/review")


def error(request):
    if request.method == "GET":
        error_code = request.GET.get('err', 0)
        error_message = ""

        if error_code is "1":
            error_message = "Your email did not pass validation, are you sure you signed in with your school email?"
        elif error_code is "2":
            error_message = "You tried to order again. Please don't do that."

        return render(request, 'order/error.html', {'error_code': error_code, 'error_message': error_message})
    else:
        return render(request, 'order/error.html', {'error_code': 0, 'error_message': "No message specified."})


def review(request):
        email = request.session['email']
        name = request.session['name']
        return render(request, 'order/review.html', {'name': name, 'email': email})
