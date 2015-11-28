from django.shortcuts import render
from django.contrib.auth import authenticate, logout as lg
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'login.html', {'error': 'Sorry! username & password mismatch'})
        else:
            auth.login(request, user)
            return HttpResponseRedirect('dashboard')
    return render(request, 'login.html', {})


@login_required
def dashboard(request):
    current_user = "{0} {1}".format(request.user.first_name, request.user.last_name)
    return render(request, 'dashboard.html', {'logged_in_user': current_user})


def logout(request):
    lg(request)
    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()
    return HttpResponseRedirect('/')