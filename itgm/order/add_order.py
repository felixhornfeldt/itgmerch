import random, datetime
from .models import Order


def add_order(name, email, order_text):
	order_number = random.randrange(1000000000000000, 9999999999999999)
	Order.objects.create(
	name=name,
	email=email,
	order_number=order_number,
	order=order_text,
	date_time=datetime.datetime.now()
)
	print("Order added.")
	return order_number
