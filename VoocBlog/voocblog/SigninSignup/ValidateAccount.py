import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def login(self):
    
    if request.method == 'POST':
        inputUsername = request.POST['username']
        inputPassword = request.POST['password']
        requestUser = User.objects.filter(username = inputUsername)
        passwordUser = requestUser.last_name
        if requestUser:
            if inputPassword == passwordUser:
                username = request.POST['username']
                request.session['username'] = username
                return HttpResponseRedirect("profile")
            else:
                return render(request, 'LoginRegister/sign-up.html')
        else:
            # raise forms.ValidationError('Invalid password')
            return render(request, 'LoginRegister/sign-up.html')
    return render(request, 'LoginRegister/sign-in.html')

def profile(request):
    if request.session.has_key('username'):
        loginUser = request.session['username']
        query = User.objects.filter(username = loginUser)
        return render(request, 'pages/profile.html', {'query':query})
    else:
        return render(request, 'LoginRegister/sign-in.html')

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'LoginRegister/sign-in.html')