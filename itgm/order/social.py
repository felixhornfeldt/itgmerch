import re
from django.shortcuts import redirect


def validate_usr(backend, user, response, *args, **kwargs):
    if backend.name == "google-oauth2":
        email = response['emails'][0]['value']
        name = response['displayName']
        print(email)
        if re.match('^[\w!#$%&*+\/=?^`{|}~-]+(?:\.[\w!#$%&*+\/=?`{|}~-]+)*@+(?:itggot\.se)$', email):
            return redirect('/order/success?email=' + email + '&name=' + name)
        else:
            return redirect('/order/failed?email=' + email)

