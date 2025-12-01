from django.shortcuts import render

def dashboard(request):
    return render(request, "seller/seller-panel-index.html")

def orders(request):
    return render(request, 'seller/orders/seller-panel-order.html')




def order_resend(request):
    return render(request, "seller/orders/seller-panel-order-resend.html") 

def order_edit(request):
    return render(request, "seller/orders/seller-panel-order-edit.html") 

def order_detail(request):
    return render(request, "seller/orders/seller-panel-order-detail.html") 

def order_deadline(request):
    return render(request, "seller/orders/seller-panel-order-deadline.html") 

def order_cancell(request):
    return render(request, "seller/orders/seller-panel-order-cancell.html") 
