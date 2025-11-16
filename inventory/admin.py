from django.contrib import admin
from .models import Warehouse, Stock, StockOperation


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    search_fields = ('name', 'code')
    list_filter = ('is_active',)

    class Meta:
        verbose_name = "انبار"
        verbose_name_plural = "انبارها"


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('variant', 'warehouse', 'quantity')
    search_fields = ('variant__sku', 'warehouse__name')
    list_filter = ('warehouse',)

    class Meta:
        verbose_name = "موجودی"
        verbose_name_plural = "موجودی‌ها"


@admin.register(StockOperation)
class StockOperationAdmin(admin.ModelAdmin):
    list_display = ('variant', 'warehouse', 'op_type', 'quantity', 'created_at')
    list_filter = ('op_type', 'warehouse')
    search_fields = ('variant__sku', 'note')

    class Meta:
        verbose_name = "عملیات موجودی"
        verbose_name_plural = "عملیات موجودی‌ها"
