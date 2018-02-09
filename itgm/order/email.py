from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order

from_email = settings.EMAIL_HOST_USER


def email(usr_email, name, order_number, order):
    to_email = [from_email, usr_email]
    order_text = ""

    total = 0

    for i in range(1, (int(order['itemCount']) + 1)):
        order_text += "<tr>"
        order_text += "<td>" + order[('item_name_' + str(i))] + "</td>"
        order_text += "<td>" + order[('item_quantity_' + str(i))] + "</td>"
        order_text += "<td>" + ((order[('item_options_' + str(i))]).split(' '))[1] + "</td>"
        order_text += "<td>" + order[('item_price_' + str(i))] + "</td>"
        order_text += "</tr>"
        
        total += (int(order[('item_quantity_' + str(i))]) * int(order[('item_price_' + str(i))]))
        
        # order_text += f"<p>Grand total: {total}</p>"

    # total = order['total'] 

    msg_plain = "Read html plz." # render_to_string('templates/email.txt', {'some_params': some_params})
    msg_html = render_to_string('order/email.html', {'name': name, 'order_number': order_number, 'order': order_text, 'total':total})

    send_mail(
        'ITG Marketplace order #' + str(order_number),
        msg_plain,
        from_email,
        to_email,
        fail_silently=False,
        html_message=msg_html,
        )


def delivery_email(usr_email, name, order_number, date):
    to_email = [usr_email]
    fourlast = int(str(order_number)[12:16])

    msg_plain = "Your order is ready for pick up. {} {} {}".format(usr_email, name, order_number)
    msg_html = render_to_string('order/email_delivery.html', {
        'name': name,
        'order_number': order_number,
        'usr_email': usr_email,
        'fourlast': fourlast,
        'date': date
    })

    send_mail(
        'ITG Marketplace order #{}'.format(order_number),
        msg_plain,
        from_email,
        to_email,
        fail_silently=False,
        html_message=msg_html,
    )
