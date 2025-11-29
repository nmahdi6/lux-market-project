from django.shortcuts import render

def dashboard(request):
    return render(request, "account/user-panel-index.html")

def orders(request):
    return render(request, 'account/orders/user-panel-order.html')
