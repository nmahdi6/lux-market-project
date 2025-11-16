from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('unit_price','total_price')
    verbose_name = "آیتم سفارش"
    verbose_name_plural = "آیتم‌های سفارش"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer','total','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('id','customer__full_name','customer__email')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at','updated_at')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','variant','quantity','unit_price','total_price')
    search_fields = ('variant__sku','order__id')
