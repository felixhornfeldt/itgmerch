from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^success', views.success, name='success'),
    url(r'^error', views.error, name='error'),
    url(r'^review', views.review, name='review'),
    url(r'^rdr', views.rdr, name='rdr'),
    url(r'^manage', views.manage, name='manage'),
    url(r'^login', views.login, name='login')
]