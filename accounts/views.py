from django.shortcuts import render, redirect
from django.contrib.auth import  logout

def register(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'registration/register.html')

def user_login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')
