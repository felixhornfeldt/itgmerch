from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .email import email, delivery_email
import re
from .add_order import add_order
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

def success(request):
    if request.method == "GET":
        if 'email' not in request.session:
            return HttpResponseRedirect('error?err=2')

        usr_email = request.session['email']
        name = request.session['name']
        order_text = request.session['order']
        # total = request.session['total']

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
    order = request.session['order']
    order_text = ""

    for i in range(1, (int(order['itemCount']) + 1)):
        order_text += "<tr>"
        order_text += "<td>" + order[('item_name_' + str(i))] + "</td>"
        order_text += "<td>" + order[('item_quantity_' + str(i))] + "</td>"
        order_text += "<td>" + ((order[('item_options_' + str(i))]).split(' '))[1] + "</td>"
        order_text += "<td>" + order[('item_price_' + str(i))] + "</td>"
        order_text += "</tr>"
    email = request.session['email']
    name = request.session['name']
    return render(request, 'order/review.html', {'name': name, 'email': email, 'order_text': order_text})


@login_required(login_url='/order/login/')
def manage(request):
    if request.method == "POST":

        for order in Order.objects.all():
            order.orderDelivered = False
            order.save()

        for item in request.POST:
            if item != "csrfmiddlewaretoken":
                item = Order.objects.get(order_number=item)
                item.orderDelivered = True
                item.save()

    for order in Order.objects.all():
        if order.is_mail_sent is False and order.orderDelivered is True:
            delivery_email(order.email, order.name, order.order_number, order.date_time)
            order.is_mail_sent = True
            order.save()

    return render(request, 'order/manage.html', {'orders': Order.objects.all(), 'id': "embas"})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/order/login/')


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/order/manage/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('/order/login/')
    else:
        form = LoginForm()
        return render(request, 'order/login.html', {'form': form})
