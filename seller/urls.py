from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('order/', views.orders, name='order'),


    path('order-resend/', views.order_resend, name='order-resend'),
    path('order-edit/', views.order_edit, name='order-edit'),
    path('order-detail/', views.order_detail, name='order-detail'),
    path('order-deadline/', views.order_deadline, name='order-deadline'),
    path('order-cancell/', views.order_cancell, name='order-cancell'),
]