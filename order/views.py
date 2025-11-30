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



def order_resend(request):
    return render(request, "account/orders/seller-panel-order-resend.html") 

def order_edit(request):
    return render(request, "account/orders/seller-panel-order-edit.html") 

def order_detail(request):
    return render(request, "account/orders/seller-panel-order-detail.html") 

def order_deadline(request):
    return render(request, "account/orders/seller-panel-order-deadline.html") 

def order_cancell(request):
    return render(request, "account/orders/seller-panel-order-cancell.html") 
