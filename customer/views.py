from django.shortcuts import render
from django.shortcuts import redirect

def login(request):
    return render(request, "customer/login.html")

def register(request):
    return render(request, "customer/register.html")

def forgot_password(request):
    return render(request, "customer/forgot-password.html")

def logout(request):
     return redirect('core:index')