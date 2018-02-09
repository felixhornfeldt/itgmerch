from django.db import models

# Create your models here.


class Product(models.Model):
    id_n = models.IntegerField(default=0)
    image = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200)
    price = models.IntegerField(default=69)
    name = models.CharField(max_length=30, default="A product")
    description = models.CharField(max_length=400, default='Empty description')
    sizes = models.CharField(max_length=200, default=['OneSize'])

    def __str__(self):
        return self.name
