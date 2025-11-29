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
]