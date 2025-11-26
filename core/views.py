from django.shortcuts import render

def index(request):
    return render(request, "index.html") 

def about_us(request):
    return render(request, "core/about-us.html")

def contact_us(request):
    return render(request, "core/contact-us.html")

def faq(request):
    return render(request, "core/faq.html")

def privacy_policy(request):
    return render(request, "core/privacy-policy.html")

def terms_and_rules(request):
    return render(request, "core/terms-and-rules.html")
