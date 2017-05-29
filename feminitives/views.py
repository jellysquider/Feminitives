from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf #cross-site request forgery
from django.views.decorators.csrf import csrf_protect


# Create your views here.

@csrf_protect
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponse('/accounts/loggedin/')
    else:
        return HttpResponse('/accounts/invalid/')

def loggedin(request):
    return render(request, 'loggedin.html',
                 {'full_name': request.user.username })

def invalid_login(request):
    return render(request, 'invalid_login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')
