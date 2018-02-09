import re
from django.shortcuts import redirect
import requests
from social_django.models import UserSocialAuth
from social_django import strategy


def validate_usr(request, backend, user, response, *args, **kwargs):
    if backend.name == "google-oauth2":
        email = response['emails'][0]['value']
        name = response['displayName']

        if re.match('^[\w!#$%&*+\/=?^`{|}~-]+(?:\.[\w!#$%&*+\/=?`{|}~-]+)*@+(?:itggot\.se)$', email):
            return redirect('/order/rdr?email=' + email + '&name=' + name)
        else:
            return redirect('/order/error?err=1')

