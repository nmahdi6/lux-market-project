from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart-empty/', views.cart_empty, name='cart-empty'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
]
