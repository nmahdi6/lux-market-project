from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart-empty/', views.cart_empty, name='cart-empty'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('success-payment/', views.success_payment, name='success-payment'),
    path('fail-payment/', views.fail_payment, name='fail-payment'),
    path('return-procedure/', views.return_procedure, name='return-procedure'),


    path('order-resend/', views.order_resend, name='order-resend'),
    path('order-edit/', views.order_edit, name='order-edit'),
    path('order-detail/', views.order_detail, name='order-detail'),
    path('order-deadline/', views.order_deadline, name='order-deadline'),
    path('order-cancell/', views.order_cancell, name='order-cancell'),
]
