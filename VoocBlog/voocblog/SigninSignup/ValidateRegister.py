from django.http import HttpResponseRedirect
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django import forms


def Validate_Username(email):
    #Test the input email type
    # if not re.search(r'^w+$', email):
    #     return HttpResponseRedirect("error")
    try:
        User.objects.get(username = email)
    except ObjectDoesNotExist:
        return email
    return False


def Validate_Password(password1, password2):
    if (password1 == password2):
        return True
    else:
        #raise error here
        return False



def save(email, password, fname, lname):
    User.objects.create_user(username = email, password = password, first_name = fname ,last_name = lname)