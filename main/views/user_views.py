from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from main.function import login_function


def login_view(request):
    if request.method == 'POST':
        return login_function(request)
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    return redirect('main:login')