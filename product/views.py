# product/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, "product/about-us.html")

def contact_us(request):
    return render(request, "product/contact-us.html")

def faq(request):
    return render(request, "product/faq.html")

def privacy_policy(request):
    return render(request, "product/privacy-policy.html")

def terms_and_rules(request):
    return render(request, "product/terms-and-rules.html")

def shop(request):
    return render(request, "product/shop.html")

def product_detail(request):
    return render(request, "product/product.html")

