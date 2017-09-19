from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^success', views.success, name='success'),
    url(r'^failed', views.failed, name='failed'),
    url(r'^review', views.review, name='review'),
    url(r'^rdr', views.rdr, name='rdr'),
]