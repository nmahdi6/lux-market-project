# product/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, "about-us.html")

def contact_us(request):
    return render(request, "contact-us.html")

def faq(request):
    return render(request, "faq.html")
