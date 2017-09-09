from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product', views.product, name='product'),
    url(r'^cart', views.cart, name='cart'),
]
