from django.db import models
from datetime import datetime

# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    order_number = models.IntegerField()
    order = models.TextField(max_length=1000)
    date_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        x = self.email + ' ' + str(self.date_time)
        return x
