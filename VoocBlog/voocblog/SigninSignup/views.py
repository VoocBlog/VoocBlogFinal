from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.db import models
from django.http import HttpResponseRedirect

from django import forms


# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

# def login(request):
#     return render(request, 'LoginRegister/sign-in.html')

def signup(request):
    return render(request, 'LoginRegister/sign-up.html')


def login(request):
    if request.method == 'POST':
        inputUsername = request.POST['username']
        inputPassword = request.POST['password']
        user = authenticate(request, username = inputUsername, password = inputPassword)
        
        if user is not None:
            username = request.POST['username']
            request.session['username'] = username
            return HttpResponseRedirect("profile")
        else:
            print("Invalid password")
            return render(request, 'LoginRegister/sign-up.html')
        # requestUser = User.objects.filter(username = inputUsername)
        # userSelected = User.objects.get(username = 'phat@gmail.com')
        # passwordUser = userSelected.password
        # if requestUser:
        #     if inputPassword == passwordUser:
        #         username = request.POST['username']
        #         request.session['username'] = username
        #         return HttpResponseRedirect("profile")
        #     else:
        #         return render(request, 'LoginRegister/sign-up.html')
        # else:
        #     # raise forms.ValidationError('Invalid password')
        #     return render(request, 'LoginRegister/sign-up.html')
    return render(request, 'LoginRegister/sign-in.html')

def profile(request):
    if request.session.has_key('username'):
        loginUser = request.session['username']
        query = User.objects.filter(username = loginUser)
        return render(request, 'pages/profile.html', {'Query':query})
    else:
        return render(request, 'LoginRegister/sign-in.html')

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'LoginRegister/sign-in.html')