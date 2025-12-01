from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('orders/', views.orders, name='orders'),
    path('addresses/', views.addresses, name='addresses'),
    path('wallet/', views.wallet, name='wallet'),
    path('tickets/', views.ticket, name='ticket'),
    path('ticket-form/', views.ticket_form, name='ticket-form'),
    path('ticket-chat/', views.ticket_chat, name='ticket-chat'),


    path('order-detail/', views.order_detail, name='order-detail'),
    path('order-return-step-one/', views.order_return_step_one, name='order-return-step-one'),
    path('order-return-step-two/', views.order_return_step_two, name='order-return-step-two'),
    path('order-return-step-three/', views.order_return_step_three, name='order-return-step-three'),

]