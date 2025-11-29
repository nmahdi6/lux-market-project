from django.shortcuts import render

def dashboard(request):
    return render(request, "seller/seller-panel-index.html")

def orders(request):
    return render(request, 'seller/order/seller-panel-order.html')
