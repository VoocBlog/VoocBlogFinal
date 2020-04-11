from django.shortcuts import render
from django.contrib.auth.models import User


def TakeUserOfSessionLogin(self):
    if (request.session.has_key('username')):
        loginUser = request.session['username']
        data_query = User.objects.filter(username = loginUser)
        return data_query
    else:
        return render(request, 'LoginRegister/sign-in.html')