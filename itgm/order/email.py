from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order

from_email = settings.EMAIL_HOST_USER


def email(usr_email, name, order_number):
    to_email = [from_email, usr_email]
    order_text = Order.objects.get(order_number=order_number).order
    msg_plain = "Read html plz." # render_to_string('templates/email.txt', {'some_params': some_params})
    msg_html = render_to_string('order/email.html', {'name': name, 'order_number': order_number, 'order': order_text})

    send_mail(
        'ITG Marketplace order #' + str(order_number),
        msg_plain,
        from_email,
        to_email,
        fail_silently=False,
        html_message=msg_html,
        )