from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.shop, name='product_home'),
    path('shop/', views.shop, name='shop'),
    path('compare/', views.compare, name='compare'),
    path('<int:id>/', views.product_detail, name='product_detail'),
]
