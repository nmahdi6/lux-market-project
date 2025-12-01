from django.shortcuts import render

def cart(request):
    return render(request, "order/cart.html") 

def cart_empty(request):
    return render(request, "order/cart-empty.html") 

def checkout(request):
    return render(request, "order/checkout.html") 

def payment(request):
    return render(request, "order/payment.html") 

def success_payment(request):
    return render(request, "order/success-payment.html") 

def fail_payment(request):
    return render(request, "order/fail-payment.html") 

def return_procedure(request):
    return render(request, "order/return-procedure.html") 


