from django.shortcuts import render

def customer(request):
    return render(request, "customer/login.html")
