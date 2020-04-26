from django.shortcuts import render
from django.contrib.auth.models import User


def Is_InSessionLogin(userrequest):
    if (request.session.has_key('username')):
        data_query = User.objects.filter(username = loginUser)
        return data_query
    else:
        return False