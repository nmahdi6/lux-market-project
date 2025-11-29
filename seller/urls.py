from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('order/', views.orders, name='order'),
]