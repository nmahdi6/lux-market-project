from django.contrib import admin
from .models import ShippingMethod, Shipment

@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ('name','code','price','active')
    list_filter = ('active',)
    search_fields = ('name','code')

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('order','method','tracking_number','shipped_at','created_at')
    search_fields = ('tracking_number','order__id')
    list_filter = ('method',)
