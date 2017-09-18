from django.db import models

# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    order_number = models.IntegerField(max_length=10)
    order = models.CharField(max_length=400)