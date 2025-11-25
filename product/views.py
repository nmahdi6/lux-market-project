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

def privacy_policy(request):
    return render(request, "privacy-policy.html")

def terms_and_rules(request):
    return render(request, "terms-and-rules.html")
