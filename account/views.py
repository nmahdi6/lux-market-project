from django.shortcuts import render

def dashboard(request):
    return render(request, "account/user-panel-index.html")

def orders(request):
    return render(request, 'account/orders/user-panel-order.html')

def addresses(request):
    return render(request, 'account/addresses/user-panel-addresses.html')

def wallet(request):
    return render(request, 'account/wallet/user-panel-wallet.html')

def ticket(request):
    return render(request, 'account/tickets/user-panel-ticket.html')

def ticket_form(request):
    return render(request, 'account/tickets/user-panel-ticket-form.html')

def ticket_chat(request):
    return render(request, 'account/tickets/user-panel-ticket-chat.html')





def order_detail(request):
    return render(request, "account/orders/user-panel-order-detail.html") 


def order_return_step_one(request):
    return render(request, "account/orders/user-panel-order-return-step-one.html") 

def order_return_step_two(request):
    return render(request, "account/orders/user-panel-order-return-step-two.html") 

def order_return_step_three(request):
    return render(request, "account/orders/user-panel-order-return-step-three.html") 

