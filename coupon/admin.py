from django.contrib import admin
from .models import Coupon, CouponUsage

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code','active','valid_from','valid_until','usage_limit')
    search_fields = ('code',)
    list_filter = ('active',)

@admin.register(CouponUsage)
class CouponUsageAdmin(admin.ModelAdmin):
    list_display = ('coupon','order','used_at')
    search_fields = ('coupon__code','order__id')
