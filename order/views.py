from django.shortcuts import render

def cart(request):
    return render(request, "order/cart.html") 

def cart_empty(request):
    return render(request, "order/cart-empty.html") 

def checkout(request):
    return render(request, "order/checkout.html") 

def payment(request):
    return render(request, "order/payment.html") 
